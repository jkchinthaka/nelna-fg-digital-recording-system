"""Read helpers for HACCP foundation."""

from __future__ import annotations

import uuid
from datetime import date

from django.db.models import Q, QuerySet

from apps.haccp.models import ControlPoint, HaccpPlan, HaccpPlanVersion, HaccpPlanVersionStatus


def plans_for_organization(organization_id: uuid.UUID) -> QuerySet[HaccpPlan]:
    return HaccpPlan.objects.filter(organization_id=organization_id, is_active=True)


def versions_for_plan(plan_id: uuid.UUID) -> QuerySet[HaccpPlanVersion]:
    return HaccpPlanVersion.objects.filter(plan_id=plan_id).order_by("-version_number")


def control_points_for_version(plan_version_id: uuid.UUID) -> QuerySet[ControlPoint]:
    return ControlPoint.objects.filter(plan_version_id=plan_version_id).select_related(
        "process_step", "hazard"
    )


def approved_versions_effective_on(
    *,
    organization_id: uuid.UUID,
    as_of: date,
) -> QuerySet[HaccpPlanVersion]:
    """Return APPROVED versions whose effective window covers as_of (null bounds = open)."""
    qs = HaccpPlanVersion.objects.filter(
        plan__organization_id=organization_id,
        status=HaccpPlanVersionStatus.APPROVED,
    )
    qs = qs.filter(_effective_window_q(as_of))
    return qs.select_related("plan")


def _effective_window_q(as_of: date) -> Q:
    return (Q(effective_from__isnull=True) | Q(effective_from__lte=as_of)) & (
        Q(effective_to__isnull=True) | Q(effective_to__gte=as_of)
    )
