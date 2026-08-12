# Same-Database MongoDB Cutover Audit — FG + MaintainPro

**Branch:** `feature/mongodb-same-maintainpro-db`  
**Baseline SHA:** `d5a44605219884de6467ecb94a3730e7f2d1c87e`  
**Classification:** **MONGODB SAME-DATABASE CUTOVER BLOCKED — INVARIANTS OR BACKEND LIMITATIONS NOT SAFELY RESOLVED**  
**Additional gate:** **MONGODB CUTOVER BLOCKED — EXACT MAINTAINPRO DATABASE NAME REQUIRED** (production name not supplied in this phase)

Do not merge to `main`. PostgreSQL remains the application default on `main`.

---

## Pre-cutover checklist (not completed)

| Field | Value |
| --- | --- |
| EXISTING_DATABASE_NAME | **UNKNOWN — company must supply exact `MONGODB_DATABASE`** |
| EXISTING_COLLECTION_COUNT | ~120+ Prisma models in MaintainPro schema (estimate only; production inventory required) |
| PLANNED_FG_COLLECTION_COUNT | **225** Django models (default `app_label_modelname` tables) |
| COLLECTION_COLLISIONS | **UNKNOWN — MANUAL REVIEW REQUIRED** (no production read-only inventory performed) |
| MONGODB_VERSION | Not verified against company server |
| TOPOLOGY | MaintainPro uses MongoDB via Prisma; **transaction support on company topology not verified** |
| TRANSACTIONS_AVAILABLE | **UNKNOWN** — FG requires multi-doc semantics for recording/submit/review |
| AUTH_SCOPE | Independent FG auth; no SSO |
| BACKUP_VERIFIED | **No** |
| MAINTAINPRO_HEALTH_BEFORE | **Not measured** (no production access) |

---

## Business constraint vs technical reality

The required end state is FG and MaintainPro sharing **one logical MongoDB database** on the company server, with **zero modification** to MaintainPro data.

Current repository evidence:

1. **Isolated MongoDB POC** (`apps/mongo_poc`, 16 tests) — PASS on dedicated `nelna_fg_mongo_poc` only  
2. **Full application** — designed and tested on **PostgreSQL** (893 pytest, 83.45% coverage)  
3. **Prior formal assessment** — `MONGODB POC FAILED FOR CUTOVER — DO NOT MIGRATE` ([MONGODB_POC_RESULTS.md](MONGODB_POC_RESULTS.md))

---

## Mongo backend

| Item | Value |
| --- | --- |
| Package | `django-mongodb-backend==5.2.3` (official; pinned in `pyproject.toml`) |
| Prohibited | djongo, mongoengine, ODM replacement |
| POC settings | `config.settings.mongo_poc` (isolated; not production) |
| Production mode | **Not implemented** — `config.settings.database.build_databases()` still PostgreSQL-only |

Required production shape (when authorized):

```python
DATABASES = {
    "default": {
        "ENGINE": "django_mongodb_backend",
        "HOST": env("MONGODB_URI"),
        "NAME": env("MONGODB_DATABASE"),
    }
}
```

Fail-closed if `MONGODB_URI` or `MONGODB_DATABASE` missing.

---

## Compatibility matrix summary

Full matrix: [MONGODB_COMPATIBILITY_MATRIX.md](MONGODB_COMPATIBILITY_MATRIX.md)

| Area | PostgreSQL today | Mongo status | Decision |
| --- | --- | --- | --- |
| Default engine | `django.db.backends.postgresql` | Not wired for prod | BLOCK until redesign |
| `select_for_update()` | **~138 call sites** in `apps/` | **Unsupported** | REDESIGN required |
| `prefetch_related` | **~30+ usages** in selectors/services | **Unsupported** | REDESIGN required |
| `OuterRef` / `Subquery` | QA/supervisor queues, daily selectors | Partial / unproven | POC / REDESIGN |
| `django.db.transaction.atomic` | Ubiquitous | **No-op** on Mongo backend | Use `django_mongodb_backend.transaction.atomic` |
| Nested savepoints | Checklist version allocation | **Unsupported** | REDESIGN required |
| `IntegrityError` idempotency | Widespread | Mapping unproven at scale | TEST on Mongo |
| `UniqueConstraint` + `Lower()` | User employee_code, products | Functional unique POC needed | EVIDENCE REQUIRED |
| `CheckConstraint` | Recording XOR, shifts | Not equivalent | App-layer validation |
| `auth.User` / sessions / admin | Django contrib | UUID User OK; contrib collections need **fg_** namespace | B with namespace |
| Migrations | 100+ PostgreSQL migrations | Not portable as-is | New Mongo migration strategy |
| Full pytest on Mongo | N/A | **Not run** (893 tests PG-only) | BLOCK |

---

## Primary keys

| Model class | PK strategy | Mongo notes |
| --- | --- | --- |
| `accounts.User` | **UUID** | Compatible intent; contrib still needs Mongo backend validation |
| Most domain models | **UUID** (`UUIDField`) | Preferred for identity preservation |
| Django implicit IDs | `BigAutoField` on some contrib/M2M through tables | Requires `ObjectIdAutoField` or explicit strategy — **not fully audited** |
| MaintainPro (Prisma) | **ObjectId** (`@db.ObjectId`) | Different ID space — **no shared documents** |

Identity-preserving cutover from PostgreSQL → Mongo **not demonstrated**. No silent ID regeneration permitted.

---

## Transaction / concurrency blockers

Critical invariants (all currently rely on PostgreSQL row locks or savepoints):

- Duplicate daily records prevented  
- Duplicate submissions prevented  
- Latest submission only reviewable  
- Supervisor / QA decision races  
- Closed/cancelled RCA immutability  
- Correction history immutability  
- Duplicate business identifiers (RCA code, etc.)

**`select_for_update` replacement status:** **0% production-path complete** (RCA hardening added on PostgreSQL only).

If company MongoDB is standalone (no replica set), multi-document transactions may be unavailable:

```text
SAME-DATABASE MONGODB CUTOVER BLOCKED — REQUIRED TRANSACTION SEMANTICS UNAVAILABLE
```

Do not weaken invariants to pass migration.

---

## Collection namespace / collision audit

### MaintainPro (Prisma → MongoDB)

- MaintainPro repo: `C:\Users\chint\source\newmone\maintainpro`  
- Schema: `prisma/schema.prisma` — provider `mongodb`  
- Collection names follow **Prisma model names** (e.g. `User`, `Tenant`, `Department`, `WorkOrder`, `AuditLog`)

### FG (Django default table names)

- **225 models** → default names like `accounts_user`, `recording_checklistrecord`, `organizations_department`  
- **No `db_table` / `fg_` prefix applied today** — collision risk with any future shared naming is **UNKNOWN**

### Django contrib collections FG would create

| Planned FG collection | MaintainPro Prisma model | Preliminary class |
| --- | --- | --- |
| `django_migrations` | (none observed) | SAFE — FG-only |
| `django_session` | (none observed) | SAFE — FG-only |
| `django_admin_log` | (none observed) | SAFE — FG-only |
| `django_content_type` | (none observed) | SAFE — FG-only |
| `auth_permission` | (none observed) | SAFE — FG-only |
| `auth_group` | (none observed) | SAFE — FG-only |
| `accounts_user` | `User` | **UNKNOWN** — different names but both are “user” stores; must not merge |
| `organizations_department` | `Department` | **UNKNOWN** — semantic overlap, separate collections if names differ |

**Required before any write to company DB:**

1. Read-only `listCollections` on production/staging MaintainPro database  
2. Compare against `scripts/migration/fg_collection_inventory.py` output  
3. Apply **`fg_` prefix** via `Meta.db_table` on all FG models if any name collision  
4. Re-run collision script until zero `COLLISION` rows

---

## Isolated POC evidence (this session)

```text
RESTORE DRILL: N/A
Mongo POC: 16 passed on nelna_fg_mongo_poc @ 127.0.0.1:27027 (replica set)
Full app pytest on Mongo: NOT RUN
```

---

## Redis / Celery

Unchanged — Redis remains cache + Celery broker/result. **Do not** store Celery queues in MaintainPro MongoDB.

Celery against Mongo-backed FG: **not verified**.

---

## Security — FG database user (prepare only)

Do not create credentials in this phase. Administrator template:

```javascript
// PLACEHOLDER — run on company MongoDB by DBA only
use <MAINTAINPRO_DATABASE_NAME>
db.createUser({
  user: "fg_digital_recording_app",
  pwd: "<FROM_VAULT>",
  roles: [{ role: "readWrite", db: "<MAINTAINPRO_DATABASE_NAME>" }]
})
```

FG user must **not** use MaintainPro root credentials. MaintainPro credentials remain untouched.

---

## Workflow verification on Mongo

| Workflow | PostgreSQL | Mongo |
| --- | --- | --- |
| Recorder draft/submit | Tested (893 tests) | **NOT TESTED** |
| Supervisor approve/return | Tested | **NOT TESTED** |
| QA Release/Hold/Reject | Tested | **NOT TESTED** |
| Correction/resubmit | Tested | **NOT TESTED** |
| RCA/CAPA/NCR | Tested | **NOT TESTED** |
| CL/24, CL/39, CL/30, CL/18 | Human UAT partial | **NOT TESTED** |
| Print / export / RBAC | Tested on PG | **NOT TESTED** |

---

## Required work before merge (not done)

1. Company supplies exact `MONGODB_DATABASE` name  
2. Read-only collection inventory on that database  
3. Implement `fg_*` `db_table` namespace across all FG models  
4. Replace **138** `select_for_update` call sites with Mongo-safe concurrency  
5. Rewrite `prefetch_related` / `OuterRef` selectors  
6. New Mongo settings module + fail-closed production config  
7. Full pytest + ≥80% coverage **on Mongo**  
8. Concurrency integration tests  
9. Staging same-DB dry run with MaintainPro health check before/after  
10. Written infrastructure approval for MongoDB transaction topology if required  
11. APR-020 / architecture decision superseding ADR-002 PostgreSQL SoR

---

## Final classification

```text
MONGODB SAME-DATABASE CUTOVER BLOCKED — INVARIANTS OR BACKEND LIMITATIONS NOT SAFELY RESOLVED
```

**Main merged?** No — work remains on `feature/mongodb-same-maintainpro-db` only.  
**MaintainPro impact:** None — no production Mongo writes, no MaintainPro code changes.
