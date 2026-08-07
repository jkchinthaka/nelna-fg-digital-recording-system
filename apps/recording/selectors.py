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
from apps.recording.models import ChecklistRecord, ChecklistResponse
from apps.scheduling.models import ChecklistTask, ChecklistTaskStatus
from apps.scheduling.selectors import actor_can_record_task, task_is_eligible_for_recording
from apps.scheduling.services import RECORD_CHECKLIST_TASK, task_authorization_scope


def actor_can_access_recording_module(actor: User | None) -> bool:
    return bool(organization_ids_with_permission(actor, RECORD_CHECKLIST_TASK))


def list_recordable_checklist_tasks(actor: User | None) -> QuerySet[ChecklistTask]:
    """
    PENDING tasks the actor may record, scoped by Organization permission once.

    Prefetches optional draft ChecklistRecord for list state without N+1.
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


def load_record_editor_context(actor: User | None, record_id: uuid.UUID) -> dict[str, Any] | None:
    """
    Efficient editor payload: record, sections/items/options, existing responses.

    Uses select_related / prefetch_related — no per-item permission queries.
    """
    record = get_checklist_record(actor, record_id)
    if record is None:
        return None

    version = record.checklist_task.checklist_version
    sections = list(
        ChecklistSection.objects.filter(version_id=version.id)
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
    responses = {
        response.checklist_item_id: response
        for response in ChecklistResponse.objects.filter(
            checklist_record_id=record.id
        ).select_related("selected_option")
    }
    return {
        "record": record,
        "task": record.checklist_task,
        "sections": sections,
        "responses": responses,
    }
