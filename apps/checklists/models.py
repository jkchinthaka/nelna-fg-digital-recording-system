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


class ChecklistItemKind(models.TextChoices):
    """
    Engine v2 item structure (ADR-019 / Phase 06H).

    CALCULATED is reserved for 06I — rejected by services until implemented.
    """

    SIMPLE = "SIMPLE", "Simple"
    REPEATING_GROUP = "REPEATING_GROUP", "Repeating group"
    CALCULATED = "CALCULATED", "Calculated"


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
    Phase 06H adds optional repeating-group structure (ADR-019).
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    section = models.ForeignKey(
        ChecklistSection,
        on_delete=models.CASCADE,
        related_name="items",
    )
    parent_item = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="child_items",
        help_text="Set only for children of a REPEATING_GROUP (one level).",
    )
    item_kind = models.CharField(
        max_length=32,
        choices=ChecklistItemKind.choices,
        default=ChecklistItemKind.SIMPLE,
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
    repeat_min = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Optional minimum sample rows when defined by evidence — not invented.",
    )
    repeat_max = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Optional maximum sample rows when defined by evidence — not invented.",
    )
    repeat_default = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Optional default sample row count when defined — not invented.",
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
        indexes = [
            models.Index(
                fields=["section", "parent_item", "position"],
                name="chk_item_sect_parent_pos_idx",
            ),
            models.Index(fields=["item_kind"], name="chk_item_kind_idx"),
        ]

    def __str__(self) -> str:
        return f"{self.code}: {self.label}"

    @property
    def is_repeating_group(self) -> bool:
        return self.item_kind == ChecklistItemKind.REPEATING_GROUP

    @property
    def is_simple(self) -> bool:
        return self.item_kind == ChecklistItemKind.SIMPLE

    def clean(self) -> None:
        from apps.checklists.constants import REPEAT_SAMPLE_TECHNICAL_CEILING

        super().clean()
        if not (self.code or "").strip():
            raise ValidationError({"code": "Code cannot be blank."})
        if not (self.label or "").strip():
            raise ValidationError({"label": "Label cannot be blank."})

        kind = (self.item_kind or "").strip() or ChecklistItemKind.SIMPLE
        if kind not in ChecklistItemKind.values:
            raise ValidationError({"item_kind": "Unknown item kind."})
        if kind == ChecklistItemKind.CALCULATED:
            raise ValidationError(
                {"item_kind": "CALCULATED items are not enabled until Phase 06I."}
            )

        if self.parent_item_id is not None:
            parent = self.parent_item
            if parent is None:
                raise ValidationError({"parent_item": "Parent item not found."})
            if parent.section_id != self.section_id:
                raise ValidationError(
                    {"parent_item": "Parent item must belong to the same section."}
                )
            if parent.item_kind != ChecklistItemKind.REPEATING_GROUP:
                raise ValidationError({"parent_item": "Parent item must be a REPEATING_GROUP."})
            if parent.parent_item_id is not None:
                raise ValidationError({"parent_item": "Nested repeating groups are not supported."})
            if kind != ChecklistItemKind.SIMPLE:
                raise ValidationError(
                    {
                        "item_kind": (
                            "Only SIMPLE child items are supported under a "
                            "REPEATING_GROUP in Phase 06H."
                        )
                    }
                )

        if kind == ChecklistItemKind.REPEATING_GROUP:
            if self.parent_item_id is not None:
                raise ValidationError(
                    {"parent_item": "A REPEATING_GROUP cannot be nested under another item."}
                )
            if (self.response_type or "").strip():
                raise ValidationError(
                    {"response_type": "REPEATING_GROUP items do not take a response type."}
                )
            if self.unit or self.minimum_value is not None or self.maximum_value is not None:
                raise ValidationError(
                    {"response_type": "REPEATING_GROUP items cannot have numeric limits or unit."}
                )
            for field_name in ("repeat_min", "repeat_max", "repeat_default"):
                value = getattr(self, field_name)
                if value is not None and value > REPEAT_SAMPLE_TECHNICAL_CEILING:
                    raise ValidationError(
                        {
                            field_name: (
                                f"Cannot exceed technical sample ceiling "
                                f"({REPEAT_SAMPLE_TECHNICAL_CEILING})."
                            )
                        }
                    )
            if (
                self.repeat_min is not None
                and self.repeat_max is not None
                and self.repeat_min > self.repeat_max
            ):
                raise ValidationError(
                    {"repeat_min": "repeat_min cannot be greater than repeat_max."}
                )
            if self.repeat_default is not None:
                if self.repeat_min is not None and self.repeat_default < self.repeat_min:
                    raise ValidationError(
                        {"repeat_default": "repeat_default cannot be less than repeat_min."}
                    )
                if self.repeat_max is not None and self.repeat_default > self.repeat_max:
                    raise ValidationError(
                        {"repeat_default": "repeat_default cannot exceed repeat_max."}
                    )
            return

        # SIMPLE (and future leaf kinds)
        if any(
            value is not None for value in (self.repeat_min, self.repeat_max, self.repeat_default)
        ):
            raise ValidationError(
                {"repeat_min": "Repeat configuration is only allowed on REPEATING_GROUP items."}
            )
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
