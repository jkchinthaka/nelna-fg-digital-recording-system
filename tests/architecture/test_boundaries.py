"""Architecture boundary tests."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
APPS = ROOT / "apps"
ALLOWED_APPS = {
    "core",
    "accounts",
    "organizations",
    "master_data",
    "checklists",
    "scheduling",
    "recording",
    "reviews",
    "access_control",
    "security_audit",
}
FORBIDDEN_APPS = {
    "tasks",
    "records",
    "evidence",
    "quality",
    "integrations",
    "reporting",
    "notifications",
    "schedules",
}


def test_apps_namespace_exists() -> None:
    assert (APPS / "__init__.py").exists()
    for name in ALLOWED_APPS:
        assert (APPS / name).is_dir(), f"Expected app directory missing: {name}"


def test_no_future_business_apps() -> None:
    present = {p.name for p in APPS.iterdir() if p.is_dir() and not p.name.startswith("_")}
    assert present == ALLOWED_APPS
    assert FORBIDDEN_APPS.isdisjoint(present)


def test_no_sqlite_engine_configured_in_settings_modules() -> None:
    settings_dir = ROOT / "config" / "settings"
    for path in settings_dir.glob("*.py"):
        text = path.read_text(encoding="utf-8")
        assert "django.db.backends.sqlite3" not in text
        assert "backends.sqlite" not in text


def test_config_has_no_business_models() -> None:
    config_dir = ROOT / "config"
    for path in config_dir.rglob("*.py"):
        text = path.read_text(encoding="utf-8")
        assert "class Meta:" not in text or "settings" in str(path)


def test_core_does_not_import_accounts_business_logic() -> None:
    core_dir = APPS / "core"
    for path in core_dir.rglob("*.py"):
        if "migrations" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        assert "from apps.accounts" not in text
        assert "import apps.accounts" not in text


def test_redis_not_modeled_as_orm_repository() -> None:
    models = (APPS / "core" / "models.py").read_text(encoding="utf-8").lower()
    assert "redis" not in models
