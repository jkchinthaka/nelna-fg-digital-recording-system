"""Django admin for FG Product master data."""

from __future__ import annotations

from django.contrib import admin
from django.http import HttpRequest

from apps.master_data.models import FGProduct


@admin.register(FGProduct)
class FGProductAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = (
        "code",
        "name",
        "organization",
        "erp_item_code",
        "category",
        "is_active",
        "effective_from",
        "effective_to",
        "updated_at",
    )
    list_filter = ("is_active", "organization", "category")
    search_fields = (
        "code",
        "name",
        "erp_item_code",
        "barcode",
        "category",
        "brand",
        "organization__code",
    )
    readonly_fields = ("id", "created_at", "updated_at")
    autocomplete_fields = ("organization",)
    ordering = ("organization__code", "code")

    def has_delete_permission(self, request: HttpRequest, obj: FGProduct | None = None) -> bool:
        return False

    def get_actions(self, request: HttpRequest):  # type: ignore[no-untyped-def]
        actions = super().get_actions(request)
        actions.pop("delete_selected", None)
        return actions
