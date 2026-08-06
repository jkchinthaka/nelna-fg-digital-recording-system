"""Account authentication and password lifecycle services."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import timedelta
from typing import Any

from django.conf import settings
from django.contrib.auth import login, logout
from django.core.exceptions import ValidationError
from django.db import transaction
from django.http import HttpRequest
from django.utils import timezone

from apps.accounts.backends import EmployeeCodeBackend
from apps.accounts.models import User
from apps.accounts.validators import normalize_employee_code


@dataclass(frozen=True, slots=True)
class AuthResult:
    success: bool
    user: User | None = None
    locked: bool = False
    error_code: str = ""


def _max_failed_attempts() -> int:
    return int(getattr(settings, "AUTH_MAX_FAILED_ATTEMPTS", 5))


def _lockout_minutes() -> int:
    return int(getattr(settings, "AUTH_LOCKOUT_MINUTES", 15))


def _client_meta(request: HttpRequest | None) -> dict[str, Any]:
    if request is None:
        return {"request_id": None, "ip_address": None, "user_agent": ""}
    return {
        "request_id": getattr(request, "correlation_id", None),
        "ip_address": request.META.get("REMOTE_ADDR"),
        "user_agent": (request.META.get("HTTP_USER_AGENT") or "")[:512],
    }


def authenticate_login(
    request: HttpRequest,
    *,
    employee_code: str,
    password: str,
) -> AuthResult:
    """
    Authenticate with employee_code + password.

    Returns a generic failure for unknown users, inactive users, and bad passwords.
    Locked accounts return locked=True without revealing other details.
    """
    from apps.security_audit.services import record_event

    meta = _client_meta(request)
    normalized = normalize_employee_code(employee_code)

    # Pre-check lockout for known users to avoid incrementing while locked.
    existing = User.objects.filter(employee_code__iexact=normalized).first() if normalized else None
    if existing is not None and existing.is_locked:
        record_event(
            event_type="LOGIN_FAILURE",
            subject_user=existing,
            request_id=meta["request_id"],
            ip_address=meta["ip_address"],
            user_agent_summary=meta["user_agent"],
            metadata={"reason": "account_locked"},
        )
        return AuthResult(success=False, locked=True, error_code="account_locked")

    backend = EmployeeCodeBackend()
    user = backend.authenticate(
        request,
        employee_code=normalized,
        password=password,
    )

    if user is None:
        # Distinguish lockout race vs generic failure via fresh lookup.
        candidate = (
            User.objects.filter(employee_code__iexact=normalized).first() if normalized else None
        )
        if candidate is not None and candidate.is_locked:
            record_event(
                event_type="LOGIN_FAILURE",
                subject_user=candidate,
                request_id=meta["request_id"],
                ip_address=meta["ip_address"],
                user_agent_summary=meta["user_agent"],
                metadata={"reason": "account_locked"},
            )
            return AuthResult(success=False, locked=True, error_code="account_locked")

        if candidate is not None:
            if not candidate.is_active:
                record_event(
                    event_type="LOGIN_FAILURE",
                    subject_user=candidate,
                    request_id=meta["request_id"],
                    ip_address=meta["ip_address"],
                    user_agent_summary=meta["user_agent"],
                    metadata={"reason": "inactive"},
                )
                return AuthResult(success=False, error_code="invalid_credentials")

            locked_user = record_failed_login(candidate, request=request)
            record_event(
                event_type="LOGIN_FAILURE",
                subject_user=candidate,
                request_id=meta["request_id"],
                ip_address=meta["ip_address"],
                user_agent_summary=meta["user_agent"],
                metadata={"reason": "invalid_credentials"},
            )
            if locked_user.is_locked:
                return AuthResult(success=False, locked=True, error_code="account_locked")
            return AuthResult(success=False, error_code="invalid_credentials")
        record_event(
            event_type="LOGIN_FAILURE",
            subject_user=None,
            request_id=meta["request_id"],
            ip_address=meta["ip_address"],
            user_agent_summary=meta["user_agent"],
            metadata={"reason": "invalid_credentials"},
            unknown_identifier=normalized or employee_code,
        )
        return AuthResult(success=False, error_code="invalid_credentials")

    assert isinstance(user, User)
    record_successful_login(user, request=request)
    record_event(
        event_type="LOGIN_SUCCESS",
        actor=user,
        subject_user=user,
        request_id=meta["request_id"],
        ip_address=meta["ip_address"],
        user_agent_summary=meta["user_agent"],
        metadata={},
    )
    return AuthResult(success=True, user=user)


@transaction.atomic
def record_failed_login(user: User, *, request: HttpRequest | None = None) -> User:
    """Increment failure counters under row lock; lock account at threshold."""
    from apps.security_audit.services import record_event

    locked_user = User.objects.select_for_update().get(pk=user.pk)
    if locked_user.is_locked:
        return locked_user

    now = timezone.now()
    locked_user.failed_login_count += 1
    locked_user.last_failed_login_at = now
    update_fields = ["failed_login_count", "last_failed_login_at"]

    if locked_user.failed_login_count >= _max_failed_attempts():
        locked_user.locked_until = now + timedelta(minutes=_lockout_minutes())
        update_fields.append("locked_until")
        locked_user.save(update_fields=update_fields)
        meta = _client_meta(request)
        record_event(
            event_type="ACCOUNT_LOCKED",
            subject_user=locked_user,
            request_id=meta["request_id"],
            ip_address=meta["ip_address"],
            user_agent_summary=meta["user_agent"],
            metadata={"failed_login_count": locked_user.failed_login_count},
        )
    else:
        locked_user.save(update_fields=update_fields)

    return locked_user


@transaction.atomic
def record_successful_login(user: User, *, request: HttpRequest) -> User:
    """Reset failure counters, stamp success time, establish session with key cycle."""
    locked_user = User.objects.select_for_update().get(pk=user.pk)
    now = timezone.now()
    locked_user.failed_login_count = 0
    locked_user.locked_until = None
    locked_user.last_successful_login_at = now
    locked_user.save(
        update_fields=[
            "failed_login_count",
            "locked_until",
            "last_successful_login_at",
        ]
    )
    login(request, locked_user, backend="apps.accounts.backends.EmployeeCodeBackend")
    request.session.cycle_key()
    return locked_user


def logout_user(request: HttpRequest) -> None:
    from apps.security_audit.services import record_event

    user = request.user if request.user.is_authenticated else None
    meta = _client_meta(request)
    logout(request)
    if user is not None and isinstance(user, User):
        record_event(
            event_type="LOGOUT",
            actor=user,
            subject_user=user,
            request_id=meta["request_id"],
            ip_address=meta["ip_address"],
            user_agent_summary=meta["user_agent"],
            metadata={},
        )


@transaction.atomic
def change_password(
    user: User,
    *,
    current_password: str,
    new_password: str,
    request: HttpRequest | None = None,
) -> User:
    from apps.security_audit.services import record_event

    if not user.check_password(current_password):
        raise ValidationError({"current_password": "Current password is incorrect."})

    user.set_password(new_password)
    user.must_change_password = False
    user.password_changed_at = timezone.now()
    user.save(update_fields=["password", "must_change_password", "password_changed_at"])

    meta = _client_meta(request)
    record_event(
        event_type="PASSWORD_CHANGED",
        actor=user,
        subject_user=user,
        request_id=meta["request_id"],
        ip_address=meta["ip_address"],
        user_agent_summary=meta["user_agent"],
        metadata={},
    )
    if request is not None and request.user.is_authenticated:
        login(request, user, backend="apps.accounts.backends.EmployeeCodeBackend")
        request.session.cycle_key()
    return user


@transaction.atomic
def force_password_change(
    user: User,
    *,
    new_password: str,
    request: HttpRequest | None = None,
) -> User:
    """Set a new password when must_change_password is required (no current password)."""
    from apps.security_audit.services import record_event

    user.set_password(new_password)
    user.must_change_password = False
    user.password_changed_at = timezone.now()
    user.save(update_fields=["password", "must_change_password", "password_changed_at"])

    meta = _client_meta(request)
    record_event(
        event_type="PASSWORD_CHANGED",
        actor=user,
        subject_user=user,
        request_id=meta["request_id"],
        ip_address=meta["ip_address"],
        user_agent_summary=meta["user_agent"],
        metadata={"forced": True},
    )
    if request is not None and request.user.is_authenticated:
        login(request, user, backend="apps.accounts.backends.EmployeeCodeBackend")
        request.session.cycle_key()
    return user


@transaction.atomic
def unlock_account(
    user: User,
    *,
    actor: User | None = None,
    request: HttpRequest | None = None,
) -> User:
    from apps.security_audit.services import record_event

    locked_user = User.objects.select_for_update().get(pk=user.pk)
    locked_user.failed_login_count = 0
    locked_user.locked_until = None
    locked_user.save(update_fields=["failed_login_count", "locked_until"])

    meta = _client_meta(request)
    record_event(
        event_type="ACCOUNT_UNLOCKED",
        actor=actor,
        subject_user=locked_user,
        request_id=meta["request_id"],
        ip_address=meta["ip_address"],
        user_agent_summary=meta["user_agent"],
        metadata={},
    )
    return locked_user


@transaction.atomic
def set_must_change_password(user: User, *, enabled: bool = True) -> User:
    user.must_change_password = enabled
    user.save(update_fields=["must_change_password"])
    return user


@transaction.atomic
def admin_reset_password(
    user: User,
    *,
    new_password: str,
    actor: User | None = None,
    request: HttpRequest | None = None,
) -> User:
    from apps.security_audit.services import record_event

    user.set_password(new_password)
    require_change = bool(getattr(settings, "AUTH_PASSWORD_CHANGE_REQUIRED_ON_ADMIN_RESET", True))
    user.must_change_password = require_change
    user.password_changed_at = timezone.now()
    user.failed_login_count = 0
    user.locked_until = None
    user.save(
        update_fields=[
            "password",
            "must_change_password",
            "password_changed_at",
            "failed_login_count",
            "locked_until",
        ]
    )
    meta = _client_meta(request)
    record_event(
        event_type="PASSWORD_RESET_BY_ADMIN",
        actor=actor,
        subject_user=user,
        request_id=meta["request_id"],
        ip_address=meta["ip_address"],
        user_agent_summary=meta["user_agent"],
        metadata={},
    )
    return user
