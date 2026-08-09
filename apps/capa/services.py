"""CAPA domain services — human closure only."""

from __future__ import annotations

import uuid

from django.core.exceptions import PermissionDenied, ValidationError
from django.db import IntegrityError, transaction
from django.utils import timezone

from apps.access_control.services import Scope, require_permission
from apps.accounts.models import User
from apps.capa.models import CorrectiveAction, CorrectiveActionStatus
from apps.nonconformance.models import NonConformanceRecord
from apps.organizations.models import Organization
from apps.organizations.services import normalize_code, normalize_name
from apps.security_audit.services import record_event

VIEW_CAPA = "capa.view_correctiveaction"
MANAGE_CAPA = "capa.manage_capa"


def _require_authenticated_actor(actor: User | None) -> User:
    if actor is None or not getattr(actor, "is_authenticated", False) or not actor.is_active:
        raise PermissionDenied("Authentication required.")
    return actor


@transaction.atomic
def create_corrective_action(
    *,
    actor: User | None,
    organization: Organization,
    code: str,
    title: str,
    summary: str = "",
    nonconformance_id: uuid.UUID | None = None,
) -> CorrectiveAction:
    user = _require_authenticated_actor(actor)
    require_permission(user, MANAGE_CAPA, scope=Scope(organization_id=organization.id))
    normalized_code = normalize_code(code)
    normalized_title = normalize_name(title)
    if not normalized_code:
        raise ValidationError({"code": "Code cannot be blank."})
    if not normalized_title:
        raise ValidationError({"title": "Title cannot be blank."})
    ncr: NonConformanceRecord | None = None
    if nonconformance_id is not None:
        ncr = NonConformanceRecord.objects.filter(
            pk=nonconformance_id, organization_id=organization.id
        ).first()
        if ncr is None:
            raise ValidationError({"nonconformance": "Nonconformance not found in organization."})
    action = CorrectiveAction(
        organization=organization,
        code=normalized_code,
        title=normalized_title,
        summary=(summary or "").strip(),
        nonconformance=ncr,
        status=CorrectiveActionStatus.OPEN,
        created_by=user,
    )
    try:
        action.full_clean()
        action.save()
    except (ValidationError, IntegrityError) as exc:
        if isinstance(exc, IntegrityError) or "unique" in str(exc).lower():
            raise ValidationError(
                {"code": "A CAPA with this code already exists in the organization."}
            ) from exc
        raise
    record_event(
        event_type="CAPA_CREATED",
        actor=user,
        metadata={
            "capa_id": str(action.id),
            "organization_id": str(organization.id),
            "code": action.code,
            "nonconformance_id": str(ncr.id) if ncr else None,
        },
    )
    return action


@transaction.atomic
def close_corrective_action(*, actor: User | None, capa_id: uuid.UUID) -> CorrectiveAction:
    """Human-only CAPA closure. Never callable by AI decision paths."""
    user = _require_authenticated_actor(actor)
    action = CorrectiveAction.objects.select_for_update().filter(pk=capa_id).first()
    if action is None:
        raise ValidationError({"capa": "Corrective action not found."})
    require_permission(user, MANAGE_CAPA, scope=Scope(organization_id=action.organization_id))
    if action.status == CorrectiveActionStatus.CLOSED:
        return action
    action.status = CorrectiveActionStatus.CLOSED
    action.closed_by = user
    action.closed_at = timezone.now()
    action.full_clean()
    action.save(update_fields=["status", "closed_by", "closed_at", "updated_at"])
    record_event(
        event_type="CAPA_CLOSED",
        actor=user,
        metadata={
            "capa_id": str(action.id),
            "organization_id": str(action.organization_id),
            "code": action.code,
        },
    )
    return action
