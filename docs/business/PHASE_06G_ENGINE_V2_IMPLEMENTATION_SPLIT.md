# Phase 06G — Checklist Engine v2 Implementation Split (06H–06M)

**Document status:** Sequenced implementation plan — **design authorized by ADR-019**; **06H/06I implemented as technical foundations** (no invented AQL/sample sizes or business formulas)
**Created:** 2026-08-09
**Updated:** 2026-08-10 (06I)
**Rule:** Do not invent Nelna limits, sample sizes, AQL, CCP/OPRP, or role authority. Prefer APPROVED FOR DIGITALIZATION forms (06F) before enabling form-specific structures in production content.

## 06G (design)

Architecture + ADR only. No separate engine.

## 06H — Repeating / sample foundation — IMPLEMENTED (technical)

**Objective:** Support `REPEATING_GROUP` + child SIMPLE items + runtime `sample_index`.

| Deliverable | Notes |
| --- | --- |
| `item_kind` + `parent_item` | Default SIMPLE; one-level groups |
| `repeat_min` / `repeat_max` / `repeat_default` | Nullable; technical ceiling 100; no invented AQL |
| Draft/snapshot uniqueness | `(record\|submission, item, sample_index)` |
| UI | Add/remove sample rows; server validates indexes |
| Clone/publish | Copies group graph |

**Out of scope (still):** nested groups, calculated, conditionals, evaluation engine.

## 06I — Calculated fields — IMPLEMENTED (technical)

**Objective:** `CALCULATED` items with closed operators `SUM|AVERAGE|MIN|MAX|COUNT|RANGE`.

| Deliverable | Notes |
| --- | --- |
| Operator + operand refs | Same-version only; cycle detection; sibling/top-level scope |
| Server compute | On save/submit; no `eval()`; client values ignored |
| Snapshot | Persist computed Decimal + `calculation_context` immutably |

**Out of scope:** free-form formulas, client-authoritative math, seeded business formulas.

**Exit:** Deterministic tests for each operator; injection attempts denied.

## 06J — Conditional logic — IMPLEMENTED (technical)

**Objective:** Server-authoritative `VISIBLE_IF` / `REQUIRED_IF` / `EVIDENCE_REQUIRED_IF` (evidence kind fail-closed stub until `evidence` module).

| Deliverable | Notes |
| --- | --- |
| Structured predicates | Closed comparators; typed expected values; no expression language |
| Save/submit re-eval | Hidden bypass fails; dynamic requiredness |
| Snapshot | `condition_context` frozen at submit |
| UI mirror | Non-authoritative progressive display hooks (optional) |

**Out of scope:** expression language, cross-template predicates, invented form predicates.

**Exit:** Authorization + bypass + org-isolation / snapshot tests.

## 06K — Deterministic evaluation

**Objective:** Optional item result `PASS|FAIL|WARN|NOT_EVALUATED` from bounds/rules.

| Deliverable | Notes |
| --- | --- |
| Evaluation service | Domain service; auditable summary counts only |
| Policy boundary | FAIL does **not** auto HOLD/REJECT/ERP/CAPA |
| Snapshot | Freeze evaluation at submit if enabled |

**Out of scope:** Auto disposition, product-spec engine beyond definition bounds.

**Exit:** Explicit tests that FAIL ≠ QA disposition side effects.

## 06L — Control-point metadata

**Objective:** Extensibility field `NONE|CCP|OPRP|PRP|GMP|QUALITY` default `NONE`.

| Deliverable | Notes |
| --- | --- |
| Metadata on item (or side table) | No invented classifications in loaders |
| Publish | Allows NONE without evidence; non-NONE may require future evidence gate flag |

**Out of scope:** HACCP plan management module.

**Exit:** Defaulting + immutability + no auto-disposition coupling.

## 06M — Precision / units / boundaries

**Objective:** Harden numeric definition: precision, rounding mode, inclusive/exclusive bounds.

| Deliverable | Notes |
| --- | --- |
| `decimal_precision`, `rounding_mode` | Decimal-safe apply on input |
| `min_inclusive` / `max_inclusive` | Defaults inclusive |
| Recording | Consistent round-trip in draft + snapshot |

**Out of scope:** Inventing product limits; dual-unit conversion engines unless evidenced.

**Exit:** Property tests for rounding/boundary edge cases.

## Suggested dependency order

```text
06H (repeating)
  ├── 06I (calculated; often on group children)
  ├── 06J (conditionals; may reference SIMPLE answers)
  │     └── 06K (evaluation; uses bounds + conditions)
  ├── 06L (metadata; parallel-safe after ADR)
  └── 06M (numeric hardening; parallel-safe / early)
```

`06M` may proceed in parallel with `06H` if staffing allows. `06K` should follow enough of `06H/06J/06M` to evaluate real shapes.

## Explicit non-goals until evidence

- JSON Schema definition SoR
- New SPA framework
- MongoDB production cutover
- Seeding real CCP/limits/sample sizes
- Manual paper-form module as a second engine (paper remains discovery input via 06F)
