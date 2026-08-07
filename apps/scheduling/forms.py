"""Forms for checklist task orchestration UI."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from django import forms
from django.db.models import QuerySet

from apps.checklists.models import ChecklistTemplate, ChecklistVersion
from apps.organizations.models import Organization
from apps.scheduling.models import BATCH_REFERENCE_MAX_LENGTH
from apps.scheduling.services import normalize_batch_reference


class ChecklistTaskCreateForm(forms.Form):
    organization = forms.ModelChoiceField(
        queryset=Organization.objects.none(),
        empty_label="Select organization",
        widget=forms.Select(attrs={"class": "form-input"}),
    )
    checklist_template = forms.ModelChoiceField(
        queryset=ChecklistTemplate.objects.none(),
        empty_label="Select checklist template",
        widget=forms.Select(attrs={"class": "form-input"}),
    )
    checklist_version = forms.ModelChoiceField(
        queryset=ChecklistVersion.objects.none(),
        empty_label="Select published version",
        help_text="Only PUBLISHED versions are eligible. Version selection is explicit.",
        widget=forms.Select(attrs={"class": "form-input"}),
    )
    batch_reference = forms.CharField(
        max_length=BATCH_REFERENCE_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "autocomplete": "off",
                "placeholder": "Production batch reference",
            }
        ),
    )

    def __init__(
        self,
        data: Mapping[str, Any] | None = None,
        *,
        organizations: QuerySet[Organization] | None = None,
        templates: QuerySet[ChecklistTemplate] | None = None,
        versions: QuerySet[ChecklistVersion] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(data, **kwargs)
        org_field = self.fields["organization"]
        template_field = self.fields["checklist_template"]
        version_field = self.fields["checklist_version"]
        assert isinstance(org_field, forms.ModelChoiceField)
        assert isinstance(template_field, forms.ModelChoiceField)
        assert isinstance(version_field, forms.ModelChoiceField)
        org_field.queryset = organizations or Organization.objects.none()
        template_field.queryset = templates or ChecklistTemplate.objects.none()
        version_field.queryset = versions or ChecklistVersion.objects.none()
        version_field.label_from_instance = lambda obj: (  # type: ignore[method-assign]
            f"{obj.template.code} — Version {obj.version_number} (Published)"
        )

    def clean_batch_reference(self) -> str:
        return normalize_batch_reference(self.cleaned_data.get("batch_reference", ""))
