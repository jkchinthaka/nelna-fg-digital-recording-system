"""Role template and role-permission governance services (Phase 03C).

OWNER_APPROVED requires non-blank evidence_reference. No migration seed.
create_role_from_template copies permissions into a new Role only (no user assignment).
"""

from __future__ import annotations

import uuid
from collections.abc import Iterable, Sequence

from django.contrib.auth.models import Permission
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import transaction

from apps.access_control.models import Role, RoleTemplate, RoleTemplateBusinessStatus
from apps.accounts.models import User

SOD_PENDING = "PENDING"
_UNSET = object()


def _request_meta(request: object | None) -> tuple[str | None, str | None, str]:
    request_id = getattr(request, "correlation_id", None) if request else None
    ip = None
    ua = ""
    if request is not None and hasattr(request, "META"):
        meta = request.META
        ip = meta.get("REMOTE_ADDR")
        ua = (meta.get("HTTP_USER_AGENT") or "")[:512]
    return request_id, ip, ua


def normalize_template_code(value: str) -> str:
    return (value or "").strip().upper()


def _permission_keys(perms: Iterable[Permission]) -> list[str]:
    return sorted(f"{p.content_type.app_label}.{p.codename}" for p in perms)


def _resolve_permission_ids(permission_ids: Sequence[uuid.UUID | int]) -> list[Permission]:
    ids = [pid for pid in permission_ids if pid is not None]
    if not ids:
        return []
    found = list(Permission.objects.filter(pk__in=ids).select_related("content_type"))
    if len(found) != len(set(ids)):
        raise ValidationError("One or more permission ids are unknown.")
    return found


def _assert_owner_approved_evidence(*, business_status: str, evidence_reference: str) -> str:
    status = (business_status or "").strip().upper() or RoleTemplateBusinessStatus.PROPOSED
    evidence = (evidence_reference or "").strip()
    if status == RoleTemplateBusinessStatus.OWNER_APPROVED and not evidence:
        raise ValidationError(
            "OWNER_APPROVED requires a non-blank evidence_reference "
            "(APR / controlled-document pointer). Do not invent approval."
        )
    return evidence


def list_sod_open_questions() -> list[dict[str, str]]:
    questions = (
        "Can a recorder review their own submission?",
        "Can a Supervisor act as QA for the same submission?",
        "Can QA record production checks?",
        "Can System Admin make QA disposition?",
        "Can a user publish checklist definitions and approve their own content?",
        "Can specification editor approve their own change?",
    )
    return [{"question": q, "status": SOD_PENDING} for q in questions]


def list_proposed_business_categories() -> list[dict[str, str]]:
    return [
        {"category": c, "status": "PROPOSED", "approved": "No"}
        for c in (
            "Operator",
            "Stores",
            "Supervisor",
            "QA Officer",
            "QA Manager",
            "Site Manager",
            "System Administrator",
            "Management",
            "Auditor",
        )
    ]


@transaction.atomic
def set_role_permissions(
    *,
    actor: User | None,
    role_id: uuid.UUID,
    permission_ids: Sequence[uuid.UUID | int],
    request: object | None = None,
) -> Role:
    from apps.security_audit.services import record_event

    try:
        role = Role.objects.select_for_update().get(pk=role_id)
    except ObjectDoesNotExist as exc:
        raise ValidationError("Role not found.") from exc
    perms = _resolve_permission_ids(permission_ids)
    before = _permission_keys(role.permissions.select_related("content_type"))
    role.permissions.set(perms)
    after = _permission_keys(perms)
    request_id, ip, ua = _request_meta(request)
    record_event(
        event_type="ROLE_PERMISSIONS_SET",
        actor=actor,
        request_id=request_id,
        ip_address=ip,
        user_agent_summary=ua,
        metadata={
            "role_id": str(role.id),
            "role_code": role.code,
            "permissions_before": before,
            "permissions_after": after,
            "user_assigned": False,
        },
    )
    return role


@transaction.atomic
def create_role_template(
    *,
    actor: User | None,
    code: str,
    name: str,
    description: str = "",
    business_status: str = RoleTemplateBusinessStatus.PROPOSED,
    evidence_reference: str = "",
    is_active: bool = True,
    permission_ids: Sequence[uuid.UUID | int] | None = None,
    request: object | None = None,
) -> RoleTemplate:
    from apps.security_audit.services import record_event

    status = (business_status or "").strip().upper() or RoleTemplateBusinessStatus.PROPOSED
    if status not in RoleTemplateBusinessStatus.values:
        raise ValidationError("Invalid business_status.")
    evidence = _assert_owner_approved_evidence(
        business_status=status, evidence_reference=evidence_reference
    )
    template = RoleTemplate(
        code=normalize_template_code(code),
        name=(name or "").strip(),
        description=description or "",
        is_active=bool(is_active),
        business_status=status,
        evidence_reference=evidence,
    )
    template.full_clean()
    template.save()
    if permission_ids:
        template.permissions.set(_resolve_permission_ids(permission_ids))
    request_id, ip, ua = _request_meta(request)
    record_event(
        event_type="ROLE_TEMPLATE_CREATED",
        actor=actor,
        request_id=request_id,
        ip_address=ip,
        user_agent_summary=ua,
        metadata={
            "template_id": str(template.id),
            "template_code": template.code,
            "business_status": template.business_status,
            "evidence_reference": template.evidence_reference or None,
            "treated_as_company_approved": False,
            "company_approved": False,
        },
    )
    return template


@transaction.atomic
def update_role_template(
    *,
    actor: User | None,
    template_id: uuid.UUID,
    name: str | object = _UNSET,
    description: str | object = _UNSET,
    is_active: bool | object = _UNSET,
    business_status: str | object = _UNSET,
    evidence_reference: str | object = _UNSET,
    request: object | None = None,
) -> RoleTemplate:
    from apps.security_audit.services import record_event

    try:
        template = RoleTemplate.objects.select_for_update().get(pk=template_id)
    except ObjectDoesNotExist as exc:
        raise ValidationError("Role template not found.") from exc
    before = {
        "name": template.name,
        "description": template.description,
        "is_active": template.is_active,
        "business_status": template.business_status,
        "evidence_reference": template.evidence_reference,
    }
    if name is not _UNSET:
        template.name = str(name or "").strip()
    if description is not _UNSET:
        template.description = str(description or "")
    if is_active is not _UNSET:
        template.is_active = bool(is_active)
    if business_status is not _UNSET:
        next_status = str(business_status or "").strip().upper()
        if next_status not in RoleTemplateBusinessStatus.values:
            raise ValidationError("Invalid business_status.")
        template.business_status = next_status
    next_evidence = template.evidence_reference
    if evidence_reference is not _UNSET:
        next_evidence = str(evidence_reference or "").strip()
    template.evidence_reference = _assert_owner_approved_evidence(
        business_status=template.business_status,
        evidence_reference=next_evidence,
    )
    template.full_clean()
    template.save()
    after = {
        "name": template.name,
        "description": template.description,
        "is_active": template.is_active,
        "business_status": template.business_status,
        "evidence_reference": template.evidence_reference,
    }
    request_id, ip, ua = _request_meta(request)
    record_event(
        event_type="ROLE_TEMPLATE_UPDATED",
        actor=actor,
        request_id=request_id,
        ip_address=ip,
        user_agent_summary=ua,
        metadata={
            "template_id": str(template.id),
            "template_code": template.code,
            "before": before,
            "after": after,
            "treated_as_company_approved": False,
        },
    )
    return template


@transaction.atomic
def set_role_template_permissions(
    *,
    actor: User | None,
    template_id: uuid.UUID,
    permission_ids: Sequence[uuid.UUID | int],
    request: object | None = None,
) -> RoleTemplate:
    from apps.security_audit.services import record_event

    try:
        template = RoleTemplate.objects.select_for_update().get(pk=template_id)
    except ObjectDoesNotExist as exc:
        raise ValidationError("Role template not found.") from exc
    perms = _resolve_permission_ids(permission_ids)
    before = _permission_keys(template.permissions.select_related("content_type"))
    template.permissions.set(perms)
    after = _permission_keys(perms)
    template.save(update_fields=["updated_at"])
    request_id, ip, ua = _request_meta(request)
    record_event(
        event_type="ROLE_TEMPLATE_PERMISSIONS_SET",
        actor=actor,
        request_id=request_id,
        ip_address=ip,
        user_agent_summary=ua,
        metadata={
            "template_id": str(template.id),
            "template_code": template.code,
            "business_status": template.business_status,
            "permissions_before": before,
            "permissions_after": after,
        },
    )
    return template


@transaction.atomic
def create_role_from_template(
    *,
    actor: User | None,
    template_id: uuid.UUID,
    role_code: str,
    role_name: str,
    role_description: str = "",
    request: object | None = None,
) -> Role:
    from apps.access_control.services import create_role, normalize_role_code
    from apps.security_audit.services import record_event

    try:
        template = RoleTemplate.objects.prefetch_related("permissions__content_type").get(
            pk=template_id
        )
    except ObjectDoesNotExist as exc:
        raise ValidationError("Role template not found.") from exc
    if not template.is_active:
        raise ValidationError("Cannot create a role from an inactive template.")
    perms = list(template.permissions.all())
    role = create_role(
        code=normalize_role_code(role_code),
        name=(role_name or "").strip(),
        description=role_description
        or (
            f"Created from role template {template.code} "
            f"(template business_status={template.business_status})."
        ),
        permissions=perms,
    )
    request_id, ip, ua = _request_meta(request)
    record_event(
        event_type="ROLE_PERMISSIONS_SET",
        actor=actor,
        request_id=request_id,
        ip_address=ip,
        user_agent_summary=ua,
        metadata={
            "role_id": str(role.id),
            "role_code": role.code,
            "source_template_id": str(template.id),
            "source_template_code": template.code,
            "source_template_business_status": template.business_status,
            "permissions_after": _permission_keys(perms),
            "user_assigned": False,
            "scoped_role_assignments_created": 0,
            "treated_as_company_approved": False,
        },
    )
    return role
