"""Checklist task orchestration services — create/cancel only; no recording."""

from __future__ import annotations

import uuid
from typing import Any

from django.core.exceptions import PermissionDenied, ValidationError
from django.db import IntegrityError, transaction

from apps.access_control.services import Scope, require_permission
from apps.accounts.models import User
from apps.checklists.models import (
    ChecklistTemplate,
    ChecklistVersion,
    ChecklistVersionStatus,
)
from apps.organizations.models import Organization
from apps.scheduling.models import (
    BATCH_REFERENCE_MAX_LENGTH,
    ChecklistTask,
    ChecklistTaskStatus,
)
from apps.security_audit.services import record_event

VIEW_CHECKLIST_TASK = "scheduling.view_checklisttask"
MANAGE_CHECKLIST_TASK = "scheduling.manage_checklisttask"
RECORD_CHECKLIST_TASK = "scheduling.record_checklisttask"


def _require_authenticated_actor(actor: User | None) -> User:
    if actor is None or not getattr(actor, "is_authenticated", False) or not actor.is_active:
        raise PermissionDenied("Authentication required.")
    return actor


def task_authorization_scope(task: ChecklistTask) -> Scope:
    return Scope(organization_id=task.organization_id)


def normalize_batch_reference(raw: str) -> str:
    """Trim only — do not invent case-insensitive batch semantics."""
    if raw is None:
        raise ValidationError({"batch_reference": "Batch reference cannot be blank."})
    value = str(raw).strip()
    if not value:
        raise ValidationError({"batch_reference": "Batch reference cannot be blank."})
    if len(value) > BATCH_REFERENCE_MAX_LENGTH:
        raise ValidationError(
            {
                "batch_reference": (
                    f"Batch reference must be at most {BATCH_REFERENCE_MAX_LENGTH} characters."
                )
            }
        )
    return value


def _task_metadata(task: ChecklistTask) -> dict[str, Any]:
    return {
        "checklist_task_id": str(task.id),
        "organization_id": str(task.organization_id),
        "checklist_template_id": str(task.checklist_template_id),
        "checklist_template_code": task.checklist_template.code,
        "checklist_version_id": str(task.checklist_version_id),
        "checklist_version_number": task.checklist_version.version_number,
        "batch_reference": task.batch_reference,
        "status": task.status,
    }


def create_batch_checklist_task(
    *,
    actor: User | None,
    organization_id: uuid.UUID,
    checklist_template_id: uuid.UUID,
    checklist_version_id: uuid.UUID,
    batch_reference: str,
) -> ChecklistTask:
    """
    Create (or return idempotently) a PENDING checklist task for one batch reference.

    Requires an explicit PUBLISHED ChecklistVersion — never auto-selects latest.
    """
    user = _require_authenticated_actor(actor)
    batch_ref = normalize_batch_reference(batch_reference)

    organization = Organization.objects.filter(pk=organization_id).first()
    if organization is None:
        raise ValidationError({"organization": "Organization not found."})

    require_permission(user, MANAGE_CHECKLIST_TASK, scope=Scope(organization_id=organization.id))

    template = (
        ChecklistTemplate.objects.select_related("organization")
        .filter(pk=checklist_template_id)
        .first()
    )
    if template is None:
        raise ValidationError({"checklist_template": "Checklist template not found."})
    if template.organization_id != organization.id:
        raise ValidationError(
            {"checklist_template": ("Checklist template must belong to the selected organization.")}
        )

    version = (
        ChecklistVersion.objects.select_related("template", "template__organization")
        .filter(pk=checklist_version_id)
        .first()
    )
    if version is None:
        raise ValidationError({"checklist_version": "Checklist version not found."})
    if version.template_id != template.id:
        raise ValidationError(
            {
                "checklist_version": (
                    "Checklist version must belong to the selected checklist template."
                )
            }
        )
    if version.status != ChecklistVersionStatus.PUBLISHED:
        raise ValidationError(
            {
                "checklist_version": (
                    "Checklist tasks may reference only PUBLISHED checklist versions. "
                    "DRAFT and RETIRED versions are not eligible."
                )
            }
        )

    existing = (
        ChecklistTask.objects.select_related(
            "organization", "checklist_template", "checklist_version"
        )
        .filter(
            organization_id=organization.id,
            checklist_template_id=template.id,
            batch_reference=batch_ref,
        )
        .first()
    )
    if existing is not None:
        if existing.checklist_version_id != version.id:
            raise ValidationError(
                {
                    "checklist_version": (
                        "A checklist task already exists for this organization, "
                        "template, and batch reference with a different published version. "
                        "Historical task definition cannot be changed."
                    )
                }
            )
        return existing

    try:
        with transaction.atomic():
            task = ChecklistTask(
                organization=organization,
                checklist_template=template,
                checklist_version=version,
                batch_reference=batch_ref,
                status=ChecklistTaskStatus.PENDING,
            )
            task.full_clean()
            task.save()
            record_event(
                event_type="CHECKLIST_TASK_CREATED",
                actor=user,
                metadata=_task_metadata(task),
            )
    except IntegrityError:
        raced = (
            ChecklistTask.objects.select_related(
                "organization", "checklist_template", "checklist_version"
            )
            .filter(
                organization_id=organization.id,
                checklist_template_id=template.id,
                batch_reference=batch_ref,
            )
            .first()
        )
        if raced is None:
            raise
        if raced.checklist_version_id != version.id:
            raise ValidationError(
                {
                    "checklist_version": (
                        "A checklist task already exists for this organization, "
                        "template, and batch reference with a different published version. "
                        "Historical task definition cannot be changed."
                    )
                }
            ) from None
        return raced

    return ChecklistTask.objects.select_related(
        "organization", "checklist_template", "checklist_version"
    ).get(pk=task.id)


def cancel_checklist_task(*, actor: User | None, task_id: uuid.UUID) -> ChecklistTask:
    """Cancel a PENDING task. Soft cancel only — never hard-delete."""
    user = _require_authenticated_actor(actor)

    with transaction.atomic():
        task = (
            ChecklistTask.objects.select_related(
                "organization", "checklist_template", "checklist_version"
            )
            .select_for_update()
            .filter(pk=task_id)
            .first()
        )
        if task is None:
            raise ValidationError({"task": "Checklist task not found."})

        require_permission(user, MANAGE_CHECKLIST_TASK, scope=task_authorization_scope(task))

        if task.status == ChecklistTaskStatus.CANCELLED:
            return task
        if task.status != ChecklistTaskStatus.PENDING:
            raise ValidationError(
                {"status": f"Cannot cancel checklist task in status {task.status}."}
            )

        task.status = ChecklistTaskStatus.CANCELLED
        task.save(update_fields=["status", "updated_at"])
        record_event(
            event_type="CHECKLIST_TASK_CANCELLED",
            actor=user,
            metadata=_task_metadata(task),
        )
        return task
