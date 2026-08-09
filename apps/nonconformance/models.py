"""Generic NCR foundation — no invented severity, hold, or CAPA automation rules."""

from __future__ import annotations

import uuid

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.functions import Lower

from apps.organizations.models import Organization


class NonConformanceStatus(models.TextChoices):
    """Lifecycle only — business severity / HOLD / disposition remain EVIDENCE REQUIRED."""

    OPEN = "OPEN", "Open"
    CLOSED = "CLOSED", "Closed"


class NonConformanceRecord(models.Model):
    """
    Organization-scoped nonconformance identity for later workflow depth (Phase 12).

    Does not invent root-cause categories, severity scales, or automatic HOLD/RELEASE.
    Soft retention: no hard delete via services/admin.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="nonconformances",
    )
    code = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
    status = models.CharField(
        max_length=16,
        choices=NonConformanceStatus.choices,
        default=NonConformanceStatus.OPEN,
    )
    summary = models.TextField(blank=True, default="")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="nonconformances_created",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("organization__code", "code")
        verbose_name = "Nonconformance record"
        verbose_name_plural = "Nonconformance records"
        permissions = [
            ("manage_nonconformance", "Can manage nonconformance records"),
        ]
        constraints = [
            models.UniqueConstraint(
                Lower("code"),
                "organization",
                name="ncr_org_code_ci_uniq",
            ),
        ]
        indexes = [
            models.Index(
                fields=["organization", "status"],
                name="ncr_org_status_idx",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.organization.code}/{self.code}"

    def clean(self) -> None:
        super().clean()
        if not (self.code or "").strip():
            raise ValidationError({"code": "Code cannot be blank."})
        if not (self.title or "").strip():
            raise ValidationError({"title": "Title cannot be blank."})
