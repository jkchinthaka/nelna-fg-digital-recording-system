# Authentication and Access Control

**Document status:** Phase 03 foundation guidance
**Last updated:** 2026-08-06

## Login lifecycle

1. Operator submits employee code + password (CSRF-protected).
2. Code is normalized; backend authenticates via Django password verification.
3. Inactive or locked accounts fail closed with generic messaging (locked accounts redirect to lockout page).
4. Success: failed counters reset, session rotated, audit `LOGIN_SUCCESS`, redirect to landing or forced password change.

## Lockout

| Setting | Default | Meaning |
| --- | --- | --- |
| `AUTH_MAX_FAILED_ATTEMPTS` | 5 | Failures before temporary lock |
| `AUTH_LOCKOUT_MINUTES` | 15 | Lock duration |
| `AUTH_LOGIN_RATE_LIMIT_WINDOW` | 300 | Reserved for short-lived throttling (optional) |

Lockout state lives on PostgreSQL (`failed_login_count`, `locked_until`). Updates use transactions and `select_for_update`. Redis is not authoritative for lockout.

## Password change

- Authenticated change requires current password and Django validators.
- Clears `must_change_password`, sets `password_changed_at`, audits `PASSWORD_CHANGED`.
- Forced-change middleware restricts users flagged `must_change_password` to password-change and logout routes only.

## Admin account management

- Create users with employee code; set initial password safely; mark forced change.
- Unlock via explicit admin action; view lockout and login timestamps.
- Assign scoped roles through controlled admin forms.
- Never display or log raw passwords.

## Session security

- HttpOnly session cookie; Secure + HTTPS redirect in production.
- Session rotation on login; logout is POST + CSRF and flushes the session.

## Permission checks

Server-side enforcement via `access_control` services, decorators, and mixins. Fail closed. Cross-scope denial is mandatory.

## Security audit

See [SECURITY_EVENT_CATALOGUE.md](SECURITY_EVENT_CATALOGUE.md). Prohibited: passwords, session IDs, cookies, Authorization headers, CSRF tokens, raw bodies, full DB/Redis URLs.

## Related

- ADR-006, ADR-007
- [PHASE_03_TEST_PLAN.md](../testing/PHASE_03_TEST_PLAN.md)
