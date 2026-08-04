# Nelna FG Digital Recording System

Secure, auditable Finished Goods digital recording delivered as a responsive Progressive Web Application.

## Project purpose

Provide named-account, scoped-role digital recording, checking, verification, evidence capture, and audit export for Finished Goods operations — using approved business rules only, with Sinhala-capable operator experiences, without requiring ERP availability for factory-floor recording.

## Current phase

**Phase 01B — Design tokens and component system** (under review — PR #3)

| Phase | Status |
| --- | --- |
| Phase 00 — Discovery and governance | Merged to `main` |
| Phase 01A — Journeys, IA, lo-fi specification | **Approved** as proposed design baseline (2026-08-04) |
| Phase 01B — Design tokens and components | **Under review** on PR #3 — do not start 01C until approved |
| Phase 01C — High-fidelity MVP screens and prototype | Not started — blocked on 01B approval |

This repository contains governance documentation, architecture decision records, Cursor rules, and design specifications through Phase 01B (including machine-readable tokens). It does **not** contain an application codebase. No Django/HTML/CSS/JS implementation has started.

Open business decisions remain proposed or decision-required and are **not** final Nelna operational approvals. Phase 01B is **not approved** until its design approval form is signed.

**Figma:** Draft file created — see [docs/design/FIGMA_IMPLEMENTATION_LOG.md](docs/design/FIGMA_IMPLEMENTATION_LOG.md). Not an approved published library.

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
| Personas | [docs/design/PERSONAS.md](docs/design/PERSONAS.md) |
| User journeys | [docs/design/USER_JOURNEYS.md](docs/design/USER_JOURNEYS.md) |
| Information architecture | [docs/design/INFORMATION_ARCHITECTURE.md](docs/design/INFORMATION_ARCHITECTURE.md) |
| Screen inventory | [docs/design/SCREEN_INVENTORY.md](docs/design/SCREEN_INVENTORY.md) |
| Low-fidelity wireframes | [docs/design/LOW_FIDELITY_WIREFRAMES.md](docs/design/LOW_FIDELITY_WIREFRAMES.md) |
| Workflow state map | [docs/design/WORKFLOW_STATE_MAP.md](docs/design/WORKFLOW_STATE_MAP.md) |
| Content and language | [docs/design/CONTENT_AND_LANGUAGE_GUIDE.md](docs/design/CONTENT_AND_LANGUAGE_GUIDE.md) |
| Accessibility and usability | [docs/design/ACCESSIBILITY_AND_USABILITY.md](docs/design/ACCESSIBILITY_AND_USABILITY.md) |
| Responsive behaviour | [docs/design/RESPONSIVE_BEHAVIOUR.md](docs/design/RESPONSIVE_BEHAVIOUR.md) |
| Figma build specification (01A) | [docs/design/FIGMA_BUILD_SPECIFICATION.md](docs/design/FIGMA_BUILD_SPECIFICATION.md) |
| Design tokens | [docs/design/DESIGN_TOKENS.md](docs/design/DESIGN_TOKENS.md) |
| Design system foundations | [docs/design/DESIGN_SYSTEM_FOUNDATIONS.md](docs/design/DESIGN_SYSTEM_FOUNDATIONS.md) |
| Component system | [docs/design/COMPONENT_SYSTEM.md](docs/design/COMPONENT_SYSTEM.md) |
| Component catalogue | [docs/design/COMPONENT_CATALOGUE.md](docs/design/COMPONENT_CATALOGUE.md) |
| Component anatomy and states | [docs/design/COMPONENT_ANATOMY_AND_STATES.md](docs/design/COMPONENT_ANATOMY_AND_STATES.md) |
| Operator component patterns | [docs/design/OPERATOR_COMPONENT_PATTERNS.md](docs/design/OPERATOR_COMPONENT_PATTERNS.md) |
| Critical state patterns | [docs/design/CRITICAL_STATE_PATTERNS.md](docs/design/CRITICAL_STATE_PATTERNS.md) |
| Figma variables spec | [docs/design/FIGMA_VARIABLES_SPEC.md](docs/design/FIGMA_VARIABLES_SPEC.md) |
| Figma component build guide | [docs/design/FIGMA_COMPONENT_BUILD_GUIDE.md](docs/design/FIGMA_COMPONENT_BUILD_GUIDE.md) |
| Figma implementation log | [docs/design/FIGMA_IMPLEMENTATION_LOG.md](docs/design/FIGMA_IMPLEMENTATION_LOG.md) |
| Design-to-Django handoff | [docs/design/DESIGN_TO_DJANGO_HANDOFF.md](docs/design/DESIGN_TO_DJANGO_HANDOFF.md) |
| Design QA checklist | [docs/design/DESIGN_QA_CHECKLIST.md](docs/design/DESIGN_QA_CHECKLIST.md) |
| Contrast validation | [docs/design/CONTRAST_VALIDATION.md](docs/design/CONTRAST_VALIDATION.md) |
| Phase 01B decisions | [docs/design/PHASE_01B_DECISIONS.md](docs/design/PHASE_01B_DECISIONS.md) |
| Machine-readable tokens | [design/tokens/nelna-fg.tokens.json](design/tokens/nelna-fg.tokens.json) |
| Figma tokens/components spec (01B) | [docs/design/FIGMA_TOKENS_COMPONENTS_SPEC.md](docs/design/FIGMA_TOKENS_COMPONENTS_SPEC.md) |
| Figma review checklist (01A) | [docs/design/FIGMA_REVIEW_CHECKLIST.md](docs/design/FIGMA_REVIEW_CHECKLIST.md) |
| Figma review checklist (01B) | [docs/design/FIGMA_REVIEW_CHECKLIST_01B.md](docs/design/FIGMA_REVIEW_CHECKLIST_01B.md) |
| Design decision register | [docs/design/DESIGN_DECISION_REGISTER.md](docs/design/DESIGN_DECISION_REGISTER.md) |
| Phase 01A approval | [docs/approvals/PHASE_01A_DESIGN_APPROVAL.md](docs/approvals/PHASE_01A_DESIGN_APPROVAL.md) |
| Phase 01B approval form | [docs/approvals/PHASE_01B_DESIGN_APPROVAL.md](docs/approvals/PHASE_01B_DESIGN_APPROVAL.md) |
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

1. Manual design-system review of Phase 01B (PR #3) using [docs/design/DESIGN_QA_CHECKLIST.md](docs/design/DESIGN_QA_CHECKLIST.md) and [docs/approvals/PHASE_01B_DESIGN_APPROVAL.md](docs/approvals/PHASE_01B_DESIGN_APPROVAL.md).
2. Complete remaining Figma manual steps in [docs/design/FIGMA_IMPLEMENTATION_LOG.md](docs/design/FIGMA_IMPLEMENTATION_LOG.md).
3. Keep resolving open business decisions — they are not final operational approvals.
4. **Do not start Phase 01C** until Phase 01B is approved.

## Important

This project is **not production-ready**. Production readiness requires UAT, restore testing, security review, and owner approval.
