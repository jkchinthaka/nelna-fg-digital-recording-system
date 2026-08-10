"""Dispatch quality selectors."""

from __future__ import annotations

import uuid

from django.db.models import QuerySet

from apps.access_control.services import Scope, user_has_permission
from apps.accounts.models import User
from apps.dispatch.models import DispatchQualityRecord, DispatchReleasePolicy
from apps.dispatch.services import MANAGE_DISPATCH, VIEW_DISPATCH


def list_dispatch_records_for_org(
    *, actor: User, organization_id: uuid.UUID
) -> QuerySet[DispatchQualityRecord]:
    scope = Scope(organization_id=organization_id)
    if not (
        user_has_permission(actor, VIEW_DISPATCH, scope=scope)
        or user_has_permission(actor, MANAGE_DISPATCH, scope=scope)
    ):
        return DispatchQualityRecord.objects.none()
    return (
        DispatchQualityRecord.objects.filter(organization_id=organization_id)
        .select_related("owner", "created_by", "qa_review", "organization")
        .order_by("-created_at")
    )


def get_release_policy(*, organization_id: uuid.UUID) -> DispatchReleasePolicy | None:
    return DispatchReleasePolicy.objects.filter(organization_id=organization_id).first()
