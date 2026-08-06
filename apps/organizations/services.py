"""Organization domain services — soft deactivate/reactivate only; no hard delete."""

from __future__ import annotations

from django.core.exceptions import ValidationError
from django.db import transaction

from apps.organizations.models import Department, Organization, Site


def normalize_code(value: str) -> str:
    """Strip surrounding whitespace and uppercase for consistent code storage."""
    return value.strip().upper()


@transaction.atomic
def deactivate_organization(organization: Organization) -> Organization:
    organization.is_active = False
    organization.save(update_fields=["is_active", "updated_at"])
    return organization


@transaction.atomic
def reactivate_organization(organization: Organization) -> Organization:
    organization.is_active = True
    organization.save(update_fields=["is_active", "updated_at"])
    return organization


@transaction.atomic
def deactivate_site(site: Site) -> Site:
    site.is_active = False
    site.save(update_fields=["is_active", "updated_at"])
    return site


@transaction.atomic
def reactivate_site(site: Site) -> Site:
    if not site.organization.is_active:
        raise ValidationError("Cannot reactivate a site whose organization is inactive.")
    site.is_active = True
    site.save(update_fields=["is_active", "updated_at"])
    return site


@transaction.atomic
def deactivate_department(department: Department) -> Department:
    department.is_active = False
    department.save(update_fields=["is_active", "updated_at"])
    return department


@transaction.atomic
def reactivate_department(department: Department) -> Department:
    if not department.organization.is_active:
        raise ValidationError("Cannot reactivate a department whose organization is inactive.")
    site = department.site
    if site is not None and not site.is_active:
        raise ValidationError("Cannot reactivate a department whose site is inactive.")
    department.is_active = True
    department.save(update_fields=["is_active", "updated_at"])
    return department


@transaction.atomic
def create_organization(*, code: str, name: str, is_active: bool = True) -> Organization:
    return Organization.objects.create(
        code=normalize_code(code),
        name=name.strip(),
        is_active=is_active,
    )


@transaction.atomic
def create_site(
    *,
    organization: Organization,
    code: str,
    name: str,
    is_active: bool = True,
) -> Site:
    return Site.objects.create(
        organization=organization,
        code=normalize_code(code),
        name=name.strip(),
        is_active=is_active,
    )


@transaction.atomic
def create_department(
    *,
    organization: Organization,
    code: str,
    name: str,
    site: Site | None = None,
    is_active: bool = True,
) -> Department:
    department = Department(
        organization=organization,
        site=site,
        code=normalize_code(code),
        name=name.strip(),
        is_active=is_active,
    )
    department.full_clean()
    department.save()
    return department
