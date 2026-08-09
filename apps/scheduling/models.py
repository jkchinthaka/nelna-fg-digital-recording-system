"""Batch checklist task orchestration — Phase 07A foundation (no execution records)."""

from __future__ import annotations

import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q

from apps.checklists.models import ChecklistTemplate, ChecklistVersion, ChecklistVersionStatus
from apps.master_data.models import FGProduct
from apps.organizations.models import Department, Organization, Shift, Site

BATCH_REFERENCE_MAX_LENGTH = 128


class ChecklistTaskStatus(models.TextChoices):
    """Orchestration-only lifecycle for Phase 07A.

    Execution statuses (IN_PROGRESS, SUBMITTED, HOLD, RELEASED, etc.) belong to
    Phase 08+ and must not be invented here.
    """

    PENDING = "PENDING", "Pending"
    CANCELLED = "CANCELLED", "Cancelled"


class ApplicabilityMatchOutcome(models.TextChoices):
    """
    Explicit resolution outcomes for checklist applicability (Phase 07C).

    Never silently pick the first of multiple matches.
    """

    NO_MATCH = "NO_MATCH", "No match"
    ONE_MATCH = "ONE_MATCH", "One match"
    MULTIPLE_MATCHES = "MULTIPLE_MATCHES", "Multiple matches (conflict)"
    INVALID_INACTIVE_REFERENCE = "INVALID_INACTIVE_REFERENCE", "Invalid or inactive reference"


class ChecklistTask(models.Model):
    """
    Organization-scoped checklist work item for an explicit production-batch reference.

    Does not own responses, reviews, or QA decisions. Does not invent a ProductionBatch master.
    Historical binding: checklist_version is pinned at create time and is not rewritten when
    applicability rules change later (Phase 07C historical safety).
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


class ChecklistApplicabilityRule(models.Model):
    """
    Configurable, version-safe checklist applicability rule (Phase 07C).

    Dimensions justified by existing architecture / evidence gates (APR-013/014):
    Organization (required scope), optional Product / Site / Department / Shift,
    and optional effective dates. Null dimension = wildcard (any).

    Production Line and Process masters are NOT modeled here — no architecture
    evidence; treat as DECISION REQUIRED / EVIDENCE REQUIRED.

    Pins an exact ChecklistVersion (never auto-latest). Matching never silently
    picks the first of multiple rules — see ApplicabilityMatchOutcome.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="checklist_applicability_rules",
    )
    checklist_template = models.ForeignKey(
        ChecklistTemplate,
        on_delete=models.PROTECT,
        related_name="applicability_rules",
    )
    checklist_version = models.ForeignKey(
        ChecklistVersion,
        on_delete=models.PROTECT,
        related_name="applicability_rules",
        help_text="Exact PUBLISHED version pin — never auto-select latest.",
    )
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=255)
    process_reference = models.CharField(
        max_length=128,
        blank=True,
        default="",
        help_text=(
            "Optional free-text process/stage label only — not a Process master. "
            "Process master remains DECISION REQUIRED / EVIDENCE REQUIRED."
        ),
    )
    product = models.ForeignKey(
        FGProduct,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="checklist_applicability_rules",
        help_text="Optional FG Product constraint. Null = any product (wildcard).",
    )
    site = models.ForeignKey(
        Site,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="checklist_applicability_rules",
        help_text="Optional Site constraint. Null = any site (wildcard).",
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="checklist_applicability_rules",
        help_text="Optional Department constraint. Null = any department (wildcard).",
    )
    shift = models.ForeignKey(
        Shift,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="checklist_applicability_rules",
        help_text="Optional Shift constraint. Null = any shift (wildcard).",
    )
    effective_from = models.DateField(
        null=True,
        blank=True,
        help_text="Optional effective-from. Blank = unbounded start.",
    )
    effective_to = models.DateField(
        null=True,
        blank=True,
        help_text="Optional effective-to. Blank = unbounded end.",
    )
    is_active = models.BooleanField(default=True)
    notes = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("organization__code", "checklist_template__code", "created_at")
        verbose_name = "Checklist applicability rule"
        verbose_name_plural = "Checklist applicability rules"
        permissions = [
            (
                "manage_checklistapplicability",
                "Can manage checklist applicability rules",
            ),
            (
                "view_checklistapplicability",
                "Can view and preview checklist applicability",
            ),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["organization", "code"],
                name="sched_appl_org_code_uniq",
            ),
            models.CheckConstraint(
                condition=(
                    Q(effective_to__isnull=True)
                    | Q(effective_from__isnull=True)
                    | Q(effective_to__gte=models.F("effective_from"))
                ),
                name="sched_applicability_effective_window_valid",
            ),
        ]
        indexes = [
            models.Index(
                fields=["organization", "is_active"],
                name="sched_appl_org_act_idx",
            ),
            models.Index(
                fields=["organization", "product", "is_active"],
                name="sched_appl_org_prod_act_idx",
            ),
            models.Index(
                fields=["organization", "site", "is_active"],
                name="sched_appl_org_site_act_idx",
            ),
            models.Index(
                fields=["organization", "department", "is_active"],
                name="sched_appl_org_dept_act_idx",
            ),
            models.Index(
                fields=["organization", "shift", "is_active"],
                name="sched_appl_org_shift_act_idx",
            ),
            models.Index(
                fields=["organization", "effective_from", "effective_to"],
                name="sched_appl_org_effect_idx",
            ),
            models.Index(
                fields=["checklist_template", "is_active"],
                name="sched_appl_tmpl_act_idx",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.organization.code}/{self.code}"

    def clean(self) -> None:
        super().clean()
        errors: dict[str, str] = {}
        if not (self.code or "").strip():
            errors["code"] = "Code cannot be blank."
        if not (self.name or "").strip():
            errors["name"] = "Name cannot be blank."
        self.code = (self.code or "").strip()
        self.name = (self.name or "").strip()
        self.process_reference = (self.process_reference or "").strip()
        if (
            self.effective_to is not None
            and self.effective_from is not None
            and self.effective_to < self.effective_from
        ):
            errors["effective_to"] = "effective_to cannot be earlier than effective_from."

        if self.checklist_template_id and self.organization_id:
            if self.checklist_template.organization_id != self.organization_id:
                errors["checklist_template"] = (
                    "Checklist template must belong to the same organization."
                )
        if self.checklist_version_id and self.checklist_template_id:
            if self.checklist_version.template_id != self.checklist_template_id:
                errors["checklist_version"] = (
                    "Checklist version must belong to the selected checklist template."
                )
            elif self.checklist_version.status != ChecklistVersionStatus.PUBLISHED:
                errors["checklist_version"] = (
                    "Applicability rules may pin only PUBLISHED checklist versions."
                )

        if self.product_id and self.organization_id:
            if self.product.organization_id != self.organization_id:
                errors["product"] = "Product must belong to the same organization."
        if self.site_id and self.organization_id:
            if self.site.organization_id != self.organization_id:
                errors["site"] = "Site must belong to the same organization."
        if self.department_id and self.organization_id:
            if self.department.organization_id != self.organization_id:
                errors["department"] = "Department must belong to the same organization."
            elif (
                self.site_id
                and self.department.site_id
                and self.department.site_id != self.site_id
            ):
                errors["department"] = "Department site must match the rule site when both set."
        if self.shift_id and self.organization_id:
            if self.shift.organization_id != self.organization_id:
                errors["shift"] = "Shift must belong to the same organization."

        if errors:
            raise ValidationError(errors)
