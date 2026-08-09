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
OCCURRENCE_KEY_MAX_LENGTH = 160


class ChecklistTaskStatus(models.TextChoices):
    """Orchestration-only lifecycle (Phases 07A/07E).

    Execution statuses (IN_PROGRESS, SUBMITTED, HOLD, RELEASED, etc.) belong to
    Phase 08+ and must not be invented here.
    OVERDUE / MISSED are schedule timeliness states — never auto-create NCR.
    """

    PENDING = "PENDING", "Pending"
    CANCELLED = "CANCELLED", "Cancelled"
    OVERDUE = "OVERDUE", "Overdue"
    MISSED = "MISSED", "Missed"


class ChecklistTriggerType(models.TextChoices):
    """Architecture-supported task generation triggers (Phase 07E).

    Frequencies / official shift timings remain EVIDENCE REQUIRED — not seeded.
    """

    BATCH = "BATCH", "Batch"
    SHIFT_START = "SHIFT_START", "Shift start"
    SHIFT_END = "SHIFT_END", "Shift end"
    SCHEDULED = "SCHEDULED", "Scheduled window / interval"
    MANUAL = "MANUAL", "Manual"


class ChecklistMissedPolicy(models.TextChoices):
    """Configurable missed-window handling — no automatic NCR.

    Production choice among these options remains DECISION REQUIRED / EVIDENCE REQUIRED.
    """

    MARK_MISSED = "MARK_MISSED", "Mark occurrence MISSED (no NCR)"
    CREATE_OVERDUE = "CREATE_OVERDUE", "Keep/create OVERDUE task (no NCR)"
    SKIP = "SKIP", "Skip missed occurrence (no task)"


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
        blank=True,
        default="",
        help_text=(
            "Explicit external/business production-batch reference for BATCH triggers. "
            "Blank for SHIFT_*/SCHEDULED/MANUAL occurrences. "
            "Not a ProductionBatch FK — full batch master schema is deferred."
        ),
    )
    schedule = models.ForeignKey(
        "ChecklistSchedule",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="tasks",
        help_text="Null for legacy/ad-hoc BATCH tasks created without a schedule definition.",
    )
    trigger_type = models.CharField(
        max_length=16,
        choices=ChecklistTriggerType.choices,
        default=ChecklistTriggerType.BATCH,
    )
    occurrence_key = models.CharField(
        max_length=191,
        default="",
        help_text="Deterministic occurrence identity for idempotent generation / retries.",
    )
    shift = models.ForeignKey(
        Shift,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="checklist_tasks",
        help_text="Configured Shift for SHIFT_* triggers. Null for BATCH/SCHEDULED/MANUAL as applicable.",
    )
    window_start_at = models.DateTimeField(null=True, blank=True)
    window_end_at = models.DateTimeField(null=True, blank=True)
    due_at = models.DateTimeField(null=True, blank=True)
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
                fields=["organization", "checklist_template", "occurrence_key"],
                name="sched_task_org_tmpl_occ_uniq",
            ),
            models.UniqueConstraint(
                fields=["organization", "checklist_template", "batch_reference"],
                condition=Q(batch_reference__gt=""),
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
            models.Index(
                fields=["organization", "trigger_type", "status"],
                name="sched_task_org_trig_st_idx",
            ),
            models.Index(
                fields=["schedule", "status"],
                name="sched_task_sched_status_idx",
            ),
            models.Index(
                fields=["due_at", "status"],
                name="sched_task_due_status_idx",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.organization.code}/{self.checklist_template.code}/{self.batch_reference}"

    def clean(self) -> None:
        super().clean()
        ref = (self.batch_reference or "").strip()
        occ = (self.occurrence_key or "").strip()
        if not occ:
            raise ValidationError({"occurrence_key": "Occurrence key cannot be blank."})
        self.occurrence_key = occ
        if self.trigger_type == ChecklistTriggerType.BATCH:
            if not ref:
                raise ValidationError({"batch_reference": "Batch reference cannot be blank for BATCH tasks."})
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

class ChecklistSchedule(models.Model):
    """
    Configurable recurring / trigger-based checklist schedule (Phase 07E).

    Does not seed Nelna frequencies, shift catalogues, or missed-check NCR policy.
    Celery Beat polls for due occurrences; business interval/window values are
    administrator-configured and remain EVIDENCE REQUIRED until approved.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="checklist_schedules",
    )
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=255)
    checklist_template = models.ForeignKey(
        ChecklistTemplate,
        on_delete=models.PROTECT,
        related_name="schedules",
    )
    checklist_version = models.ForeignKey(
        ChecklistVersion,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="schedules",
        help_text="Optional exact PUBLISHED pin. Null = resolve via Phase 07D at generation time.",
    )
    trigger_type = models.CharField(max_length=16, choices=ChecklistTriggerType.choices)
    shift = models.ForeignKey(
        Shift,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="checklist_schedules",
        help_text="Required for SHIFT_START / SHIFT_END. Uses configured Shift rows only.",
    )
    timezone_name = models.CharField(
        max_length=64,
        default="UTC",
        help_text="IANA timezone for window/shift interpretation. Default UTC until org policy evidenced.",
    )
    window_start_time = models.TimeField(
        null=True,
        blank=True,
        help_text="Optional daily window start for SCHEDULED triggers. Not a seeded Nelna frequency.",
    )
    window_end_time = models.TimeField(
        null=True,
        blank=True,
        help_text="Optional daily window end for SCHEDULED triggers.",
    )
    interval_minutes = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Optional interval in minutes for SCHEDULED triggers. Blank = not interval-based. Do not invent production values.",
    )
    due_grace_minutes = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Optional grace after window end before OVERDUE. Production SLAs EVIDENCE REQUIRED.",
    )
    missed_policy = models.CharField(
        max_length=16,
        choices=ChecklistMissedPolicy.choices,
        default=ChecklistMissedPolicy.MARK_MISSED,
        help_text="Missed-window handling. Never auto-creates NCR. Business choice DECISION REQUIRED.",
    )
    is_active = models.BooleanField(default=True)
    notes = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("organization__code", "code")
        verbose_name = "Checklist schedule"
        verbose_name_plural = "Checklist schedules"
        permissions = [
            ("manage_checklistschedule", "Can manage checklist schedules"),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["organization", "code"],
                name="sched_schedule_org_code_uniq",
            ),
            models.CheckConstraint(
                condition=(
                    Q(interval_minutes__isnull=True) | Q(interval_minutes__gte=1)
                ),
                name="sched_schedule_interval_positive",
            ),
        ]
        indexes = [
            models.Index(
                fields=["organization", "is_active", "trigger_type"],
                name="sched_sched_org_act_trig_idx",
            ),
            models.Index(
                fields=["shift", "is_active"],
                name="sched_sched_shift_act_idx",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.organization.code}/{self.code} ({self.trigger_type})"

    def clean(self) -> None:
        super().clean()
        errors: dict[str, str] = {}
        if not (self.code or "").strip():
            errors["code"] = "Code cannot be blank."
        if not (self.name or "").strip():
            errors["name"] = "Name cannot be blank."
        self.code = (self.code or "").strip()
        self.name = (self.name or "").strip()
        self.timezone_name = (self.timezone_name or "UTC").strip() or "UTC"
        try:
            from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

            ZoneInfo(self.timezone_name)
        except ZoneInfoNotFoundError:
            errors["timezone_name"] = f"Unknown timezone: {self.timezone_name}"
        except Exception:  # noqa: BLE001
            errors["timezone_name"] = f"Unknown timezone: {self.timezone_name}"

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
                    "Schedule may pin only PUBLISHED checklist versions."
                )
        if self.trigger_type in {
            ChecklistTriggerType.SHIFT_START,
            ChecklistTriggerType.SHIFT_END,
        }:
            if not self.shift_id:
                errors["shift"] = "Shift is required for SHIFT_START / SHIFT_END schedules."
        if self.shift_id and self.organization_id:
            if self.shift.organization_id != self.organization_id:
                errors["shift"] = "Shift must belong to the same organization."
        if self.trigger_type == ChecklistTriggerType.BATCH:
            errors["trigger_type"] = (
                "BATCH generation continues to use create_batch_checklist_task; "
                "do not create BATCH ChecklistSchedule rows."
            )
        if (
            self.window_start_time is not None
            and self.window_end_time is not None
            and self.window_start_time == self.window_end_time
            and self.trigger_type == ChecklistTriggerType.SCHEDULED
        ):
            errors["window_end_time"] = (
                "window_end_time must differ from window_start_time for SCHEDULED windows."
            )
        if errors:
            raise ValidationError(errors)

