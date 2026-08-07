"""FG Product management forms."""

from __future__ import annotations

from typing import Any

from django import forms
from django.db.models import QuerySet

from apps.master_data.models import FGProduct
from apps.organizations.models import Organization


class FGProductForm(forms.Form):
    organization = forms.ModelChoiceField(
        queryset=Organization.objects.none(),
        label="Organization",
        empty_label="Select organization",
        widget=forms.Select(attrs={"class": "form-input"}),
    )
    code = forms.CharField(
        max_length=64,
        label="Product code",
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
        label="Product name",
        widget=forms.TextInput(attrs={"class": "form-input", "autocomplete": "off"}),
    )
    description = forms.CharField(
        required=False,
        label="Description",
        widget=forms.Textarea(attrs={"class": "form-input", "rows": 3}),
        help_text="Optional. Leave blank if not needed.",
    )
    is_active = forms.BooleanField(
        label="Active",
        required=False,
        initial=True,
        help_text=(
            "Inactive products remain available for history but are hidden from active lists."
        ),
    )

    def __init__(
        self,
        *args: Any,
        organizations: QuerySet[Organization] | None = None,
        instance: FGProduct | None = None,
        **kwargs: Any,
    ) -> None:
        self.instance = instance
        super().__init__(*args, **kwargs)
        org_field = self.fields["organization"]
        assert isinstance(org_field, forms.ModelChoiceField)
        org_field.queryset = (
            organizations if organizations is not None else Organization.objects.none()
        )

        if instance is not None:
            org_field.disabled = True
            org_field.initial = instance.organization_id
            org_field.help_text = "Organization cannot be changed after an FG Product is created."
            if not self.is_bound:
                self.fields["code"].initial = instance.code
                self.fields["name"].initial = instance.name
                self.fields["description"].initial = instance.description
                self.fields["is_active"].initial = instance.is_active
