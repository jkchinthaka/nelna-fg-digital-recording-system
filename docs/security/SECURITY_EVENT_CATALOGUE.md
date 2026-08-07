# Security Event Catalogue

**Document status:** Phase 03 foundation + Phase 04A Shift + Phase 05A FG Product + Phase 06A Checklist events
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
| `FG_PRODUCT_CREATED` | Configurable FG Product created via domain service |
| `FG_PRODUCT_UPDATED` | Configurable FG Product fields updated via domain service |
| `FG_PRODUCT_ACTIVATED` | FG Product reactivated (`is_active=True`) |
| `FG_PRODUCT_DEACTIVATED` | FG Product deactivated (`is_active=False`) |
| `CHECKLIST_TEMPLATE_CREATED` | Checklist template created |
| `CHECKLIST_TEMPLATE_UPDATED` | Checklist template updated |
| `CHECKLIST_TEMPLATE_ACTIVATED` | Checklist template activated |
| `CHECKLIST_TEMPLATE_DEACTIVATED` | Checklist template deactivated |
| `CHECKLIST_VERSION_CREATED` | Blank draft checklist version created |
| `CHECKLIST_VERSION_CLONED` | Draft checklist version cloned from a source version |
| `CHECKLIST_VERSION_PUBLISHED` | Checklist version published (immutable thereafter) |
| `CHECKLIST_VERSION_RETIRED` | Published checklist version retired |

## Safe metadata

Allowed examples: `reason` codes (`invalid_credentials`, `account_locked`, `inactive`), role/assignment UUIDs, organization/site/department UUIDs, boolean flags.

Shift events may include: Shift UUID, normalized Shift code, Organization UUID, optional Site UUID, optional Department UUID, active status, overnight derived flag, changed field names.

FG Product events may include: FG Product UUID, normalized Product code, Organization UUID, active status, changed field names.

Checklist events may include: template UUID/code, version UUID/number, organization UUID, optional product UUID, status, changed field names. Do not store full checklist question text in security audit metadata.

Unknown login identifiers must be masked or hashed — never store raw unknown employee codes in clear text when the account is unknown.

## Prohibited fields

Passwords, session keys, cookies, Authorization headers, CSRF tokens, raw POST bodies, full database or Redis URLs, secrets.

## Privacy and retention

Retention period is **deferred** — not decided in Phase 03. Events are append-oriented and must not be silently editable through normal admin workflows.

## Related

- [AUTHENTICATION_AND_ACCESS_CONTROL.md](AUTHENTICATION_AND_ACCESS_CONTROL.md)
- [ADR-008-CONFIGURABLE-SHIFT-FOUNDATION.md](../architecture/ADR-008-CONFIGURABLE-SHIFT-FOUNDATION.md)
- [ADR-009-FG-MASTER-DATA-DOMAIN.md](../architecture/ADR-009-FG-MASTER-DATA-DOMAIN.md)
