"""Batch checklist task orchestration — Phase 07A foundation (no execution records)."""

from __future__ import annotations

import uuid

from django.core.exceptions import ValidationError
from django.db import models

from apps.checklists.models import ChecklistTemplate, ChecklistVersion, ChecklistVersionStatus
from apps.organizations.models import Organization

BATCH_REFERENCE_MAX_LENGTH = 128


class ChecklistTaskStatus(models.TextChoices):
    """Orchestration-only lifecycle for Phase 07A.

    Execution statuses (IN_PROGRESS, SUBMITTED, HOLD, RELEASED, etc.) belong to
    Phase 08+ and must not be invented here.
    """

    PENDING = "PENDING", "Pending"
    CANCELLED = "CANCELLED", "Cancelled"


class ChecklistTask(models.Model):
    """
    Organization-scoped checklist work item for an explicit production-batch reference.

    Does not own responses, reviews, or QA decisions. Does not invent a ProductionBatch master.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="checklist_tasks",
    )
    checklist_template = models.ForeignKey(
        ChecklistTemplate,
        on_delete=models.PROTECT,
        related_name="checklist_tasks",
    )
    checklist_version = models.ForeignKey(
        ChecklistVersion,
        on_delete=models.PROTECT,
        related_name="checklist_tasks",
    )
    batch_reference = models.CharField(
        max_length=BATCH_REFERENCE_MAX_LENGTH,
        help_text=(
            "Explicit external/business production-batch reference. "
            "Not a ProductionBatch FK — full batch master schema is deferred."
        ),
    )
    status = models.CharField(
        max_length=16,
        choices=ChecklistTaskStatus.choices,
        default=ChecklistTaskStatus.PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Checklist task"
        verbose_name_plural = "Checklist tasks"
        permissions = [
            ("manage_checklisttask", "Can manage checklist tasks"),
            (
                "record_checklisttask",
                "Can record checklist task responses (Phase 08 capability foundation)",
            ),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["organization", "checklist_template", "batch_reference"],
                name="sched_task_org_tmpl_batch_uniq",
            ),
        ]
        indexes = [
            models.Index(
                fields=["organization", "status"],
                name="sched_task_org_status_idx",
            ),
            models.Index(
                fields=["organization", "batch_reference"],
                name="sched_task_org_batch_idx",
            ),
            models.Index(
                fields=["checklist_template", "status"],
                name="sched_task_tmpl_status_idx",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.organization.code}/{self.checklist_template.code}/{self.batch_reference}"

    def clean(self) -> None:
        super().clean()
        ref = (self.batch_reference or "").strip()
        if not ref:
            raise ValidationError({"batch_reference": "Batch reference cannot be blank."})
        if len(ref) > BATCH_REFERENCE_MAX_LENGTH:
            raise ValidationError(
                {
                    "batch_reference": (
                        f"Batch reference must be at most {BATCH_REFERENCE_MAX_LENGTH} characters."
                    )
                }
            )
        self.batch_reference = ref

        if self.checklist_template_id and self.organization_id:
            if self.checklist_template.organization_id != self.organization_id:
                raise ValidationError(
                    {
                        "checklist_template": (
                            "Checklist template must belong to the same organization as the task."
                        )
                    }
                )

        if self.checklist_version_id and self.checklist_template_id:
            if self.checklist_version.template_id != self.checklist_template_id:
                raise ValidationError(
                    {
                        "checklist_version": (
                            "Checklist version must belong to the selected checklist template."
                        )
                    }
                )
            if self.checklist_version.status != ChecklistVersionStatus.PUBLISHED:
                raise ValidationError(
                    {
                        "checklist_version": (
                            "Checklist tasks may reference only PUBLISHED checklist versions. "
                            "DRAFT and RETIRED versions are not eligible."
                        )
                    }
                )

    @property
    def is_pending(self) -> bool:
        return self.status == ChecklistTaskStatus.PENDING

    @property
    def is_cancelled(self) -> bool:
        return self.status == ChecklistTaskStatus.CANCELLED
