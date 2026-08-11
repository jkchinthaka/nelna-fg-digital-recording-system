# Restore Drill Evidence — Phase 19

**Executed at (UTC):** 20260811T111829Z
**Source DB:** `nelna_fg` (local/non-production Compose)
**Scratch DB:** `nelna_fg_restore_drill`
**Marker id:** `phase19_restore_drill_20260811T111829Z`
**Dump SHA-256:** `fdc84e75693380c557f9be67e941886157373e60306b8f7b7677e614a761b261`
**Client mode:** `docker:postgres`
**Result:** PASS (verify count=1)

## Scope

- PostgreSQL logical dump/restore only in this drill
- Evidence object storage restore is a separate operator procedure
- MongoDB SoR restore is N/A (PostgreSQL is primary SoR per ADR-002)

## Notes

Operator must retain dump checksums in the company-approved backup vault.
RPO/RTO remain **COMPANY DECISION REQUIRED**.
This PASS is technical evidence for Phase 19 — not production go-live approval.
