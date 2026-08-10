"""CAPA selectors."""

from __future__ import annotations

import uuid

from django.db.models import QuerySet

from apps.access_control.services import Scope, user_has_permission
from apps.accounts.models import User
from apps.capa.models import CapaHistoryEntry, CorrectiveAction
from apps.capa.services import MANAGE_CAPA, VIEW_CAPA


def list_corrective_actions_for_org(
    *, actor: User, organization_id: uuid.UUID
) -> QuerySet[CorrectiveAction]:
    scope = Scope(organization_id=organization_id)
    if not (
        user_has_permission(actor, VIEW_CAPA, scope=scope)
        or user_has_permission(actor, MANAGE_CAPA, scope=scope)
    ):
        return CorrectiveAction.objects.none()
    return (
        CorrectiveAction.objects.filter(organization_id=organization_id)
        .select_related("owner", "created_by", "nonconformance", "organization")
        .order_by("-created_at")
    )


def list_capa_history(*, capa_id: uuid.UUID) -> QuerySet[CapaHistoryEntry]:
    return CapaHistoryEntry.objects.filter(capa_id=capa_id).select_related("actor")
