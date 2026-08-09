"""Permission-aware Supervisor review selectors."""

from __future__ import annotations

import uuid
from typing import Any

from django.core.exceptions import PermissionDenied
from django.db.models import Prefetch, QuerySet

from apps.access_control.services import (
    organization_ids_with_permission,
    user_has_permission,
)
from apps.accounts.models import User
from apps.checklists.models import ChecklistItem, ChecklistItemOption, ChecklistSection
from apps.recording.models import (
    ChecklistRecordStatus,
    ChecklistSubmission,
    ChecklistSubmissionResponse,
)
from apps.recording.repeating import responses_by_key
from apps.recording.snapshot_display import render_snapshot_sections
from apps.reviews.models import SupervisorReview
from apps.reviews.services import (
    REVIEW_CHECKLIST_SUBMISSION,
    submission_authorization_scope,
)


def actor_can_access_review_module(actor: User | None) -> bool:
    return bool(organization_ids_with_permission(actor, REVIEW_CHECKLIST_SUBMISSION))


def list_supervisor_reviewable_submissions(
    actor: User | None,
) -> QuerySet[ChecklistSubmission]:
    """
    SUBMITTED submissions without a SupervisorReview, Organization-scoped once.

    No per-row permission queries.
    """
    if actor is None or not getattr(actor, "is_authenticated", False) or not actor.is_active:
        return ChecklistSubmission.objects.none()

    org_ids = organization_ids_with_permission(actor, REVIEW_CHECKLIST_SUBMISSION)
    if not org_ids:
        return ChecklistSubmission.objects.none()

    return (
        ChecklistSubmission.objects.select_related(
            "submitted_by",
            "checklist_record",
            "checklist_record__organization",
            "checklist_record__checklist_task",
            "checklist_record__checklist_task__checklist_template",
            "checklist_record__checklist_task__checklist_version",
        )
        .filter(
            checklist_record__organization_id__in=org_ids,
            checklist_record__status=ChecklistRecordStatus.SUBMITTED,
            supervisor_review__isnull=True,
        )
        .order_by("-submitted_at")
    )


def get_checklist_submission_for_review(
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
        REVIEW_CHECKLIST_SUBMISSION,
        scope=submission_authorization_scope(submission),
    ):
        raise PermissionDenied("Permission denied.")
    return submission


def get_supervisor_review(actor: User | None, review_id: uuid.UUID) -> SupervisorReview | None:
    review = (
        SupervisorReview.objects.select_related(
            "organization",
            "reviewed_by",
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
        REVIEW_CHECKLIST_SUBMISSION,
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


def load_submission_review_context(
    actor: User | None, submission_id: uuid.UUID
) -> dict[str, Any] | None:
    """Review detail payload using immutable submission snapshots."""
    submission = get_checklist_submission_for_review(actor, submission_id)
    if submission is None:
        return None

    record = submission.checklist_record
    if record.status != ChecklistRecordStatus.SUBMITTED:
        return None

    version = record.checklist_task.checklist_version
    sections = _load_sections(version.id)
    snapshot_responses = responses_by_key(
        list(
            ChecklistSubmissionResponse.objects.filter(
                checklist_submission_id=submission.id
            ).select_related("selected_option")
        )
    )

    existing_review = (
        SupervisorReview.objects.select_related("reviewed_by")
        .filter(checklist_submission_id=submission.id)
        .first()
    )

    return {
        "submission": submission,
        "record": record,
        "task": record.checklist_task,
        "sections": sections,
        "snapshot_responses": snapshot_responses,
        "rendered_sections": render_snapshot_sections(sections, snapshot_responses),
        "review": existing_review,
    }
