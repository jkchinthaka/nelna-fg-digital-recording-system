"""Admin — soft retention for IQC."""

from __future__ import annotations

from django.contrib import admin

from apps.iqc.models import (
    IncomingReceiptEvent,
    IqcHistoryEntry,
    IqcInspectionCase,
    IqcWorkflowPolicy,
)


class SoftRetentionAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None) -> bool:  # type: ignore[override]
        return False


@admin.register(IncomingReceiptEvent)
class IncomingReceiptEventAdmin(SoftRetentionAdmin):
    list_display = (
        "source_system",
        "source_event_id",
        "erp_receipt_reference",
        "status",
        "created_at",
    )
    list_filter = ("status", "source_system", "organization")
    search_fields = ("source_event_id", "erp_receipt_reference", "supplier_lot")
    readonly_fields = ("id", "created_at", "processed_at")


@admin.register(IqcInspectionCase)
class IqcInspectionCaseAdmin(SoftRetentionAdmin):
    list_display = (
        "receipt",
        "workflow_status",
        "review_required",
        "checklist_task",
        "created_at",
    )
    list_filter = ("workflow_status", "review_required", "organization")
    readonly_fields = (
        "id",
        "frozen_traceability_context",
        "sampling_snapshot",
        "created_at",
        "updated_at",
        "closed_at",
    )


@admin.register(IqcWorkflowPolicy)
class IqcWorkflowPolicyAdmin(SoftRetentionAdmin):
    list_display = (
        "organization",
        "review_required",
        "erp_outbound_enabled",
        "updated_at",
    )
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(IqcHistoryEntry)
class IqcHistoryEntryAdmin(SoftRetentionAdmin):
    list_display = ("event_type", "organization", "actor", "created_at")
    list_filter = ("event_type",)
    readonly_fields = ("id", "created_at", "metadata")
