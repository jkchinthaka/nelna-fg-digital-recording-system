"""Permission-aware QA review selectors."""

from __future__ import annotations

import uuid
from typing import Any

from django.core.exceptions import PermissionDenied
from django.db.models import OuterRef, Prefetch, QuerySet, Subquery

from apps.access_control.services import (
    organization_ids_with_permission,
    user_has_permission,
)
from apps.accounts.models import User
from apps.checklists.models import ChecklistItem, ChecklistItemOption, ChecklistSection
from apps.quality.models import QAReview
from apps.quality.services import (
    QA_REVIEW_CHECKLIST_SUBMISSION,
    submission_authorization_scope,
)
from apps.recording.models import (
    ChecklistRecordStatus,
    ChecklistSubmission,
    ChecklistSubmissionResponse,
)
from apps.reviews.models import SupervisorReview, SupervisorReviewDecision
from apps.scheduling.models import ChecklistTaskStatus


def actor_can_access_qa_module(actor: User | None) -> bool:
    return bool(organization_ids_with_permission(actor, QA_REVIEW_CHECKLIST_SUBMISSION))


def list_qa_reviewable_submissions(actor: User | None) -> QuerySet[ChecklistSubmission]:
    """
    Latest SUBMITTED submissions with Supervisor APPROVED and no QAReview.

    Organization-scoped once. No per-row permission queries.
    """
    if actor is None or not getattr(actor, "is_authenticated", False) or not actor.is_active:
        return ChecklistSubmission.objects.none()

    org_ids = organization_ids_with_permission(actor, QA_REVIEW_CHECKLIST_SUBMISSION)
    if not org_ids:
        return ChecklistSubmission.objects.none()

    latest_number = (
        ChecklistSubmission.objects.filter(checklist_record_id=OuterRef("checklist_record_id"))
        .order_by("-submission_number")
        .values("submission_number")[:1]
    )

    return (
        ChecklistSubmission.objects.select_related(
            "submitted_by",
            "checklist_record",
            "checklist_record__organization",
            "checklist_record__checklist_task",
            "checklist_record__checklist_task__checklist_template",
            "checklist_record__checklist_task__checklist_version",
            "supervisor_review",
            "supervisor_review__reviewed_by",
        )
        .filter(
            checklist_record__organization_id__in=org_ids,
            checklist_record__status=ChecklistRecordStatus.SUBMITTED,
            checklist_record__checklist_task__status=ChecklistTaskStatus.PENDING,
            submission_number=Subquery(latest_number),
            supervisor_review__decision=SupervisorReviewDecision.APPROVED,
            qa_review__isnull=True,
        )
        .order_by("-submitted_at")
    )


def get_checklist_submission_for_qa(
    actor: User | None, submission_id: uuid.UUID
) -> ChecklistSubmission | None:
    submission = (
        ChecklistSubmission.objects.select_related(
            "submitted_by",
            "checklist_record",
            "checklist_record__organization",
            "checklist_record__checklist_task",
            "checklist_record__checklist_task__organization",
            "checklist_record__checklist_task__checklist_template",
            "checklist_record__checklist_task__checklist_version",
            "supervisor_review",
            "supervisor_review__reviewed_by",
        )
        .filter(pk=submission_id)
        .first()
    )
    if submission is None:
        return None
    if not user_has_permission(
        actor,
        QA_REVIEW_CHECKLIST_SUBMISSION,
        scope=submission_authorization_scope(submission),
    ):
        raise PermissionDenied("Permission denied.")
    return submission


def get_qa_review(actor: User | None, review_id: uuid.UUID) -> QAReview | None:
    review = (
        QAReview.objects.select_related(
            "organization",
            "reviewed_by",
            "supervisor_review",
            "supervisor_review__reviewed_by",
            "checklist_submission",
            "checklist_submission__submitted_by",
            "checklist_submission__checklist_record",
            "checklist_submission__checklist_record__organization",
            "checklist_submission__checklist_record__checklist_task",
            "checklist_submission__checklist_record__checklist_task__checklist_template",
            "checklist_submission__checklist_record__checklist_task__checklist_version",
        )
        .filter(pk=review_id)
        .first()
    )
    if review is None:
        return None
    if not user_has_permission(
        actor,
        QA_REVIEW_CHECKLIST_SUBMISSION,
        scope=submission_authorization_scope(review.checklist_submission),
    ):
        raise PermissionDenied("Permission denied.")
    return review


def _load_sections(version_id: uuid.UUID) -> list[ChecklistSection]:
    return list(
        ChecklistSection.objects.filter(version_id=version_id)
        .prefetch_related(
            Prefetch(
                "items",
                queryset=ChecklistItem.objects.prefetch_related(
                    Prefetch(
                        "options",
                        queryset=ChecklistItemOption.objects.order_by("position"),
                    )
                ).order_by("position"),
            )
        )
        .order_by("position")
    )


def load_qa_submission_context(
    actor: User | None, submission_id: uuid.UUID
) -> dict[str, Any] | None:
    """QA detail payload using immutable submission snapshots + Supervisor context."""
    submission = get_checklist_submission_for_qa(actor, submission_id)
    if submission is None:
        return None

    record = submission.checklist_record
    if record.status != ChecklistRecordStatus.SUBMITTED:
        return None

    version = record.checklist_task.checklist_version
    sections = _load_sections(version.id)
    snapshot_responses = {
        response.checklist_item_id: response
        for response in ChecklistSubmissionResponse.objects.filter(
            checklist_submission_id=submission.id
        ).select_related("selected_option")
    }

    supervisor = (
        SupervisorReview.objects.select_related("reviewed_by")
        .filter(checklist_submission_id=submission.id)
        .first()
    )
    existing_qa = (
        QAReview.objects.select_related("reviewed_by", "supervisor_review")
        .filter(checklist_submission_id=submission.id)
        .first()
    )

    history_rows = []
    for hist in (
        ChecklistSubmission.objects.select_related("submitted_by")
        .filter(checklist_record_id=record.id)
        .order_by("submission_number")
    ):
        hist_supervisor = (
            SupervisorReview.objects.select_related("reviewed_by")
            .filter(checklist_submission_id=hist.id)
            .first()
        )
        hist_qa = (
            QAReview.objects.select_related("reviewed_by")
            .filter(checklist_submission_id=hist.id)
            .first()
        )
        history_rows.append(
            {
                "submission": hist,
                "supervisor_review": hist_supervisor,
                "qa_review": hist_qa,
            }
        )

    latest = (
        ChecklistSubmission.objects.filter(checklist_record_id=record.id)
        .order_by("-submission_number")
        .first()
    )
    is_latest = latest is not None and latest.id == submission.id

    return {
        "submission": submission,
        "record": record,
        "task": record.checklist_task,
        "sections": sections,
        "snapshot_responses": snapshot_responses,
        "supervisor_review": supervisor,
        "qa_review": existing_qa,
        "history_rows": history_rows,
        "is_latest": is_latest,
        "SupervisorReviewDecision": SupervisorReviewDecision,
    }
