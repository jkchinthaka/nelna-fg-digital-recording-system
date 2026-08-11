"""Daily Records print, history, export, and review workflow tests."""

from __future__ import annotations

from datetime import date

import pytest
from django.test import Client
from django.urls import reverse

from apps.checklists.models import ChecklistItem, ChecklistResponseType
from apps.quality.models import QAReviewDecision
from apps.recording.controlled_form_seed import seed_controlled_form_templates
from apps.recording.models import ChecklistRecord, ChecklistSubmission
from apps.recording.services import save_checklist_draft_responses, submit_checklist_record
from apps.recording.synthetic_demo import load_synthetic_demo_data
from apps.reviews.models import SupervisorReviewDecision
from apps.scheduling.services import ensure_controlled_daily_task


def _submit_cleaning(demo, record_date: date) -> ChecklistSubmission:
    seed_controlled_form_templates(actor=demo.admin, organization=demo.organization)
    task = ensure_controlled_daily_task(
        actor=demo.recorder,
        organization_id=demo.organization.id,
        form_code="NMS/PPU/CL/24",
        record_date=record_date,
    )
    from apps.recording.services import start_checklist_recording

    record = start_checklist_recording(actor=demo.recorder, task_id=task.id)
    items = ChecklistItem.objects.filter(section__version=task.checklist_version)
    answers = {}
    for item in items:
        if item.response_type == ChecklistResponseType.YES_NO:
            answers[(item.id, 1)] = "YES"
        elif item.code == "CORR":
            answers[(item.id, 1)] = "DEMO correction note"
    save_checklist_draft_responses(actor=demo.recorder, record_id=record.id, answers=answers)
    return submit_checklist_record(actor=demo.recorder, record_id=record.id)


@pytest.mark.django_db
def test_print_contains_saved_answers(client: Client) -> None:
    demo = load_synthetic_demo_data()
    submission = _submit_cleaning(demo, date(2026, 8, 11))
    client.force_login(demo.recorder)
    printed = client.get(
        reverse("recording:daily_print", kwargs={"record_id": submission.checklist_record_id})
    )
    assert printed.status_code == 200
    assert b"NMS/PPU/CL/24" in printed.content
    assert b"YES" in printed.content
    assert b"DEMO correction note" in printed.content
    assert b"DEMO-REC-001" in printed.content


@pytest.mark.django_db
def test_history_and_csv_export(client: Client) -> None:
    demo = load_synthetic_demo_data()
    _submit_cleaning(demo, date(2026, 8, 11))
    client.force_login(demo.recorder)
    history = client.get(reverse("recording:daily_history"), {"form": "NMS/PPU/CL/24"})
    assert history.status_code == 200
    assert b"NMS/PPU/CL/24" in history.content
    export = client.get(reverse("recording:daily_export_csv"), {"form": "NMS/PPU/CL/24"})
    assert export.status_code == 200
    assert export["Content-Type"].startswith("text/csv")
    assert b"NMS/PPU/CL/24" in export.content


@pytest.mark.django_db
def test_supervisor_and_qa_http_workflow(client: Client) -> None:
    demo = load_synthetic_demo_data()
    submission = _submit_cleaning(demo, date(2026, 8, 12))
    client.force_login(demo.supervisor)
    confirm = client.post(
        reverse(
            "reviews:confirm_decision",
            kwargs={
                "submission_id": submission.id,
                "decision": SupervisorReviewDecision.APPROVED,
            },
        ),
        {"review_note": "DEMO supervisor approve"},
    )
    assert confirm.status_code in {200, 302}
    client.force_login(demo.qa)
    qa = client.post(
        reverse(
            "quality:confirm_decision",
            kwargs={"submission_id": submission.id, "decision": QAReviewDecision.RELEASE},
        ),
        {"review_note": "DEMO qa release"},
    )
    assert qa.status_code in {200, 302}
    client.force_login(demo.recorder)
    printed = client.get(
        reverse("recording:daily_print", kwargs={"record_id": submission.checklist_record_id})
    )
    assert b"DEMO-SUP-001" in printed.content
    assert b"DEMO-QA-001" in printed.content


@pytest.mark.django_db
def test_daily_home_shows_queue_counts(client: Client) -> None:
    demo = load_synthetic_demo_data()
    _submit_cleaning(demo, date(2026, 8, 11))
    client.force_login(demo.recorder)
    home = client.get(reverse("recording:daily_home"), {"date": "2026-08-11"})
    assert home.status_code == 200
    assert b"Awaiting check" in home.content
    assert ChecklistRecord.objects.filter(
        checklist_task__checklist_template__code="NMS/PPU/CL/24"
    ).exists()
