"""Django admin for roles, role templates, and scoped assignments.

Prefer governance_services / assign_role / revoke_role_assignment for audited mutations.
RoleAdmin.save_related routes permission M2M changes through set_role_permissions.
"""

from __future__ import annotations

from django.contrib import admin, messages
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpRequest

from apps.access_control.governance_services import set_role_permissions
from apps.access_control.models import Role, RoleTemplate, ScopedRoleAssignment


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = ("code", "name", "is_active", "created_at", "updated_at")
    list_filter = ("is_active",)
    search_fields = ("code", "name")
    filter_horizontal = ("permissions",)
    readonly_fields = ("id", "created_at", "updated_at")
    ordering = ("code",)

    def save_related(
        self,
        request: HttpRequest,
        form: object,
        formsets: object,
        change: bool,
    ) -> None:
        for formset in formsets:  # type: ignore[union-attr]
            self.save_formset(request, form, formset, change=change)
        instance = form.instance  # type: ignore[attr-defined]
        cleaned = getattr(form, "cleaned_data", {}) or {}
        perms = cleaned.get("permissions")
        if perms is not None:
            set_role_permissions(
                actor=request.user if request.user.is_authenticated else None,
                role_id=instance.id,
                permission_ids=[p.pk for p in perms],
                request=request,
            )
        elif hasattr(form, "save_m2m"):
            form.save_m2m()  # type: ignore[attr-defined]


@admin.register(RoleTemplate)
class RoleTemplateAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = (
        "code",
        "name",
        "business_status",
        "is_active",
        "created_at",
        "updated_at",
    )
    list_filter = ("is_active", "business_status")
    search_fields = ("code", "name", "evidence_reference")
    filter_horizontal = ("permissions",)
    readonly_fields = ("id", "created_at", "updated_at")
    ordering = ("code",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "id",
                    "code",
                    "name",
                    "description",
                    "is_active",
                    "business_status",
                    "evidence_reference",
                    "permissions",
                    "created_at",
                    "updated_at",
                ),
                "description": (
                    "Prefer create_role_template / update_role_template / "
                    "set_role_template_permissions for audited changes. "
                    "OWNER_APPROVED requires APR evidence — never invent."
                ),
            },
        ),
    )


@admin.register(ScopedRoleAssignment)
class ScopedRoleAssignmentAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = (
        "user",
        "role",
        "organization",
        "site",
        "department",
        "is_active",
        "valid_from",
        "valid_until",
        "created_at",
    )
    list_filter = ("is_active", "role", "organization")
    search_fields = (
        "user__employee_code",
        "user__username",
        "role__code",
        "organization__code",
    )
    autocomplete_fields = ("user", "role", "organization", "site", "department", "assigned_by")
    readonly_fields = ("id", "created_at", "updated_at")
    ordering = ("-created_at",)

    def save_model(
        self,
        request: HttpRequest,
        obj: ScopedRoleAssignment,
        form: object,
        change: bool,
    ) -> None:
        try:
            obj.full_clean()
            super().save_model(request, obj, form, change)
        except IntegrityError as exc:
            messages.error(
                request,
                "An active assignment with this scope already exists.",
            )
            raise ValidationError("An active assignment with this scope already exists.") from exc
