"""Product recall / withdrawal case management — Phase 37.

Controlled case management only. Does not invent regulatory recall classes,
reporting times, or notification obligations. External notification and ERP
distribution pulls remain dual-gated OFF (APR-062).
"""

from __future__ import annotations

import uuid

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.functions import Lower

from apps.organizations.models import Organization


class RecallCaseStatus(models.TextChoices):
    """Technical workflow statuses — not regulatory classification."""

    DRAFT = "DRAFT", "Draft"
    OPEN = "OPEN", "Open"
    IN_PROGRESS = "IN_PROGRESS", "In progress"
    RECONCILING = "RECONCILING", "Quantity reconciliation"
    PENDING_CLOSURE = "PENDING_CLOSURE", "Pending closure"
    CLOSED = "CLOSED", "Closed"
    CANCELLED = "CANCELLED", "Cancelled"


RECALL_STATUS_TRANSITIONS: dict[str, frozenset[str]] = {
    RecallCaseStatus.DRAFT: frozenset(
        {RecallCaseStatus.OPEN, RecallCaseStatus.CANCELLED}
    ),
    RecallCaseStatus.OPEN: frozenset(
        {
            RecallCaseStatus.IN_PROGRESS,
            RecallCaseStatus.RECONCILING,
            RecallCaseStatus.PENDING_CLOSURE,
            RecallCaseStatus.CANCELLED,
        }
    ),
    RecallCaseStatus.IN_PROGRESS: frozenset(
        {
            RecallCaseStatus.RECONCILING,
            RecallCaseStatus.PENDING_CLOSURE,
            RecallCaseStatus.CANCELLED,
        }
    ),
    RecallCaseStatus.RECONCILING: frozenset(
        {
            RecallCaseStatus.IN_PROGRESS,
            RecallCaseStatus.PENDING_CLOSURE,
            RecallCaseStatus.CANCELLED,
        }
    ),
    RecallCaseStatus.PENDING_CLOSURE: frozenset(
        {
            RecallCaseStatus.CLOSED,
            RecallCaseStatus.IN_PROGRESS,
            RecallCaseStatus.CANCELLED,
        }
    ),
    RecallCaseStatus.CLOSED: frozenset(),
    RecallCaseStatus.CANCELLED: frozenset(),
}


class RecallCase(models.Model):
    """
    Organization-scoped recall/withdrawal case.

    case_type_reference is an opaque company/procedure reference — not a seeded
    regulatory class catalogue.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="recall_cases",
    )
    code = models.CharField(max_length=64, help_text="Opaque case ID / reference.")
    case_type_reference = models.CharField(
        max_length=128,
        blank=True,
        default="",
        help_text="Opaque type/procedure reference — not a regulatory class invent.",
    )
    reason = models.TextField()
    status = models.CharField(
        max_length=32,
        choices=RecallCaseStatus.choices,
        default=RecallCaseStatus.DRAFT,
    )
    scope_notes = models.TextField(
        blank=True,
        default="",
        help_text="Free-text scope description — company SOPs EVIDENCE REQUIRED.",
    )
    initiated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="recall_cases_initiated",
        null=True,
        blank=True,
    )
    initiated_at = models.DateTimeField(null=True, blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="recall_cases_owned",
        null=True,
        blank=True,
    )
    closed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="recall_cases_closed",
        null=True,
        blank=True,
    )
    closed_at = models.DateTimeField(null=True, blank=True)
    closure_notes = models.TextField(blank=True, default="")
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Recall case"
        verbose_name_plural = "Recall cases"
        constraints = [
            models.UniqueConstraint(
                Lower("code"),
                "organization",
                name="recall_case_org_code_ci_uniq",
            ),
        ]
        indexes = [
            models.Index(fields=["organization", "status"]),
            models.Index(fields=["organization", "code"]),
        ]
        permissions = [
            ("view_recall", "Can view recall/withdrawal cases"),
            (
                "initiate_recall",
                "Can initiate recall/withdrawal cases (high-risk; not System Admin by default)",
            ),
            ("manage_recallcase", "Can update recall case scope and quantities"),
            ("close_recall", "Can close recall/withdrawal cases"),
            ("manage_recallpolicy", "Can manage recall policy stubs"),
        ]

    def __str__(self) -> str:
        return f"{self.code}/{self.status}"

    def clean(self) -> None:
        super().clean()
        code = (self.code or "").strip()
        if not code:
            raise ValidationError({"code": "Case ID / code is required."})
        self.code = code
        if not (self.reason or "").strip():
            raise ValidationError({"reason": "Reason is required."})


class RecallAffectedProduct(models.Model):
    """Opaque product reference on a recall case — no invented SKU catalogue."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recall_case = models.ForeignKey(
        RecallCase,
        on_delete=models.PROTECT,
        related_name="affected_products",
    )
    product_reference = models.CharField(max_length=128)
    notes = models.CharField(max_length=512, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("product_reference"),
                "recall_case",
                name="recall_product_case_ref_ci_uniq",
            ),
        ]

    def __str__(self) -> str:
        return self.product_reference


class RecallAffectedBatch(models.Model):
    """Affected batch / lot reference; optional genealogy node link."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recall_case = models.ForeignKey(
        RecallCase,
        on_delete=models.PROTECT,
        related_name="affected_batches",
    )
    batch_reference = models.CharField(max_length=128)
    genealogy_node_id = models.UUIDField(
        null=True,
        blank=True,
        help_text="Optional Phase 36 GenealogyNode id — reference only.",
    )
    genealogy_node_kind = models.CharField(max_length=32, blank=True, default="")
    selected_via = models.CharField(
        max_length=64,
        blank=True,
        default="MANUAL",
        help_text="MANUAL | GENEALOGY_EXPANSION — how the batch entered the case.",
    )
    notes = models.CharField(max_length=512, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("batch_reference"),
                "recall_case",
                name="recall_batch_case_ref_ci_uniq",
            ),
        ]
        indexes = [
            models.Index(fields=["recall_case", "batch_reference"]),
        ]

    def __str__(self) -> str:
        return self.batch_reference


class RecallQuantityLine(models.Model):
    """
    Quantity reconciliation shell for an affected batch.

    Opaque quantity/UOM strings from ERP/operations — no invented acceptable
    variance thresholds or pass/fail math.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recall_case = models.ForeignKey(
        RecallCase,
        on_delete=models.PROTECT,
        related_name="quantity_lines",
    )
    affected_batch = models.ForeignKey(
        RecallAffectedBatch,
        on_delete=models.PROTECT,
        related_name="quantity_lines",
    )
    produced_reference = models.CharField(max_length=128, blank=True, default="")
    distributed_reference = models.CharField(max_length=128, blank=True, default="")
    remaining_reference = models.CharField(max_length=128, blank=True, default="")
    recovered_reference = models.CharField(max_length=128, blank=True, default="")
    disposed_reference = models.CharField(max_length=128, blank=True, default="")
    reworked_reference = models.CharField(max_length=128, blank=True, default="")
    uom_reference = models.CharField(max_length=64, blank=True, default="")
    erp_source_system = models.CharField(max_length=64, blank=True, default="")
    erp_source_event_id = models.CharField(max_length=128, blank=True, default="")
    notes = models.TextField(blank=True, default="")
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="recall_quantity_lines_updated",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["recall_case", "affected_batch"],
                name="recall_qty_case_batch_uniq",
            ),
        ]

    def __str__(self) -> str:
        return f"QTY/{self.affected_batch.batch_reference}"


class RecallCommunicationRecord(models.Model):
    """
    Communication reference / evidence shell.

    Does not send messages. Automatic authority/customer contact remains
    dual-gated OFF (APR-062).
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recall_case = models.ForeignKey(
        RecallCase,
        on_delete=models.PROTECT,
        related_name="communications",
    )
    reference = models.CharField(max_length=128)
    channel_reference = models.CharField(
        max_length=128,
        blank=True,
        default="",
        help_text="Opaque channel/procedure reference — not an auto-send.",
    )
    audience_reference = models.CharField(
        max_length=128,
        blank=True,
        default="",
        help_text="Opaque audience label — no customer PII invent.",
    )
    evidence_attachment_id = models.UUIDField(null=True, blank=True)
    notes = models.TextField(blank=True, default="")
    recorded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="recall_communications_recorded",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("created_at",)

    def __str__(self) -> str:
        return self.reference


class RecallTimelineEntry(models.Model):
    """Immutable append-only recall case timeline."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recall_case = models.ForeignKey(
        RecallCase,
        on_delete=models.PROTECT,
        related_name="timeline_entries",
    )
    event_type = models.CharField(max_length=64)
    summary = models.CharField(max_length=512)
    payload = models.JSONField(default=dict, blank=True)
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="recall_timeline_entries",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("created_at",)
        indexes = [
            models.Index(fields=["recall_case", "created_at"]),
        ]

    def __str__(self) -> str:
        return f"{self.event_type}@{self.created_at:%Y-%m-%d}"


class RecallPolicy(models.Model):
    """Org policy stubs — external notify / ERP pull dual-gated OFF (APR-062)."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.OneToOneField(
        Organization,
        on_delete=models.PROTECT,
        related_name="recall_policy",
    )
    external_notification_enabled = models.BooleanField(
        default=False,
        help_text="Org stub only — still requires RECALL_EXTERNAL_NOTIFICATION_APPROVED.",
    )
    erp_distribution_pull_enabled = models.BooleanField(
        default=False,
        help_text="Org stub only — still requires RECALL_ERP_DISTRIBUTION_PULL_APPROVED.",
    )
    procedure_reference = models.CharField(max_length=255, blank=True, default="")
    notes = models.TextField(blank=True, default="")
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="recall_policies_updated",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Recall policy"
        verbose_name_plural = "Recall policies"

    def __str__(self) -> str:
        return f"{self.organization.code} recall policy"
