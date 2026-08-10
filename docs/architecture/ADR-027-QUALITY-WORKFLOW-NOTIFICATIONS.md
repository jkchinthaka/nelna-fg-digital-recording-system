# ADR-027 — Quality workflow notifications

**Status:** Accepted (technical foundation)  
**Date:** 2026-08-10  
**Phase:** 15

## Context

Workflow actors need timely notices (assignment, overdue, review pending, QA HOLD/REJECT, CAPA due, integration failure) without emailing checklist answers or sensitive review notes. SMS provider/budget is not approved.

## Decision

1. Introduce `apps.notifications` with in-app `Notification` rows (recipient, event type, title, safe_message, created_at, read_at, delivery status).
2. Org `OrganizationNotificationPolicy`: all event types **default OFF**; optional email channel **default OFF**.
3. Email only when SMTP env is configured **and** policy enables email; credentials never in repo.
4. **No SMS** until provider/budget EVIDENCE REQUIRED / approved.
5. Privacy: `privacy.py` rejects sensitive title/message/metadata; email bodies HTML-escape safe fields only.
6. Async email via Celery with unique `idempotency_key` and retry — duplicate delivery attempts are no-ops when already DELIVERED.
7. Soft retention; recipient-only mark-read.

## Consequences

- Call sites must opt into enabled event types; no default spam.
- Which events IT enables remains APPROVAL REQUIRED.
- SMS remains out of scope for this phase.
