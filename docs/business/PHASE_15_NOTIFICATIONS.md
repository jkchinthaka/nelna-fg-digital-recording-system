# Phase 15 — Quality workflow notifications

**Status:** Technical foundation complete (not production-approved routing)  
**Date:** 2026-08-10  
**ADR:** [ADR-027-QUALITY-WORKFLOW-NOTIFICATIONS.md](../architecture/ADR-027-QUALITY-WORKFLOW-NOTIFICATIONS.md)

## Delivered

- In-app notifications (recipient, event/type, title, safe message, created_at, read_at, delivery status)
- Org policy: event types configurable, **all default OFF**
- Optional email via existing SMTP env settings when policy enables it
- SMS explicitly **not** integrated (provider/budget EVIDENCE REQUIRED)
- Idempotent create (`dedupe_key`) + Celery email delivery retries
- Privacy validation + template escaping; no checklist answers/sensitive notes by default
- Inbox UI at `/notifications/`; soft-retention admin

## Candidate events (not enabled by default)

task assignment, due/overdue, submission, Supervisor pending, returned correction, QA pending, QA HOLD/REJECT, CAPA due, integration failure

## Non-claims

- Not a company-approved notification routing matrix
- Not SMS capability
- Not automatic wiring of every workflow event until owners enable types

## STATUS: PHASE 15 NOTIFICATIONS COMPLETE
