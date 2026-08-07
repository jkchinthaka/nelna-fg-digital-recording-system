"""Permission-aware FG Product selectors — query-level organization scoping."""

from __future__ import annotations

import uuid
from typing import Literal

from django.core.exceptions import PermissionDenied
from django.db.models import Q, QuerySet

from apps.access_control.services import (
    organization_ids_with_permission,
    user_has_permission,
    user_has_permission_any_scope,
)
from apps.accounts.models import User
from apps.master_data.models import FGProduct
from apps.master_data.services import (
    MANAGE_FG_PRODUCT,
    VIEW_FG_PRODUCT,
    product_authorization_scope,
)
from apps.organizations.models import Organization

StatusFilter = Literal["all", "active", "inactive"]


def actor_can_view_fg_products(actor: User | None) -> bool:
    return user_has_permission_any_scope(actor, VIEW_FG_PRODUCT)


def actor_can_manage_fg_products(actor: User | None) -> bool:
    return user_has_permission_any_scope(actor, MANAGE_FG_PRODUCT)


def actor_can_manage_fg_product(actor: User | None, product: FGProduct) -> bool:
    if actor is None or not getattr(actor, "is_authenticated", False) or not actor.is_active:
        return False
    return user_has_permission(actor, MANAGE_FG_PRODUCT, scope=product_authorization_scope(product))


def _actor_may_view_product(actor: User | None, product: FGProduct) -> bool:
    if actor is None or not getattr(actor, "is_authenticated", False) or not actor.is_active:
        return False
    return user_has_permission(actor, VIEW_FG_PRODUCT, scope=product_authorization_scope(product))


def get_fg_product(actor: User | None, product_id: uuid.UUID) -> FGProduct | None:
    product = FGProduct.objects.select_related("organization").filter(pk=product_id).first()
    if product is None:
        return None
    if not _actor_may_view_product(actor, product):
        raise PermissionDenied("Permission denied.")
    return product


def list_fg_products(
    actor: User | None,
    *,
    organization: Organization | None = None,
    status: StatusFilter = "all",
    search: str | None = None,
) -> QuerySet[FGProduct]:
    if actor is None or not getattr(actor, "is_authenticated", False) or not actor.is_active:
        return FGProduct.objects.none()

    allowed_org_ids = organization_ids_with_permission(actor, VIEW_FG_PRODUCT)
    if not allowed_org_ids:
        return FGProduct.objects.none()

    qs = FGProduct.objects.select_related("organization").filter(
        organization_id__in=allowed_org_ids
    )
    if organization is not None:
        if organization.id not in allowed_org_ids:
            return FGProduct.objects.none()
        qs = qs.filter(organization=organization)

    if status == "active":
        qs = qs.filter(is_active=True)
    elif status == "inactive":
        qs = qs.filter(is_active=False)

    if search:
        term = search.strip()
        if term:
            qs = qs.filter(Q(code__icontains=term) | Q(name__icontains=term))

    return qs.order_by("organization__code", "code")


def list_active_fg_products(
    actor: User | None,
    *,
    organization: Organization | None = None,
) -> QuerySet[FGProduct]:
    return list_fg_products(actor, organization=organization, status="active")


def organizations_for_fg_product_actor(actor: User | None) -> QuerySet[Organization]:
    allowed = organization_ids_with_permission(actor, VIEW_FG_PRODUCT)
    manage_ids = organization_ids_with_permission(actor, MANAGE_FG_PRODUCT)
    # Form create needs manage; list filters use view. Union for filter dropdowns.
    org_ids = allowed | manage_ids
    if not org_ids:
        return Organization.objects.none()
    return Organization.objects.filter(pk__in=org_ids).order_by("code")


def organizations_for_fg_product_manage(actor: User | None) -> QuerySet[Organization]:
    org_ids = organization_ids_with_permission(actor, MANAGE_FG_PRODUCT)
    if not org_ids:
        return Organization.objects.none()
    return Organization.objects.filter(pk__in=org_ids).order_by("code")
