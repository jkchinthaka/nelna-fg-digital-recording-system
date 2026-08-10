"""Read selectors for laboratory foundation."""

from __future__ import annotations

import uuid

from django.db.models import QuerySet

from apps.laboratory.models import LabResult, LabResultStatus, LabSample


def samples_for_organization(organization_id: uuid.UUID) -> QuerySet[LabSample]:
    return LabSample.objects.filter(organization_id=organization_id).select_related(
        "product", "site", "registered_by"
    )


def latest_results_for_sample(sample_id: uuid.UUID) -> list[LabResult]:
    rows = (
        LabResult.objects.filter(lab_test__sample_id=sample_id)
        .exclude(status__in=[LabResultStatus.CANCELLED, LabResultStatus.SUPERSEDED])
        .select_related("parameter", "lab_test")
        .order_by("parameter__code", "-revision_number")
    )
    latest: dict[uuid.UUID, LabResult] = {}
    for row in rows:
        if row.parameter_id not in latest:
            latest[row.parameter_id] = row
    return list(latest.values())
