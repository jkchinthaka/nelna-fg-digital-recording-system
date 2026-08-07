"""FG Product domain services — writes and authorization; no seed data."""

from __future__ import annotations

import uuid
from typing import Any

from django.core.exceptions import PermissionDenied, ValidationError
from django.db import IntegrityError, transaction

from apps.access_control.services import Scope, require_permission
from apps.accounts.models import User
from apps.master_data.models import FGProduct
from apps.organizations.models import Organization
from apps.organizations.services import normalize_code, normalize_name
from apps.security_audit.services import record_event

VIEW_FG_PRODUCT = "master_data.view_fgproduct"
MANAGE_FG_PRODUCT = "master_data.manage_fgproduct"

_UNSET: Any = object()


def _require_authenticated_actor(actor: User | None) -> User:
    if actor is None or not getattr(actor, "is_authenticated", False) or not actor.is_active:
        raise PermissionDenied("Authentication required.")
    return actor


def product_authorization_scope(product: FGProduct) -> Scope:
    return Scope(organization_id=product.organization_id)


def _product_metadata(
    product: FGProduct,
    *,
    changed_fields: list[str] | None = None,
) -> dict[str, Any]:
    meta: dict[str, Any] = {
        "fg_product_id": str(product.id),
        "fg_product_code": product.code,
        "organization_id": str(product.organization_id),
        "is_active": product.is_active,
    }
    if changed_fields:
        meta["changed_fields"] = changed_fields
    return meta


def _prepare_product_fields(
    *, code: str, name: str, description: str | None
) -> tuple[str, str, str]:
    normalized_code = normalize_code(code)
    normalized_name = normalize_name(name)
    if not normalized_code:
        raise ValidationError({"code": "Code cannot be blank."})
    if not normalized_name:
        raise ValidationError({"name": "Name cannot be blank."})
    normalized_description = (description or "").strip()
    return normalized_code, normalized_name, normalized_description


def _reraise_product_persistence_error(exc: Exception) -> None:
    if isinstance(exc, ValidationError):
        messages = " ".join(str(m) for m in exc.messages)
        if "md_fgproduct_org_code_ci_uniq" in messages or "unique" in messages.lower():
            raise ValidationError(
                {
                    "code": (
                        "An FG Product with this code already exists in the selected organization."
                    )
                }
            ) from exc
        raise
    if isinstance(exc, IntegrityError):
        raise ValidationError(
            {"code": "An FG Product with this code already exists in the selected organization."}
        ) from exc
    raise


@transaction.atomic
def create_fg_product(
    *,
    actor: User | None,
    organization: Organization,
    code: str,
    name: str,
    description: str = "",
    is_active: bool = True,
) -> FGProduct:
    user = _require_authenticated_actor(actor)
    require_permission(
        user,
        MANAGE_FG_PRODUCT,
        scope=Scope(organization_id=organization.id),
    )
    normalized_code, normalized_name, normalized_description = _prepare_product_fields(
        code=code,
        name=name,
        description=description,
    )
    product = FGProduct(
        organization=organization,
        code=normalized_code,
        name=normalized_name,
        description=normalized_description,
        is_active=is_active,
    )
    try:
        product.full_clean()
        product.save()
    except (ValidationError, IntegrityError) as exc:
        _reraise_product_persistence_error(exc)

    record_event(
        event_type="FG_PRODUCT_CREATED",
        actor=user,
        metadata=_product_metadata(product),
    )
    return product


@transaction.atomic
def update_fg_product(
    *,
    actor: User | None,
    product_id: uuid.UUID,
    code: str | None = None,
    name: str | None = None,
    description: Any = _UNSET,
) -> FGProduct:
    user = _require_authenticated_actor(actor)
    product = (
        FGProduct.objects.select_for_update(of=("self",))
        .select_related("organization")
        .filter(pk=product_id)
        .first()
    )
    if product is None:
        raise ValidationError({"product": "FG Product not found."})

    require_permission(user, MANAGE_FG_PRODUCT, scope=product_authorization_scope(product))

    next_code = product.code if code is None else code
    next_name = product.name if name is None else name
    next_description: str = product.description if description is _UNSET else str(description or "")
    normalized_code, normalized_name, normalized_description = _prepare_product_fields(
        code=next_code,
        name=next_name,
        description=next_description,
    )

    field_map: dict[str, Any] = {
        "code": normalized_code,
        "name": normalized_name,
        "description": normalized_description,
    }
    changed: list[str] = []
    for field, value in field_map.items():
        if getattr(product, field) != value:
            setattr(product, field, value)
            changed.append(field)

    if not changed:
        return product

    try:
        product.full_clean()
        product.save()
    except (ValidationError, IntegrityError) as exc:
        _reraise_product_persistence_error(exc)

    record_event(
        event_type="FG_PRODUCT_UPDATED",
        actor=user,
        metadata=_product_metadata(product, changed_fields=changed),
    )
    return product


@transaction.atomic
def activate_fg_product(*, actor: User | None, product_id: uuid.UUID) -> FGProduct:
    user = _require_authenticated_actor(actor)
    product = FGProduct.objects.select_for_update().filter(pk=product_id).first()
    if product is None:
        raise ValidationError({"product": "FG Product not found."})
    require_permission(user, MANAGE_FG_PRODUCT, scope=product_authorization_scope(product))
    if product.is_active:
        return product
    product.is_active = True
    product.save(update_fields=["is_active", "updated_at"])
    record_event(
        event_type="FG_PRODUCT_ACTIVATED",
        actor=user,
        metadata=_product_metadata(product),
    )
    return product


@transaction.atomic
def deactivate_fg_product(*, actor: User | None, product_id: uuid.UUID) -> FGProduct:
    user = _require_authenticated_actor(actor)
    product = FGProduct.objects.select_for_update().filter(pk=product_id).first()
    if product is None:
        raise ValidationError({"product": "FG Product not found."})
    require_permission(user, MANAGE_FG_PRODUCT, scope=product_authorization_scope(product))
    if not product.is_active:
        return product
    product.is_active = False
    product.save(update_fields=["is_active", "updated_at"])
    record_event(
        event_type="FG_PRODUCT_DEACTIVATED",
        actor=user,
        metadata=_product_metadata(product),
    )
    return product
