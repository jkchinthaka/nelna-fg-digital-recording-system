"""Admin — soft retention (no hard delete) for nonconformance records."""

from __future__ import annotations

from django.contrib import admin
from django.http import HttpRequest

from apps.nonconformance.models import NonConformanceRecord


@admin.register(NonConformanceRecord)
class NonConformanceRecordAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = ("code", "title", "organization", "status", "created_at")
    list_filter = ("status", "organization")
    search_fields = ("code", "title")
    readonly_fields = ("id", "created_at", "updated_at")
    autocomplete_fields = ("organization", "created_by")

    def has_delete_permission(
        self, request: HttpRequest, obj: NonConformanceRecord | None = None
    ) -> bool:
        return False

    def get_actions(self, request: HttpRequest):  # type: ignore[no-untyped-def]
        actions = super().get_actions(request)
        actions.pop("delete_selected", None)
        return actions
