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
        CHECKLIST_TEMPLATE_CREATED = "CHECKLIST_TEMPLATE_CREATED", "Checklist template created"
        CHECKLIST_TEMPLATE_UPDATED = "CHECKLIST_TEMPLATE_UPDATED", "Checklist template updated"
        CHECKLIST_TEMPLATE_ACTIVATED = (
            "CHECKLIST_TEMPLATE_ACTIVATED",
            "Checklist template activated",
        )
        CHECKLIST_TEMPLATE_DEACTIVATED = (
            "CHECKLIST_TEMPLATE_DEACTIVATED",
            "Checklist template deactivated",
        )
        CHECKLIST_VERSION_CREATED = "CHECKLIST_VERSION_CREATED", "Checklist version created"
        CHECKLIST_VERSION_CLONED = "CHECKLIST_VERSION_CLONED", "Checklist version cloned"
        CHECKLIST_VERSION_PUBLISHED = "CHECKLIST_VERSION_PUBLISHED", "Checklist version published"
        CHECKLIST_VERSION_RETIRED = "CHECKLIST_VERSION_RETIRED", "Checklist version retired"
        CHECKLIST_TASK_CREATED = "CHECKLIST_TASK_CREATED", "Checklist task created"
        CHECKLIST_TASK_CANCELLED = "CHECKLIST_TASK_CANCELLED", "Checklist task cancelled"
        CHECKLIST_RECORD_STARTED = "CHECKLIST_RECORD_STARTED", "Checklist record started"
        CHECKLIST_RECORD_DRAFT_SAVED = (
            "CHECKLIST_RECORD_DRAFT_SAVED",
            "Checklist record draft saved",
        )
        CHECKLIST_RECORD_SUBMITTED = (
            "CHECKLIST_RECORD_SUBMITTED",
            "Checklist record submitted",
        )
        SUPERVISOR_REVIEW_COMPLETED = (
            "SUPERVISOR_REVIEW_COMPLETED",
            "Supervisor review completed",
        )
        CHECKLIST_CORRECTION_STARTED = (
            "CHECKLIST_CORRECTION_STARTED",
            "Checklist correction started",
        )
        CHECKLIST_CORRECTION_RESUBMITTED = (
            "CHECKLIST_CORRECTION_RESUBMITTED",
            "Checklist correction resubmitted",
        )
        QA_REVIEW_COMPLETED = (
            "QA_REVIEW_COMPLETED",
            "QA review disposition completed",
        )
        NONCONFORMANCE_CREATED = "NONCONFORMANCE_CREATED", "Nonconformance created"
        NONCONFORMANCE_CLOSED = "NONCONFORMANCE_CLOSED", "Nonconformance closed"
        CAPA_CREATED = "CAPA_CREATED", "CAPA created"
        CAPA_CLOSED = "CAPA_CLOSED", "CAPA closed"
        SUPPLIER_QUALITY_PROFILE_CREATED = (
            "SUPPLIER_QUALITY_PROFILE_CREATED",
            "Supplier quality profile created",
        )
        SUPPLIER_QUALITY_PROFILE_UPDATED = (
            "SUPPLIER_QUALITY_PROFILE_UPDATED",
            "Supplier quality profile updated",
        )
        SUPPLIER_CERTIFICATE_RECORDED = (
            "SUPPLIER_CERTIFICATE_RECORDED",
            "Supplier certificate recorded",
        )
        SUPPLIER_CERTIFICATE_VERIFIED = (
            "SUPPLIER_CERTIFICATE_VERIFIED",
            "Supplier certificate verified",
        )
        SUPPLIER_QUALITY_EVENT_RECORDED = (
            "SUPPLIER_QUALITY_EVENT_RECORDED",
            "Supplier quality event recorded",
        )

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
