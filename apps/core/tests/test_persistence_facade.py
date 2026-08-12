"""Tests for backend-neutral persistence facade."""

from __future__ import annotations

import pytest
from django.test import override_settings

from apps.core.persistence import (
    DatabaseVendor,
    atomic,
    detect_database_vendor,
    is_mongodb,
)


def test_detect_postgresql_default() -> None:
    assert detect_database_vendor() is DatabaseVendor.POSTGRESQL
    assert is_mongodb() is False


@override_settings(
    DATABASES={
        "default": {
            "ENGINE": "django_mongodb_backend",
            "HOST": "mongodb://127.0.0.1:27027",
            "NAME": "fg_same_db_poc",
        }
    }
)
def test_detect_mongodb_engine() -> None:
    assert detect_database_vendor() is DatabaseVendor.MONGODB
    assert is_mongodb() is True


@pytest.mark.django_db
def test_atomic_facade_commits_on_postgresql() -> None:
    from tests.factories import make_org

    with atomic():
        org = make_org(code="PERSIST01", name="Persistence Org")
    from apps.organizations.models import Organization

    assert Organization.objects.filter(pk=org.pk).exists()
