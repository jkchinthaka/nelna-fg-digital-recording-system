# Nelna FG Digital Recording System

Secure, auditable Finished Goods digital recording delivered as a responsive Progressive Web Application.

## Project purpose

Provide named-account, scoped-role digital recording, checking, verification, evidence capture, and audit export for Finished Goods operations — using approved business rules only, with Sinhala-capable operator experiences, without requiring ERP availability for factory-floor recording.

## Current phase

**Phase 01C — High-fidelity MVP screens and prototype** (01C-R remediation under review; **not approved**)

| Phase | Status |
| --- | --- |
| Phase 00 — Discovery and governance | Merged to `main` |
| Phase 01A — Journeys, IA, lo-fi specification | **Approved** as proposed design baseline (2026-08-04) |
| Phase 01B — Design tokens and components | **Approved with conditions** (2026-08-05) — merged via PR #3 |
| Phase 01C — High-fidelity MVP screens and prototype | **Current / 01C-R** — coverage expanded on `design/figma-high-fidelity-mvp` (PR #4); **Noto Sans Sinhala owner verification still blocking**; approval pending |

This repository contains governance documentation, architecture decision records, Cursor rules, and design specifications through Phase 01C (design only). It does **not** contain an application codebase. No Django/HTML/CSS/JS implementation has started.

Open business decisions remain proposed or decision-required and are **not** final Nelna operational approvals. Coverage matrix: [docs/design/FIGMA_01C_COVERAGE_MATRIX.md](docs/design/FIGMA_01C_COVERAGE_MATRIX.md). High-fidelity approval is **pending**. Figma library is **not** published. Do **not** start Phase 02 until Noto verification and owner high-fidelity approval.

**Figma ownership and editing access:** Verified — owner/handle `chinthaka` (`chinthakajayaweera1@gmail.com`); plan CHINTHAKA JAYAWEERA's team; Full seat; MCP and browser authentication verified. Draft file: https://www.figma.com/design/jnn8Xhsg1zFEHxYShCUb4M — not a published approved library.

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
| Phase 01C high-fidelity approval form | [docs/approvals/PHASE_01C_HIGH_FIDELITY_APPROVAL.md](docs/approvals/PHASE_01C_HIGH_FIDELITY_APPROVAL.md) |
| High-fidelity screen spec | [docs/design/HIGH_FIDELITY_SCREEN_SPEC.md](docs/design/HIGH_FIDELITY_SCREEN_SPEC.md) |
| Prototype flow map | [docs/design/PROTOTYPE_FLOW_MAP.md](docs/design/PROTOTYPE_FLOW_MAP.md) |
| Figma 01C implementation log | [docs/design/FIGMA_01C_IMPLEMENTATION_LOG.md](docs/design/FIGMA_01C_IMPLEMENTATION_LOG.md) |
| Design debt register | [docs/design/DESIGN_DEBT_REGISTER.md](docs/design/DESIGN_DEBT_REGISTER.md) |
| Django foundation design handoff | [docs/design/DJANGO_FOUNDATION_DESIGN_HANDOFF.md](docs/design/DJANGO_FOUNDATION_DESIGN_HANDOFF.md) |
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

1. In Figma Desktop, install/enable **Noto Sans Sinhala** and complete frame `04/tokens/MANUAL-Noto-Sans-Sinhala` (`31:23`); replace interim Abhaya Libre samples.
2. Manually review Phase 01C-R coverage + P1–P7 prototypes (PR #4 / Figma pages 04–13). Approval form stays blank until owner sign-off.
3. Do **not** publish the Figma component library before final design-system review.
4. Do **not** begin Phase 02 until high-fidelity design review gate passes (including Noto verification).
5. Keep resolving open business decisions — they are not final operational approvals.

## Important

This project is **not production-ready**. Production readiness requires UAT, restore testing, security review, and owner approval.
