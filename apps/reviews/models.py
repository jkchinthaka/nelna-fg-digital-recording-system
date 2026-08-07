"""Supervisor review models — immutable decisions bound to ChecklistSubmission."""

from __future__ import annotations

import uuid

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

from apps.organizations.models import Organization
from apps.recording.models import ChecklistRecordStatus, ChecklistSubmission


class SupervisorReviewDecision(models.TextChoices):
    """
    Provisional technical workflow labels — not formal QA policy.

    APPROVED: Supervisor review complete; may eventually enter future QA stage.
    Does NOT mean QA approved, RELEASED, or product acceptance.

    RETURNED_FOR_CORRECTION: Correction/resubmission will eventually be required.
    Phase 09A records the decision only — does not reopen or resubmit.
    """

    APPROVED = "APPROVED", "Approved (supervisor review complete)"
    RETURNED_FOR_CORRECTION = (
        "RETURNED_FOR_CORRECTION",
        "Returned for correction",
    )


class SupervisorReview(models.Model):
    """
    Immutable Supervisor decision for exactly one ChecklistSubmission.

    Future Submission #2 receives its own SupervisorReview. Do not bind reviews
    to ChecklistRecord mutable draft responses.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="supervisor_reviews",
    )
    checklist_submission = models.OneToOneField(
        ChecklistSubmission,
        on_delete=models.PROTECT,
        related_name="supervisor_review",
    )
    decision = models.CharField(
        max_length=32,
        choices=SupervisorReviewDecision.choices,
    )
    review_note = models.TextField(blank=True, default="")
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="supervisor_reviews",
    )
    reviewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-reviewed_at",)
        verbose_name = "Supervisor review"
        verbose_name_plural = "Supervisor reviews"
        permissions = [
            (
                "review_checklistsubmission",
                "Can review checklist submissions (Supervisor review)",
            ),
        ]
        indexes = [
            models.Index(
                fields=["organization", "reviewed_at"],
                name="rev_sup_org_reviewed_idx",
            ),
            models.Index(
                fields=["organization", "decision"],
                name="rev_sup_org_decision_idx",
            ),
        ]

    def __str__(self) -> str:
        return f"SupervisorReview {self.decision} / submission {self.checklist_submission_id}"

    def clean(self) -> None:
        super().clean()
        if not self.checklist_submission_id:
            return
        submission = self.checklist_submission
        record = submission.checklist_record
        if self.organization_id and record.organization_id != self.organization_id:
            raise ValidationError(
                {
                    "organization": (
                        "Review organization must match the submission record organization."
                    )
                }
            )
        if record.status != ChecklistRecordStatus.SUBMITTED:
            raise ValidationError(
                {
                    "checklist_submission": (
                        "Supervisor review requires a SUBMITTED checklist record."
                    )
                }
            )
