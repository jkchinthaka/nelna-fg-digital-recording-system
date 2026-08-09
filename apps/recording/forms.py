"""Forms for checklist draft recording (including repeating sample rows)."""

from __future__ import annotations

import uuid
from typing import Any

from django import forms

from apps.checklists.models import ChecklistItem, ChecklistItemKind, ChecklistResponseType
from apps.recording.models import ChoiceResponseValue
from apps.recording.repeating import ResponseKey, partition_definition_items


def response_field_name(item_id: uuid.UUID, sample_index: int = 1) -> str:
    if sample_index == 1:
        # Preserve legacy field names for top-level SIMPLE (sample_index=1).
        return f"response_{item_id.hex}"
    return f"response_{item_id.hex}_s{sample_index}"


def sample_count_field_name(group_id: uuid.UUID) -> str:
    return f"sample_count_{group_id.hex}"


class ChecklistDraftForm(forms.Form):
    """Dynamic draft form — blank answers are allowed for required items."""

    def __init__(
        self,
        *args: Any,
        items: list[ChecklistItem],
        initial_responses: dict[ResponseKey, Any] | None = None,
        sample_indexes_by_group: dict[uuid.UUID, list[int]] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.items = items
        self.sample_indexes_by_group = sample_indexes_by_group or {}
        initial_responses = initial_responses or {}
        top_simple, groups, children_by_parent = partition_definition_items(items)
        self.top_simple = top_simple
        self.groups = groups
        self.children_by_parent = children_by_parent

        for group in groups:
            count_name = sample_count_field_name(group.id)
            indexes = self.sample_indexes_by_group.get(group.id) or [1]
            self.fields[count_name] = forms.IntegerField(
                required=False,
                min_value=0,
                initial=len(indexes),
                widget=forms.HiddenInput,
            )

        for item in top_simple:
            self._add_item_field(item, sample_index=1, initial_responses=initial_responses)

        for group in groups:
            children = children_by_parent.get(group.id, [])
            indexes = self.sample_indexes_by_group.get(group.id) or []
            for sample_index in indexes:
                for child in children:
                    self._add_item_field(
                        child,
                        sample_index=sample_index,
                        initial_responses=initial_responses,
                    )

    def _add_item_field(
        self,
        item: ChecklistItem,
        *,
        sample_index: int,
        initial_responses: dict[ResponseKey, Any],
    ) -> None:
        if item.item_kind != ChecklistItemKind.SIMPLE:
            return
        name = response_field_name(item.id, sample_index)
        initial = initial_responses.get((item.id, sample_index))
        label = item.label
        if sample_index > 1 or item.parent_item_id is not None:
            label = f"{label} (sample {sample_index})"
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

    def answers_by_item_id(self) -> dict[ResponseKey, Any]:
        """Return answers keyed by ``(item_id, sample_index)``."""
        answers: dict[ResponseKey, Any] = {}
        for item in self.top_simple:
            name = response_field_name(item.id, 1)
            if name in self.fields:
                answers[(item.id, 1)] = self.cleaned_data.get(name)
        for group in self.groups:
            children = self.children_by_parent.get(group.id, [])
            indexes = self.sample_indexes_by_group.get(group.id) or []
            for sample_index in indexes:
                for child in children:
                    name = response_field_name(child.id, sample_index)
                    if name in self.fields:
                        answers[(child.id, sample_index)] = self.cleaned_data.get(name)
        return answers
