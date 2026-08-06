"""Read-side selectors for organization hierarchy and Shift foundation."""

from __future__ import annotations

import uuid

from django.core.exceptions import PermissionDenied
from django.db.models import QuerySet

from apps.access_control.services import user_has_permission
from apps.accounts.models import User
from apps.organizations.models import Department, Organization, Shift, Site
from apps.organizations.services import VIEW_SHIFT, shift_authorization_scope


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


def _actor_may_view_shift(actor: User | None, shift: Shift) -> bool:
    if actor is None or not getattr(actor, "is_authenticated", False) or not actor.is_active:
        return False
    return user_has_permission(actor, VIEW_SHIFT, scope=shift_authorization_scope(shift))


def get_shift_by_id(actor: User | None, shift_id: uuid.UUID) -> Shift | None:
    shift = (
        Shift.objects.select_related("organization", "site", "department")
        .filter(pk=shift_id)
        .first()
    )
    if shift is None:
        return None
    if not _actor_may_view_shift(actor, shift):
        raise PermissionDenied("Permission denied.")
    return shift


def list_shifts_for_actor(
    actor: User | None,
    *,
    organization: Organization | None = None,
    site: Site | None = None,
    department: Department | None = None,
    active_only: bool = False,
) -> QuerySet[Shift]:
    if actor is None or not getattr(actor, "is_authenticated", False) or not actor.is_active:
        return Shift.objects.none()

    qs = Shift.objects.select_related("organization", "site", "department").all()
    if organization is not None:
        qs = qs.filter(organization=organization)
    if site is not None:
        qs = qs.filter(site=site)
    if department is not None:
        qs = qs.filter(department=department)
    if active_only:
        qs = qs.filter(is_active=True)

    if actor.is_superuser:
        return qs

    allowed_ids = [shift.pk for shift in qs if _actor_may_view_shift(actor, shift)]
    return (
        Shift.objects.filter(pk__in=allowed_ids)
        .select_related("organization", "site", "department")
        .order_by("organization__code", "code", "effective_from")
    )


def list_active_shifts_for_actor(
    actor: User | None,
    *,
    organization: Organization | None = None,
    site: Site | None = None,
    department: Department | None = None,
) -> QuerySet[Shift]:
    return list_shifts_for_actor(
        actor,
        organization=organization,
        site=site,
        department=department,
        active_only=True,
    )
