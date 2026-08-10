"""Customer complaint read selectors — Phase 39."""

from __future__ import annotations

import uuid

from django.db.models import QuerySet

from apps.customer_complaints.models import (
    CustomerComplaintCase,
    CustomerComplaintTimelineEntry,
)


def get_complaint_case(
    *, organization_id: uuid.UUID, case_id: uuid.UUID
) -> CustomerComplaintCase | None:
    return (
        CustomerComplaintCase.objects.filter(pk=case_id, organization_id=organization_id)
        .select_related("owner", "closed_by", "created_by")
        .first()
    )


def get_complaint_by_code(*, organization_id: uuid.UUID, code: str) -> CustomerComplaintCase | None:
    key = (code or "").strip()
    if not key:
        return None
    return CustomerComplaintCase.objects.filter(
        organization_id=organization_id, code__iexact=key
    ).first()


def timeline_for_case(*, case_id: uuid.UUID) -> QuerySet[CustomerComplaintTimelineEntry]:
    return (
        CustomerComplaintTimelineEntry.objects.filter(complaint_case_id=case_id)
        .select_related("actor")
        .order_by("created_at")
    )
