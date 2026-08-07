"""Forms for checklist draft recording."""

from __future__ import annotations

import uuid
from typing import Any

from django import forms

from apps.checklists.models import ChecklistItem, ChecklistResponseType
from apps.recording.models import ChoiceResponseValue


def response_field_name(item_id: uuid.UUID) -> str:
    return f"response_{item_id.hex}"


class ChecklistDraftForm(forms.Form):
    """Dynamic draft form — blank answers are allowed for required items."""

    def __init__(
        self,
        *args: Any,
        items: list[ChecklistItem],
        initial_responses: dict[uuid.UUID, Any] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.items = items
        initial_responses = initial_responses or {}

        for item in items:
            name = response_field_name(item.id)
            initial = initial_responses.get(item.id)
            label = item.label
            if item.is_required:
                label = f"{label} (required)"

            if item.response_type == ChecklistResponseType.YES_NO:
                self.fields[name] = forms.ChoiceField(
                    label=label,
                    required=False,
                    choices=[
                        ("", "— Not answered —"),
                        (ChoiceResponseValue.YES, "Yes"),
                        (ChoiceResponseValue.NO, "No"),
                    ],
                    widget=forms.RadioSelect,
                    initial=initial or "",
                )
            elif item.response_type == ChecklistResponseType.YES_NO_NA:
                self.fields[name] = forms.ChoiceField(
                    label=label,
                    required=False,
                    choices=[
                        ("", "— Not answered —"),
                        (ChoiceResponseValue.YES, "Yes"),
                        (ChoiceResponseValue.NO, "No"),
                        (ChoiceResponseValue.NA, "N/A"),
                    ],
                    widget=forms.RadioSelect,
                    initial=initial or "",
                )
            elif item.response_type == ChecklistResponseType.NUMBER:
                self.fields[name] = forms.DecimalField(
                    label=label,
                    required=False,
                    max_digits=14,
                    decimal_places=4,
                    widget=forms.NumberInput(attrs={"class": "form-input", "step": "any"}),
                    initial=initial,
                )
            elif item.response_type == ChecklistResponseType.TEXT:
                self.fields[name] = forms.CharField(
                    label=label,
                    required=False,
                    widget=forms.Textarea(attrs={"class": "form-input", "rows": 3}),
                    initial=initial or "",
                )
            elif item.response_type == ChecklistResponseType.SELECT:
                choices = [("", "— Not answered —")]
                for option in item.options.all():
                    choices.append((str(option.id), option.label))
                self.fields[name] = forms.ChoiceField(
                    label=label,
                    required=False,
                    choices=choices,
                    widget=forms.Select(attrs={"class": "form-input"}),
                    initial=str(initial) if initial else "",
                )
            else:
                self.fields[name] = forms.CharField(
                    label=label,
                    required=False,
                    disabled=True,
                    initial="",
                )

    def answers_by_item_id(self) -> dict[uuid.UUID, Any]:
        answers: dict[uuid.UUID, Any] = {}
        for item in self.items:
            name = response_field_name(item.id)
            answers[item.id] = self.cleaned_data.get(name)
        return answers
