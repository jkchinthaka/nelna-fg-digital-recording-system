"""Checklist definition management forms."""

from __future__ import annotations

from typing import Any

from django import forms
from django.db.models import QuerySet

from apps.checklists.models import (
    ChecklistControlPointClass,
    ChecklistItem,
    ChecklistItemCriticality,
    ChecklistItemOption,
    ChecklistResponseType,
    ChecklistSection,
    ChecklistTemplate,
    ChecklistVersion,
)
from apps.master_data.models import FGProduct
from apps.organizations.models import Organization


class ChecklistTemplateForm(forms.Form):
    organization = forms.ModelChoiceField(
        queryset=Organization.objects.none(),
        label="Organization",
        empty_label="Select organization",
        widget=forms.Select(attrs={"class": "form-input"}),
    )
    product = forms.ModelChoiceField(
        queryset=FGProduct.objects.none(),
        label="FG Product (optional)",
        required=False,
        empty_label="No product association",
        widget=forms.Select(attrs={"class": "form-input"}),
        help_text="Provisional optional association. Product binding remains evidence-gated.",
    )
    code = forms.CharField(
        max_length=64,
        label="Template code",
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "autocomplete": "off",
                "autocapitalize": "characters",
            }
        ),
        help_text="Normalized to uppercase. Unique within the selected organization.",
    )
    name = forms.CharField(
        max_length=255,
        label="Template name",
        widget=forms.TextInput(attrs={"class": "form-input", "autocomplete": "off"}),
    )
    description = forms.CharField(
        required=False,
        label="Description",
        widget=forms.Textarea(attrs={"class": "form-input", "rows": 3}),
    )
    is_active = forms.BooleanField(label="Active", required=False, initial=True)

    def __init__(
        self,
        *args: Any,
        organizations: QuerySet[Organization] | None = None,
        products: QuerySet[FGProduct] | None = None,
        instance: ChecklistTemplate | None = None,
        **kwargs: Any,
    ) -> None:
        self.instance = instance
        super().__init__(*args, **kwargs)
        from apps.core.type_guards import require_model_choice_field

        org_field = require_model_choice_field(self.fields["organization"], name="organization")
        product_field = require_model_choice_field(self.fields["product"], name="product")
        org_field.queryset = (
            organizations if organizations is not None else Organization.objects.none()
        )
        product_field.queryset = products if products is not None else FGProduct.objects.none()
        if instance is not None:
            org_field.disabled = True
            org_field.initial = instance.organization_id
            org_field.help_text = "Organization cannot be changed after a template is created."
            if not self.is_bound:
                self.fields["code"].initial = instance.code
                self.fields["name"].initial = instance.name
                self.fields["description"].initial = instance.description
                self.fields["is_active"].initial = instance.is_active
                product_field.initial = instance.product_id


class CreateVersionForm(forms.Form):
    source_version = forms.ModelChoiceField(
        queryset=ChecklistVersion.objects.none(),
        required=False,
        label="Clone from version (optional)",
        empty_label="Start blank draft",
        widget=forms.Select(attrs={"class": "form-input"}),
        help_text="Cloning copies section/item definitions into a new draft. Rows are not shared.",
    )

    def __init__(
        self,
        *args: Any,
        versions: QuerySet[ChecklistVersion] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(*args, **kwargs)
        from apps.core.type_guards import require_model_choice_field

        field = require_model_choice_field(self.fields["source_version"], name="source_version")
        field.queryset = versions if versions is not None else ChecklistVersion.objects.none()


class ChecklistSectionForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        label="Section title",
        widget=forms.TextInput(attrs={"class": "form-input", "autocomplete": "off"}),
    )
    description = forms.CharField(
        required=False,
        label="Description",
        widget=forms.Textarea(attrs={"class": "form-input", "rows": 2}),
    )

    def __init__(self, *args: Any, instance: ChecklistSection | None = None, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        if instance is not None and not self.is_bound:
            self.fields["title"].initial = instance.title
            self.fields["description"].initial = instance.description


class ChecklistItemForm(forms.Form):
    code = forms.CharField(
        max_length=64,
        label="Item code",
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "autocomplete": "off",
                "autocapitalize": "characters",
            }
        ),
    )
    label = forms.CharField(
        max_length=500,
        label="Label / question text",
        widget=forms.TextInput(attrs={"class": "form-input", "autocomplete": "off"}),
    )
    help_text = forms.CharField(
        required=False,
        label="Help / instruction text",
        widget=forms.Textarea(attrs={"class": "form-input", "rows": 2}),
    )
    is_required = forms.BooleanField(
        label="Required",
        required=False,
        initial=True,
        help_text="Technical required flag for later recording — not a QA threshold.",
    )
    response_type = forms.ChoiceField(
        label="Response type",
        choices=[("", "Select response type"), *ChecklistResponseType.choices],
        required=False,
        widget=forms.Select(attrs={"class": "form-input"}),
        help_text=(
            "Technical primitive only. Publish requires a type. "
            "Temperature uses NUMBER with an optional unit (for example °C)."
        ),
    )
    unit = forms.CharField(
        required=False,
        max_length=32,
        label="Unit (NUMBER only)",
        widget=forms.TextInput(attrs={"class": "form-input", "autocomplete": "off"}),
        help_text="Optional. Leave blank unless this NUMBER item records a measured unit.",
    )
    minimum_value = forms.DecimalField(
        required=False,
        max_digits=14,
        decimal_places=4,
        label="Minimum (NUMBER only, optional)",
        widget=forms.NumberInput(attrs={"class": "form-input", "step": "any"}),
        help_text="Optional. Do not invent Product limits.",
    )
    maximum_value = forms.DecimalField(
        required=False,
        max_digits=14,
        decimal_places=4,
        label="Maximum (NUMBER only, optional)",
        widget=forms.NumberInput(attrs={"class": "form-input", "step": "any"}),
        help_text="Optional. Do not invent Product limits.",
    )
    control_point_class = forms.ChoiceField(
        label="Control-point class",
        choices=ChecklistControlPointClass.choices,
        initial=ChecklistControlPointClass.NONE,
        required=False,
        widget=forms.Select(attrs={"class": "form-input"}),
        help_text=(
            "Default NONE. Non-NONE production values require ASM-002 / APR-027. "
            "Metadata does not HOLD/REJECT/RELEASE."
        ),
    )
    criticality = forms.ChoiceField(
        label="Criticality (optional)",
        choices=[("", "Unset"), *ChecklistItemCriticality.choices],
        required=False,
        initial="",
        widget=forms.Select(attrs={"class": "form-input"}),
        help_text="Optional display metadata only. Blank = unset. Not a disposition.",
    )

    def __init__(self, *args: Any, instance: ChecklistItem | None = None, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        if instance is not None and not self.is_bound:
            self.fields["code"].initial = instance.code
            self.fields["label"].initial = instance.label
            self.fields["help_text"].initial = instance.help_text
            self.fields["is_required"].initial = instance.is_required
            self.fields["response_type"].initial = instance.response_type
            self.fields["unit"].initial = instance.unit
            self.fields["minimum_value"].initial = instance.minimum_value
            self.fields["maximum_value"].initial = instance.maximum_value
            self.fields["control_point_class"].initial = instance.control_point_class
            self.fields["criticality"].initial = instance.criticality


class ChecklistItemOptionForm(forms.Form):
    value = forms.CharField(
        max_length=64,
        label="Option value",
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "autocomplete": "off",
                "autocapitalize": "characters",
            }
        ),
        help_text="Stable machine value (normalized uppercase).",
    )
    label = forms.CharField(
        max_length=255,
        label="Option label",
        widget=forms.TextInput(attrs={"class": "form-input", "autocomplete": "off"}),
    )

    def __init__(
        self, *args: Any, instance: ChecklistItemOption | None = None, **kwargs: Any
    ) -> None:
        super().__init__(*args, **kwargs)
        if instance is not None and not self.is_bound:
            self.fields["value"].initial = instance.value
            self.fields["label"].initial = instance.label
