# ADR-007: Scoped RBAC

**Status:** Accepted (Phase 03 foundation)
**Date:** 2026-08-06
**Deciders:** Project Owner (technical foundation)

## Context

Finished Goods recording requires organization, site, and department isolation. Permissions must fail closed and must not invent business role names until owners confirm them.

## Decision

1. **Permission authority:** `django.contrib.auth.models.Permission`.
2. **Role model:** `access_control.Role` — UUID, code, name, description, `is_active`, M2M to Permission. No seeded business roles.
3. **Assignments:** `ScopedRoleAssignment` links user + role with optional organization, site, and department scope, validity window, and `assigned_by`.
4. **Hierarchy:** Site requires organization and must belong to it; department requires organization and, if site-bound, must belong to that site.
5. **Global assignment:** Allowed only when organization/site/department are all unset and the assignment service explicitly permits it.
6. **Authorization API:** Central services (`user_has_permission`, scope accessors) — views stay thin; UI hiding is never sufficient.
7. **Fail closed:** Inactive users, roles, assignments, future `valid_from`, and expired `valid_until` grant nothing. Cross-organization access is denied.
8. **Superuser:** Explicit Django superuser privilege remains and is tested separately.

## Consequences

- Future FG modules check permissions via access-control services/decorators/mixins.
- Role catalogues are data, not hard-coded Phase 03 seeds.
- PostgreSQL constraints plus service validation enforce hierarchy.

## Related

- [ADR-006-IDENTITY-AND-EMPLOYEE-CODE-AUTHENTICATION.md](ADR-006-IDENTITY-AND-EMPLOYEE-CODE-AUTHENTICATION.md)
- [AUTHENTICATION_AND_ACCESS_CONTROL.md](../security/AUTHENTICATION_AND_ACCESS_CONTROL.md)
