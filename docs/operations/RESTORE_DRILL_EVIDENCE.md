# Restore Drill Evidence — Phase 19

**Executed at (UTC):** 20260810T010616Z
**Mode:** `docker-compose:postgres`
**Source DB:** `nelna_fg` (non-production local/compose)
**Scratch DB:** `nelna_fg_restore_drill`
**Marker id:** `phase19_restore_drill_20260810T010616Z`
**Result:** PASS (verify count=1)

## Scope

- PostgreSQL logical dump/restore only in this drill
- Evidence object storage restore is a separate operator procedure
- MongoDB SoR restore is N/A (PostgreSQL is primary SoR)

## Notes

Operator must retain dump checksums in the company-approved backup vault.
RPO/RTO remain **COMPANY DECISION REQUIRED**.
This drill does **not** authorize production go-live.
