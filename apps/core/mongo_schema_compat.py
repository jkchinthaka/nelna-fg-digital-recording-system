"""Mongo schema compatibility for Lower()-based unique indexes/constraints.

django-mongodb-backend does not support expression indexes
(``supports_expression_indexes = False``). Nelna stores business codes via
``normalize_code`` / ``normalize_employee_code`` (uppercase), so a unique index
on the stored field is the Mongo-equivalent of ``UniqueConstraint(Lower(...))``.

Activated only when the active database engine is MongoDB.
"""

from __future__ import annotations

import logging
from typing import Any

from django.db.models import Index, UniqueConstraint
from django.db.models.expressions import F
from django.db.models.functions import Lower, Upper

logger = logging.getLogger(__name__)

_APPLIED = False


def _expression_field_name(expr: Any) -> str | None:
    """Extract a simple field name from Lower/Upper/F/str expressions."""
    if isinstance(expr, str):
        return expr
    if isinstance(expr, F):
        return str(expr.name)
    if isinstance(expr, (Lower, Upper)):
        sources = getattr(expr, "source_expressions", None) or ()
        if len(sources) == 1:
            return _expression_field_name(sources[0])
        return None
    name = getattr(expr, "name", None)
    if isinstance(name, str) and name:
        return name
    return None


def _condition_contains_isnull(condition: Any) -> bool:
    if condition is None:
        return False
    try:
        children = list(condition.children)
    except Exception:  # noqa: BLE001
        return True  # fail closed: drop unknown condition shapes
    for child in children:
        if isinstance(child, tuple) and len(child) == 2:
            key, _value = child
            if isinstance(key, str) and "__isnull" in key:
                return True
        else:
            # Nested Q nodes
            if _condition_contains_isnull(child):
                return True
    return False


def rewrite_unique_constraint(constraint: UniqueConstraint) -> UniqueConstraint:
    """Rewrite Lower/Upper expression unique constraints to field-based uniques."""
    if not isinstance(constraint, UniqueConstraint):
        return constraint
    expressions = list(getattr(constraint, "expressions", ()) or ())
    fields = list(constraint.fields or [])
    if expressions:
        for expr in expressions:
            field_name = _expression_field_name(expr)
            if field_name is None:
                logger.warning(
                    "Mongo schema compat: cannot rewrite unique constraint %s expression %r",
                    constraint.name,
                    expr,
                )
                return constraint
            if field_name not in fields:
                fields.append(field_name)
    condition = constraint.condition
    # Partial unique predicates (isnull / ~ / complex Q) are not fully supported by
    # django-mongodb-backend index builders. Drop them; field uniqueness still applies
    # and service-layer guards remain authoritative for partial business rules.
    if condition is not None:
        logger.warning(
            "Mongo schema compat: dropping partial predicate on unique %s "
            "(service-layer uniqueness remains authoritative for partial cases)",
            constraint.name,
        )
        condition = None
    if not expressions and condition is constraint.condition:
        return constraint
    logger.info(
        "Mongo schema compat: rewriting unique constraint %s → fields=%s",
        constraint.name,
        fields,
    )
    return UniqueConstraint(
        fields=fields,
        name=constraint.name,
        condition=condition,
        deferrable=constraint.deferrable,
        include=constraint.include,
        nulls_distinct=getattr(constraint, "nulls_distinct", None),
    )


def rewrite_index(index: Index) -> Index:
    """Rewrite Lower/Upper expression indexes to plain field indexes."""
    if not isinstance(index, Index):
        return index
    expressions = list(getattr(index, "expressions", ()) or ())
    fields: list[str] = list(index.fields or [])
    if index.contains_expressions:
        for expr in expressions:
            field_name = _expression_field_name(expr)
            if field_name is None:
                logger.warning(
                    "Mongo schema compat: cannot rewrite index %s expression %r",
                    index.name,
                    expr,
                )
                return index
            if field_name not in fields:
                fields.append(field_name)
    condition = index.condition
    if condition is not None:
        logger.warning(
            "Mongo schema compat: dropping partial predicate on index %s",
            index.name,
        )
        condition = None
    if not index.contains_expressions and condition is index.condition:
        return index
    logger.info("Mongo schema compat: rewriting index %s → fields=%s", index.name, fields)
    return Index(fields=fields, name=index.name, condition=condition)


def apply_mongo_schema_compat() -> None:
    """Patch Mongo schema editor to rewrite Lower()/Upper() constraints and indexes."""
    global _APPLIED
    if _APPLIED:
        return
    from apps.core.persistence.backend import is_mongodb

    if not is_mongodb():
        return

    from django.db import NotSupportedError
    from django.db.models import CheckConstraint
    from django_mongodb_backend.schema import DatabaseSchemaEditor

    if getattr(DatabaseSchemaEditor.add_constraint, "_fg_mongo_lower_compat", False):
        _APPLIED = True
        return

    # Prefix all schema-editor collection names with fg_ (migration + DDL path).
    from apps.core.db_namespace import fg_prefix, namespace_enabled

    def _ensure_model_table_prefixed(model: Any) -> None:
        if not namespace_enabled():
            return
        prefix = fg_prefix()
        table = getattr(getattr(model, "_meta", None), "db_table", None)
        if isinstance(table, str) and table and not table.startswith(prefix):
            model._meta.db_table = f"{prefix}{table}"

    _orig_get_collection = DatabaseSchemaEditor.get_collection
    _orig_create_model = DatabaseSchemaEditor.create_model
    _orig_delete_model = DatabaseSchemaEditor.delete_model
    _orig_alter_db_table = DatabaseSchemaEditor.alter_db_table

    def get_collection(self: Any, name: str) -> Any:
        prefix = fg_prefix()
        if (
            namespace_enabled()
            and isinstance(name, str)
            and name
            and not name.startswith(prefix)
            and not name.startswith("system.")
        ):
            name = f"{prefix}{name}"
        return _orig_get_collection(self, name)

    def create_model(self: Any, model: Any, *args: Any, **kwargs: Any) -> None:
        _ensure_model_table_prefixed(model)
        return _orig_create_model(self, model, *args, **kwargs)

    def delete_model(self: Any, model: Any, *args: Any, **kwargs: Any) -> None:
        _ensure_model_table_prefixed(model)
        return _orig_delete_model(self, model, *args, **kwargs)

    def alter_db_table(
        self: Any, model: Any, old_db_table: str, new_db_table: str, *args: Any, **kwargs: Any
    ) -> None:
        prefix = fg_prefix()
        if namespace_enabled():
            if old_db_table and not old_db_table.startswith(prefix):
                old_db_table = f"{prefix}{old_db_table}"
            if new_db_table and not new_db_table.startswith(prefix):
                new_db_table = f"{prefix}{new_db_table}"
            if getattr(model._meta, "db_table", None) == new_db_table.removeprefix(prefix):
                model._meta.db_table = new_db_table
        return _orig_alter_db_table(self, model, old_db_table, new_db_table, *args, **kwargs)

    DatabaseSchemaEditor.get_collection = get_collection  # type: ignore[method-assign]
    DatabaseSchemaEditor.create_model = create_model  # type: ignore[method-assign]
    DatabaseSchemaEditor.delete_model = delete_model  # type: ignore[method-assign]
    DatabaseSchemaEditor.alter_db_table = alter_db_table  # type: ignore[method-assign]

    # ORM / QuerySet path uses DatabaseWrapper.get_collection(model._meta.db_table).
    # Historical migration models may still carry unprefixed db_table names during
    # post_migrate (create_permissions / ContentType sync). Class-level wrap keeps
    # all runtime + migrate writers on fg_* collections.
    from django_mongodb_backend.base import DatabaseWrapper

    if not getattr(DatabaseWrapper.get_collection, "_fg_collection_namespace", False):
        _orig_wrapper_get_collection = DatabaseWrapper.get_collection

        def wrapper_get_collection(self: Any, name: str, *args: Any, **kwargs: Any) -> Any:
            prefix = fg_prefix()
            if (
                namespace_enabled()
                and isinstance(name, str)
                and name
                and not name.startswith(prefix)
                and not name.startswith("system.")
            ):
                name = f"{prefix}{name}"
            return _orig_wrapper_get_collection(self, name, *args, **kwargs)

        wrapper_get_collection._fg_collection_namespace = True  # type: ignore[attr-defined]
        DatabaseWrapper.get_collection = wrapper_get_collection  # type: ignore[method-assign]

    _orig_add_constraint = DatabaseSchemaEditor.add_constraint
    _orig_remove_constraint = DatabaseSchemaEditor.remove_constraint
    _orig_add_index = DatabaseSchemaEditor.add_index
    _orig_remove_index = DatabaseSchemaEditor.remove_index

    def add_constraint(self: Any, model: Any, constraint: Any, *args: Any, **kwargs: Any) -> None:
        if isinstance(constraint, CheckConstraint):
            logger.warning(
                "Mongo schema compat: skipping CheckConstraint %s on %s "
                "(enforce via model/service validation)",
                getattr(constraint, "name", constraint),
                model._meta.label,
            )
            return
        if isinstance(constraint, UniqueConstraint):
            constraint = rewrite_unique_constraint(constraint)
        try:
            return _orig_add_constraint(self, model, constraint, *args, **kwargs)
        except NotSupportedError as exc:
            logger.warning(
                "Mongo schema compat: skipping unsupported constraint %s on %s (%s)",
                getattr(constraint, "name", constraint),
                model._meta.label,
                exc,
            )
            return None

    def remove_constraint(self: Any, model: Any, constraint: Any, *args: Any, **kwargs: Any) -> None:
        if isinstance(constraint, CheckConstraint):
            return None
        if isinstance(constraint, UniqueConstraint):
            constraint = rewrite_unique_constraint(constraint)
        try:
            return _orig_remove_constraint(self, model, constraint, *args, **kwargs)
        except Exception as exc:  # noqa: BLE001
            logger.warning(
                "Mongo schema compat: remove_constraint skipped for %s (%s)",
                getattr(constraint, "name", constraint),
                exc,
            )
            return None

    def add_index(self: Any, model: Any, index: Any, *args: Any, **kwargs: Any) -> None:
        if isinstance(index, Index):
            index = rewrite_index(index)
        try:
            return _orig_add_index(self, model, index, *args, **kwargs)
        except NotSupportedError as exc:
            logger.warning(
                "Mongo schema compat: skipping unsupported index %s on %s (%s)",
                getattr(index, "name", index),
                model._meta.label,
                exc,
            )
            return None

    def remove_index(self: Any, model: Any, index: Any, *args: Any, **kwargs: Any) -> None:
        if isinstance(index, Index):
            index = rewrite_index(index)
        try:
            return _orig_remove_index(self, model, index, *args, **kwargs)
        except Exception as exc:  # noqa: BLE001
            logger.warning(
                "Mongo schema compat: remove_index skipped for %s (%s)",
                getattr(index, "name", index),
                exc,
            )
            return None

    add_constraint._fg_mongo_lower_compat = True  # type: ignore[attr-defined]
    DatabaseSchemaEditor.add_constraint = add_constraint  # type: ignore[method-assign]
    DatabaseSchemaEditor.remove_constraint = remove_constraint  # type: ignore[method-assign]
    DatabaseSchemaEditor.add_index = add_index  # type: ignore[method-assign]
    DatabaseSchemaEditor.remove_index = remove_index  # type: ignore[method-assign]
    _APPLIED = True
    logger.info("Mongo schema Lower()/Upper() constraint rewrite enabled")
