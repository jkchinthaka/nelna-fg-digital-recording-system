# MongoDB Migration Status

## Executive status

```text
STARTING_BRANCH=feature/mongodb-same-maintainpro-db
STARTING_SHA=5fce899
FINAL_SHA=(see git after commit)
MAIN_SHA=(do not merge)
WORKING_TREE=Mongo POC runtime work committed; unrelated WIP may remain local
```

PostgreSQL remains the authoritative system of record on `main`.

```text
CONTINUATION REQUIRED — MONGODB FUNCTIONAL PARITY MIGRATION CHECKPOINT CREATED
```

---

## Production target (unchanged)

```text
Host route: via MONGODB_URI (do not hard-code credentials/host in Python)
Logical database: mgintginpro_prod
FG namespace: fg_
Isolated POC only: fg_same_db_poc
Company Mongo writes: NONE
MaintainPro impact: NONE
main merged: NO
REAL COMPANY MONGO WRITTEN TO: NO
```

---

## This checkpoint — actual isolated Mongo runtime

| Item | Status |
| --- | --- |
| Contrib ObjectId AppConfigs (POC only) | Done — `config/mongo_contrib.py` + `mongo_migrations/` |
| Safety guard rejects `mgintginpro_prod` as POC DB | Proven |
| `migrate` on `fg_same_db_poc` | **Succeeded** (full app graph) |
| FG collection namespace | **232 `fg_*` collections; 0 bare leftovers** after ORM `DatabaseWrapper.get_collection` prefix |
| Auth on Mongo | **Proven** — create/login/bad password/lockout/inactive/password change/session/logout + concurrent `ABC001`/`abc001`/`AbC001` → 1 row |
| Auth pytest (`apps/accounts/tests/test_auth.py`) | **13 passed** under `--ds=config.settings.mongo_same_db_poc` |
| Core workflow + CL forms HTTP | **`test_daily_records_completion` + `test_controlled_daily_records` + auth + recording/supervisor/QA spikes: 40 passed** |
| Persistence `atomic()` on Mongo | **No-op by design** (CAS/unique); explicit `mongo_multi_doc_atomic` for rare multi-doc cases |
| Employee code uniqueness | Normalized field unique + migration `0004`; concurrent case variants OK |
| Schema compat | Lower/Upper rewrite; CheckConstraint skip+warn; partial unique predicate drop |
| Remaining concurrency spikes | Checklist version alloc / scheduling generator / some CAPA·NCR races still failing on Mongo |
| Full Mongo pytest suite | Not complete |
| Mongo coverage ≥80% | Not measured |
| PG full regression this SHA | Not re-run yet |
| Browser smoke | Not run |
| FG-only dump/restore drill | Not run |

### Inventory notes (recalculated direction)

```text
SELECT_FOR_UPDATE raw production: 0 (facade only)
PREFETCH_RELATED raw production: 0 (compat / Mongo no-op)
TRANSACTION: service atomic() is PG-real / Mongo-noop; classify remaining django.db.transaction.atomic sites
LOWER/function: schema rewrite active; query iexact largely works via backend regex path; inventory rewrite still open
```

---

## Next exact action

1. Fix remaining Mongo concurrency spikes (checklist version allocation retry, scheduling duplicate-key normalize, CAPA/NCR CAS edge cases)
2. Continue full pytest under `mongo_same_db_poc` — fix failures without mass-skip
3. Mongo coverage ≥80%; then PostgreSQL full regression + quality gates
4. FG-only mongodump/restore drill on isolated POC
5. Browser smoke against isolated Mongo runtime
6. Company cutover remains **authorization-blocked** (no writes to `mgintginpro_prod`)

---

## Safety

- Do not use the OneDrive clone for this branch
- Do not merge `main` automatically
- Do not write to MaintainPro / `mgintginpro_prod`
