# MongoDB Migration Status

## Executive status

```text
STARTING_BRANCH=feature/mongodb-same-maintainpro-db
STARTING_SHA=3c99312
FINAL_SHA=(see git after this commit)
MAIN_SHA=d5a4460
MAIN_MERGED=NO
REAL_COMPANY_MONGO_WRITTEN_TO=NO
```

```text
CONTINUATION REQUIRED — MONGODB FUNCTIONAL PARITY MIGRATION CHECKPOINT CREATED
```

PostgreSQL remains authoritative on `main`. Isolated Mongo POC proves runtime for migrated paths.

---

## Production target (unchanged)

```text
Logical database: mgintginpro_prod
FG namespace: fg_
Isolated POC: fg_same_db_poc @ compose.mongo-poc.yaml (127.0.0.1:27027 / nelnaPocRs)
```

---

## Checkpoint progress (this pass)

| Item | Status |
| --- | --- |
| Partial unique rewrite | **Fixed** — `isnull=False` → field unique; other partials (e.g. empty batch) **skipped** (not converted to full unique) |
| Checklist version allocation on Mongo | **Green** (retry on unique ValidationError + order_by alloc) |
| Scheduling generator concurrency | **Green** (no false batch unique collision) |
| NCR update vs close race | **Fixed** — open-filtered update_fields; no status clobber |
| CAPA / RCA / recording / Supervisor / QA spikes | **Green** |
| Auth + employee_code uniqueness on Mongo | **Green** (13 auth + concurrent case variants) |
| Core daily/controlled forms HTTP on Mongo | **Previously green** (40-test batch) |
| `/health/ready/` Mongo mode | **mongodb+redis ok** (no PostgreSQL check) |
| FG-only backup/restore tooling | **Added** — refuses `mgintginpro_prod` write/restore; dry-run inventory 232 `fg_*` |
| Full Mongo pytest / coverage ≥80% | Not complete |
| Full PG regression | Targeted changed modules **31 passed**; full suite not re-run |
| Browser smoke | Not run |

### Focused Mongo evidence this pass

```text
SPIKES+AUTH: 43 passed
PRIOR CORE BATCH (auth+daily+controlled+recording/supervisor/QA spikes): 40 passed (then 52/53 with one unique flake before rewrite fix)
PG CHANGED-MODULE REGRESSION: 31 passed
FG COLLECTIONS (POC): 232 fg_*; 0 non-fg leftovers
```

---

## Next exact action

1. Run full application pytest under `config.settings.mongo_same_db_poc`; fix failures continuously
2. Mongo coverage ≥80%
3. Full PostgreSQL regression + quality/security gates
4. Isolated FG mongodump/mongorestore drill (requires mongodump binary)
5. Browser smoke against Mongo runtime
6. Company cutover remains authorization-blocked

---

## Safety

- Do not use the OneDrive clone
- Do not merge `main` automatically
- Do not write to `mgintginpro_prod` / MaintainPro
