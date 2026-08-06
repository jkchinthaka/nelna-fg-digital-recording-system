"""Read-side selectors for organization hierarchy."""

from __future__ import annotations

import uuid

from django.db.models import QuerySet

from apps.organizations.models import Department, Organization, Site


def get_organization_by_id(organization_id: uuid.UUID) -> Organization | None:
    return Organization.objects.filter(pk=organization_id).first()


def get_organization_by_code(code: str) -> Organization | None:
    return Organization.objects.filter(code__iexact=code.strip()).first()


def list_active_organizations() -> QuerySet[Organization]:
    return Organization.objects.filter(is_active=True)


def get_site_by_id(site_id: uuid.UUID) -> Site | None:
    return Site.objects.select_related("organization").filter(pk=site_id).first()


def list_sites_for_organization(
    organization: Organization,
    *,
    active_only: bool = True,
) -> QuerySet[Site]:
    qs = Site.objects.filter(organization=organization)
    if active_only:
        qs = qs.filter(is_active=True)
    return qs.select_related("organization")


def get_department_by_id(department_id: uuid.UUID) -> Department | None:
    return (
        Department.objects.select_related("organization", "site").filter(pk=department_id).first()
    )


def list_departments_for_organization(
    organization: Organization,
    *,
    active_only: bool = True,
) -> QuerySet[Department]:
    qs = Department.objects.filter(organization=organization)
    if active_only:
        qs = qs.filter(is_active=True)
    return qs.select_related("organization", "site")


def list_departments_for_site(
    site: Site,
    *,
    active_only: bool = True,
) -> QuerySet[Department]:
    qs = Department.objects.filter(site=site)
    if active_only:
        qs = qs.filter(is_active=True)
    return qs.select_related("organization", "site")
