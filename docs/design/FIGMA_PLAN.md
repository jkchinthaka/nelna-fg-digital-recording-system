# Figma Plan

**Document status:** Preparation plan — no final UI designs are created in Phase 00  
**Phase:** 00 — Discovery and governance  
**Tool:** Figma Professional  
**Last updated:** 2026-08-04

## Purpose

Define the Figma file structure, required screens, components, states, breakpoints, accessibility expectations, language strategy, and handoff method for Phase 01 design work.

## Figma pages

| Page | Intent |
| --- | --- |
| 00 Project Brief | Goals, roles, constraints, non-goals, MVP summary |
| 01 User Journeys | Operator, supervisor, QA, admin, auditor journeys for MVP |
| 02 Information Architecture | Navigation and object model for MVP |
| 03 Design Tokens | Color, type, space, elevation, semantic status tokens |
| 04 Components | Buttons, inputs, task cards, status chips, evidence uploader, empty/error |
| 05 Operator Mobile | Mobile-first recording screens |
| 06 Supervisor Mobile and Tablet | Check queues and detail actions |
| 07 QA Console | Verification queues and detail |
| 08 Administration | Users, roles, org, templates (admin) |
| 09 Management Dashboard | High-level status (post-MVP elements marked) |
| 10 Offline and Error States | Connectivity loss, sync pending, conflicts (future-aware) |
| 11 Interactive Prototypes | Clickable MVP paths |
| 12 Developer Handoff | Specs, assets, behavior notes for Django/HTMX implementation |

## Required screens (MVP-focused)

- Login / session expired
- Home / my tasks
- Task detail / checklist fill
- Submission confirmation
- Evidence capture/upload
- Supervisor queue / check detail
- QA queue / verify detail
- Amendment request / history view (as approved)
- Basic audit export trigger/download (admin/QA)
- Denied access / not found
- Read-only auditor record view

Exact field lists await approved forms (**EVIDENCE REQUIRED**).

## Required components

- Primary/secondary/destructive buttons
- Text, select, toggle, numeric, pass/fail controls (as needed by forms)
- Task list item and filters
- Status indicators (semantic, not color-only)
- Evidence thumbnail + upload progress
- Banner alerts and inline field errors
- Language toggle or locale presentation pattern
- Sticky operator action bar

## Required states

- Empty, loading, success, validation error
- Forbidden / unauthorized
- Offline / degraded connectivity (design even if MVP is online-only)
- Sync pending / sync conflict (future)
- Retrospective entry indicator (for BC procedures)

## Responsive breakpoints

| Name | Min width (proposed) | Primary users |
| --- | --- | --- |
| Operator mobile | 360px | Operators |
| Supervisor large phone / small tablet | 600px | Supervisors |
| Tablet | 768px | Supervisors / QA |
| Desktop | 1024px+ | QA / Admin / Management |

All breakpoint pixel values are **PROPOSED** until design-system approval.

## Accessibility requirements

- Visible labels and focus states
- Contrast aligned to WCAG-oriented targets in NFRs
- Do not convey critical status by color alone
- Touch targets sized for gloved/factory use where practical
- Error messages tied to fields

## Sinhala and English content strategy

- Operator-facing MVP content: Sinhala mandatory; English optional secondary as owners confirm
- QA/Admin: language mix **DECISION REQUIRED** via questionnaire
- Figma must include real string containers for both languages once translations are provided — do not invent operational terminology
- Layout must tolerate Sinhala string length differences

## Figma-to-Django handoff method

1. Freeze MVP frames in page 12 with tokens and component mappings.
2. Export semantic tokens to CSS variables consumed by Tailwind configuration in implementation phases.
3. Annotate HTMX interaction expectations (partial swaps, targets) in handoff notes.
4. Map each screen to template path naming agreed in Phase 02+.
5. Link frames to requirement IDs where applicable in the traceability matrix.
6. Developers implement templates/partials to match approved frames; deviations require design+QA note.

## Phase 00 boundary

This document prepares Figma work. **Do not treat Phase 00 as delivering final UI designs.**
