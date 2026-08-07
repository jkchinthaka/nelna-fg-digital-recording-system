"""Permission-aware checklist recording selectors."""

from __future__ import annotations

import uuid
from typing import Any

from django.core.exceptions import PermissionDenied
from django.db.models import Prefetch, QuerySet

from apps.access_control.services import (
    organization_ids_with_permission,
    user_has_permission,
)
from apps.accounts.models import User
from apps.checklists.models import ChecklistItem, ChecklistItemOption, ChecklistSection
from apps.recording.models import (
    ChecklistRecord,
    ChecklistRecordStatus,
    ChecklistResponse,
    ChecklistSubmission,
    ChecklistSubmissionResponse,
)
from apps.recording.services import collect_submission_completeness
from apps.scheduling.models import ChecklistTask, ChecklistTaskStatus
from apps.scheduling.selectors import actor_can_record_task, task_is_eligible_for_recording
from apps.scheduling.services import RECORD_CHECKLIST_TASK, task_authorization_scope


def actor_can_access_recording_module(actor: User | None) -> bool:
    return bool(organization_ids_with_permission(actor, RECORD_CHECKLIST_TASK))


def list_recordable_checklist_tasks(actor: User | None) -> QuerySet[ChecklistTask]:
    """
    PENDING tasks the actor may record, scoped by Organization permission once.

    Includes DRAFT and SUBMITTED records for Continue / View Submitted.
    """
    if actor is None or not getattr(actor, "is_authenticated", False) or not actor.is_active:
        return ChecklistTask.objects.none()

    org_ids = organization_ids_with_permission(actor, RECORD_CHECKLIST_TASK)
    if not org_ids:
        return ChecklistTask.objects.none()

    return (
        ChecklistTask.objects.select_related(
            "organization",
            "checklist_template",
            "checklist_version",
            "checklist_record",
        )
        .filter(
            organization_id__in=org_ids,
            status=ChecklistTaskStatus.PENDING,
            checklist_version__status="PUBLISHED",
        )
        .order_by("-created_at")
    )


def get_recordable_task(actor: User | None, task_id: uuid.UUID) -> ChecklistTask | None:
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
        return None
    if not actor_can_record_task(actor, task):
        raise PermissionDenied("Permission denied.")
    if not task_is_eligible_for_recording(task):
        return None
    return task


def get_checklist_record(actor: User | None, record_id: uuid.UUID) -> ChecklistRecord | None:
    record = (
        ChecklistRecord.objects.select_related(
            "organization",
            "started_by",
            "checklist_task",
            "checklist_task__organization",
            "checklist_task__checklist_template",
            "checklist_task__checklist_version",
        )
        .filter(pk=record_id)
        .first()
    )
    if record is None:
        return None
    if not user_has_permission(
        actor, RECORD_CHECKLIST_TASK, scope=task_authorization_scope(record.checklist_task)
    ):
        raise PermissionDenied("Permission denied.")
    return record


def get_checklist_submission(
    actor: User | None, submission_id: uuid.UUID
) -> ChecklistSubmission | None:
    submission = (
        ChecklistSubmission.objects.select_related(
            "submitted_by",
            "checklist_record",
            "checklist_record__organization",
            "checklist_record__started_by",
            "checklist_record__checklist_task",
            "checklist_record__checklist_task__organization",
            "checklist_record__checklist_task__checklist_template",
            "checklist_record__checklist_task__checklist_version",
        )
        .filter(pk=submission_id)
        .first()
    )
    if submission is None:
        return None
    record = submission.checklist_record
    if not user_has_permission(
        actor, RECORD_CHECKLIST_TASK, scope=task_authorization_scope(record.checklist_task)
    ):
        raise PermissionDenied("Permission denied.")
    return submission


def get_latest_checklist_submission_for_record(
    actor: User | None, record_id: uuid.UUID
) -> ChecklistSubmission | None:
    record = get_checklist_record(actor, record_id)
    if record is None:
        return None
    return (
        ChecklistSubmission.objects.select_related("submitted_by", "checklist_record")
        .filter(checklist_record_id=record.id)
        .order_by("-submission_number")
        .first()
    )


def _load_sections(version_id: uuid.UUID) -> list[ChecklistSection]:
    return list(
        ChecklistSection.objects.filter(version_id=version_id)
        .prefetch_related(
            Prefetch(
                "items",
                queryset=ChecklistItem.objects.prefetch_related(
                    Prefetch(
                        "options",
                        queryset=ChecklistItemOption.objects.order_by("position"),
                    )
                ).order_by("position"),
            )
        )
        .order_by("position")
    )


def load_record_editor_context(actor: User | None, record_id: uuid.UUID) -> dict[str, Any] | None:
    """
    Efficient editor payload for DRAFT records.

    Uses select_related / prefetch_related — no per-item permission queries.
    """
    record = get_checklist_record(actor, record_id)
    if record is None:
        return None

    version = record.checklist_task.checklist_version
    sections = _load_sections(version.id)
    responses = {
        response.checklist_item_id: response
        for response in ChecklistResponse.objects.filter(
            checklist_record_id=record.id
        ).select_related("selected_option")
    }
    items = [item for section in sections for item in section.items.all()]
    completeness = collect_submission_completeness(record=record, items=items, responses=responses)
    return {
        "record": record,
        "task": record.checklist_task,
        "sections": sections,
        "responses": responses,
        "completeness": completeness,
    }


def load_submitted_record_context(
    actor: User | None, record_id: uuid.UUID
) -> dict[str, Any] | None:
    """Read-only submitted view using immutable snapshot responses."""
    record = get_checklist_record(actor, record_id)
    if record is None:
        return None
    if record.status != ChecklistRecordStatus.SUBMITTED:
        return None

    submission = (
        ChecklistSubmission.objects.select_related("submitted_by")
        .filter(checklist_record_id=record.id)
        .order_by("-submission_number")
        .first()
    )
    if submission is None:
        return None

    version = record.checklist_task.checklist_version
    sections = _load_sections(version.id)
    snapshot_responses = {
        response.checklist_item_id: response
        for response in ChecklistSubmissionResponse.objects.filter(
            checklist_submission_id=submission.id
        ).select_related("selected_option")
    }
    return {
        "record": record,
        "task": record.checklist_task,
        "submission": submission,
        "sections": sections,
        "snapshot_responses": snapshot_responses,
    }
