"""Security audit event model — append-oriented auth/RBAC events."""

from __future__ import annotations

import uuid

from django.conf import settings
from django.db import models


class SecurityAuditEvent(models.Model):
    class EventType(models.TextChoices):
        LOGIN_SUCCESS = "LOGIN_SUCCESS", "Login success"
        LOGIN_FAILURE = "LOGIN_FAILURE", "Login failure"
        ACCOUNT_LOCKED = "ACCOUNT_LOCKED", "Account locked"
        ACCOUNT_UNLOCKED = "ACCOUNT_UNLOCKED", "Account unlocked"
        LOGOUT = "LOGOUT", "Logout"
        PASSWORD_CHANGED = "PASSWORD_CHANGED", "Password changed"
        PASSWORD_RESET_BY_ADMIN = "PASSWORD_RESET_BY_ADMIN", "Password reset by admin"
        USER_ACTIVATED = "USER_ACTIVATED", "User activated"
        USER_DEACTIVATED = "USER_DEACTIVATED", "User deactivated"
        ROLE_ASSIGNED = "ROLE_ASSIGNED", "Role assigned"
        ROLE_REVOKED = "ROLE_REVOKED", "Role revoked"
        SHIFT_CREATED = "SHIFT_CREATED", "Shift created"
        SHIFT_UPDATED = "SHIFT_UPDATED", "Shift updated"
        SHIFT_ACTIVATED = "SHIFT_ACTIVATED", "Shift activated"
        SHIFT_DEACTIVATED = "SHIFT_DEACTIVATED", "Shift deactivated"
        FG_PRODUCT_CREATED = "FG_PRODUCT_CREATED", "FG Product created"
        FG_PRODUCT_UPDATED = "FG_PRODUCT_UPDATED", "FG Product updated"
        FG_PRODUCT_ACTIVATED = "FG_PRODUCT_ACTIVATED", "FG Product activated"
        FG_PRODUCT_DEACTIVATED = "FG_PRODUCT_DEACTIVATED", "FG Product deactivated"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_type = models.CharField(max_length=64, choices=EventType.choices)
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="security_audit_actions",
    )
    subject_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="security_audit_subjects",
    )
    request_id = models.CharField(max_length=128, blank=True, default="")
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent_summary = models.CharField(max_length=512, blank=True, default="")
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
        indexes = [
            models.Index(fields=["event_type", "created_at"], name="sa_type_created_idx"),
            models.Index(fields=["subject_user", "created_at"], name="sa_subject_idx"),
            models.Index(fields=["actor", "created_at"], name="sa_actor_idx"),
            models.Index(fields=["request_id"], name="sa_request_id_idx"),
        ]

    def __str__(self) -> str:
        return f"{self.event_type} @ {self.created_at}"
