"""Checklist definition services — writes, lifecycle, authorization; no seed content."""

from __future__ import annotations

import uuid
from typing import Any

from django.core.exceptions import PermissionDenied, ValidationError
from django.db import IntegrityError, transaction
from django.db.models import Max
from django.utils import timezone

from apps.access_control.services import Scope, require_permission
from apps.accounts.models import User
from apps.checklists.models import (
    ChecklistItem,
    ChecklistSection,
    ChecklistTemplate,
    ChecklistVersion,
    ChecklistVersionStatus,
)
from apps.master_data.models import FGProduct
from apps.organizations.models import Organization
from apps.organizations.services import normalize_code, normalize_name
from apps.security_audit.services import record_event

VIEW_CHECKLIST = "checklists.view_checklisttemplate"
MANAGE_CHECKLIST = "checklists.manage_checklist"

_UNSET: Any = object()

# Centralized lifecycle — only these transitions are supported.
ALLOWED_VERSION_TRANSITIONS: frozenset[tuple[str, str]] = frozenset(
    {
        (ChecklistVersionStatus.DRAFT, ChecklistVersionStatus.PUBLISHED),
        (ChecklistVersionStatus.PUBLISHED, ChecklistVersionStatus.RETIRED),
    }
)


def assert_version_transition_allowed(*, current: str, target: str) -> None:
    """Raise ValidationError when ``current`` → ``target`` is not an allowed transition."""
    if (current, target) not in ALLOWED_VERSION_TRANSITIONS:
        raise ValidationError(
            {
                "version": (
                    f"Illegal checklist version transition from {current} to {target}. "
                    "Allowed transitions: DRAFT→PUBLISHED, PUBLISHED→RETIRED."
                )
            }
        )


def _require_authenticated_actor(actor: User | None) -> User:
    if actor is None or not getattr(actor, "is_authenticated", False) or not actor.is_active:
        raise PermissionDenied("Authentication required.")
    return actor


def template_authorization_scope(template: ChecklistTemplate) -> Scope:
    return Scope(organization_id=template.organization_id)


def version_authorization_scope(version: ChecklistVersion) -> Scope:
    return Scope(organization_id=version.template.organization_id)


def _template_metadata(
    template: ChecklistTemplate,
    *,
    changed_fields: list[str] | None = None,
) -> dict[str, Any]:
    meta: dict[str, Any] = {
        "checklist_template_id": str(template.id),
        "checklist_template_code": template.code,
        "organization_id": str(template.organization_id),
        "is_active": template.is_active,
        "product_id": str(template.product_id) if template.product_id else None,
    }
    if changed_fields:
        meta["changed_fields"] = changed_fields
    return meta


def _version_metadata(
    version: ChecklistVersion,
    *,
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    meta: dict[str, Any] = {
        "checklist_version_id": str(version.id),
        "checklist_template_id": str(version.template_id),
        "checklist_template_code": version.template.code,
        "organization_id": str(version.template.organization_id),
        "version_number": version.version_number,
        "status": version.status,
    }
    if extra:
        meta.update(extra)
    return meta


def _prepare_template_fields(
    *,
    code: str,
    name: str,
    description: str | None,
) -> tuple[str, str, str]:
    normalized_code = normalize_code(code)
    normalized_name = normalize_name(name)
    if not normalized_code:
        raise ValidationError({"code": "Code cannot be blank."})
    if not normalized_name:
        raise ValidationError({"name": "Name cannot be blank."})
    return normalized_code, normalized_name, (description or "").strip()


def _validate_product_for_org(
    *,
    organization: Organization,
    product: FGProduct | None,
) -> FGProduct | None:
    if product is None:
        return None
    if product.organization_id != organization.id:
        raise ValidationError(
            {"product": "Product must belong to the same organization as the template."}
        )
    return product


def _reraise_template_persistence_error(exc: Exception) -> None:
    if isinstance(exc, ValidationError):
        messages = " ".join(str(m) for m in exc.messages)
        if "chk_template_org_code_ci_uniq" in messages or "unique" in messages.lower():
            raise ValidationError(
                {
                    "code": (
                        "A checklist template with this code already exists "
                        "in the selected organization."
                    )
                }
            ) from exc
        raise
    if isinstance(exc, IntegrityError):
        raise ValidationError(
            {
                "code": (
                    "A checklist template with this code already exists "
                    "in the selected organization."
                )
            }
        ) from exc
    raise


def _require_draft(version: ChecklistVersion) -> None:
    if not version.is_draft:
        raise ValidationError(
            {
                "version": (
                    "Published or retired checklist versions cannot be modified. "
                    "Create a new draft version instead."
                )
            }
        )


def _lock_version(version_id: uuid.UUID) -> ChecklistVersion:
    version = (
        ChecklistVersion.objects.select_for_update(of=("self",))
        .select_related("template", "template__organization", "template__product")
        .filter(pk=version_id)
        .first()
    )
    if version is None:
        raise ValidationError({"version": "Checklist version not found."})
    return version


def _next_section_position(version: ChecklistVersion) -> int:
    current = version.sections.aggregate(m=Max("position"))["m"]
    return int(current or 0) + 1


def _next_item_position(section: ChecklistSection) -> int:
    current = section.items.aggregate(m=Max("position"))["m"]
    return int(current or 0) + 1


def _swap_positions(
    *,
    queryset_model: type[ChecklistSection] | type[ChecklistItem],
    parent_filter: dict[str, Any],
    current: ChecklistSection | ChecklistItem,
    direction: str,
) -> None:
    if direction not in {"up", "down"}:
        raise ValidationError({"direction": "Direction must be up or down."})
    siblings: list[ChecklistSection | ChecklistItem] = list(
        queryset_model.objects.select_for_update()
        .filter(**parent_filter)
        .order_by("position", "pk")
    )
    ids = [row.pk for row in siblings]
    try:
        index = ids.index(current.pk)
    except ValueError as exc:
        raise ValidationError({"object": "Row not found in parent."}) from exc
    target_index = index - 1 if direction == "up" else index + 1
    if target_index < 0 or target_index >= len(siblings):
        return
    other = siblings[target_index]
    current_pos, other_pos = current.position, other.position
    # Temporary unique-safe swap using a high sentinel.
    sentinel = max((row.position for row in siblings), default=0) + 1000
    other.position = sentinel
    other.save(update_fields=["position"])
    current.position = other_pos
    current.save(update_fields=["position"])
    other.position = current_pos
    other.save(update_fields=["position"])


@transaction.atomic
def create_checklist_template(
    *,
    actor: User | None,
    organization: Organization,
    code: str,
    name: str,
    description: str = "",
    product: FGProduct | None = None,
    is_active: bool = True,
) -> ChecklistTemplate:
    user = _require_authenticated_actor(actor)
    require_permission(user, MANAGE_CHECKLIST, scope=Scope(organization_id=organization.id))
    normalized_code, normalized_name, normalized_description = _prepare_template_fields(
        code=code,
        name=name,
        description=description,
    )
    product = _validate_product_for_org(organization=organization, product=product)
    template = ChecklistTemplate(
        organization=organization,
        product=product,
        code=normalized_code,
        name=normalized_name,
        description=normalized_description,
        is_active=is_active,
    )
    try:
        template.full_clean()
        template.save()
    except (ValidationError, IntegrityError) as exc:
        _reraise_template_persistence_error(exc)

    record_event(
        event_type="CHECKLIST_TEMPLATE_CREATED",
        actor=user,
        metadata=_template_metadata(template),
    )
    return template


@transaction.atomic
def update_checklist_template(
    *,
    actor: User | None,
    template_id: uuid.UUID,
    code: str | None = None,
    name: str | None = None,
    description: Any = _UNSET,
    product: Any = _UNSET,
) -> ChecklistTemplate:
    user = _require_authenticated_actor(actor)
    template = (
        ChecklistTemplate.objects.select_for_update(of=("self",))
        .select_related("organization", "product")
        .filter(pk=template_id)
        .first()
    )
    if template is None:
        raise ValidationError({"template": "Checklist template not found."})
    require_permission(user, MANAGE_CHECKLIST, scope=template_authorization_scope(template))

    next_code = template.code if code is None else code
    next_name = template.name if name is None else name
    next_description = template.description if description is _UNSET else str(description or "")
    normalized_code, normalized_name, normalized_description = _prepare_template_fields(
        code=next_code,
        name=next_name,
        description=next_description,
    )
    next_product: FGProduct | None
    if product is _UNSET:
        next_product = template.product
    else:
        next_product = _validate_product_for_org(
            organization=template.organization,
            product=product,
        )

    field_map: dict[str, Any] = {
        "code": normalized_code,
        "name": normalized_name,
        "description": normalized_description,
        "product": next_product,
    }
    changed: list[str] = []
    for field, value in field_map.items():
        if getattr(template, field) != value:
            setattr(template, field, value)
            changed.append(field)
    if not changed:
        return template
    try:
        template.full_clean()
        template.save()
    except (ValidationError, IntegrityError) as exc:
        _reraise_template_persistence_error(exc)

    record_event(
        event_type="CHECKLIST_TEMPLATE_UPDATED",
        actor=user,
        metadata=_template_metadata(template, changed_fields=changed),
    )
    return template


@transaction.atomic
def activate_checklist_template(*, actor: User | None, template_id: uuid.UUID) -> ChecklistTemplate:
    user = _require_authenticated_actor(actor)
    template = ChecklistTemplate.objects.select_for_update().filter(pk=template_id).first()
    if template is None:
        raise ValidationError({"template": "Checklist template not found."})
    require_permission(user, MANAGE_CHECKLIST, scope=template_authorization_scope(template))
    if template.is_active:
        return template
    template.is_active = True
    template.save(update_fields=["is_active", "updated_at"])
    record_event(
        event_type="CHECKLIST_TEMPLATE_ACTIVATED",
        actor=user,
        metadata=_template_metadata(template),
    )
    return template


@transaction.atomic
def deactivate_checklist_template(
    *, actor: User | None, template_id: uuid.UUID
) -> ChecklistTemplate:
    user = _require_authenticated_actor(actor)
    template = ChecklistTemplate.objects.select_for_update().filter(pk=template_id).first()
    if template is None:
        raise ValidationError({"template": "Checklist template not found."})
    require_permission(user, MANAGE_CHECKLIST, scope=template_authorization_scope(template))
    if not template.is_active:
        return template
    template.is_active = False
    template.save(update_fields=["is_active", "updated_at"])
    record_event(
        event_type="CHECKLIST_TEMPLATE_DEACTIVATED",
        actor=user,
        metadata=_template_metadata(template),
    )
    return template


def _allocate_next_version_number(template: ChecklistTemplate) -> int:
    locked = ChecklistTemplate.objects.select_for_update().filter(pk=template.pk).first()
    if locked is None:
        raise ValidationError({"template": "Checklist template not found."})
    current = locked.versions.aggregate(m=Max("version_number"))["m"]
    return int(current or 0) + 1


def _clone_structure(*, source: ChecklistVersion, target: ChecklistVersion) -> None:
    for section in source.sections.prefetch_related("items").order_by("position", "pk"):
        new_section = ChecklistSection.objects.create(
            version=target,
            title=section.title,
            description=section.description,
            position=section.position,
        )
        for item in section.items.order_by("position", "pk"):
            ChecklistItem.objects.create(
                section=new_section,
                code=item.code,
                label=item.label,
                help_text=item.help_text,
                position=item.position,
                is_required=item.is_required,
            )


@transaction.atomic
@transaction.atomic
def create_checklist_version(
    *,
    actor: User | None,
    template_id: uuid.UUID,
    source_version_id: uuid.UUID | None = None,
) -> ChecklistVersion:
    """
    Create a new DRAFT version.

    When ``source_version_id`` is provided, clone section/item rows into new rows
    (never share mutable structure across versions).
    """
    user = _require_authenticated_actor(actor)
    template = (
        ChecklistTemplate.objects.select_for_update(of=("self",))
        .select_related("organization")
        .filter(pk=template_id)
        .first()
    )
    if template is None:
        raise ValidationError({"template": "Checklist template not found."})
    require_permission(user, MANAGE_CHECKLIST, scope=template_authorization_scope(template))

    source: ChecklistVersion | None = None
    if source_version_id is not None:
        source = (
            ChecklistVersion.objects.select_related("template")
            .filter(pk=source_version_id, template_id=template.id)
            .first()
        )
        if source is None:
            raise ValidationError({"source_version": "Source version not found for this template."})

    version: ChecklistVersion | None = None
    last_error: Exception | None = None
    # Template row lock serializes allocation; unique constraint + savepoint retry
    # covers residual races if another writer sneaks between max() and insert.
    for _attempt in range(2):
        version_number = _allocate_next_version_number(template)
        candidate = ChecklistVersion(
            template=template,
            version_number=version_number,
            status=ChecklistVersionStatus.DRAFT,
        )
        try:
            with transaction.atomic():
                candidate.full_clean()
                candidate.save()
            version = candidate
            break
        except IntegrityError as exc:
            last_error = exc
            continue
        except ValidationError as exc:
            raise ValidationError(
                {"version_number": "Unable to allocate the next checklist version number."}
            ) from exc
    if version is None:
        raise ValidationError(
            {"version_number": "Unable to allocate the next checklist version number."}
        ) from last_error

    if source is not None:
        _clone_structure(source=source, target=version)
        record_event(
            event_type="CHECKLIST_VERSION_CLONED",
            actor=user,
            metadata=_version_metadata(
                version,
                extra={
                    "source_version_id": str(source.id),
                    "source_version_number": source.version_number,
                },
            ),
        )
    else:
        record_event(
            event_type="CHECKLIST_VERSION_CREATED",
            actor=user,
            metadata=_version_metadata(version),
        )
    return version


@transaction.atomic
def add_checklist_section(
    *,
    actor: User | None,
    version_id: uuid.UUID,
    title: str,
    description: str = "",
) -> ChecklistSection:
    user = _require_authenticated_actor(actor)
    version = _lock_version(version_id)
    require_permission(user, MANAGE_CHECKLIST, scope=version_authorization_scope(version))
    _require_draft(version)
    normalized_title = normalize_name(title)
    if not normalized_title:
        raise ValidationError({"title": "Title cannot be blank."})
    section = ChecklistSection(
        version=version,
        title=normalized_title,
        description=(description or "").strip(),
        position=_next_section_position(version),
    )
    try:
        section.full_clean()
        section.save()
    except (ValidationError, IntegrityError) as exc:
        raise ValidationError({"section": "Unable to add checklist section."}) from exc
    return section


@transaction.atomic
def update_checklist_section(
    *,
    actor: User | None,
    section_id: uuid.UUID,
    title: str | None = None,
    description: Any = _UNSET,
) -> ChecklistSection:
    user = _require_authenticated_actor(actor)
    section = (
        ChecklistSection.objects.select_for_update(of=("self",))
        .select_related("version", "version__template")
        .filter(pk=section_id)
        .first()
    )
    if section is None:
        raise ValidationError({"section": "Checklist section not found."})
    require_permission(user, MANAGE_CHECKLIST, scope=version_authorization_scope(section.version))
    _require_draft(section.version)
    if title is not None:
        normalized_title = normalize_name(title)
        if not normalized_title:
            raise ValidationError({"title": "Title cannot be blank."})
        section.title = normalized_title
    if description is not _UNSET:
        section.description = str(description or "").strip()
    try:
        section.full_clean()
        section.save()
    except (ValidationError, IntegrityError) as exc:
        raise ValidationError({"section": "Unable to update checklist section."}) from exc
    return section


@transaction.atomic
def remove_checklist_section(*, actor: User | None, section_id: uuid.UUID) -> None:
    user = _require_authenticated_actor(actor)
    section = (
        ChecklistSection.objects.select_for_update(of=("self",))
        .select_related("version", "version__template")
        .filter(pk=section_id)
        .first()
    )
    if section is None:
        raise ValidationError({"section": "Checklist section not found."})
    require_permission(user, MANAGE_CHECKLIST, scope=version_authorization_scope(section.version))
    _require_draft(section.version)
    version = section.version
    section.delete()
    # Compact positions sequentially.
    for index, sibling in enumerate(
        version.sections.order_by("position", "pk"),
        start=1,
    ):
        if sibling.position != index:
            sibling.position = index
            sibling.save(update_fields=["position"])


@transaction.atomic
def move_checklist_section(
    *,
    actor: User | None,
    section_id: uuid.UUID,
    direction: str,
) -> ChecklistSection:
    user = _require_authenticated_actor(actor)
    section = (
        ChecklistSection.objects.select_for_update(of=("self",))
        .select_related("version", "version__template")
        .filter(pk=section_id)
        .first()
    )
    if section is None:
        raise ValidationError({"section": "Checklist section not found."})
    require_permission(user, MANAGE_CHECKLIST, scope=version_authorization_scope(section.version))
    _require_draft(section.version)
    _swap_positions(
        queryset_model=ChecklistSection,
        parent_filter={"version_id": section.version_id},
        current=section,
        direction=direction,
    )
    section.refresh_from_db()
    return section


@transaction.atomic
def add_checklist_item(
    *,
    actor: User | None,
    section_id: uuid.UUID,
    code: str,
    label: str,
    help_text: str = "",
    is_required: bool = True,
) -> ChecklistItem:
    user = _require_authenticated_actor(actor)
    section = (
        ChecklistSection.objects.select_for_update(of=("self",))
        .select_related("version", "version__template")
        .filter(pk=section_id)
        .first()
    )
    if section is None:
        raise ValidationError({"section": "Checklist section not found."})
    require_permission(user, MANAGE_CHECKLIST, scope=version_authorization_scope(section.version))
    _require_draft(section.version)
    normalized_code = normalize_code(code)
    normalized_label = normalize_name(label)
    if not normalized_code:
        raise ValidationError({"code": "Code cannot be blank."})
    if not normalized_label:
        raise ValidationError({"label": "Label cannot be blank."})
    item = ChecklistItem(
        section=section,
        code=normalized_code,
        label=normalized_label,
        help_text=(help_text or "").strip(),
        position=_next_item_position(section),
        is_required=is_required,
    )
    try:
        item.full_clean()
        item.save()
    except (ValidationError, IntegrityError) as exc:
        messages = " ".join(str(m) for m in getattr(exc, "messages", [str(exc)]))
        if "chk_item_section_code_ci_uniq" in messages or "unique" in messages.lower():
            raise ValidationError(
                {"code": "An item with this code already exists in the section."}
            ) from exc
        raise ValidationError({"item": "Unable to add checklist item."}) from exc
    return item


@transaction.atomic
def update_checklist_item(
    *,
    actor: User | None,
    item_id: uuid.UUID,
    code: str | None = None,
    label: str | None = None,
    help_text: Any = _UNSET,
    is_required: bool | None = None,
) -> ChecklistItem:
    user = _require_authenticated_actor(actor)
    item = (
        ChecklistItem.objects.select_for_update(of=("self",))
        .select_related("section", "section__version", "section__version__template")
        .filter(pk=item_id)
        .first()
    )
    if item is None:
        raise ValidationError({"item": "Checklist item not found."})
    require_permission(
        user, MANAGE_CHECKLIST, scope=version_authorization_scope(item.section.version)
    )
    _require_draft(item.section.version)
    if code is not None:
        normalized_code = normalize_code(code)
        if not normalized_code:
            raise ValidationError({"code": "Code cannot be blank."})
        item.code = normalized_code
    if label is not None:
        normalized_label = normalize_name(label)
        if not normalized_label:
            raise ValidationError({"label": "Label cannot be blank."})
        item.label = normalized_label
    if help_text is not _UNSET:
        item.help_text = str(help_text or "").strip()
    if is_required is not None:
        item.is_required = is_required
    try:
        item.full_clean()
        item.save()
    except (ValidationError, IntegrityError) as exc:
        messages = " ".join(str(m) for m in getattr(exc, "messages", [str(exc)]))
        if "chk_item_section_code_ci_uniq" in messages or "unique" in messages.lower():
            raise ValidationError(
                {"code": "An item with this code already exists in the section."}
            ) from exc
        raise ValidationError({"item": "Unable to update checklist item."}) from exc
    return item


@transaction.atomic
def remove_checklist_item(*, actor: User | None, item_id: uuid.UUID) -> None:
    user = _require_authenticated_actor(actor)
    item = (
        ChecklistItem.objects.select_for_update(of=("self",))
        .select_related("section", "section__version", "section__version__template")
        .filter(pk=item_id)
        .first()
    )
    if item is None:
        raise ValidationError({"item": "Checklist item not found."})
    require_permission(
        user, MANAGE_CHECKLIST, scope=version_authorization_scope(item.section.version)
    )
    _require_draft(item.section.version)
    section = item.section
    item.delete()
    for index, sibling in enumerate(section.items.order_by("position", "pk"), start=1):
        if sibling.position != index:
            sibling.position = index
            sibling.save(update_fields=["position"])


@transaction.atomic
def move_checklist_item(
    *,
    actor: User | None,
    item_id: uuid.UUID,
    direction: str,
) -> ChecklistItem:
    user = _require_authenticated_actor(actor)
    item = (
        ChecklistItem.objects.select_for_update(of=("self",))
        .select_related("section", "section__version", "section__version__template")
        .filter(pk=item_id)
        .first()
    )
    if item is None:
        raise ValidationError({"item": "Checklist item not found."})
    require_permission(
        user, MANAGE_CHECKLIST, scope=version_authorization_scope(item.section.version)
    )
    _require_draft(item.section.version)
    _swap_positions(
        queryset_model=ChecklistItem,
        parent_filter={"section_id": item.section_id},
        current=item,
        direction=direction,
    )
    item.refresh_from_db()
    return item


def _validate_publish_structure(version: ChecklistVersion) -> None:
    """
    Technical structural checks only — not business completeness rules.

    Empty definitions cannot be published because a published version must be a
    coherent, non-empty definition graph. Minimum question counts / temperature
    rules remain EVIDENCE REQUIRED and are not enforced here.
    """
    sections = list(version.sections.prefetch_related("items").order_by("position"))
    if not sections:
        raise ValidationError({"version": "A checklist version must have at least one section."})
    if not any(section.items.exists() for section in sections):
        raise ValidationError(
            {"version": "A checklist version must have at least one item before publishing."}
        )
    for section in sections:
        if not section.title.strip():
            raise ValidationError({"version": "All sections must have a title."})
        for item in section.items.all():
            if not item.code.strip() or not item.label.strip():
                raise ValidationError({"version": "All items must have a code and label."})


@transaction.atomic
def publish_checklist_version(*, actor: User | None, version_id: uuid.UUID) -> ChecklistVersion:
    user = _require_authenticated_actor(actor)
    version = _lock_version(version_id)
    require_permission(user, MANAGE_CHECKLIST, scope=version_authorization_scope(version))
    assert_version_transition_allowed(
        current=version.status,
        target=ChecklistVersionStatus.PUBLISHED,
    )
    _validate_publish_structure(version)

    version.status = ChecklistVersionStatus.PUBLISHED
    version.published_at = timezone.now()
    version.save(update_fields=["status", "published_at", "updated_at"])
    record_event(
        event_type="CHECKLIST_VERSION_PUBLISHED",
        actor=user,
        metadata=_version_metadata(version),
    )
    return version


@transaction.atomic
def retire_checklist_version(*, actor: User | None, version_id: uuid.UUID) -> ChecklistVersion:
    user = _require_authenticated_actor(actor)
    version = _lock_version(version_id)
    require_permission(user, MANAGE_CHECKLIST, scope=version_authorization_scope(version))
    assert_version_transition_allowed(
        current=version.status,
        target=ChecklistVersionStatus.RETIRED,
    )
    version.status = ChecklistVersionStatus.RETIRED
    version.save(update_fields=["status", "updated_at"])
    record_event(
        event_type="CHECKLIST_VERSION_RETIRED",
        actor=user,
        metadata=_version_metadata(version),
    )
    return version
