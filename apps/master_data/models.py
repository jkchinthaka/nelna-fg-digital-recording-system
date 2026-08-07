"""FG Product master — configurable, unseeded; MASTER-001 remains evidence-required."""

from __future__ import annotations

import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.functions import Lower

from apps.organizations.models import Organization


class FGProduct(models.Model):
    """
    Organization-scoped Finished Goods Product definition.

    Codes and names are administrator-configured. No business Product rows are seeded.
    Official Nelna Product Master inventory remains gated by MASTER-001 evidence.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="fg_products",
    )
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("organization__code", "code")
        verbose_name = "FG Product"
        verbose_name_plural = "FG Products"
        permissions = [
            ("manage_fgproduct", "Can manage FG product"),
        ]
        constraints = [
            models.UniqueConstraint(
                Lower("code"),
                "organization",
                name="md_fgproduct_org_code_ci_uniq",
            ),
        ]
        indexes = [
            models.Index(
                fields=["organization", "is_active"],
                name="md_fgproduct_org_act_idx",
            ),
            models.Index(Lower("code"), name="md_fgproduct_code_lower_idx"),
        ]

    def __str__(self) -> str:
        return f"{self.organization.code}/{self.code}"

    def clean(self) -> None:
        super().clean()
        if not (self.code or "").strip():
            raise ValidationError({"code": "Code cannot be blank."})
        if not (self.name or "").strip():
            raise ValidationError({"name": "Name cannot be blank."})
