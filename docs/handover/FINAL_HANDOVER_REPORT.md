# Final Handover Report

**Report date:** 2026-08-11  
**Authoritative repository:** `C:\Projects\nelna-fg-digital-recording-system`  
**Remote:** `https://github.com/jkchinthaka/nelna-fg-digital-recording-system.git`  
**Branch:** `main`  
**Do not use** the OneDrive clone for day-to-day work.

This report is an engineering continuity handover. It is **not** a production release certificate.

---

## Classification

**A. TECHNICAL HANDOVER READY — BUSINESS/UAT GATES PENDING**

| Forbidden claim | Status |
| --- | --- |
| PRODUCTION READY | **Not claimed** |
| UAT PASSED | **Not claimed** — Phase 20 remains BLOCKED |
| Phase 21 go-live | **GO-LIVE BLOCKED** |
| MongoDB cutover | **DO NOT MIGRATE** |

---

## Repository sync (this run)

| Item | Value |
| --- | --- |
| Observed GitHub `origin/main` at start | `c64d7ca90d5ee957b98b5d31ddba98d47df6b337` (Phase 23 HACCP snapshot freeze) |
| Local `HEAD` at start | `fbc28e2c6e701b90bae87db17a56279c2c3ff624` (27 commits ahead — Phases 24–41) |
| Divergence | Local ahead only; no overwrite risk versus `origin/main` |
| Authoritative SoR | PostgreSQL (ADR-002) |
| MongoDB gate | `STATUS: MONGODB POC PARTIAL — … — DO NOT MIGRATE` — exact `MONGODB POC PASSED — DB-03 MAY PROCEED` **absent** |

---

## Host quality gates (this run)

| Gate | Result |
| --- | --- |
| `uv lock --check` | PASS |
| `ruff check` / `ruff format --check` | PASS after repair |
| `mypy apps config scripts` | PASS (0 errors / 582 files after type repair) |
| `djlint templates --check` | PASS |
| `pip-audit` | PASS — no known vulnerabilities |
| `bandit` | Known low/medium findings confined to ops restore-drill / synthetic URL helpers; runtime B101 regression cleared |
| `npm ci` / `npm run build` | PASS |
| `makemigrations --check` | PASS |
| `manage.py check` | PASS |
| `pytest` (full, `--cov-fail-under=80`) | **820 passed**, 6 failed on first full run; failures repaired (Phase 44 assertions vs service order were mid-edit; architecture allowlist; core/accounts import; rework `assert`) |
| Coverage | **81.03%** (threshold 80% not reduced) |
| Docker engine | Healthy (Docker Desktop 4.65 / Engine 29.2.1) |
| `docker compose config` | PASS |
| Compose postgres/redis | Already healthy on host ports 5433 / 6380 |

Re-run the full suite after the remaining commit set lands if additional uncommitted phase directories appear.

---

## Core modules verified (code + tests exist)

Recording spine: accounts, organizations, access_control, security_audit, master_data, instruments, training, checklists, scheduling, recording, reviews, quality, evidence, notifications, reports.

Quality operations: nonconformance, capa, dispatch, laboratory, haccp, sampling, foreign_body, sanitation, environmental, packaging, changeover, receiving, supplier_quality, iqc, ipqc, batch_dossier, batch_genealogy, recall (+ mock), customer_complaints, product_returns, quality_quarantine, rework.

QMS shells: document_control (43), change_control (44), quality_audits (45), compliance_mapping (46).

Integrations: `apps.integrations` boundary/mocks only. AI: advisory, default OFF.

---

## Database / MongoDB

- PostgreSQL remains the application System of Record.
- Isolated MongoDB POC is **not** sufficient for cutover.
- Do not execute DB-03.
- See [MONGODB_MIGRATION_STATUS.md](MONGODB_MIGRATION_STATUS.md) and `docs/migration/MONGODB_POC_RESULTS.md`.

---

## Phase 00–23

Technical foundations **IMPLEMENTED** on local `main` (00–23 plus later expansions). Business approval, production configuration, UAT, and production-ready labels remain **not** equivalent.

Notable blocked units: 06N FG-QA-001; 07 production generation; 08–10 production use; 14 offline not implemented; 17 live Bileeta; 20 UAT; 21 go-live.

---

## Phase 24–130 (evidence-based)

| Range | Classification | Status |
| --- | --- | --- |
| 24 Sampling | B | IMPLEMENTED foundation — no AQL/ISO tables |
| 25 Device traceability | B | IMPLEMENTED — enforcement default OFF |
| 26 Foreign body | B/C | IMPLEMENTED — auto-HOLD OFF |
| 27 Sanitation | B/C | IMPLEMENTED — fail-stop OFF |
| 28 Environmental | B/C | IMPLEMENTED — auto-HOLD OFF |
| 29 Label/artwork | B/C | IMPLEMENTED — no shelf-life math |
| 30 Allergen/changeover | B/C | IMPLEMENTED — block OFF |
| 31 Receiving | B | IMPLEMENTED — ERP outbound blocked |
| 32 Supplier quality | B | IMPLEMENTED — count-only metrics |
| 33 IQC | B | IMPLEMENTED — ERP dual-gate OFF |
| 34 IPQC | B | IMPLEMENTED — not FG RELEASE |
| 35 EBR / dossier | B | IMPLEMENTED — PDF dual-gate OFF |
| 36 Genealogy | B | IMPLEMENTED — Mongo projection OFF |
| 37–38 Recall / mock | B | IMPLEMENTED — notify/ERP OFF; mock isolated |
| 39 Complaints | B | IMPLEMENTED — auto-send OFF |
| 40 Returns | B | IMPLEMENTED — ERP stock OFF |
| 41 Quarantine | B | IMPLEMENTED — ERP is inventory ledger |
| 42 Rework | B | IMPLEMENTED — REJECT ≠ auto rework |
| 43 Document control | B | IMPLEMENTED foundation — APR-068 |
| 44 Change control | B | IMPLEMENTED foundation — APR-069 |
| 45 Quality audits | B | IMPLEMENTED foundation — APR-070; ≠ security_audit |
| 46 Compliance mapping | B | IMPLEMENTED foundation — IMPLEMENTED ≠ COMPLIANT |
| 47–55 Analytics / QRM / SPC | E/C | Not justified for forced delivery; no invented scores |
| 56–62 Auth / devices / i18n | C/D/E | Partial prior auth exists; SSO/MFA/native not done |
| 63–65 API / warehouse / BI | E | Not implemented as a platform |
| 66–80 AI / IoT / OT | E/D/F | AI remains advisory; no OT write; no PLC |
| 81–89 Portals / native / offline | E | Offline already decided NOT IMPLEMENTED (ADR-026) |
| 90–100 Flags / engines / Kafka | E | Do not add workflow engine/Kafka without demonstrated need |
| 101–108 Secrets / pentest | E | Phase 19 technical controls exist; pen-test EVIDENCE REQUIRED |
| 109–117 HA / DR / Mongo replica | F/E | Mongo replica only if Mongo becomes approved SoR |
| 118–130 UX / ops portals | E | Optional later |

---

## Intentionally not implemented

- Live Bileeta / ERP writes
- MongoDB application cutover
- Official Nelna master data, roles, SoD, FG-QA-001 publish
- AQL/ISO tables, CCP limits, temperature classes
- Offline PWA sync
- Native mobile
- AI final quality decisions
- Production deploy / UAT execution / fake signatures
- Phases 47–130 product delivery

---

## Business evidence blockers

See [BUSINESS_EVIDENCE_REQUIRED.md](BUSINESS_EVIDENCE_REQUIRED.md) and [OPEN_BLOCKERS.md](OPEN_BLOCKERS.md). Highest-risk business issue: **no approved published checklist + no recorder/Supervisor/QA mapping + no SoD evidence**, so the factory-floor spine cannot be used for real product.

---

## UAT / production

- Phase 20 package is executable by humans; actual/PASS/signature fields remain blank / NOT EXECUTED.
- Phase 21 remains **GO-LIVE BLOCKED** until Phase 20 PASS plus hosting, config, support, backup custody, security signoff, and paper-decommission decision.

---

## Handover entry

Start at [HANDOVER_README.md](HANDOVER_README.md).

Synthetic demo (not company data):

```powershell
uv run python manage.py load_synthetic_demo_data
```

---

## Highest-risk unresolved technical issue

Unpushed local history (27+ commits and a large working tree spanning Phases 24–46) must be committed in logical units and pushed so GitHub `main` matches the validated local tree. Competing long-running local pytest/DB creation can lock `test_nelna_fg`.

## Highest-risk unresolved business issue

Missing owner evidence for FG-QA-001, official org/shift/product catalogues, role mappings, SoD, Bileeta contract, and UAT participants.

## Actions required from Nelna management / QA / IT

1. Name owners for every row in [BUSINESS_EVIDENCE_REQUIRED.md](BUSINESS_EVIDENCE_REQUIRED.md).
2. Return paper-form inventory and FG-QA-001 approval (or written reject).
3. Supply official org/site/dept/shift and product catalogues.
4. Approve recorder / Supervisor / QA mappings and SoD.
5. Provide Bileeta API docs + sandbox or formally defer integration.
6. Decide hosted UAT environment, RPO/RTO, backup custody, support owner.
7. Execute Phase 20 with real people; do not ask engineering to invent PASS.

---

## Final statement

This is a professional **technical** handover for continued development and controlled readiness work. **Silence is not approval.** PostgreSQL remains SoR. Paper records must continue.
