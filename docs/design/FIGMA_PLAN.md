# Figma Plan

**Document status:** Active design plan — Phase 01B token/component specs in review; Figma binary not claimed created in-repo  
**Phase:** 01A approved baseline · **01B current** · 01C high-fidelity after 01B approval  
**Tool:** Figma Professional  
**Last updated:** 2026-08-04

## Purpose

Define the Figma file structure, journeys, IA, lo-fi wireframes, tokens, components, screens, breakpoints, accessibility, language strategy, and handoff method.

## Phase status

| Phase | Status |
| --- | --- |
| Phase 00 Discovery and governance | **Merged** to main |
| Phase 01A Journeys, IA, lo-fi specification | **Approved** as proposed baseline (2026-08-04); open operational decisions remain non-final |
| Phase 01B Design tokens and components | **Under review** (PR #3); draft Figma file exists — see FIGMA_IMPLEMENTATION_LOG |
| Phase 01C High-fidelity MVP screens and prototype | Not started |
| Application development | **Not started** |

Phase 01B is **not approved** until [PHASE_01B_DESIGN_APPROVAL.md](../approvals/PHASE_01B_DESIGN_APPROVAL.md) is signed.

## Specification documents (01A)

| Doc | Path |
| --- | --- |
| Personas | [PERSONAS.md](PERSONAS.md) |
| User journeys | [USER_JOURNEYS.md](USER_JOURNEYS.md) |
| Information architecture | [INFORMATION_ARCHITECTURE.md](INFORMATION_ARCHITECTURE.md) |
| Screen inventory | [SCREEN_INVENTORY.md](SCREEN_INVENTORY.md) |
| Low-fidelity wireframes | [LOW_FIDELITY_WIREFRAMES.md](LOW_FIDELITY_WIREFRAMES.md) |
| Workflow states | [WORKFLOW_STATE_MAP.md](WORKFLOW_STATE_MAP.md) |
| Content and language | [CONTENT_AND_LANGUAGE_GUIDE.md](CONTENT_AND_LANGUAGE_GUIDE.md) |
| Accessibility | [ACCESSIBILITY_AND_USABILITY.md](ACCESSIBILITY_AND_USABILITY.md) |
| Responsive behaviour | [RESPONSIVE_BEHAVIOUR.md](RESPONSIVE_BEHAVIOUR.md) |
| Figma build specification (01A) | [FIGMA_BUILD_SPECIFICATION.md](FIGMA_BUILD_SPECIFICATION.md) |
| Review checklist (01A) | [FIGMA_REVIEW_CHECKLIST.md](FIGMA_REVIEW_CHECKLIST.md) |
| Design decisions | [DESIGN_DECISION_REGISTER.md](DESIGN_DECISION_REGISTER.md) |

## Specification documents (01B)

| Doc | Path |
| --- | --- |
| Design tokens | [DESIGN_TOKENS.md](DESIGN_TOKENS.md) |
| Component system | [COMPONENT_SYSTEM.md](COMPONENT_SYSTEM.md) |
| Figma tokens/components build spec | [FIGMA_TOKENS_COMPONENTS_SPEC.md](FIGMA_TOKENS_COMPONENTS_SPEC.md) |
| Review checklist (01B) | [FIGMA_REVIEW_CHECKLIST_01B.md](FIGMA_REVIEW_CHECKLIST_01B.md) |

## Figma pages

| Page | Intent | 01A | 01B | 01C |
| --- | --- | --- | --- | --- |
| 00 Project Brief | Goals, roles, constraints, MVP summary | Spec + frames to build | | |
| 01 User Journeys | J1–J8 boards | Spec + frames to build | | |
| 02 Information Architecture | Nav + sitemap | Spec + frames to build | | |
| 03 Low-Fidelity Wireframes | MVP lo-fi | Spec + frames to build | | |
| 04 Design Tokens | Colour, type, space, semantic status | Stub | **Build** | |
| 05 Components | Buttons, inputs, cards, status, uploader | Stub | **Build** | |
| 06 Operator Mobile | Hi-fi operator | Stub | | **Build** |
| 07 Supervisor Mobile and Tablet | Hi-fi supervisor | Stub | | **Build** |
| 08 QA Console | Hi-fi QA | Stub | | **Build** |
| 09 Administration | Hi-fi admin | Stub | | **Build** |
| 10 Management Dashboard | Hi-fi management | Stub | | **Build** |
| 11 Offline and Error States | Sync/error lo-fi | Spec + frames | Refine | |
| 12 Interactive Prototypes | Clickable MVP | Stub | | **Build** |
| 13 Developer Handoff | Specs for Django/HTMX | Light links | | Expand |
| 99 Archive | Retired frames | Ready | | |

Detailed build rules: [FIGMA_BUILD_SPECIFICATION.md](FIGMA_BUILD_SPECIFICATION.md).

## Required screens (MVP-focused)

See [SCREEN_INVENTORY.md](SCREEN_INVENTORY.md). Exact field lists await approved forms (**EVIDENCE REQUIRED**).

## Required components

Deferred to Phase 01B (tokens + components). Lo-fi annotations only in 01A.

## Required states

Empty, loading, success, validation error, forbidden, offline/degraded, sync pending/conflict (design), retrospective indicator — see wireframes and Journey 6.

## Responsive breakpoints

See [RESPONSIVE_BEHAVIOUR.md](RESPONSIVE_BEHAVIOUR.md). Values remain **PROPOSED**.

## Accessibility requirements

See [ACCESSIBILITY_AND_USABILITY.md](ACCESSIBILITY_AND_USABILITY.md). WCAG 2.2 AA target — not claimed certified.

## Sinhala and English content strategy

See [CONTENT_AND_LANGUAGE_GUIDE.md](CONTENT_AND_LANGUAGE_GUIDE.md). Sinhala-first operators; no invented final regulatory Sinhala.

## Figma-to-Django handoff method

1. Freeze approved frames (after 01C) with tokens/components.
2. Export semantic tokens to CSS variables / Tailwind in implementation phases.
3. Annotate HTMX partial-swap expectations in handoff.
4. Map screens to template paths from Phase 02+.
5. Link frames to requirement IDs in the traceability matrix.
6. Deviations require design + QA note.

## Boundary

This plan does **not** claim a Figma binary was created in-repo. Owners create the Figma file from the build specification.
