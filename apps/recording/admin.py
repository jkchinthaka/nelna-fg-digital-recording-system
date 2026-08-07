"""Django admin for draft checklist recording — support-oriented, no hard delete."""

from __future__ import annotations

from django.contrib import admin
from django.http import HttpRequest

from apps.recording.models import ChecklistRecord, ChecklistResponse


class ChecklistResponseInline(admin.TabularInline):  # type: ignore[type-arg]
    model = ChecklistResponse
    extra = 0
    can_delete = False
    readonly_fields = (
        "id",
        "checklist_item",
        "choice_value",
        "number_value",
        "text_value",
        "selected_option",
        "created_at",
        "updated_at",
    )
    fields = readonly_fields

    def has_add_permission(self, request: HttpRequest, obj: ChecklistRecord | None = None) -> bool:
        return False


@admin.register(ChecklistRecord)
class ChecklistRecordAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = (
        "id",
        "organization",
        "checklist_task",
        "started_by",
        "started_at",
        "updated_at",
    )
    list_filter = ("organization",)
    search_fields = (
        "checklist_task__batch_reference",
        "checklist_task__checklist_template__code",
    )
    ordering = ("-updated_at",)
    inlines = (ChecklistResponseInline,)
    readonly_fields = (
        "id",
        "organization",
        "checklist_task",
        "started_by",
        "started_at",
        "updated_at",
    )

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_delete_permission(
        self, request: HttpRequest, obj: ChecklistRecord | None = None
    ) -> bool:
        return False

    def get_actions(self, request: HttpRequest):  # type: ignore[no-untyped-def]
        actions = super().get_actions(request)
        actions.pop("delete_selected", None)
        return actions


@admin.register(ChecklistResponse)
class ChecklistResponseAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = (
        "id",
        "checklist_record",
        "checklist_item",
        "choice_value",
        "number_value",
        "updated_at",
    )
    search_fields = ("checklist_item__code",)
    ordering = ("-updated_at",)
    readonly_fields = (
        "id",
        "checklist_record",
        "checklist_item",
        "choice_value",
        "number_value",
        "text_value",
        "selected_option",
        "created_at",
        "updated_at",
    )

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_change_permission(
        self, request: HttpRequest, obj: ChecklistResponse | None = None
    ) -> bool:
        return request.method in {"GET", "HEAD", "OPTIONS"}

    def has_delete_permission(
        self, request: HttpRequest, obj: ChecklistResponse | None = None
    ) -> bool:
        return False

    def get_actions(self, request: HttpRequest):  # type: ignore[no-untyped-def]
        actions = super().get_actions(request)
        actions.pop("delete_selected", None)
        return actions
