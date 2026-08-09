"""FG Product master — configurable, unseeded; MASTER-001 remains evidence-required."""

from __future__ import annotations

import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.db.models.functions import Lower

from apps.organizations.models import Organization


class FGProduct(models.Model):
    """
    Organization-scoped Finished Goods Product definition.

    Codes and names are administrator-configured. No business Product rows are seeded.
    Optional mapping / attribute fields are TECHNICALLY SUPPORTED blanks until
    MASTER-001 evidence supplies official values. Do not invent Nelna catalogue data.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="fg_products",
    )
    # Primary identity (organization-scoped)
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    # ERP mapping reference — not primary identity; no live Bileeta calls
    erp_item_code = models.CharField(
        max_length=128,
        blank=True,
        default="",
        help_text="Optional ERP / Bileeta item mapping reference. Not primary Product identity.",
    )
    # Optional generic attributes — empty until MASTER-001 evidence (no seeded catalogues)
    category = models.CharField(max_length=128, blank=True, default="")
    brand = models.CharField(max_length=128, blank=True, default="")
    pack_size = models.CharField(max_length=64, blank=True, default="")
    uom = models.CharField(
        max_length=32,
        blank=True,
        default="",
        help_text="Unit of measure label (free text). No seeded UOM catalogue.",
    )
    barcode = models.CharField(
        max_length=128,
        blank=True,
        default="",
        help_text="Optional barcode / SKU reference.",
    )
    storage_category = models.CharField(
        max_length=128,
        blank=True,
        default="",
        help_text=(
            "Optional storage-category label only. Not a CCP/temperature class approval."
        ),
    )
    shelf_life_reference = models.CharField(
        max_length=255,
        blank=True,
        default="",
        help_text="Optional shelf-life document / policy reference — not a computed limit.",
    )
    label_artwork_reference = models.CharField(
        max_length=255,
        blank=True,
        default="",
        help_text="Optional label / artwork document reference.",
    )
    effective_from = models.DateField(
        null=True,
        blank=True,
        help_text="Optional effective-from date. Blank until business rules evidenced.",
    )
    effective_to = models.DateField(
        null=True,
        blank=True,
        help_text="Optional effective-to date. Prefer over hard delete.",
    )
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
            models.UniqueConstraint(
                Lower("erp_item_code"),
                "organization",
                condition=~Q(erp_item_code=""),
                name="md_fgproduct_org_erp_ci_uniq",
            ),
            models.CheckConstraint(
                condition=(
                    Q(effective_to__isnull=True)
                    | Q(effective_from__isnull=True)
                    | Q(effective_to__gte=models.F("effective_from"))
                ),
                name="md_fgproduct_effective_window_valid",
            ),
        ]
        indexes = [
            models.Index(
                fields=["organization", "is_active"],
                name="md_fgproduct_org_act_idx",
            ),
            models.Index(Lower("code"), name="md_fgproduct_code_lower_idx"),
            models.Index(
                Lower("erp_item_code"),
                name="md_fgproduct_erp_lower_idx",
            ),
            models.Index(
                fields=["organization", "category"],
                name="md_fgproduct_org_cat_idx",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.organization.code}/{self.code}"

    def clean(self) -> None:
        super().clean()
        errors: dict[str, str] = {}
        if not (self.code or "").strip():
            errors["code"] = "Code cannot be blank."
        if not (self.name or "").strip():
            errors["name"] = "Name cannot be blank."
        if (
            self.effective_to is not None
            and self.effective_from is not None
            and self.effective_to < self.effective_from
        ):
            errors["effective_to"] = "effective_to cannot be earlier than effective_from."
        if errors:
            raise ValidationError(errors)
