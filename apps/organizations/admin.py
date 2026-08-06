"""Django admin for organization hierarchy."""

from __future__ import annotations

from django.contrib import admin

from apps.organizations.models import Department, Organization, Site


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = ("code", "name", "is_active", "created_at", "updated_at")
    list_filter = ("is_active",)
    search_fields = ("code", "name")
    readonly_fields = ("id", "created_at", "updated_at")
    ordering = ("code",)


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = ("code", "name", "organization", "is_active", "created_at")
    list_filter = ("is_active", "organization")
    search_fields = ("code", "name", "organization__code")
    readonly_fields = ("id", "created_at", "updated_at")
    autocomplete_fields = ("organization",)
    ordering = ("organization__code", "code")


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = ("code", "name", "organization", "site", "is_active", "created_at")
    list_filter = ("is_active", "organization")
    search_fields = ("code", "name", "organization__code", "site__code")
    readonly_fields = ("id", "created_at", "updated_at")
    autocomplete_fields = ("organization", "site")
    ordering = ("organization__code", "code")
