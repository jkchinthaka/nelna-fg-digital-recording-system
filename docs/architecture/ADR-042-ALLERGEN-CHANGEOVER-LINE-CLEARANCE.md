# ADR-042 — Allergen / changeover / line-clearance foundation

**Status:** Accepted (technical foundation)  
**Date:** 2026-08-10  
**Phase:** 30

## Context

Factories need configurable allergen declaration association, product-to-product
changeover records, and line-clearance evidence without inventing company allergen
lists, cleaning sequences, or matrix-based production block rules.

## Decision

1. Introduce `apps.changeover` with optional `AllergenReference` shells (unseeded).
2. `ProductAllergenDeclaration` links FG products to opaque approved declaration
   references; optional M2M to allergen references remains empty until evidenced.
3. `ChangeoverRecord` captures previous/next product, opaque line code, time,
   checklist cleaning references, optional packaging artwork hook, verification,
   evidence object keys, and frozen context for future batch dossiers.
4. `LineClearanceRecord` prefers checklist template/version/submission references
   rather than hardcoded clearance fields.
5. `AllergenRiskPolicy` + `CHANGEOVER_ALLERGEN_BLOCK_APPROVED` dual-gate production
   block — default OFF; never invent matrix outcomes.
6. Permissions separate record (`manage_changeover`) from verify/approve
   (`verify_changeover`) and policy (`manage_allergenriskpolicy`).

## Consequences

- Company allergen catalogues, cleaning SOPs, sequencing, and matrix block policy
  remain **EVIDENCE REQUIRED** (APR-056).
- Batch dossier UI integration is deferred; frozen contexts are dossier-ready.
