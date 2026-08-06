"""Organization domain services — soft deactivate/reactivate only; no hard delete."""

from __future__ import annotations

import datetime
import uuid
from typing import Any

from django.core.exceptions import PermissionDenied, ValidationError
from django.db import IntegrityError, transaction

from apps.access_control.services import Scope, require_permission
from apps.accounts.models import User
from apps.organizations.models import Department, Organization, Shift, Site
from apps.security_audit.services import record_event

VIEW_SHIFT = "organizations.view_shift"
MANAGE_SHIFT = "organizations.manage_shift"


def normalize_code(value: str) -> str:
    """Strip surrounding whitespace and uppercase for consistent code storage."""
    return value.strip().upper()


def normalize_name(value: str) -> str:
    """Strip surrounding whitespace only; do not alter display-name casing."""
    return value.strip()


def _require_authenticated_actor(actor: User | None) -> User:
    if actor is None or not getattr(actor, "is_authenticated", False) or not actor.is_active:
        raise PermissionDenied("Authentication required.")
    return actor


def shift_authorization_scope(shift: Shift) -> Scope:
    return Scope(
        organization_id=shift.organization_id,
        site_id=shift.site_id,
        department_id=shift.department_id,
    )


def _shift_metadata(shift: Shift, *, changed_fields: list[str] | None = None) -> dict[str, Any]:
    meta: dict[str, Any] = {
        "shift_id": str(shift.id),
        "shift_code": shift.code,
        "organization_id": str(shift.organization_id),
        "is_active": shift.is_active,
        "is_overnight": shift.is_overnight,
    }
    if shift.site_id:
        meta["site_id"] = str(shift.site_id)
    if shift.department_id:
        meta["department_id"] = str(shift.department_id)
    if changed_fields:
        meta["changed_fields"] = changed_fields
    return meta


def _validate_shift_scope(
    *,
    organization: Organization,
    site: Site | None,
    department: Department | None,
) -> None:
    if department is not None and site is None:
        raise ValidationError({"department": "Department requires a site."})
    if site is not None and site.organization_id != organization.id:
        raise ValidationError({"site": "Site must belong to the selected organization."})
    if department is not None and department.organization_id != organization.id:
        raise ValidationError(
            {"department": "Department must belong to the selected organization."}
        )
    if department is not None and site is not None and department.site_id != site.id:
        raise ValidationError({"department": "Department must belong to the selected site."})


def _prepare_shift_fields(
    *,
    code: str,
    name: str,
    effective_from: datetime.date,
    effective_to: datetime.date | None,
) -> tuple[str, str]:
    normalized_code = normalize_code(code)
    normalized_name = normalize_name(name)
    if not normalized_code:
        raise ValidationError({"code": "Shift code is required."})
    if not normalized_name:
        raise ValidationError({"name": "Shift name is required."})
    if effective_to is not None and effective_to < effective_from:
        raise ValidationError(
            {"effective_to": "effective_to cannot be earlier than effective_from."}
        )
    return normalized_code, normalized_name


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


def _reraise_shift_persistence_error(exc: Exception) -> None:
    """Map DB/unique failures to a stable field error for forms and APIs."""
    if isinstance(exc, ValidationError):
        messages = " ".join(str(m) for m in exc.messages)
        if "org_shift_scope_code_ci_uniq" in messages or "unique" in messages.lower():
            raise ValidationError(
                {"code": "A Shift with this code already exists in the selected scope."}
            ) from exc
        raise
    if isinstance(exc, IntegrityError):
        raise ValidationError(
            {"code": "A Shift with this code already exists in the selected scope."}
        ) from exc
    raise


@transaction.atomic
def create_shift(
    *,
    actor: User | None,
    organization: Organization,
    code: str,
    name: str,
    start_time: datetime.time,
    end_time: datetime.time,
    effective_from: datetime.date,
    site: Site | None = None,
    department: Department | None = None,
    effective_to: datetime.date | None = None,
    is_active: bool = True,
) -> Shift:
    user = _require_authenticated_actor(actor)
    scope = Scope(
        organization_id=organization.id,
        site_id=site.id if site is not None else None,
        department_id=department.id if department is not None else None,
    )
    require_permission(user, MANAGE_SHIFT, scope=scope)
    _validate_shift_scope(organization=organization, site=site, department=department)
    normalized_code, normalized_name = _prepare_shift_fields(
        code=code,
        name=name,
        effective_from=effective_from,
        effective_to=effective_to,
    )

    shift = Shift(
        organization=organization,
        site=site,
        department=department,
        code=normalized_code,
        name=normalized_name,
        start_time=start_time,
        end_time=end_time,
        effective_from=effective_from,
        effective_to=effective_to,
        is_active=is_active,
    )
    try:
        shift.full_clean()
        shift.save()
    except (ValidationError, IntegrityError) as exc:
        _reraise_shift_persistence_error(exc)

    record_event(
        event_type="SHIFT_CREATED",
        actor=user,
        metadata=_shift_metadata(shift),
    )
    return shift


_UNSET: Any = object()


@transaction.atomic
def update_shift(
    *,
    actor: User | None,
    shift_id: uuid.UUID,
    code: str | None = None,
    name: str | None = None,
    start_time: datetime.time | None = None,
    end_time: datetime.time | None = None,
    effective_from: datetime.date | None = None,
    effective_to: Any = _UNSET,
    site: Any = _UNSET,
    department: Any = _UNSET,
) -> Shift:
    user = _require_authenticated_actor(actor)
    # Lock only Shift rows — nullable site/department joins cannot use FOR UPDATE.
    shift = (
        Shift.objects.select_for_update(of=("self",))
        .select_related("organization", "site", "department")
        .filter(pk=shift_id)
        .first()
    )
    if shift is None:
        raise ValidationError({"shift": "Shift not found."})

    require_permission(user, MANAGE_SHIFT, scope=shift_authorization_scope(shift))

    next_site: Site | None = shift.site if site is _UNSET else site
    next_department: Department | None = shift.department if department is _UNSET else department
    next_code = shift.code if code is None else code
    next_name = shift.name if name is None else name
    next_start = shift.start_time if start_time is None else start_time
    next_end = shift.end_time if end_time is None else end_time
    next_from = shift.effective_from if effective_from is None else effective_from
    next_to: datetime.date | None = shift.effective_to if effective_to is _UNSET else effective_to

    _validate_shift_scope(
        organization=shift.organization,
        site=next_site,
        department=next_department,
    )
    normalized_code, normalized_name = _prepare_shift_fields(
        code=next_code,
        name=next_name,
        effective_from=next_from,
        effective_to=next_to,
    )

    field_map: dict[str, Any] = {
        "code": normalized_code,
        "name": normalized_name,
        "start_time": next_start,
        "end_time": next_end,
        "effective_from": next_from,
        "effective_to": next_to,
        "site": next_site,
        "department": next_department,
    }
    changed: list[str] = []
    for field, value in field_map.items():
        if getattr(shift, field) != value:
            setattr(shift, field, value)
            changed.append(field)

    if not changed:
        return shift

    try:
        shift.full_clean()
        shift.save()
    except (ValidationError, IntegrityError) as exc:
        _reraise_shift_persistence_error(exc)

    record_event(
        event_type="SHIFT_UPDATED",
        actor=user,
        metadata=_shift_metadata(shift, changed_fields=changed),
    )
    return shift


@transaction.atomic
def activate_shift(*, actor: User | None, shift_id: uuid.UUID) -> Shift:
    user = _require_authenticated_actor(actor)
    shift = Shift.objects.select_for_update().filter(pk=shift_id).first()
    if shift is None:
        raise ValidationError({"shift": "Shift not found."})
    require_permission(user, MANAGE_SHIFT, scope=shift_authorization_scope(shift))
    if shift.is_active:
        return shift
    shift.is_active = True
    shift.save(update_fields=["is_active", "updated_at"])
    record_event(
        event_type="SHIFT_ACTIVATED",
        actor=user,
        metadata=_shift_metadata(shift),
    )
    return shift


@transaction.atomic
def deactivate_shift(*, actor: User | None, shift_id: uuid.UUID) -> Shift:
    user = _require_authenticated_actor(actor)
    shift = Shift.objects.select_for_update().filter(pk=shift_id).first()
    if shift is None:
        raise ValidationError({"shift": "Shift not found."})
    require_permission(user, MANAGE_SHIFT, scope=shift_authorization_scope(shift))
    if not shift.is_active:
        return shift
    shift.is_active = False
    shift.save(update_fields=["is_active", "updated_at"])
    record_event(
        event_type="SHIFT_DEACTIVATED",
        actor=user,
        metadata=_shift_metadata(shift),
    )
    return shift
