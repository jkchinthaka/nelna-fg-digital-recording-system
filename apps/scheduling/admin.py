"""Django admin for checklist task orchestration, applicability, and schedules."""

from __future__ import annotations

from django.contrib import admin
from django.http import HttpRequest

from apps.scheduling.models import (
    ChecklistApplicabilityRule,
    ChecklistSchedule,
    ChecklistTask,
)


@admin.register(ChecklistTask)
class ChecklistTaskAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = (
        "occurrence_key",
        "trigger_type",
        "batch_reference",
        "checklist_template",
        "checklist_version",
        "organization",
        "status",
        "due_at",
        "created_at",
    )
    list_filter = ("status", "trigger_type", "organization", "checklist_template")
    search_fields = (
        "occurrence_key",
        "batch_reference",
        "checklist_template__code",
        "checklist_template__name",
    )
    autocomplete_fields = (
        "organization",
        "checklist_template",
        "checklist_version",
        "schedule",
        "shift",
    )
    ordering = ("-created_at",)
    readonly_fields = (
        "id",
        "organization",
        "checklist_template",
        "checklist_version",
        "batch_reference",
        "schedule",
        "trigger_type",
        "occurrence_key",
        "shift",
        "window_start_at",
        "window_end_at",
        "due_at",
        "created_at",
        "updated_at",
    )

    def get_readonly_fields(
        self, request: HttpRequest, obj: ChecklistTask | None = None
    ) -> tuple[str, ...]:
        if obj is None:
            return ("id", "created_at", "updated_at")
        return self.readonly_fields

    def has_delete_permission(self, request: HttpRequest, obj: ChecklistTask | None = None) -> bool:
        return False

    def get_actions(self, request: HttpRequest):  # type: ignore[no-untyped-def]
        actions = super().get_actions(request)
        actions.pop("delete_selected", None)
        return actions


@admin.register(ChecklistSchedule)
class ChecklistScheduleAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = (
        "code",
        "name",
        "trigger_type",
        "organization",
        "checklist_template",
        "shift",
        "interval_minutes",
        "missed_policy",
        "is_active",
        "updated_at",
    )
    list_filter = ("trigger_type", "is_active", "organization", "missed_policy")
    search_fields = ("code", "name", "checklist_template__code", "notes")
    autocomplete_fields = (
        "organization",
        "checklist_template",
        "checklist_version",
        "shift",
    )
    readonly_fields = ("id", "created_at", "updated_at")
    ordering = ("organization__code", "code")

    def has_delete_permission(
        self, request: HttpRequest, obj: ChecklistSchedule | None = None
    ) -> bool:
        return False

    def get_actions(self, request: HttpRequest):  # type: ignore[no-untyped-def]
        actions = super().get_actions(request)
        actions.pop("delete_selected", None)
        return actions


@admin.register(ChecklistApplicabilityRule)
class ChecklistApplicabilityRuleAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = (
        "code",
        "name",
        "checklist_template",
        "checklist_version",
        "organization",
        "product",
        "site",
        "department",
        "shift",
        "effective_from",
        "effective_to",
        "is_active",
        "updated_at",
    )
    list_filter = ("is_active", "organization")
    search_fields = (
        "code",
        "name",
        "process_reference",
        "checklist_template__code",
        "notes",
        "product__code",
        "site__code",
        "department__code",
        "shift__code",
    )
    autocomplete_fields = (
        "organization",
        "checklist_template",
        "checklist_version",
        "product",
        "site",
        "department",
        "shift",
    )
    readonly_fields = ("id", "created_at", "updated_at")
    ordering = ("organization__code", "code")

    def has_delete_permission(
        self, request: HttpRequest, obj: ChecklistApplicabilityRule | None = None
    ) -> bool:
        return False

    def get_actions(self, request: HttpRequest):  # type: ignore[no-untyped-def]
        actions = super().get_actions(request)
        actions.pop("delete_selected", None)
        return actions
