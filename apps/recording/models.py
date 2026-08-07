"""Checklist recording models — draft working state + immutable submissions."""

from __future__ import annotations

import uuid

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q

from apps.checklists.models import ChecklistItem, ChecklistItemOption
from apps.organizations.models import Organization
from apps.scheduling.models import ChecklistTask


class ChoiceResponseValue(models.TextChoices):
    """Typed YES/NO/NA choice storage — not a QA disposition."""

    YES = "YES", "Yes"
    NO = "NO", "No"
    NA = "NA", "N/A"


class ChecklistRecordStatus(models.TextChoices):
    """Phase 08B record lifecycle — draft working state vs submitted."""

    DRAFT = "DRAFT", "Draft"
    SUBMITTED = "SUBMITTED", "Submitted"


class ChecklistRecord(models.Model):
    """
    Operator recording session bound to exactly one ChecklistTask.

    DRAFT uses mutable ChecklistResponse rows. SUBMITTED freezes answers into
    ChecklistSubmission / ChecklistSubmissionResponse snapshots.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="checklist_records",
    )
    checklist_task = models.OneToOneField(
        ChecklistTask,
        on_delete=models.PROTECT,
        related_name="checklist_record",
    )
    status = models.CharField(
        max_length=16,
        choices=ChecklistRecordStatus.choices,
        default=ChecklistRecordStatus.DRAFT,
    )
    started_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="started_checklist_records",
    )
    started_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-updated_at",)
        verbose_name = "Checklist record"
        verbose_name_plural = "Checklist records"
        indexes = [
            models.Index(
                fields=["organization", "updated_at"],
                name="rec_record_org_updated_idx",
            ),
            models.Index(
                fields=["organization", "status"],
                name="rec_record_org_status_idx",
            ),
        ]

    def __str__(self) -> str:
        return f"Record {self.id} / task {self.checklist_task_id}"

    @property
    def is_draft(self) -> bool:
        return self.status == ChecklistRecordStatus.DRAFT

    @property
    def is_submitted(self) -> bool:
        return self.status == ChecklistRecordStatus.SUBMITTED

    def clean(self) -> None:
        super().clean()
        if self.checklist_task_id and self.organization_id:
            if self.checklist_task.organization_id != self.organization_id:
                raise ValidationError(
                    {
                        "organization": (
                            "Record organization must match the checklist task organization."
                        )
                    }
                )


class ChecklistResponse(models.Model):
    """
    Typed mutable draft answer for one ChecklistItem on a ChecklistRecord.

    Not historical truth after submission — see ChecklistSubmissionResponse.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    checklist_record = models.ForeignKey(
        ChecklistRecord,
        on_delete=models.CASCADE,
        related_name="responses",
    )
    checklist_item = models.ForeignKey(
        ChecklistItem,
        on_delete=models.PROTECT,
        related_name="draft_responses",
    )
    choice_value = models.CharField(
        max_length=8,
        choices=ChoiceResponseValue.choices,
        blank=True,
        default="",
    )
    number_value = models.DecimalField(
        max_digits=14,
        decimal_places=4,
        null=True,
        blank=True,
    )
    text_value = models.TextField(blank=True, default="")
    selected_option = models.ForeignKey(
        ChecklistItemOption,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="draft_responses",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("checklist_item__section__position", "checklist_item__position")
        verbose_name = "Checklist response"
        verbose_name_plural = "Checklist responses"
        constraints = [
            models.UniqueConstraint(
                fields=["checklist_record", "checklist_item"],
                name="rec_response_record_item_uniq",
            ),
            models.CheckConstraint(
                condition=(
                    (
                        ~Q(choice_value="")
                        & Q(number_value__isnull=True)
                        & Q(text_value="")
                        & Q(selected_option__isnull=True)
                    )
                    | (
                        Q(choice_value="")
                        & Q(number_value__isnull=False)
                        & Q(text_value="")
                        & Q(selected_option__isnull=True)
                    )
                    | (
                        Q(choice_value="")
                        & Q(number_value__isnull=True)
                        & ~Q(text_value="")
                        & Q(selected_option__isnull=True)
                    )
                    | (
                        Q(choice_value="")
                        & Q(number_value__isnull=True)
                        & Q(text_value="")
                        & Q(selected_option__isnull=False)
                    )
                ),
                name="rec_response_exactly_one_value",
            ),
        ]
        indexes = [
            models.Index(
                fields=["checklist_record", "updated_at"],
                name="rec_response_record_upd_idx",
            ),
        ]

    def __str__(self) -> str:
        return f"Response {self.id} / item {self.checklist_item_id}"

    def clean(self) -> None:
        super().clean()
        filled = [
            bool(self.choice_value),
            self.number_value is not None,
            bool(self.text_value),
            self.selected_option_id is not None,
        ]
        if sum(1 for flag in filled if flag) != 1:
            raise ValidationError("Exactly one typed response value must be set.")


class ChecklistSubmission(models.Model):
    """
    Immutable submission of a ChecklistRecord.

    Phase 08B creates submission_number=1 only. Future corrections may add 2+.
    Supervisor/QA must bind to a specific submission — not mutable draft rows.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    checklist_record = models.ForeignKey(
        ChecklistRecord,
        on_delete=models.PROTECT,
        related_name="submissions",
    )
    submission_number = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    submitted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="checklist_submissions",
    )
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("checklist_record_id", "submission_number")
        verbose_name = "Checklist submission"
        verbose_name_plural = "Checklist submissions"
        constraints = [
            models.UniqueConstraint(
                fields=["checklist_record", "submission_number"],
                name="rec_submission_record_number_uniq",
            ),
        ]
        indexes = [
            models.Index(
                fields=["checklist_record", "submitted_at"],
                name="rec_submission_record_at_idx",
            ),
        ]

    def __str__(self) -> str:
        return f"Submission #{self.submission_number} / record {self.checklist_record_id}"


class ChecklistSubmissionResponse(models.Model):
    """
    Immutable typed snapshot of one answered item at submission time.

    Survives future mutation/correction of working ChecklistResponse rows.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    checklist_submission = models.ForeignKey(
        ChecklistSubmission,
        on_delete=models.PROTECT,
        related_name="responses",
    )
    checklist_item = models.ForeignKey(
        ChecklistItem,
        on_delete=models.PROTECT,
        related_name="submission_responses",
    )
    choice_value = models.CharField(
        max_length=8,
        choices=ChoiceResponseValue.choices,
        blank=True,
        default="",
    )
    number_value = models.DecimalField(
        max_digits=14,
        decimal_places=4,
        null=True,
        blank=True,
    )
    text_value = models.TextField(blank=True, default="")
    selected_option = models.ForeignKey(
        ChecklistItemOption,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="submission_responses",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("checklist_item__section__position", "checklist_item__position")
        verbose_name = "Checklist submission response"
        verbose_name_plural = "Checklist submission responses"
        constraints = [
            models.UniqueConstraint(
                fields=["checklist_submission", "checklist_item"],
                name="rec_sub_resp_submission_item_uniq",
            ),
            models.CheckConstraint(
                condition=(
                    (
                        ~Q(choice_value="")
                        & Q(number_value__isnull=True)
                        & Q(text_value="")
                        & Q(selected_option__isnull=True)
                    )
                    | (
                        Q(choice_value="")
                        & Q(number_value__isnull=False)
                        & Q(text_value="")
                        & Q(selected_option__isnull=True)
                    )
                    | (
                        Q(choice_value="")
                        & Q(number_value__isnull=True)
                        & ~Q(text_value="")
                        & Q(selected_option__isnull=True)
                    )
                    | (
                        Q(choice_value="")
                        & Q(number_value__isnull=True)
                        & Q(text_value="")
                        & Q(selected_option__isnull=False)
                    )
                ),
                name="rec_sub_resp_exactly_one_value",
            ),
        ]

    def __str__(self) -> str:
        return f"Submission response {self.id} / item {self.checklist_item_id}"

    def clean(self) -> None:
        super().clean()
        filled = [
            bool(self.choice_value),
            self.number_value is not None,
            bool(self.text_value),
            self.selected_option_id is not None,
        ]
        if sum(1 for flag in filled if flag) != 1:
            raise ValidationError("Exactly one typed response value must be set.")
