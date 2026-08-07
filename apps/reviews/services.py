"""Supervisor review services — create immutable decisions only."""

from __future__ import annotations

import uuid
from typing import Any

from django.core.exceptions import PermissionDenied, ValidationError
from django.db import IntegrityError, transaction

from apps.access_control.services import Scope, require_permission
from apps.accounts.models import User
from apps.recording.models import ChecklistRecordStatus, ChecklistSubmission
from apps.reviews.models import SupervisorReview, SupervisorReviewDecision
from apps.security_audit.services import record_event

REVIEW_CHECKLIST_SUBMISSION = "reviews.review_checklistsubmission"

REVIEW_NOTE_MAX_LENGTH = 4000


def _require_authenticated_actor(actor: User | None) -> User:
    if actor is None or not getattr(actor, "is_authenticated", False) or not actor.is_active:
        raise PermissionDenied("Authentication required.")
    return actor


def submission_authorization_scope(submission: ChecklistSubmission) -> Scope:
    return Scope(organization_id=submission.checklist_record.organization_id)


def normalize_review_note(raw: str | None) -> str:
    """Trim only — optional in Phase 09A; do not invent mandatory-reason policy."""
    if raw is None:
        return ""
    value = str(raw).strip()
    if len(value) > REVIEW_NOTE_MAX_LENGTH:
        raise ValidationError(
            {"review_note": f"Review note must be at most {REVIEW_NOTE_MAX_LENGTH} characters."}
        )
    return value


def _review_metadata(review: SupervisorReview) -> dict[str, Any]:
    submission = review.checklist_submission
    record = submission.checklist_record
    task = record.checklist_task
    return {
        "supervisor_review_id": str(review.id),
        "checklist_submission_id": str(submission.id),
        "submission_number": submission.submission_number,
        "checklist_record_id": str(record.id),
        "checklist_task_id": str(task.id),
        "organization_id": str(review.organization_id),
        "checklist_template_id": str(task.checklist_template_id),
        "checklist_version_id": str(task.checklist_version_id),
        "batch_reference": task.batch_reference,
        "decision": review.decision,
    }


def create_supervisor_review(
    *,
    actor: User | None,
    submission_id: uuid.UUID,
    decision: str,
    review_note: str | None = None,
) -> SupervisorReview:
    """
    Record an immutable SupervisorReview for a SUBMITTED ChecklistSubmission.

    Idempotent when the same decision already exists.
    Conflict when an existing review has a different decision.
    Does not reopen records, mutate snapshots, create Submission #2, or start QA.
    Segregation-of-duties (submitted_by != reviewed_by) is EVIDENCE REQUIRED —
    not enforced in Phase 09A.
    """
    user = _require_authenticated_actor(actor)

    if decision not in SupervisorReviewDecision.values:
        raise ValidationError({"decision": "Invalid supervisor review decision."})

    note = normalize_review_note(review_note)

    try:
        with transaction.atomic():
            submission = (
                ChecklistSubmission.objects.select_related(
                    "checklist_record",
                    "checklist_record__organization",
                    "checklist_record__checklist_task",
                    "checklist_record__checklist_task__checklist_template",
                    "checklist_record__checklist_task__checklist_version",
                    "submitted_by",
                )
                .select_for_update()
                .filter(pk=submission_id)
                .first()
            )
            if submission is None:
                raise ValidationError({"submission": "Checklist submission not found."})

            record = submission.checklist_record
            require_permission(
                user,
                REVIEW_CHECKLIST_SUBMISSION,
                scope=submission_authorization_scope(submission),
            )

            if record.status != ChecklistRecordStatus.SUBMITTED:
                raise ValidationError(
                    {
                        "submission": (
                            "Only SUBMITTED checklist records may receive Supervisor review."
                        )
                    }
                )

            existing = (
                SupervisorReview.objects.select_for_update()
                .filter(checklist_submission_id=submission.id)
                .first()
            )
            if existing is not None:
                if existing.decision == decision:
                    return existing
                raise ValidationError(
                    {
                        "decision": (
                            "This submission already has an immutable Supervisor review "
                            f"({existing.decision}). Different decisions cannot overwrite it."
                        )
                    }
                )

            review = SupervisorReview(
                organization_id=record.organization_id,
                checklist_submission=submission,
                decision=decision,
                review_note=note,
                reviewed_by=user,
            )
            review.full_clean()
            review.save()

            record_event(
                event_type="SUPERVISOR_REVIEW_COMPLETED",
                actor=user,
                metadata=_review_metadata(review),
            )
    except IntegrityError:
        raced = (
            SupervisorReview.objects.select_related(
                "organization",
                "checklist_submission",
                "reviewed_by",
            )
            .filter(checklist_submission_id=submission_id)
            .first()
        )
        if raced is not None:
            if raced.decision == decision:
                return raced
            raise ValidationError(
                {
                    "decision": (
                        "This submission already has an immutable Supervisor review "
                        f"({raced.decision}). Different decisions cannot overwrite it."
                    )
                }
            ) from None
        raise ValidationError({"review": "Unable to create Supervisor review."}) from None

    return SupervisorReview.objects.select_related(
        "organization",
        "checklist_submission",
        "checklist_submission__checklist_record",
        "checklist_submission__checklist_record__checklist_task",
        "checklist_submission__checklist_record__checklist_task__checklist_template",
        "checklist_submission__checklist_record__checklist_task__checklist_version",
        "checklist_submission__submitted_by",
        "reviewed_by",
    ).get(pk=review.id)
