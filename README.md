# Nelna FG Digital Recording System

Secure, auditable Finished Goods digital recording delivered as a responsive Progressive Web Application.

## Project purpose

Provide named-account, scoped-role digital recording, checking, verification, evidence capture, and audit export for Finished Goods operations — using approved business rules only, with Sinhala-capable operator experiences, without requiring ERP availability for factory-floor recording.

## Current phase

**Phase 00 — Discovery and governance**

This repository currently contains project-discovery documentation, architecture decision records, governance artefacts, and Cursor project rules. It does **not** contain an application codebase yet.

## Approved architecture (technical direction)

| Area | Direction |
| --- | --- |
| Backend | Python, Django 5.2 LTS |
| Architecture | Modular monolith |
| Database | PostgreSQL (+ JSONB where appropriate) |
| Cache / jobs | Redis, Celery |
| UI | Django Templates, HTMX, Tailwind CSS, minimal JS, Alpine.js only when needed |
| Client | One responsive installable PWA (no native app in initial phases) |
| Evidence | MinIO locally; S3-compatible object storage in production |
| Local dev | Docker Compose (introduced in later phases) |
| Production edge | Nginx (later) |
| Tests | Pytest, Playwright |
| CI | GitHub Actions (later) |
| Design | Figma Professional |
| AI | Optional local assistance later; never final FS/QA/loading/CAPA/access decisions |

## Repository status

| Item | Status |
| --- | --- |
| Greenfield repository | Yes |
| Application source code | Not started |
| Production readiness | **Not claimed** |
| Secrets in repo | None intended; do not add any |
| Previous repository code | Not used |

## Documentation map

| Document | Path |
| --- | --- |
| Project charter | [docs/business/PROJECT_CHARTER.md](docs/business/PROJECT_CHARTER.md) |
| Assumption register | [docs/business/ASSUMPTION_REGISTER.md](docs/business/ASSUMPTION_REGISTER.md) |
| Stakeholder questionnaire | [docs/business/STAKEHOLDER_QUESTIONNAIRE.md](docs/business/STAKEHOLDER_QUESTIONNAIRE.md) |
| MVP scope | [docs/requirements/MVP_SCOPE.md](docs/requirements/MVP_SCOPE.md) |
| Requirements catalogue | [docs/requirements/REQUIREMENTS_CATALOGUE.md](docs/requirements/REQUIREMENTS_CATALOGUE.md) |
| Traceability matrix | [docs/requirements/TRACEABILITY_MATRIX.md](docs/requirements/TRACEABILITY_MATRIX.md) |
| Non-functional requirements | [docs/requirements/NON_FUNCTIONAL_REQUIREMENTS.md](docs/requirements/NON_FUNCTIONAL_REQUIREMENTS.md) |
| Decision register | [docs/decisions/DECISION_REGISTER.md](docs/decisions/DECISION_REGISTER.md) |
| ADR modular monolith | [docs/architecture/ADR-001-MODULAR-MONOLITH.md](docs/architecture/ADR-001-MODULAR-MONOLITH.md) |
| ADR PostgreSQL | [docs/architecture/ADR-002-POSTGRESQL-PRIMARY-DATABASE.md](docs/architecture/ADR-002-POSTGRESQL-PRIMARY-DATABASE.md) |
| ADR responsive PWA | [docs/architecture/ADR-003-RESPONSIVE-PWA.md](docs/architecture/ADR-003-RESPONSIVE-PWA.md) |
| System context | [docs/architecture/SYSTEM_CONTEXT.md](docs/architecture/SYSTEM_CONTEXT.md) |
| Module map | [docs/architecture/MODULE_MAP.md](docs/architecture/MODULE_MAP.md) |
| Security baseline | [docs/security/SECURITY_BASELINE.md](docs/security/SECURITY_BASELINE.md) |
| AI safety policy | [docs/security/AI_SAFETY_POLICY.md](docs/security/AI_SAFETY_POLICY.md) |
| Environment strategy | [docs/operations/ENVIRONMENT_STRATEGY.md](docs/operations/ENVIRONMENT_STRATEGY.md) |
| Business continuity draft | [docs/operations/BUSINESS_CONTINUITY_DRAFT.md](docs/operations/BUSINESS_CONTINUITY_DRAFT.md) |
| Validation strategy | [docs/testing/VALIDATION_STRATEGY.md](docs/testing/VALIDATION_STRATEGY.md) |
| Risk register | [docs/risks/PROJECT_RISK_REGISTER.md](docs/risks/PROJECT_RISK_REGISTER.md) |
| Figma plan | [docs/design/FIGMA_PLAN.md](docs/design/FIGMA_PLAN.md) |
| Roadmap | [docs/ROADMAP.md](docs/ROADMAP.md) |
| Approvals | [docs/approvals/](docs/approvals/) |

## Contribution workflow

1. Work on a phase-specific branch (never commit directly to `main`).
2. Open a pull request for manual review.
3. Do not force-push to `main` or merge without human review.
4. Do not invent Nelna operational values; use assumption/evidence gates.
5. Do not deploy to production without explicit written approval.
6. Follow version-controlled Cursor rules under `.cursor/rules/`.

## Next action

1. Complete manual review of this Phase 00 foundation pull request.
2. Capture named owners and questionnaire answers into the assumption register and approvals.
3. After Phase 00 approval, begin **Phase 01 — Figma journeys and design system** using [docs/design/FIGMA_PLAN.md](docs/design/FIGMA_PLAN.md).

## Important

This project is **not production-ready**. Production readiness requires UAT, restore testing, security review, and owner approval.
