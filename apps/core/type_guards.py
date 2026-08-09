"""Runtime type guards for request/auth paths — avoid assert (stripped under -O)."""

from __future__ import annotations

from typing import Any

from django import forms
from django.contrib.auth import get_user_model


def require_model_choice_field(field: forms.Field, *, name: str) -> forms.ModelChoiceField:
    """Return field as ModelChoiceField or raise TypeError (never rely on assert)."""
    if not isinstance(field, forms.ModelChoiceField):
        raise TypeError(f"{name} must be a ModelChoiceField, got {type(field)!r}.")
    return field


def require_user_instance(value: object, *, context: str = "user") -> Any:
    """Return value as the configured auth user model or raise TypeError.

    Resolves the user model via Django get_user_model() so core stays free of
    direct accounts-app imports (architecture boundary).
    """
    user_model = get_user_model()
    if not isinstance(value, user_model):
        raise TypeError(f"{context} must be apps.accounts.User, got {type(value)!r}.")
    return value
