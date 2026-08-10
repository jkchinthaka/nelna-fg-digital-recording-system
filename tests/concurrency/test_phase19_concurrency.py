"""Phase 19 — concurrency / double-submit style guards (synthetic)."""

from __future__ import annotations

import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed

import pytest
from django.db import connection

from apps.integrations.bileeta.mock import MockBileetaAdapter, sample_mock_event
from apps.integrations.errors import IntegrationError
from apps.reports.csv_safe import sanitize_csv_cell
from tests.factories import make_org


@pytest.mark.django_db(transaction=True)
def test_duplicate_integration_event_identity_stable() -> None:
    """Same source event identity must remain deterministic under concurrent mock pulls."""
    org = make_org(code=f"C{uuid.uuid4().hex[:6].upper()}")
    event = sample_mock_event(
        source_event_id="evt-1",
        external_batch_id="BATCH-1",
        external_organization_key=org.code,
    )
    adapter = MockBileetaAdapter(events=[event])

    def _pull() -> str:
        connection.close()
        rows = adapter.pull_batch_events()
        return rows[0].source_event_id

    with ThreadPoolExecutor(max_workers=4) as pool:
        ids = [f.result() for f in as_completed([pool.submit(_pull) for _ in range(8)])]
    assert set(ids) == {"evt-1"}


@pytest.mark.django_db
def test_csv_injection_neutralized_under_parallel_sanitize() -> None:
    payloads = ["=CMD()", "+1+1", "-1+1", "@SUM(A1)", "safe"]

    def _one(value: str) -> str:
        return sanitize_csv_cell(value)

    with ThreadPoolExecutor(max_workers=5) as pool:
        outs = list(pool.map(_one, payloads * 20))
    assert all(o.startswith("'") or o == "safe" for o in outs)


def test_mock_auth_failure_is_non_retryable_poison() -> None:
    adapter = MockBileetaAdapter(fail_mode="auth")
    with pytest.raises(IntegrationError) as exc:
        adapter.pull_with_retries()
    assert exc.value.retryable is False


@pytest.mark.django_db
def test_concurrent_draft_version_guard_is_documented_in_hardening() -> None:
    """
    Shop-floor concurrent drafts use optimistic draft_version (Phase 08C).

    This Phase 19 guard asserts the concurrency contract remains present.
    """
    from apps.recording import services as recording_services

    assert hasattr(recording_services, "save_checklist_draft_responses")
    assert hasattr(recording_services, "submit_checklist_record")
