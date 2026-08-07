"""Checklist definition models — configurable, unseeded; TEMPLATE evidence required."""

from __future__ import annotations

import uuid
from decimal import Decimal

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


class ChecklistResponseType(models.TextChoices):
    """Technical response primitives — not product-specific business rules."""

    YES_NO = "YES_NO", "Yes / No"
    YES_NO_NA = "YES_NO_NA", "Yes / No / N/A"
    NUMBER = "NUMBER", "Number"
    TEXT = "TEXT", "Text"
    SELECT = "SELECT", "Select"


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

    Response primitives are technical definition schema only.
    Numerical Product limits and release automation remain evidence-gated.
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
    response_type = models.CharField(
        max_length=16,
        choices=ChecklistResponseType.choices,
        blank=True,
        default="",
        help_text="Blank allowed on DRAFT only; publish requires a valid response type.",
    )
    unit = models.CharField(
        max_length=32,
        blank=True,
        default="",
        help_text="Optional unit for NUMBER items (e.g. °C). Not a limit.",
    )
    minimum_value = models.DecimalField(
        max_digits=14,
        decimal_places=4,
        null=True,
        blank=True,
        help_text="Optional NUMBER lower bound. Unset is allowed.",
    )
    maximum_value = models.DecimalField(
        max_digits=14,
        decimal_places=4,
        null=True,
        blank=True,
        help_text="Optional NUMBER upper bound. Unset is allowed.",
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
        errors = validate_item_response_definition(
            response_type=self.response_type,
            unit=self.unit,
            minimum_value=self.minimum_value,
            maximum_value=self.maximum_value,
            require_response_type=False,
        )
        if errors:
            raise ValidationError(errors)


class ChecklistItemOption(models.Model):
    """Ordered SELECT option belonging to exactly one ChecklistItem (version-owned)."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(
        ChecklistItem,
        on_delete=models.CASCADE,
        related_name="options",
    )
    value = models.CharField(max_length=64)
    label = models.CharField(max_length=255)
    position = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        ordering = ("position", "value")
        verbose_name = "Checklist item option"
        verbose_name_plural = "Checklist item options"
        constraints = [
            models.UniqueConstraint(
                fields=["item", "position"],
                name="chk_option_item_position_uniq",
            ),
            models.UniqueConstraint(
                Lower("value"),
                "item",
                name="chk_option_item_value_ci_uniq",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.value}: {self.label}"

    def clean(self) -> None:
        super().clean()
        if not (self.value or "").strip():
            raise ValidationError({"value": "Option value cannot be blank."})
        if not (self.label or "").strip():
            raise ValidationError({"label": "Option label cannot be blank."})


def validate_item_response_definition(
    *,
    response_type: str,
    unit: str = "",
    minimum_value: Decimal | None = None,
    maximum_value: Decimal | None = None,
    require_response_type: bool = False,
) -> dict[str, str]:
    """
    Central structural response-definition rules.

    Returns a field→message error map (empty when valid).
    Does not invent Product limits or release rules.
    """
    errors: dict[str, str] = {}
    normalized_type = (response_type or "").strip()
    unit_text = (unit or "").strip()

    if not normalized_type:
        if require_response_type:
            errors["response_type"] = "Response type is required."
        elif minimum_value is not None or maximum_value is not None or unit_text:
            errors["response_type"] = (
                "Response type is required when unit or numeric limits are set."
            )
        return errors

    if normalized_type not in ChecklistResponseType.values:
        errors["response_type"] = "Unknown response type."
        return errors

    if normalized_type != ChecklistResponseType.NUMBER:
        if minimum_value is not None or maximum_value is not None:
            errors["minimum_value"] = "Numeric limits are only allowed for NUMBER responses."
        if unit_text:
            errors["unit"] = "Unit is only applicable for NUMBER responses."
    else:
        if (
            minimum_value is not None
            and maximum_value is not None
            and minimum_value > maximum_value
        ):
            errors["minimum_value"] = "Minimum value cannot be greater than maximum value."

    return errors
