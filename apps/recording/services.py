"""Checklist recording services — draft save + immutable submission (Phase 08B)."""

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
    ChecklistItemKind,
    ChecklistItemOption,
    ChecklistResponseType,
    ChecklistVersionStatus,
)
from apps.recording.models import (
    ChecklistRecord,
    ChecklistRecordStatus,
    ChecklistResponse,
    ChecklistSubmission,
    ChecklistSubmissionResponse,
    ChoiceResponseValue,
)
from apps.recording.repeating import (
    ResponseKey,
    active_sample_count,
    assert_sample_index_allowed,
    effective_repeat_min,
    normalize_answers,
    partition_definition_items,
    responses_by_key,
    validate_repeating_submit_shape,
)
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
    record: ChecklistRecord,
    *,
    changed_item_count: int | None = None,
    submission: ChecklistSubmission | None = None,
    answered_item_count: int | None = None,
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
    if answered_item_count is not None:
        metadata["answered_item_count"] = answered_item_count
    if submission is not None:
        metadata["checklist_submission_id"] = str(submission.id)
        metadata["submission_number"] = submission.submission_number
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


def _assert_record_is_draft(record: ChecklistRecord) -> None:
    if record.status != ChecklistRecordStatus.DRAFT:
        raise ValidationError(
            {
                "status": (
                    "Submitted checklist records cannot be edited. "
                    "Future corrections require an explicit resubmission workflow."
                )
            }
        )


def transition_record_to_submitted(record: ChecklistRecord) -> ChecklistRecord:
    """Centralized DRAFT → SUBMITTED transition. Reverse is not allowed in 08B."""
    if record.status == ChecklistRecordStatus.SUBMITTED:
        return record
    if record.status != ChecklistRecordStatus.DRAFT:
        raise ValidationError(
            {"status": f"Cannot transition checklist record from {record.status} to SUBMITTED."}
        )
    record.status = ChecklistRecordStatus.SUBMITTED
    record.save(update_fields=["status", "updated_at"])
    return record


def start_checklist_recording(
    *,
    actor: User | None,
    task_id: uuid.UUID,
) -> ChecklistRecord:
    """
    Start (or return existing) ChecklistRecord for a PENDING task.

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
                status=ChecklistRecordStatus.DRAFT,
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
        # Out-of-range values are intentionally accepted.
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


def _response_is_structurally_valid(item: ChecklistItem, response: ChecklistResponse) -> bool:
    response_type = item.response_type
    if response_type == ChecklistResponseType.YES_NO:
        return response.choice_value in YES_NO_VALUES
    if response_type == ChecklistResponseType.YES_NO_NA:
        return response.choice_value in YES_NO_NA_VALUES
    if response_type == ChecklistResponseType.NUMBER:
        return response.number_value is not None
    if response_type == ChecklistResponseType.TEXT:
        return bool((response.text_value or "").strip())
    if response_type == ChecklistResponseType.SELECT:
        return (
            response.selected_option_id is not None
            and response.selected_option is not None
            and response.selected_option.item_id == item.id
        )
    return False


def collect_submission_completeness(
    *,
    record: ChecklistRecord,
    items: list[ChecklistItem] | None = None,
    responses: dict[ResponseKey, ChecklistResponse] | None = None,
) -> dict[str, Any]:
    """
    Completeness metrics for submission UX / validation.

    Does not evaluate PASS/FAIL or min/max conformance.
    REPEATING_GROUP containers are not answerable; child SIMPLE rows use sample_index.
    """
    version_id = record.checklist_task.checklist_version_id
    if items is None:
        items = list(
            ChecklistItem.objects.select_related("section", "parent_item")
            .prefetch_related("options")
            .filter(section__version_id=version_id)
            .order_by("section__position", "position")
        )
    if responses is None:
        responses = responses_by_key(
            list(
                ChecklistResponse.objects.filter(checklist_record_id=record.id).select_related(
                    "selected_option"
                )
            )
        )

    top_simple, groups, children_by_parent = partition_definition_items(items)
    missing_required: list[ChecklistItem] = []
    answered_count = 0
    required_slots = 0
    answered_required_slots = 0

    for item in top_simple:
        response = responses.get((item.id, 1))
        valid = response is not None and _response_is_structurally_valid(item, response)
        if valid:
            answered_count += 1
        if item.is_required:
            required_slots += 1
            if valid:
                answered_required_slots += 1
            else:
                missing_required.append(item)

    for group in groups:
        children = children_by_parent.get(group.id, [])
        n = active_sample_count(children=children, responses=responses)
        min_required = effective_repeat_min(group, children)
        target_n = max(n, min_required)
        if n < min_required:
            for child in children:
                if child.is_required and child not in missing_required:
                    missing_required.append(child)
        for sample_index in range(1, target_n + 1):
            for child in children:
                response = responses.get((child.id, sample_index))
                valid = response is not None and _response_is_structurally_valid(child, response)
                if valid and sample_index <= n:
                    answered_count += 1
                if child.is_required and sample_index <= target_n:
                    required_slots += 1
                    if valid and sample_index <= n:
                        answered_required_slots += 1
                    elif sample_index <= max(n, min_required):
                        if child not in missing_required:
                            missing_required.append(child)

    answerable = [item for item in items if item.item_kind == ChecklistItemKind.SIMPLE]
    return {
        "total_items": len(answerable),
        "required_items": required_slots,
        "answered_required_items": answered_required_slots,
        "missing_required_items": missing_required,
        "answered_items": answered_count,
        "items": items,
        "responses": responses,
    }


def validate_record_ready_for_submission(
    *,
    record: ChecklistRecord,
    items: list[ChecklistItem] | None = None,
    responses: dict[ResponseKey, ChecklistResponse] | None = None,
) -> dict[str, Any]:
    """Raise ValidationError if required completeness is not met."""
    stats = collect_submission_completeness(record=record, items=items, responses=responses)
    _, groups, children_by_parent = partition_definition_items(stats["items"])
    validate_repeating_submit_shape(
        groups=groups,
        children_by_parent=children_by_parent,
        responses=stats["responses"],
    )
    missing = stats["missing_required_items"]
    if missing:
        errors: dict[str, list[str]] = {
            str(item.id): [f"Required item {item.code} must be answered before submission."]
            for item in missing
        }
        errors["completeness"] = [f"{len(missing)} required item(s) remain unanswered."]
        raise ValidationError(errors)
    return stats


def save_checklist_draft_responses(
    *,
    actor: User | None,
    record_id: uuid.UUID,
    answers: dict[Any, Any],
) -> ChecklistRecord:
    """
    Save/update/clear typed draft responses.

    ``answers`` keys may be ``item_id`` (legacy sample_index=1) or
    ``(item_id, sample_index)``.

    Allowed when:
    - ChecklistRecord is DRAFT (initial recording), or
    - ChecklistRecord is SUBMITTED with an eligible active ChecklistCorrection(DRAFT).
    """
    user = _require_authenticated_actor(actor)
    normalized = normalize_answers(answers)

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
        from apps.recording.correction_services import assert_record_editable_for_actor

        assert_record_editable_for_actor(record)

        version_id = task.checklist_version_id
        items = {
            item.id: item
            for item in ChecklistItem.objects.select_related("section", "parent_item").filter(
                section__version_id=version_id
            )
        }
        existing = responses_by_key(
            list(
                ChecklistResponse.objects.select_for_update().filter(checklist_record_id=record.id)
            )
        )

        changed = 0
        errors: dict[str, list[str]] = {}

        for (item_id, sample_index), raw in normalized.items():
            item = items.get(item_id)
            if item is None:
                errors[str(item_id)] = ["Item is not part of this checklist definition."]
                continue
            try:
                assert_sample_index_allowed(item=item, sample_index=sample_index, items_by_id=items)
            except ValidationError as exc:
                if hasattr(exc, "message_dict"):
                    for err_key, msgs in exc.message_dict.items():
                        errors.setdefault(str(err_key), []).extend(str(m) for m in msgs)
                else:
                    errors.setdefault(str(item_id), []).extend(str(m) for m in exc.messages)
                continue

            response_key = (item_id, sample_index)
            if _is_blank_answer(raw):
                current = existing.get(response_key)
                if current is not None:
                    current.delete()
                    existing.pop(response_key, None)
                    changed += 1
                continue

            response = existing.get(response_key) or ChecklistResponse(
                checklist_record=record,
                checklist_item=item,
                sample_index=sample_index,
            )
            response.sample_index = sample_index
            try:
                _apply_typed_value(response=response, item=item, raw=raw)
                response.full_clean()
                response.save()
                existing[response_key] = response
                changed += 1
            except ValidationError as exc:
                if hasattr(exc, "message_dict"):
                    for key_name, msgs in exc.message_dict.items():
                        bucket = errors.setdefault(str(key_name), [])
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


def submit_checklist_record(
    *,
    actor: User | None,
    record_id: uuid.UUID,
) -> ChecklistSubmission:
    """
    Submit a complete DRAFT record and create immutable Submission #1 snapshot.

    Idempotent for already-submitted records with submission #1.
    Does not evaluate PASS/FAIL, HOLD, or QA disposition.
    ChecklistTask status remains PENDING until a later lifecycle unit.
    """
    user = _require_authenticated_actor(actor)

    try:
        with transaction.atomic():
            record = (
                ChecklistRecord.objects.select_related(
                    "organization",
                    "checklist_task",
                    "checklist_task__organization",
                    "checklist_task__checklist_template",
                    "checklist_task__checklist_version",
                    "started_by",
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

            if record.status == ChecklistRecordStatus.SUBMITTED:
                existing = (
                    ChecklistSubmission.objects.select_related(
                        "checklist_record",
                        "submitted_by",
                    )
                    .filter(checklist_record_id=record.id, submission_number=1)
                    .first()
                )
                if existing is not None:
                    return existing
                raise ValidationError(
                    {
                        "status": (
                            "Record is SUBMITTED but Submission #1 is missing. "
                            "Contact support — do not invent a replacement submission."
                        )
                    }
                )

            _assert_record_is_draft(record)
            stats = validate_record_ready_for_submission(record=record)
            responses: dict[ResponseKey, ChecklistResponse] = stats["responses"]

            submission = ChecklistSubmission(
                checklist_record=record,
                submission_number=1,
                submitted_by=user,
            )
            submission.full_clean()
            submission.save()

            snapshot_rows: list[ChecklistSubmissionResponse] = []
            items_by_id = {item.id: item for item in stats["items"]}
            for (item_id, sample_index), response in sorted(
                responses.items(), key=lambda pair: (str(pair[0][0]), pair[0][1])
            ):
                item = items_by_id.get(item_id)
                if item is None or item.item_kind != ChecklistItemKind.SIMPLE:
                    continue
                if not _response_is_structurally_valid(item, response):
                    continue
                snapshot = ChecklistSubmissionResponse(
                    checklist_submission=submission,
                    checklist_item=item,
                    sample_index=sample_index,
                    choice_value=response.choice_value,
                    number_value=response.number_value,
                    text_value=response.text_value,
                    selected_option_id=response.selected_option_id,
                )
                snapshot.full_clean()
                snapshot_rows.append(snapshot)
            ChecklistSubmissionResponse.objects.bulk_create(snapshot_rows)

            transition_record_to_submitted(record)
            record_event(
                event_type="CHECKLIST_RECORD_SUBMITTED",
                actor=user,
                metadata=_record_metadata(
                    record,
                    submission=submission,
                    answered_item_count=len(snapshot_rows),
                ),
            )
    except IntegrityError:
        raced = (
            ChecklistSubmission.objects.select_related(
                "checklist_record",
                "submitted_by",
            )
            .filter(checklist_record_id=record_id, submission_number=1)
            .first()
        )
        if raced is not None:
            return raced
        raise ValidationError({"submission": "Unable to create checklist submission."}) from None

    return ChecklistSubmission.objects.select_related(
        "checklist_record",
        "checklist_record__organization",
        "checklist_record__checklist_task",
        "checklist_record__checklist_task__checklist_template",
        "checklist_record__checklist_task__checklist_version",
        "submitted_by",
    ).get(pk=submission.id)
