"""Checklist definition models — configurable, unseeded; TEMPLATE evidence required."""

from __future__ import annotations

import uuid

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.functions import Lower

from apps.master_data.models import FGProduct
from apps.organizations.models import Organization


class ChecklistVersionStatus(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    PUBLISHED = "PUBLISHED", "Published"
    RETIRED = "RETIRED", "Retired"


class ChecklistTemplate(models.Model):
    """
    Stable logical identity of a checklist across versions.

    Codes/names are administrator-configured. No operational checklist rows are seeded.
    Official forms remain gated by TEMPLATE / ASM evidence.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="checklist_templates",
    )
    product = models.ForeignKey(
        FGProduct,
        on_delete=models.PROTECT,
        related_name="checklist_templates",
        null=True,
        blank=True,
        help_text=(
            "Optional provisional Product association — not proven mandatory by business evidence."
        ),
    )
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("organization__code", "code")
        verbose_name = "Checklist template"
        verbose_name_plural = "Checklist templates"
        permissions = [
            ("manage_checklist", "Can manage checklist definitions"),
        ]
        constraints = [
            models.UniqueConstraint(
                Lower("code"),
                "organization",
                name="chk_template_org_code_ci_uniq",
            ),
        ]
        indexes = [
            models.Index(
                fields=["organization", "is_active"],
                name="chk_template_org_act_idx",
            ),
            models.Index(Lower("code"), name="chk_template_code_lower_idx"),
        ]

    def __str__(self) -> str:
        return f"{self.organization.code}/{self.code}"

    def clean(self) -> None:
        super().clean()
        if not (self.code or "").strip():
            raise ValidationError({"code": "Code cannot be blank."})
        if not (self.name or "").strip():
            raise ValidationError({"name": "Name cannot be blank."})
        if self.product_id is not None and self.organization_id is not None:
            product = self.product
            if product is not None and product.organization_id != self.organization_id:
                raise ValidationError(
                    {"product": "Product must belong to the same organization as the template."}
                )


class ChecklistVersion(models.Model):
    """Immutable publishable definition revision of a ChecklistTemplate."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    template = models.ForeignKey(
        ChecklistTemplate,
        on_delete=models.PROTECT,
        related_name="versions",
    )
    version_number = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    status = models.CharField(
        max_length=16,
        choices=ChecklistVersionStatus.choices,
        default=ChecklistVersionStatus.DRAFT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ("template__code", "-version_number")
        verbose_name = "Checklist version"
        verbose_name_plural = "Checklist versions"
        constraints = [
            models.UniqueConstraint(
                fields=["template", "version_number"],
                name="chk_version_template_number_uniq",
            ),
        ]
        indexes = [
            models.Index(
                fields=["template", "status"],
                name="chk_version_tmpl_status_idx",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.template.code} v{self.version_number} ({self.status})"

    @property
    def is_draft(self) -> bool:
        return self.status == ChecklistVersionStatus.DRAFT

    @property
    def is_immutable(self) -> bool:
        return self.status in {
            ChecklistVersionStatus.PUBLISHED,
            ChecklistVersionStatus.RETIRED,
        }


class ChecklistSection(models.Model):
    """Ordered section belonging to exactly one ChecklistVersion."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    version = models.ForeignKey(
        ChecklistVersion,
        on_delete=models.CASCADE,
        related_name="sections",
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    position = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        ordering = ("position", "title")
        verbose_name = "Checklist section"
        verbose_name_plural = "Checklist sections"
        constraints = [
            models.UniqueConstraint(
                fields=["version", "position"],
                name="chk_section_version_position_uniq",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.version} / {self.title}"

    def clean(self) -> None:
        super().clean()
        if not (self.title or "").strip():
            raise ValidationError({"title": "Title cannot be blank."})


class ChecklistItem(models.Model):
    """
    Definition metadata for a checklist prompt/question.

    Response-type schema, limits, instruments, and training are intentionally excluded
    until TEMPLATE / ASM evidence is supplied.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    section = models.ForeignKey(
        ChecklistSection,
        on_delete=models.CASCADE,
        related_name="items",
    )
    code = models.CharField(max_length=64)
    label = models.CharField(max_length=500)
    help_text = models.TextField(blank=True, default="")
    position = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    is_required = models.BooleanField(
        default=True,
        help_text="Technical required flag for later recording phases — not a QA rule.",
    )

    class Meta:
        ordering = ("position", "code")
        verbose_name = "Checklist item"
        verbose_name_plural = "Checklist items"
        constraints = [
            models.UniqueConstraint(
                fields=["section", "position"],
                name="chk_item_section_position_uniq",
            ),
            models.UniqueConstraint(
                Lower("code"),
                "section",
                name="chk_item_section_code_ci_uniq",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.code}: {self.label}"

    def clean(self) -> None:
        super().clean()
        if not (self.code or "").strip():
            raise ValidationError({"code": "Code cannot be blank."})
        if not (self.label or "").strip():
            raise ValidationError({"label": "Label cannot be blank."})
