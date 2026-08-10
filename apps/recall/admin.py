"""Admin — soft retention for recall."""

from __future__ import annotations

from django.contrib import admin

from apps.recall.models import (
    RecallAffectedBatch,
    RecallAffectedProduct,
    RecallCase,
    RecallCommunicationRecord,
    RecallPolicy,
    RecallQuantityLine,
    RecallTimelineEntry,
)


class SoftRetentionAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None) -> bool:  # type: ignore[override]
        return False


@admin.register(RecallCase)
class RecallCaseAdmin(SoftRetentionAdmin):
    list_display = ("code", "status", "organization", "initiated_at", "updated_at")
    list_filter = ("status", "organization")
    search_fields = ("code", "case_type_reference", "reason")
    readonly_fields = ("id", "created_at", "updated_at", "initiated_at", "closed_at")


@admin.register(RecallAffectedProduct)
class RecallAffectedProductAdmin(SoftRetentionAdmin):
    list_display = ("product_reference", "recall_case", "created_at")
    search_fields = ("product_reference",)


@admin.register(RecallAffectedBatch)
class RecallAffectedBatchAdmin(SoftRetentionAdmin):
    list_display = ("batch_reference", "selected_via", "recall_case", "created_at")
    search_fields = ("batch_reference",)


@admin.register(RecallQuantityLine)
class RecallQuantityLineAdmin(SoftRetentionAdmin):
    list_display = ("affected_batch", "recall_case", "updated_at")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(RecallCommunicationRecord)
class RecallCommunicationRecordAdmin(SoftRetentionAdmin):
    list_display = ("reference", "channel_reference", "recall_case", "created_at")
    readonly_fields = ("id", "created_at")


@admin.register(RecallTimelineEntry)
class RecallTimelineEntryAdmin(SoftRetentionAdmin):
    list_display = ("event_type", "recall_case", "created_at")
    readonly_fields = ("id", "created_at", "event_type", "summary", "payload", "actor")


@admin.register(RecallPolicy)
class RecallPolicyAdmin(SoftRetentionAdmin):
    list_display = (
        "organization",
        "external_notification_enabled",
        "erp_distribution_pull_enabled",
        "updated_at",
    )
    readonly_fields = ("id", "created_at", "updated_at")
