"""Read selectors for organization-scoped quality quarantine state."""

from __future__ import annotations

import uuid

from django.db.models import QuerySet

from apps.quality_quarantine.models import QualityQuarantineEvent, QualityQuarantineRecord


def get_quarantine_record(
    *, organization_id: uuid.UUID, quarantine_id: uuid.UUID
) -> QualityQuarantineRecord:
    return QualityQuarantineRecord.objects.get(
        organization_id=organization_id,
        pk=quarantine_id,
    )


def list_quarantines_by_batch(
    *, organization_id: uuid.UUID, batch_reference: str
) -> QuerySet[QualityQuarantineRecord]:
    return QualityQuarantineRecord.objects.filter(
        organization_id=organization_id,
        batch_reference=(batch_reference or "").strip(),
    )


def list_quarantines_by_source(
    *, organization_id: uuid.UUID, source: str, source_reference: str | None = None
) -> QuerySet[QualityQuarantineRecord]:
    queryset = QualityQuarantineRecord.objects.filter(
        organization_id=organization_id,
        source=source,
    )
    if source_reference is not None:
        queryset = queryset.filter(source_reference=source_reference.strip())
    return queryset


def events_for_quarantine(
    *, organization_id: uuid.UUID, quarantine_id: uuid.UUID
) -> QuerySet[QualityQuarantineEvent]:
    return QualityQuarantineEvent.objects.filter(
        quarantine__organization_id=organization_id,
        quarantine_id=quarantine_id,
    ).select_related("actor", "quarantine")
