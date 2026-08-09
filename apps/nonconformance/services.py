"""Nonconformance domain services — generic identity only."""

from __future__ import annotations

import uuid

from django.core.exceptions import PermissionDenied, ValidationError
from django.db import IntegrityError, transaction

from apps.access_control.services import Scope, require_permission
from apps.accounts.models import User
from apps.nonconformance.models import NonConformanceRecord, NonConformanceStatus
from apps.organizations.models import Organization
from apps.organizations.services import normalize_code, normalize_name
from apps.security_audit.services import record_event

VIEW_NONCONFORMANCE = "nonconformance.view_nonconformancerecord"
MANAGE_NONCONFORMANCE = "nonconformance.manage_nonconformance"


def _require_authenticated_actor(actor: User | None) -> User:
    if actor is None or not getattr(actor, "is_authenticated", False) or not actor.is_active:
        raise PermissionDenied("Authentication required.")
    return actor


@transaction.atomic
def create_nonconformance(
    *,
    actor: User | None,
    organization: Organization,
    code: str,
    title: str,
    summary: str = "",
) -> NonConformanceRecord:
    user = _require_authenticated_actor(actor)
    require_permission(user, MANAGE_NONCONFORMANCE, scope=Scope(organization_id=organization.id))
    normalized_code = normalize_code(code)
    normalized_title = normalize_name(title)
    if not normalized_code:
        raise ValidationError({"code": "Code cannot be blank."})
    if not normalized_title:
        raise ValidationError({"title": "Title cannot be blank."})
    record = NonConformanceRecord(
        organization=organization,
        code=normalized_code,
        title=normalized_title,
        summary=(summary or "").strip(),
        status=NonConformanceStatus.OPEN,
        created_by=user,
    )
    try:
        record.full_clean()
        record.save()
    except (ValidationError, IntegrityError) as exc:
        if isinstance(exc, IntegrityError) or "unique" in str(exc).lower():
            raise ValidationError(
                {"code": "A nonconformance with this code already exists in the organization."}
            ) from exc
        raise
    record_event(
        event_type="NONCONFORMANCE_CREATED",
        actor=user,
        metadata={
            "nonconformance_id": str(record.id),
            "organization_id": str(organization.id),
            "code": record.code,
        },
    )
    return record


@transaction.atomic
def close_nonconformance(
    *, actor: User | None, nonconformance_id: uuid.UUID
) -> NonConformanceRecord:
    user = _require_authenticated_actor(actor)
    record = NonConformanceRecord.objects.select_for_update().filter(pk=nonconformance_id).first()
    if record is None:
        raise ValidationError({"nonconformance": "Nonconformance not found."})
    require_permission(
        user, MANAGE_NONCONFORMANCE, scope=Scope(organization_id=record.organization_id)
    )
    if record.status == NonConformanceStatus.CLOSED:
        return record
    record.status = NonConformanceStatus.CLOSED
    record.full_clean()
    record.save(update_fields=["status", "updated_at"])
    record_event(
        event_type="NONCONFORMANCE_CLOSED",
        actor=user,
        metadata={
            "nonconformance_id": str(record.id),
            "organization_id": str(record.organization_id),
            "code": record.code,
        },
    )
    return record
