"""Checklist draft recording services — start + save draft only; no submission."""

from __future__ import annotations

import uuid
from decimal import Decimal, InvalidOperation
from typing import Any

from django.core.exceptions import PermissionDenied, ValidationError
from django.db import IntegrityError, transaction

from apps.access_control.services import require_permission
from apps.accounts.models import User
from apps.checklists.models import (
    ChecklistItem,
    ChecklistItemOption,
    ChecklistResponseType,
    ChecklistVersionStatus,
)
from apps.recording.models import ChecklistRecord, ChecklistResponse, ChoiceResponseValue
from apps.scheduling.models import ChecklistTask, ChecklistTaskStatus
from apps.scheduling.services import RECORD_CHECKLIST_TASK, task_authorization_scope
from apps.security_audit.services import record_event

YES_NO_VALUES = frozenset({ChoiceResponseValue.YES, ChoiceResponseValue.NO})
YES_NO_NA_VALUES = frozenset(
    {ChoiceResponseValue.YES, ChoiceResponseValue.NO, ChoiceResponseValue.NA}
)


def _require_authenticated_actor(actor: User | None) -> User:
    if actor is None or not getattr(actor, "is_authenticated", False) or not actor.is_active:
        raise PermissionDenied("Authentication required.")
    return actor


def _record_metadata(
    record: ChecklistRecord, *, changed_item_count: int | None = None
) -> dict[str, Any]:
    task = record.checklist_task
    metadata: dict[str, Any] = {
        "checklist_record_id": str(record.id),
        "checklist_task_id": str(task.id),
        "organization_id": str(record.organization_id),
        "checklist_template_id": str(task.checklist_template_id),
        "checklist_version_id": str(task.checklist_version_id),
        "batch_reference": task.batch_reference,
    }
    if changed_item_count is not None:
        metadata["changed_item_count"] = changed_item_count
    return metadata


def _assert_task_recordable(task: ChecklistTask) -> None:
    if task.status != ChecklistTaskStatus.PENDING:
        raise ValidationError({"task": "Only PENDING checklist tasks may be recorded."})
    if task.checklist_version.status != ChecklistVersionStatus.PUBLISHED:
        raise ValidationError(
            {
                "task": (
                    "Checklist task definition must remain a PUBLISHED version. "
                    "Recording cannot substitute another version."
                )
            }
        )


def start_checklist_recording(
    *,
    actor: User | None,
    task_id: uuid.UUID,
) -> ChecklistRecord:
    """
    Start (or return existing) draft ChecklistRecord for a PENDING task.

    Idempotent and race-safe. Does not transfer started_by ownership.
    """
    user = _require_authenticated_actor(actor)

    task = (
        ChecklistTask.objects.select_related(
            "organization",
            "checklist_template",
            "checklist_version",
        )
        .filter(pk=task_id)
        .first()
    )
    if task is None:
        raise ValidationError({"task": "Checklist task not found."})

    require_permission(user, RECORD_CHECKLIST_TASK, scope=task_authorization_scope(task))
    _assert_task_recordable(task)

    existing = (
        ChecklistRecord.objects.select_related(
            "organization",
            "checklist_task",
            "checklist_task__checklist_template",
            "checklist_task__checklist_version",
            "started_by",
        )
        .filter(checklist_task_id=task.id)
        .first()
    )
    if existing is not None:
        return existing

    try:
        with transaction.atomic():
            locked = (
                ChecklistTask.objects.select_related(
                    "organization",
                    "checklist_template",
                    "checklist_version",
                )
                .select_for_update()
                .filter(pk=task.id)
                .first()
            )
            if locked is None:
                raise ValidationError({"task": "Checklist task not found."})
            _assert_task_recordable(locked)

            raced_existing = (
                ChecklistRecord.objects.select_related(
                    "organization",
                    "checklist_task",
                    "checklist_task__checklist_template",
                    "checklist_task__checklist_version",
                    "started_by",
                )
                .filter(checklist_task_id=locked.id)
                .first()
            )
            if raced_existing is not None:
                return raced_existing

            record = ChecklistRecord(
                organization_id=locked.organization_id,
                checklist_task=locked,
                started_by=user,
            )
            record.full_clean()
            record.save()
            record_event(
                event_type="CHECKLIST_RECORD_STARTED",
                actor=user,
                metadata=_record_metadata(record),
            )
    except IntegrityError:
        raced = (
            ChecklistRecord.objects.select_related(
                "organization",
                "checklist_task",
                "checklist_task__checklist_template",
                "checklist_task__checklist_version",
                "started_by",
            )
            .filter(checklist_task_id=task.id)
            .first()
        )
        if raced is None:
            raise
        return raced

    return ChecklistRecord.objects.select_related(
        "organization",
        "checklist_task",
        "checklist_task__checklist_template",
        "checklist_task__checklist_version",
        "started_by",
    ).get(pk=record.id)


def _clear_value_fields(response: ChecklistResponse) -> None:
    response.choice_value = ""
    response.number_value = None
    response.text_value = ""
    response.selected_option = None


def _apply_typed_value(
    *,
    response: ChecklistResponse,
    item: ChecklistItem,
    raw: Any,
) -> None:
    response_type = item.response_type
    _clear_value_fields(response)

    if response_type == ChecklistResponseType.YES_NO:
        value = str(raw).strip().upper()
        if value not in YES_NO_VALUES:
            raise ValidationError({str(item.id): "Answer must be YES or NO."})
        response.choice_value = value
        return

    if response_type == ChecklistResponseType.YES_NO_NA:
        value = str(raw).strip().upper()
        if value not in YES_NO_NA_VALUES:
            raise ValidationError({str(item.id): "Answer must be YES, NO, or NA."})
        response.choice_value = value
        return

    if response_type == ChecklistResponseType.NUMBER:
        try:
            number = Decimal(str(raw).strip())
        except (InvalidOperation, AttributeError, TypeError) as exc:
            raise ValidationError({str(item.id): "Enter a valid number."}) from exc
        # Out-of-range values are intentionally accepted for draft capture.
        response.number_value = number
        return

    if response_type == ChecklistResponseType.TEXT:
        text = str(raw)
        if not text.strip():
            raise ValidationError({str(item.id): "Text answer cannot be blank."})
        response.text_value = text
        return

    if response_type == ChecklistResponseType.SELECT:
        try:
            option_id = uuid.UUID(str(raw))
        except (TypeError, ValueError, AttributeError) as exc:
            raise ValidationError({str(item.id): "Select a valid option."}) from exc
        option = ChecklistItemOption.objects.filter(pk=option_id, item_id=item.id).first()
        if option is None:
            raise ValidationError({str(item.id): "Select a valid option."})
        response.selected_option = option
        return

    raise ValidationError({str(item.id): "Unsupported response type."})


def _is_blank_answer(raw: Any) -> bool:
    if raw is None:
        return True
    if isinstance(raw, str) and not raw.strip():
        return True
    return False


def save_checklist_draft_responses(
    *,
    actor: User | None,
    record_id: uuid.UUID,
    answers: dict[uuid.UUID, Any],
) -> ChecklistRecord:
    """
    Save/update/clear typed draft responses for a ChecklistRecord.

    Partial completion is allowed — required items may remain unanswered.
    Does not evaluate min/max, PASS/FAIL, HOLD, or submission completeness.
    """
    user = _require_authenticated_actor(actor)

    with transaction.atomic():
        record = (
            ChecklistRecord.objects.select_related(
                "organization",
                "checklist_task",
                "checklist_task__organization",
                "checklist_task__checklist_template",
                "checklist_task__checklist_version",
            )
            .select_for_update()
            .filter(pk=record_id)
            .first()
        )
        if record is None:
            raise ValidationError({"record": "Checklist record not found."})

        task = record.checklist_task
        require_permission(user, RECORD_CHECKLIST_TASK, scope=task_authorization_scope(task))
        if record.organization_id != task.organization_id:
            raise ValidationError({"organization": "Record organization mismatch."})
        _assert_task_recordable(task)

        version_id = task.checklist_version_id
        items = {
            item.id: item
            for item in ChecklistItem.objects.select_related("section").filter(
                section__version_id=version_id
            )
        }
        existing = {
            response.checklist_item_id: response
            for response in ChecklistResponse.objects.select_for_update().filter(
                checklist_record_id=record.id
            )
        }

        changed = 0
        errors: dict[str, list[str]] = {}

        for item_id, raw in answers.items():
            item = items.get(item_id)
            if item is None:
                # Do not reveal whether a foreign UUID exists elsewhere.
                errors[str(item_id)] = ["Item is not part of this checklist definition."]
                continue

            if _is_blank_answer(raw):
                current = existing.get(item_id)
                if current is not None:
                    current.delete()
                    changed += 1
                continue

            response = existing.get(item_id) or ChecklistResponse(
                checklist_record=record,
                checklist_item=item,
            )
            try:
                _apply_typed_value(response=response, item=item, raw=raw)
                response.full_clean()
                response.save()
                existing[item_id] = response
                changed += 1
            except ValidationError as exc:
                if hasattr(exc, "message_dict"):
                    for key, msgs in exc.message_dict.items():
                        bucket = errors.setdefault(str(key), [])
                        bucket.extend(str(m) for m in msgs)
                else:
                    errors.setdefault(str(item_id), []).extend(str(m) for m in exc.messages)

        if errors:
            raise ValidationError(errors)

        record.save(update_fields=["updated_at"])
        record_event(
            event_type="CHECKLIST_RECORD_DRAFT_SAVED",
            actor=user,
            metadata=_record_metadata(record, changed_item_count=changed),
        )

    return ChecklistRecord.objects.select_related(
        "organization",
        "checklist_task",
        "checklist_task__checklist_template",
        "checklist_task__checklist_version",
        "started_by",
    ).get(pk=record.id)
