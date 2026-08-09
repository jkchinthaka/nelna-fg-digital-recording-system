"""Generic CAPA foundation — human closure only; no invented CAPA matrices."""

from __future__ import annotations

import uuid

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.functions import Lower

from apps.nonconformance.models import NonConformanceRecord
from apps.organizations.models import Organization


class CorrectiveActionStatus(models.TextChoices):
    OPEN = "OPEN", "Open"
    CLOSED = "CLOSED", "Closed"


class CorrectiveAction(models.Model):
    """
    Organization-scoped CAPA identity.

    Closure is human-only via services. No AI final CAPA closure.
    Optional link to a NonConformanceRecord. Soft retention: no hard delete.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="corrective_actions",
    )
    code = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
    status = models.CharField(
        max_length=16,
        choices=CorrectiveActionStatus.choices,
        default=CorrectiveActionStatus.OPEN,
    )
    summary = models.TextField(blank=True, default="")
    nonconformance = models.ForeignKey(
        NonConformanceRecord,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="corrective_actions",
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="corrective_actions_created",
    )
    closed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="corrective_actions_closed",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ("organization__code", "code")
        verbose_name = "Corrective action"
        verbose_name_plural = "Corrective actions"
        permissions = [
            ("manage_capa", "Can manage corrective actions"),
        ]
        constraints = [
            models.UniqueConstraint(
                Lower("code"),
                "organization",
                name="capa_org_code_ci_uniq",
            ),
        ]
        indexes = [
            models.Index(
                fields=["organization", "status"],
                name="capa_org_status_idx",
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
        if self.nonconformance_id and self.organization_id:
            ncr = self.nonconformance
            if ncr is not None and ncr.organization_id != self.organization_id:
                raise ValidationError(
                    {"nonconformance": "CAPA organization must match linked NCR organization."}
                )
