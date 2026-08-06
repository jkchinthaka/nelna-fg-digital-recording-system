# Security Event Catalogue

**Document status:** Phase 03 foundation + Phase 04A Shift events
**Last updated:** 2026-08-07

## Event types

| Event | When |
| --- | --- |
| `LOGIN_SUCCESS` | Successful employee-code authentication |
| `LOGIN_FAILURE` | Failed authentication (generic reasons in metadata) |
| `ACCOUNT_LOCKED` | Failure threshold reached |
| `ACCOUNT_UNLOCKED` | Explicit admin unlock |
| `LOGOUT` | Session logout |
| `PASSWORD_CHANGED` | User or forced password change |
| `PASSWORD_RESET_BY_ADMIN` | Admin sets a new password |
| `USER_ACTIVATED` / `USER_DEACTIVATED` | Active-flag changes |
| `ROLE_ASSIGNED` / `ROLE_REVOKED` | Scoped role assignment lifecycle |
| `SHIFT_CREATED` | Configurable Shift created via domain service |
| `SHIFT_UPDATED` | Configurable Shift fields updated via domain service |
| `SHIFT_ACTIVATED` | Shift reactivated (`is_active=True`) |
| `SHIFT_DEACTIVATED` | Shift deactivated (`is_active=False`) |

## Safe metadata

Allowed examples: `reason` codes (`invalid_credentials`, `account_locked`, `inactive`), role/assignment UUIDs, organization/site/department UUIDs, boolean flags.

Shift events may include: Shift UUID, normalized Shift code, Organization UUID, optional Site UUID, optional Department UUID, active status, overnight derived flag, changed field names.

Unknown login identifiers must be masked or hashed — never store raw unknown employee codes in clear text when the account is unknown.

## Prohibited fields

Passwords, session keys, cookies, Authorization headers, CSRF tokens, raw POST bodies, full database or Redis URLs, secrets.

## Privacy and retention

Retention period is **deferred** — not decided in Phase 03. Events are append-oriented and must not be silently editable through normal admin workflows.

## Related

- [AUTHENTICATION_AND_ACCESS_CONTROL.md](AUTHENTICATION_AND_ACCESS_CONTROL.md)
- [ADR-008-CONFIGURABLE-SHIFT-FOUNDATION.md](../architecture/ADR-008-CONFIGURABLE-SHIFT-FOUNDATION.md)
