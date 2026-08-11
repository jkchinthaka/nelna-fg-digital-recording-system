"""Nonconformance / Hold selectors."""

from __future__ import annotations

import uuid

from django.db.models import QuerySet

from apps.access_control.services import Scope, user_has_permission
from apps.accounts.models import User
from apps.nonconformance.models import (
    HoldCase,
    NonConformanceRecord,
    QualityCaseHistoryEntry,
)
from apps.nonconformance.services import MANAGE_HOLD, MANAGE_NCR, VIEW_NONCONFORMANCE


def list_nonconformances_for_org(
    *, actor: User, organization_id: uuid.UUID
) -> QuerySet[NonConformanceRecord]:
    scope = Scope(organization_id=organization_id)
    if not (
        user_has_permission(actor, VIEW_NONCONFORMANCE, scope=scope)
        or user_has_permission(actor, MANAGE_NCR, scope=scope)
    ):
        return NonConformanceRecord.objects.none()
    return (
        NonConformanceRecord.objects.filter(organization_id=organization_id)
        .select_related("owner", "created_by", "organization")
        .order_by("-created_at")
    )


def list_hold_cases_for_org(*, actor: User, organization_id: uuid.UUID) -> QuerySet[HoldCase]:
    scope = Scope(organization_id=organization_id)
    if not (
        user_has_permission(actor, MANAGE_HOLD, scope=scope)
        or user_has_permission(actor, "nonconformance.view_holdcase", scope=scope)
        or user_has_permission(actor, MANAGE_NCR, scope=scope)
    ):
        return HoldCase.objects.none()
    return (
        HoldCase.objects.filter(organization_id=organization_id)
        .select_related("owner", "opened_by", "nonconformance", "organization")
        .order_by("-opened_at")
    )


def list_case_history(
    *,
    organization_id: uuid.UUID,
    case_kind: str,
    case_id: uuid.UUID,
) -> QuerySet[QualityCaseHistoryEntry]:
    return QualityCaseHistoryEntry.objects.filter(
        organization_id=organization_id,
        case_kind=case_kind,
        case_id=case_id,
    ).select_related("actor")
