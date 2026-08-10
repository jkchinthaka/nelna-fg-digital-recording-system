"""CAPA domain services — Phase 12 configurable foundation.

Human-only closure. No AI final CAPA closure. No auto-create from FAIL/CCP.
"""

from __future__ import annotations

import uuid
from datetime import date
from typing import Any

from django.core.exceptions import PermissionDenied, ValidationError
from django.db import IntegrityError, transaction
from django.utils import timezone

from apps.access_control.services import Scope, require_permission, user_has_permission
from apps.accounts.models import User
from apps.capa.models import (
    CAPA_STATUS_TRANSITIONS,
    CapaActionItem,
    CapaActionItemStatus,
    CapaHistoryEntry,
    CorrectiveAction,
    CorrectiveActionStatus,
)
from apps.nonconformance.models import NonConformanceRecord
from apps.organizations.models import Organization
from apps.organizations.services import normalize_code, normalize_name
from apps.security_audit.services import record_event

VIEW_CAPA = "capa.view_correctiveaction"
CREATE_CAPA = "capa.create_capa"
MANAGE_CAPA = "capa.manage_capa"
CLOSE_CAPA = "capa.close_capa"


def _require_authenticated_actor(actor: User | None) -> User:
    if actor is None or not getattr(actor, "is_authenticated", False) or not actor.is_active:
        raise PermissionDenied("Authentication required.")
    return actor


def _append_history(
    *,
    capa: CorrectiveAction,
    event_type: str,
    actor: User,
    from_status: str = "",
    to_status: str = "",
    note: str = "",
    metadata: dict[str, Any] | None = None,
) -> CapaHistoryEntry:
    return CapaHistoryEntry.objects.create(
        organization_id=capa.organization_id,
        capa=capa,
        event_type=event_type,
        from_status=from_status or "",
        to_status=to_status or "",
        note=(note or "").strip(),
        metadata=metadata or {},
        actor=actor,
    )


def _code_conflict(exc: Exception) -> ValidationError:
    if isinstance(exc, IntegrityError) or "unique" in str(exc).lower():
        return ValidationError(
            {"code": "A CAPA with this code already exists in the organization."}
        )
    if isinstance(exc, ValidationError):
        return exc
    return ValidationError(str(exc))


def _can_close_capa(user: User, organization_id: uuid.UUID) -> bool:
    scope = Scope(organization_id=organization_id)
    return user_has_permission(user, CLOSE_CAPA, scope=scope) or user_has_permission(
        user, MANAGE_CAPA, scope=scope
    )


@transaction.atomic
def create_corrective_action(
    *,
    actor: User | None,
    organization: Organization,
    code: str,
    title: str,
    summary: str = "",
    nonconformance_id: uuid.UUID | None = None,
    owner_id: uuid.UUID | None = None,
) -> CorrectiveAction:
    user = _require_authenticated_actor(actor)
    require_permission(user, CREATE_CAPA, scope=Scope(organization_id=organization.id))
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
        owner_id=owner_id,
        status=CorrectiveActionStatus.OPEN,
        created_by=user,
    )
    try:
        action.full_clean()
        action.save()
    except (ValidationError, IntegrityError) as exc:
        raise _code_conflict(exc) from exc
    _append_history(
        capa=action,
        event_type="CREATED",
        actor=user,
        to_status=action.status,
        note=action.title,
        metadata={"code": action.code, "nonconformance_id": str(ncr.id) if ncr else None},
    )
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
def transition_capa_status(
    *,
    actor: User | None,
    capa_id: uuid.UUID,
    to_status: str,
    note: str = "",
) -> CorrectiveAction:
    user = _require_authenticated_actor(actor)
    action = CorrectiveAction.objects.select_for_update().filter(pk=capa_id).first()
    if action is None:
        raise ValidationError({"capa": "Corrective action not found."})
    require_permission(user, MANAGE_CAPA, scope=Scope(organization_id=action.organization_id))
    if to_status == CorrectiveActionStatus.CLOSED:
        raise ValidationError({"status": "Use close_corrective_action to close a CAPA."})
    allowed = CAPA_STATUS_TRANSITIONS.get(action.status, frozenset())
    if to_status not in allowed:
        raise ValidationError(
            {"status": f"Transition from {action.status} to {to_status} is not allowed."}
        )
    from_status = action.status
    action.status = to_status
    action.full_clean()
    action.save(update_fields=["status", "updated_at"])
    _append_history(
        capa=action,
        event_type="STATUS_CHANGED",
        actor=user,
        from_status=from_status,
        to_status=to_status,
        note=note,
    )
    record_event(
        event_type="CAPA_STATUS_CHANGED",
        actor=user,
        metadata={
            "capa_id": str(action.id),
            "organization_id": str(action.organization_id),
            "code": action.code,
            "from_status": from_status,
            "to_status": to_status,
        },
    )
    return action


@transaction.atomic
def record_capa_verification(
    *,
    actor: User | None,
    capa_id: uuid.UUID,
    notes: str,
) -> CorrectiveAction:
    """Record verification notes and move case to VERIFICATION."""
    user = _require_authenticated_actor(actor)
    action = CorrectiveAction.objects.select_for_update().filter(pk=capa_id).first()
    if action is None:
        raise ValidationError({"capa": "Corrective action not found."})
    require_permission(user, MANAGE_CAPA, scope=Scope(organization_id=action.organization_id))
    if action.status == CorrectiveActionStatus.CLOSED:
        raise ValidationError({"status": "Closed CAPA records cannot be verified."})
    text = (notes or "").strip()
    if not text:
        raise ValidationError({"notes": "Verification notes cannot be blank."})
    from_status = action.status
    if action.status != CorrectiveActionStatus.VERIFICATION:
        allowed = CAPA_STATUS_TRANSITIONS.get(action.status, frozenset())
        if CorrectiveActionStatus.VERIFICATION not in allowed:
            raise ValidationError(
                {
                    "status": (
                        f"Cannot move to VERIFICATION from status {action.status}."
                    )
                }
            )
        action.status = CorrectiveActionStatus.VERIFICATION
    action.verification_notes = text
    action.verified_by = user
    action.verified_at = timezone.now()
    action.full_clean()
    action.save(
        update_fields=[
            "verification_notes",
            "verified_by",
            "verified_at",
            "status",
            "updated_at",
        ]
    )
    _append_history(
        capa=action,
        event_type="VERIFICATION_RECORDED",
        actor=user,
        from_status=from_status,
        to_status=action.status,
        note=text,
    )
    record_event(
        event_type="CAPA_VERIFICATION_RECORDED",
        actor=user,
        metadata={
            "capa_id": str(action.id),
            "organization_id": str(action.organization_id),
            "code": action.code,
            "from_status": from_status,
            "to_status": action.status,
        },
    )
    return action


@transaction.atomic
def record_capa_effectiveness_review(
    *,
    actor: User | None,
    capa_id: uuid.UUID,
    notes: str,
) -> CorrectiveAction:
    """Record effectiveness review and move case to EFFECTIVENESS_REVIEW."""
    user = _require_authenticated_actor(actor)
    action = CorrectiveAction.objects.select_for_update().filter(pk=capa_id).first()
    if action is None:
        raise ValidationError({"capa": "Corrective action not found."})
    require_permission(user, MANAGE_CAPA, scope=Scope(organization_id=action.organization_id))
    if action.status == CorrectiveActionStatus.CLOSED:
        raise ValidationError({"status": "Closed CAPA records cannot be reviewed."})
    text = (notes or "").strip()
    if not text:
        raise ValidationError({"notes": "Effectiveness review notes cannot be blank."})
    from_status = action.status
    if action.status != CorrectiveActionStatus.EFFECTIVENESS_REVIEW:
        allowed = CAPA_STATUS_TRANSITIONS.get(action.status, frozenset())
        if CorrectiveActionStatus.EFFECTIVENESS_REVIEW not in allowed:
            raise ValidationError(
                {
                    "status": (
                        f"Cannot move to EFFECTIVENESS_REVIEW from status {action.status}."
                    )
                }
            )
        action.status = CorrectiveActionStatus.EFFECTIVENESS_REVIEW
    action.effectiveness_notes = text
    action.effectiveness_reviewed_by = user
    action.effectiveness_reviewed_at = timezone.now()
    action.full_clean()
    action.save(
        update_fields=[
            "effectiveness_notes",
            "effectiveness_reviewed_by",
            "effectiveness_reviewed_at",
            "status",
            "updated_at",
        ]
    )
    _append_history(
        capa=action,
        event_type="EFFECTIVENESS_REVIEW_RECORDED",
        actor=user,
        from_status=from_status,
        to_status=action.status,
        note=text,
    )
    record_event(
        event_type="CAPA_EFFECTIVENESS_REVIEWED",
        actor=user,
        metadata={
            "capa_id": str(action.id),
            "organization_id": str(action.organization_id),
            "code": action.code,
            "from_status": from_status,
            "to_status": action.status,
        },
    )
    return action


@transaction.atomic
def add_capa_action_item(
    *,
    actor: User | None,
    capa_id: uuid.UUID,
    description: str,
    owner_id: uuid.UUID | None = None,
    due_date: date | None = None,
) -> CapaActionItem:
    user = _require_authenticated_actor(actor)
    action = CorrectiveAction.objects.select_for_update().filter(pk=capa_id).first()
    if action is None:
        raise ValidationError({"capa": "Corrective action not found."})
    require_permission(user, MANAGE_CAPA, scope=Scope(organization_id=action.organization_id))
    if action.status == CorrectiveActionStatus.CLOSED:
        raise ValidationError({"status": "Cannot add actions to a closed CAPA."})
    desc = (description or "").strip()
    if not desc:
        raise ValidationError({"description": "Description cannot be blank."})
    item = CapaActionItem(
        capa=action,
        description=desc,
        owner_id=owner_id,
        due_date=due_date,
        status=CapaActionItemStatus.OPEN,
    )
    item.full_clean()
    item.save()
    _append_history(
        capa=action,
        event_type="ACTION_ITEM_ADDED",
        actor=user,
        from_status=action.status,
        to_status=action.status,
        note=desc[:200],
        metadata={"action_item_id": str(item.id)},
    )
    record_event(
        event_type="CAPA_ACTION_ADDED",
        actor=user,
        metadata={
            "capa_id": str(action.id),
            "action_item_id": str(item.id),
            "organization_id": str(action.organization_id),
            "code": action.code,
        },
    )
    return item


@transaction.atomic
def complete_capa_action_item(
    *,
    actor: User | None,
    action_item_id: uuid.UUID,
) -> CapaActionItem:
    user = _require_authenticated_actor(actor)
    item = (
        CapaActionItem.objects.select_for_update()
        .select_related("capa")
        .filter(pk=action_item_id)
        .first()
    )
    if item is None:
        raise ValidationError({"action_item": "CAPA action item not found."})
    require_permission(
        user, MANAGE_CAPA, scope=Scope(organization_id=item.capa.organization_id)
    )
    if item.capa.status == CorrectiveActionStatus.CLOSED:
        raise ValidationError({"status": "Cannot complete actions on a closed CAPA."})
    if item.status == CapaActionItemStatus.DONE:
        return item
    if item.status == CapaActionItemStatus.CANCELLED:
        raise ValidationError({"status": "Cancelled action items cannot be completed."})
    item.status = CapaActionItemStatus.DONE
    item.completed_at = timezone.now()
    item.full_clean()
    item.save(update_fields=["status", "completed_at", "updated_at"])
    _append_history(
        capa=item.capa,
        event_type="ACTION_ITEM_COMPLETED",
        actor=user,
        from_status=item.capa.status,
        to_status=item.capa.status,
        metadata={"action_item_id": str(item.id)},
    )
    return item


@transaction.atomic
def close_corrective_action(
    *,
    actor: User | None,
    capa_id: uuid.UUID,
    closure_notes: str = "",
) -> CorrectiveAction:
    """Human-only CAPA closure. Never callable by AI decision paths."""
    user = _require_authenticated_actor(actor)
    action = CorrectiveAction.objects.select_for_update().filter(pk=capa_id).first()
    if action is None:
        raise ValidationError({"capa": "Corrective action not found."})
    if not _can_close_capa(user, action.organization_id):
        raise PermissionDenied("Missing close_capa permission.")
    if action.status == CorrectiveActionStatus.CLOSED:
        return action
    allowed = CAPA_STATUS_TRANSITIONS.get(action.status, frozenset())
    if CorrectiveActionStatus.CLOSED not in allowed:
        raise ValidationError({"status": f"Cannot close CAPA from status {action.status}."})
    from_status = action.status
    action.status = CorrectiveActionStatus.CLOSED
    action.closure_notes = (closure_notes or "").strip()
    action.closed_by = user
    action.closed_at = timezone.now()
    action.full_clean()
    action.save(
        update_fields=["status", "closure_notes", "closed_by", "closed_at", "updated_at"]
    )
    _append_history(
        capa=action,
        event_type="CLOSED",
        actor=user,
        from_status=from_status,
        to_status=CorrectiveActionStatus.CLOSED,
        note=action.closure_notes,
    )
    record_event(
        event_type="CAPA_CLOSED",
        actor=user,
        metadata={
            "capa_id": str(action.id),
            "organization_id": str(action.organization_id),
            "code": action.code,
            "from_status": from_status,
        },
    )
    return action
