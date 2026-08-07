"""Permission-aware checklist task selectors."""

from __future__ import annotations

import uuid
from typing import Literal

from django.core.exceptions import PermissionDenied
from django.db.models import QuerySet

from apps.access_control.services import (
    organization_ids_with_permission,
    user_has_permission,
)
from apps.accounts.models import User
from apps.checklists.models import ChecklistTemplate, ChecklistVersion, ChecklistVersionStatus
from apps.organizations.models import Organization
from apps.scheduling.models import ChecklistTask, ChecklistTaskStatus
from apps.scheduling.services import (
    MANAGE_CHECKLIST_TASK,
    RECORD_CHECKLIST_TASK,
    VIEW_CHECKLIST_TASK,
    task_authorization_scope,
)

StatusFilter = Literal["all", "PENDING", "CANCELLED"]


def actor_can_view_checklist_tasks(actor: User | None) -> bool:
    return bool(organization_ids_with_permission(actor, VIEW_CHECKLIST_TASK))


def actor_can_manage_checklist_tasks(actor: User | None) -> bool:
    return bool(organization_ids_with_permission(actor, MANAGE_CHECKLIST_TASK))


def actor_can_record_checklist_tasks(actor: User | None) -> bool:
    """True if actor has recording capability in any organization (Phase 08 prep)."""
    return bool(organization_ids_with_permission(actor, RECORD_CHECKLIST_TASK))


def actor_can_manage_task(actor: User | None, task: ChecklistTask) -> bool:
    if actor is None or not getattr(actor, "is_authenticated", False) or not actor.is_active:
        return False
    return user_has_permission(actor, MANAGE_CHECKLIST_TASK, scope=task_authorization_scope(task))


def actor_can_record_task(actor: User | None, task: ChecklistTask) -> bool:
    """
    Capability check for future Phase 08 recording.

    Does not mutate task state and does not open recording UI in Phase 07B.
    """
    if actor is None or not getattr(actor, "is_authenticated", False) or not actor.is_active:
        return False
    return user_has_permission(actor, RECORD_CHECKLIST_TASK, scope=task_authorization_scope(task))


def task_is_eligible_for_recording(task: ChecklistTask) -> bool:
    """
    Future Phase 08 eligibility contract (documented + testable).

    Requires PENDING status and a historically bound PUBLISHED version.
    Does not grant permission by itself.
    """
    if task.status != ChecklistTaskStatus.PENDING:
        return False
    version = task.checklist_version
    return version.status == ChecklistVersionStatus.PUBLISHED


def manageable_organization_ids(actor: User | None) -> frozenset[uuid.UUID]:
    return frozenset(organization_ids_with_permission(actor, MANAGE_CHECKLIST_TASK))


def organizations_for_task_view(actor: User | None) -> QuerySet[Organization]:
    org_ids = organization_ids_with_permission(actor, VIEW_CHECKLIST_TASK)
    if not org_ids:
        return Organization.objects.none()
    return Organization.objects.filter(pk__in=org_ids).order_by("code")


def organizations_for_task_manage(actor: User | None) -> QuerySet[Organization]:
    org_ids = organization_ids_with_permission(actor, MANAGE_CHECKLIST_TASK)
    if not org_ids:
        return Organization.objects.none()
    return Organization.objects.filter(pk__in=org_ids).order_by("code")


def templates_for_task_manage(
    actor: User | None,
    *,
    organization: Organization | None = None,
) -> QuerySet[ChecklistTemplate]:
    org_ids = organization_ids_with_permission(actor, MANAGE_CHECKLIST_TASK)
    if not org_ids:
        return ChecklistTemplate.objects.none()
    qs = ChecklistTemplate.objects.filter(
        organization_id__in=org_ids, is_active=True
    ).select_related("organization")
    if organization is not None:
        if organization.id not in org_ids:
            return ChecklistTemplate.objects.none()
        qs = qs.filter(organization=organization)
    return qs.order_by("organization__code", "code")


def published_versions_for_template(
    actor: User | None,
    *,
    template: ChecklistTemplate,
) -> QuerySet[ChecklistVersion]:
    org_ids = organization_ids_with_permission(actor, MANAGE_CHECKLIST_TASK)
    if not org_ids or template.organization_id not in org_ids:
        return ChecklistVersion.objects.none()
    return (
        ChecklistVersion.objects.filter(
            template=template,
            status=ChecklistVersionStatus.PUBLISHED,
        )
        .select_related("template", "template__organization")
        .order_by("-version_number")
    )


def list_checklist_tasks(
    actor: User | None,
    *,
    organization: Organization | None = None,
    template: ChecklistTemplate | None = None,
    status: StatusFilter = "all",
    batch_reference: str | None = None,
) -> QuerySet[ChecklistTask]:
    if actor is None or not getattr(actor, "is_authenticated", False) or not actor.is_active:
        return ChecklistTask.objects.none()
    allowed = organization_ids_with_permission(actor, VIEW_CHECKLIST_TASK)
    if not allowed:
        return ChecklistTask.objects.none()

    qs = ChecklistTask.objects.select_related(
        "organization",
        "checklist_template",
        "checklist_version",
    ).filter(organization_id__in=allowed)

    if organization is not None:
        if organization.id not in allowed:
            return ChecklistTask.objects.none()
        qs = qs.filter(organization=organization)
    if template is not None:
        if template.organization_id not in allowed:
            return ChecklistTask.objects.none()
        qs = qs.filter(checklist_template=template)
    if status == ChecklistTaskStatus.PENDING:
        qs = qs.filter(status=ChecklistTaskStatus.PENDING)
    elif status == ChecklistTaskStatus.CANCELLED:
        qs = qs.filter(status=ChecklistTaskStatus.CANCELLED)
    if batch_reference:
        term = batch_reference.strip()
        if term:
            qs = qs.filter(batch_reference__icontains=term)
    return qs.order_by("-created_at")


def list_pending_checklist_tasks(
    actor: User | None,
    *,
    organization: Organization | None = None,
) -> QuerySet[ChecklistTask]:
    return list_checklist_tasks(
        actor,
        organization=organization,
        status="PENDING",
    )


def get_checklist_task(actor: User | None, task_id: uuid.UUID) -> ChecklistTask | None:
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
    if not user_has_permission(actor, VIEW_CHECKLIST_TASK, scope=task_authorization_scope(task)):
        raise PermissionDenied("Permission denied.")
    return task
