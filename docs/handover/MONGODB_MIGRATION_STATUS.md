# MongoDB Migration Status

## Executive status

```text
STARTING_BRANCH=feature/mongodb-same-maintainpro-db
STARTING_SHA=e3a5e67
FINAL_SHA=7c1e576
MAIN_SHA=d5a4460
MAIN_MERGED=NO
REAL_COMPANY_MONGO_WRITTEN_TO=NO
```

```text
CONTINUATION REQUIRED — FINAL SERVER-HOSTING VERIFICATION CHECKPOINT CREATED
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
| Production `transaction.atomic` → facade | **Done** — 303 `@atomic_fn` + 11 `with atomic()` across 50 service modules |
| Runtime `Lower()` annotate | **Rewritten** — `proposal_loader` uses `code__iexact` |
| Auth + module concurrency spikes | **Green** — 43 passed |
| Decimal BSON round-trip | **Green** — 8/8 values (dedicated test) |
| Dedicated cross-org Mongo suite | **Green** — service + HTTP history/print/CSV denial |
| FG dump → restore drill | **Green** — 232 `fg_*`; refuse prod dump/restore; `NON_FG=0`; users 1→1 |
| Celery worker live | **Green** — `health_echo` + `generate_due_checklist_tasks` on Mongo+Redis |
| Celery Beat | **Boot started**; schedule `*/5`; duplicate prevention `replay_safe=True` |
| Health | **Green** — `/health/live/` + `/health/ready/` mongodb+redis+celery_broker ok |
| Full Mongo pytest + coverage ≥80% | **In progress** |
| Full PG regression + quality/security | Not complete |
| Browser Mongo smoke | Not complete |

### Focused Mongo evidence this pass

```text
SPIKES+AUTH: 43 passed
DECIMAL+CROSS_ORG: 10 passed
FG_DUMP_COLLECTIONS: 232
FG_RESTORE: 232 fg_*; NON_FG_COLLECTIONS_WRITTEN=0
CELERY_WORKER: health_echo + generate_due executed
HEALTH_READY: mongodb ok, redis ok, celery_broker ok
```

---

## Inventory (recalculated)

```text
LOWER/FUNCTION: TOTAL≈102; UNRESOLVED runtime Lower=0 after iexact rewrite;
  remaining aggregates treated as supported-under-suite (pending full-suite proof)
TRANSACTION production raw django.atomic: 0 (migrated to facade)
NESTED_MONGO_SAVEPOINT_DEPENDENCY: 0 (facade nested atomic is Mongo no-op)
```

---

## Next exact action

1. Finish full `pytest --ds=config.settings.mongo_same_db_poc --ignore=apps/mongo_poc` + coverage ≥80%
2. Full PostgreSQL regression + quality/security gates
3. Observe Celery Beat due-tick against Mongo worker
4. Playwright/browser smoke on isolated Mongo runtime
5. Rebuild release package from final green SHA
6. Company cutover remains authorization-blocked

---

## Safety

- Do not use the OneDrive clone
- Do not merge `main` automatically
- Do not write to `mgintginpro_prod` / MaintainPro
