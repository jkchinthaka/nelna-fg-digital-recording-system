"""Org-scoped rework selectors — Phase 42."""

from __future__ import annotations

from apps.rework.models import ReworkCase, ReworkCaseEvent


def list_cases_for_org(*, organization_id):
    return ReworkCase.objects.filter(organization_id=organization_id).select_related(
        "inspection_task",
        "source_qa_review",
        "source_hold_case",
        "source_ncr",
    )


def list_cases_for_source_batch(*, organization_id, source_batch_reference: str):
    return list_cases_for_org(organization_id=organization_id).filter(
        source_batch_reference=source_batch_reference
    )


def get_case_for_org(*, organization_id, case_id):
    return ReworkCase.objects.select_related(
        "inspection_task",
        "source_qa_review",
        "source_hold_case",
        "source_ncr",
    ).get(organization_id=organization_id, pk=case_id)


def list_events_for_case(*, organization_id, case_id):
    return ReworkCaseEvent.objects.filter(
        organization_id=organization_id,
        case_id=case_id,
    )
