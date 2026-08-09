"""Recording template filters."""

from __future__ import annotations

from typing import Any

from django import template
from django.forms import BoundField, Form

from apps.recording.forms import response_field_name
from apps.recording.selectors import actor_can_access_recording_module

register = template.Library()


@register.simple_tag(takes_context=True)
def user_can_record_checklist_tasks(context: dict[str, Any]) -> bool:
    request = context.get("request")
    user = getattr(request, "user", None) if request is not None else None
    return actor_can_access_recording_module(user)


@register.filter
def response_bound_field(form: Form, item: Any) -> BoundField | None:
    name = response_field_name(item.id, 1)
    if name not in form.fields:
        return None
    return form[name]


@register.simple_tag
def response_bound_field_at(form: Form, item: Any, sample_index: int) -> BoundField | None:
    name = response_field_name(item.id, int(sample_index))
    if name not in form.fields:
        return None
    return form[name]


@register.filter
def dict_get(mapping: Any, key: Any) -> Any:
    if mapping is None:
        return None
    try:
        return mapping.get(key)
    except AttributeError:
        return None


@register.simple_tag
def calculated_preview(responses: Any, item: Any, sample_index: int = 1) -> str:
    """Read-only preview of a server-computed CALCULATED draft value."""
    if responses is None or item is None:
        return "—"
    try:
        row = responses.get((item.id, int(sample_index)))
    except AttributeError:
        return "—"
    if row is None or getattr(row, "number_value", None) is None:
        return "—"
    unit = f" {item.unit}" if getattr(item, "unit", "") else ""
    return f"{row.number_value}{unit}"
