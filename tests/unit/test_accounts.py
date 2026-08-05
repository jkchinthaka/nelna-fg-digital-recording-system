"""Accounts user model tests."""

from __future__ import annotations

import uuid

import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_user_primary_key_is_uuid() -> None:
    user = User.objects.create_user(username="foundation_user", password="complex-pass-123")
    assert isinstance(user.pk, uuid.UUID)


@pytest.mark.django_db
def test_password_is_hashed() -> None:
    user = User.objects.create_user(username="hash_user", password="complex-pass-123")
    user.refresh_from_db()
    assert user.password != "complex-pass-123"
    assert user.check_password("complex-pass-123")


@pytest.mark.django_db
def test_superuser_flags() -> None:
    admin = User.objects.create_superuser(username="admin_user", password="complex-pass-123")
    assert admin.is_staff is True
    assert admin.is_superuser is True


@pytest.mark.django_db
def test_no_default_users_seeded() -> None:
    assert User.objects.count() == 0


@pytest.mark.django_db
def test_minimal_model_has_no_business_fields() -> None:
    field_names = {f.name for f in User._meta.get_fields()}
    forbidden = {
        "employee_code",
        "site",
        "department",
        "business_role",
        "phone_number",
        "profile_image",
        "lockout_count",
    }
    assert forbidden.isdisjoint(field_names)
