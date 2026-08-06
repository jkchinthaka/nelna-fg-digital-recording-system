# Security Event Catalogue

**Document status:** Phase 03 foundation catalogue
**Last updated:** 2026-08-06

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

## Safe metadata

Allowed examples: `reason` codes (`invalid_credentials`, `account_locked`, `inactive`), role/assignment UUIDs, organization/site/department UUIDs, boolean flags.

Unknown login identifiers must be masked or hashed — never store raw unknown employee codes in clear text when the account is unknown.

## Prohibited fields

Passwords, session keys, cookies, Authorization headers, CSRF tokens, raw POST bodies, full database or Redis URLs, secrets.

## Privacy and retention

Retention period is **deferred** — not decided in Phase 03. Events are append-oriented and must not be silently editable through normal admin workflows.

## Related

- [AUTHENTICATION_AND_ACCESS_CONTROL.md](AUTHENTICATION_AND_ACCESS_CONTROL.md)
