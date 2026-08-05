"""Safe Django admin registration for the minimal User model."""

from __future__ import annotations

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from apps.accounts.models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):  # type: ignore[type-arg]
    ordering = ("username",)
    list_display = ("username", "email", "is_staff", "is_active", "date_joined")
    search_fields = ("username", "email", "first_name", "last_name")
