"""Django admin for checklist task orchestration and applicability."""

from __future__ import annotations

from django.contrib import admin
from django.http import HttpRequest

from apps.scheduling.models import ChecklistApplicabilityRule, ChecklistTask


@admin.register(ChecklistTask)
class ChecklistTaskAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = (
        "batch_reference",
        "checklist_template",
        "checklist_version",
        "organization",
        "status",
        "created_at",
    )
    list_filter = ("status", "organization", "checklist_template")
    search_fields = (
        "batch_reference",
        "checklist_template__code",
        "checklist_template__name",
    )
    autocomplete_fields = ("organization", "checklist_template", "checklist_version")
    ordering = ("-created_at",)
    readonly_fields = (
        "id",
        "organization",
        "checklist_template",
        "checklist_version",
        "batch_reference",
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
    ordering = ("organization__code", "checklist_template__code")

    def has_delete_permission(
        self, request: HttpRequest, obj: ChecklistApplicabilityRule | None = None
    ) -> bool:
        return False

    def get_actions(self, request: HttpRequest):  # type: ignore[no-untyped-def]
        actions = super().get_actions(request)
        actions.pop("delete_selected", None)
        return actions
