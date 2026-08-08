# Phase 06G — Checklist Engine v2 Implementation Split (06H–06M)

**Document status:** Sequenced implementation plan — **design authorized by ADR-019**; units not started  
**Created:** 2026-08-09  
**Rule:** Do not invent Nelna limits, sample sizes, AQL, CCP/OPRP, or role authority. Prefer APPROVED FOR DIGITALIZATION forms (06F) before enabling form-specific structures in production content.

## 06G (this phase)

Architecture + ADR only. No schema-shaping feature implementation. No separate engine.

## Shared exit rules for every later unit

- Additive migrations; default preserves existing SIMPLE behavior  
- PUBLISHED/RETIRED immutability preserved  
- Org-scoped RBAC + audit events  
- Tests: unit, authorization, cross-org, concurrency/idempotency where uniqueness changes  
- Item evaluation ≠ QA disposition  
- Coverage gate unchanged (≥80% app baseline)  
- Mongo cutover **out of scope** unless DB-02 PASS and separate authorization  

## 06H — Repeating / sample foundation

**Objective:** Support `REPEATING_GROUP` + child SIMPLE items + runtime `sample_index`.

| Deliverable | Notes |
| --- | --- |
| `item_kind` + `parent_item` | Default SIMPLE; one-level groups |
| `repeat_min` / `repeat_max` | Nullable; technical ceiling required; no invented AQL |
| Draft/snapshot uniqueness | `(record\|submission, item, sample_index)` |
| UI | Add/remove sample rows via HTMX; server validates counts |
| Clone/publish | Copy group graph |

**Out of scope:** nested groups, calculated, conditionals, evaluation engine.

**Exit:** Synthetic tests prove multi-sample save/submit/immutability; legacy one-answer rows remain valid (`sample_index=1` or equivalent).

## 06I — Calculated fields

**Objective:** `CALCULATED` items with closed operators `SUM|AVERAGE|MIN|MAX|COUNT|RANGE`.

| Deliverable | Notes |
| --- | --- |
| Operator + operand refs | Same-version only; cycle detection |
| Server compute | On save/submit; no `eval()` |
| Snapshot | Persist computed Decimal (and inputs identity) immutably |

**Out of scope:** free-form formulas, client-authoritative math.

**Exit:** Deterministic tests for each operator; injection attempts denied.

## 06J — Conditional logic

**Objective:** Server-authoritative `VISIBLE_IF` / `REQUIRED_IF` / `EVIDENCE_REQUIRED_IF` (evidence kind may stub until `evidence` module).

| Deliverable | Notes |
| --- | --- |
| Structured predicates | Closed comparators; typed expected values |
| Save/submit re-eval | Hidden bypass fails |
| UI mirror | Non-authoritative progressive display |

**Out of scope:** expression language, cross-template predicates.

**Exit:** Authorization + bypass + org-isolation tests.

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
