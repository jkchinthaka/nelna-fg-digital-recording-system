# Phase 03 Test Plan

**Document status:** Phase 03 foundation
**Last updated:** 2026-08-06
**Coverage gate:** ≥80% (`apps` + `config`)

## Identity

- UUID PK preserved; employee-code normalization and case-insensitive uniqueness
- No raw password storage; inactive behavior; no seeded accounts

## Authentication

- Valid/invalid employee-code and password; generic errors
- Session rotation; logout POST-only; unsafe `next` rejected
- Successful/failed login timestamps; counter reset after success

## Lockout

- Threshold, temporary lock, expired lock allows auth, admin unlock
- Concurrent failure safety; audit events; no credential leakage

## Password

- Validators; current password required; forced-change redirect
- Clears `must_change_password`; session remains authenticated; audit event

## Organizations

- Constraints; site/department hierarchy; inactive hierarchy; PROTECT deletion
- No seeded organization data

## RBAC

- Global / organization / site / department scopes
- Cross-organization denial; inactive/future/expired denial
- Duplicate prevention; decorator and mixin enforcement; superuser behavior

## Audit

- Required event types; sensitive fields excluded; unknown identifiers masked/hashed
- Append-oriented admin behavior

## Architecture

- Thin views; logic in services/backends; no FG workflow apps; no SQLite; no circular deps

## Runtime requirements

PostgreSQL mandatory for integration, Docker tests, and CI. Redis for cache/Celery where relevant.

## Related

- [TESTING_GUIDE.md](TESTING_GUIDE.md)
- [CI_QUALITY_GATES.md](CI_QUALITY_GATES.md)
