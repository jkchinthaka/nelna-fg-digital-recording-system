"""Runtime type guards for request/auth paths — avoid assert (stripped under -O)."""

from __future__ import annotations

from django import forms

from apps.accounts.models import User


def require_model_choice_field(field: forms.Field, *, name: str) -> forms.ModelChoiceField:
    """Return field as ModelChoiceField or raise TypeError (never rely on assert)."""
    if not isinstance(field, forms.ModelChoiceField):
        raise TypeError(f"{name} must be a ModelChoiceField, got {type(field)!r}.")
    return field


def require_user_instance(value: object, *, context: str = "user") -> User:
    """Return value as accounts.User or raise TypeError (never rely on assert)."""
    if not isinstance(value, User):
        raise TypeError(f"{context} must be apps.accounts.User, got {type(value)!r}.")
    return value
