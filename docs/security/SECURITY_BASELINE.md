# Security Baseline

**Document status:** Draft baseline for implementation phases — not a completed security assessment  
**Phase:** 00 — Discovery and governance  
**Last updated:** 2026-08-04

## Principles

- Deny access by default
- Individual accountability
- Server-side authorization
- Auditable important operations
- No secrets in source control
- No production access or deployment without explicit approval

## Individual named accounts

Every interactive user has a unique named account. Shared accounts are prohibited.

## Password hashing

Passwords are stored only using Django’s password hashers (or an approved equivalent). Plaintext passwords must never be logged or stored.

## Session authentication

The browser/PWA uses session authentication unless a later approved ADR changes the model. Session lifetime follows an approved IT policy (**EVIDENCE REQUIRED** for exact timeouts).

## Deny-by-default authorization

Policies deny unless a positive grant matches. UI hiding is never sufficient authorization.

## Scoped roles

Roles are scoped to confirmed organization hierarchy nodes (site/area/department as approved). Global privileges are minimized and reviewable.

## Separation of duties

Conflicting actions (for example submit vs check vs verify, as defined by QA) are enforced in policies with automated tests.

## Secure cookies

Production cookies use Secure, HttpOnly, and appropriate SameSite settings. CSRF tokens protect cookie-authenticated mutating requests.

## CSRF

CSRF protection remains enabled for authenticated browser workflows.

## Rate limiting

Authentication and other abuse-sensitive endpoints must be rate limited when implemented.

## Secret management

Secrets come from environment variables or a secret manager. Never commit `.env` production secrets, keys, or connection strings.

## Audit events

Important operations append audit events (who, what, when, subject, outcome). Audit history is preserved.

## Evidence access

Evidence metadata access follows the same authorization model as related records. Retrieval should prefer short-lived signed URLs from object storage.

## Object-storage signed URLs

Prefer time-limited signed URLs over long-lived public objects for evidence.

## Dependency scanning

When application dependencies exist, enable dependency vulnerability scanning in CI.

## Security headers

Production deployments should set standard security headers (for example via Django settings and/or Nginx) appropriate to the threat model.

## Privileged-access review

Admin and elevated roles require periodic review (**cadence DECISION REQUIRED**).

## Incident response

Suspected incidents trigger session revocation, access review, evidence preservation, and owner notification per an IT-approved incident process (**EVIDENCE REQUIRED** for final playbook).

## Production-access restrictions

Production shell/database access is restricted, logged where feasible, and not used for routine support without approval.

## Explicit non-claims

This baseline does not assert that the system is currently secure, certified, or production-ready. Controls must be implemented and tested in later phases.
