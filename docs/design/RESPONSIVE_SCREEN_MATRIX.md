# Responsive Screen Matrix — Phase 01C

**Document status:** Draft pending owner review — not approved  
**Phase:** 01C — High-fidelity MVP screens and prototype  
**Branch:** `design/figma-high-fidelity-mvp`  
**Created:** 2026-08-05  
**Last updated:** 2026-08-05

**Related documents:**
- [HIGH_FIDELITY_SCREEN_SPEC.md](HIGH_FIDELITY_SCREEN_SPEC.md)
- [RESPONSIVE_BEHAVIOUR.md](RESPONSIVE_BEHAVIOUR.md)
- [SCREEN_INVENTORY.md](SCREEN_INVENTORY.md)

This document maps major MVP screens to responsive breakpoints, specifying which frame sizes must be designed in Figma for Phase 01C.

---

## Breakpoint definitions

| Breakpoint | Width (px) | Device class | Primary personas |
| --- | --- | --- | --- |
| Mobile (small) | 360 | Small phone | Operator |
| Mobile (large) | 430 | Large phone | Operator, Supervisor |
| Tablet | 768 | Tablet | Supervisor, QA |
| Desktop (small) | 1024 | Desktop, laptop | QA, Admin, Auditor |
| Desktop (large) | 1440 | Large desktop | Management |

**Design priority:** Mobile-first for operator screens; tablet-first for supervisor; desktop-first for QA, admin, auditor, management.

**Responsive strategy:** Fluid layouts within breakpoint ranges; test at breakpoint boundaries and mid-ranges.

---

## Screen-to-breakpoint matrix

**Legend:**
- ✅ **Required** — Must design at this breakpoint
- ⚠️ **Optional** — Nice-to-have for completeness
- ❌ **Not needed** — Screen not used at this breakpoint

| Screen ID | Screen name | 360 (mobile-s) | 430 (mobile-l) | 768 (tablet) | 1024 (desktop-s) | 1440 (desktop-l) |
| --- | --- | --- | --- | --- | --- | --- |
| **AUTH — Authentication** |
| AUTH-LGN | Login | ✅ | ⚠️ | ⚠️ | ⚠️ | ❌ |
| AUTH-FPC | Forced password change | ✅ | ⚠️ | ⚠️ | ❌ | ❌ |
| AUTH-RST | Password reset request | ✅ | ⚠️ | ⚠️ | ❌ | ❌ |
| AUTH-LCK | Account locked | ✅ | ⚠️ | ⚠️ | ❌ | ❌ |
| AUTH-DEN | Access denied | ✅ | ⚠️ | ⚠️ | ⚠️ | ❌ |
| AUTH-EXP | Session expired | ✅ | ⚠️ | ⚠️ | ❌ | ❌ |
| **OP — Operator** |
| OP-HOME | Operator home | ✅ | ⚠️ | ⚠️ | ❌ | ❌ |
| OP-TASKS | Task list | ✅ | ⚠️ | ⚠️ | ❌ | ❌ |
| OP-TASK | Task detail | ✅ | ⚠️ | ⚠️ | ❌ | ❌ |
| OP-CHK | Checklist | ✅ | ⚠️ | ⚠️ | ❌ | ❌ |
| OP-FAIL | Failure details | ✅ | ⚠️ | ⚠️ | ❌ | ❌ |
| OP-EVD | Evidence capture | ✅ | ⚠️ | ⚠️ | ❌ | ❌ |
| OP-REV | Review before submit | ✅ | ⚠️ | ⚠️ | ❌ | ❌ |
| OP-RES | Submission result | ✅ | ⚠️ | ⚠️ | ❌ | ❌ |
| OP-REC | Own record detail | ✅ | ⚠️ | ⚠️ | ❌ | ❌ |
| OP-SYNC | Sync status (concept) | ✅ | ⚠️ | ⚠️ | ❌ | ❌ |
| OP-MORE | More / profile | ✅ | ⚠️ | ⚠️ | ❌ | ❌ |
| **SV — Supervisor** |
| SV-OVR | Supervisor overview | ⚠️ | ✅ | ✅ | ⚠️ | ❌ |
| SV-QUE | Review queue | ⚠️ | ✅ | ✅ | ⚠️ | ❌ |
| SV-REV | Record review | ❌ | ⚠️ | ✅ | ✅ | ❌ |
| SV-RET | Return for correction | ❌ | ⚠️ | ✅ | ⚠️ | ❌ |
| SV-TEAM | Team status | ❌ | ⚠️ | ✅ | ⚠️ | ❌ |
| SV-ALT | Alerts | ⚠️ | ✅ | ✅ | ⚠️ | ❌ |
| **QA — QA Officer** |
| QA-OVR | QA overview | ❌ | ❌ | ⚠️ | ✅ | ⚠️ |
| QA-QUE | Verification queue | ❌ | ❌ | ⚠️ | ✅ | ⚠️ |
| QA-VER | Record verification | ❌ | ❌ | ⚠️ | ✅ | ⚠️ |
| QA-HLD | Hold/reject/reinspection | ❌ | ❌ | ⚠️ | ✅ | ⚠️ |
| QA-NC | NC creation (concept) | ❌ | ❌ | ❌ | ✅ | ⚠️ |
| **LD — Loading (concept)** |
| LD-BLK | Loading blocked | ❌ | ⚠️ | ✅ | ✅ | ❌ |
| **AD — Administration** |
| AD-SHL | Admin shell | ❌ | ❌ | ⚠️ | ✅ | ⚠️ |
| AD-USR | User management | ❌ | ❌ | ⚠️ | ✅ | ⚠️ |
| AD-ROL | Roles and scope | ❌ | ❌ | ⚠️ | ✅ | ⚠️ |
| AD-ORG | Organization | ❌ | ❌ | ⚠️ | ✅ | ⚠️ |
| **MG — Management** |
| MG-KPI | KPI dashboard | ❌ | ❌ | ⚠️ | ⚠️ | ✅ |
| MG-ALT | Critical alerts | ❌ | ❌ | ⚠️ | ✅ | ✅ |
| **AU — Auditor** |
| AU-SRC | Audit search | ❌ | ❌ | ⚠️ | ✅ | ⚠️ |
| AU-HIS | Audit event history | ❌ | ❌ | ⚠️ | ✅ | ⚠️ |
| AU-PCK | Record pack | ❌ | ❌ | ⚠️ | ✅ | ⚠️ |

---

## Frame count summary

**Phase 01C Figma frame count estimates (required frames only):**

| Persona category | Required 360 | Required 430 | Required 768 | Required 1024 | Required 1440 | Total required |
| --- | --- | --- | --- | --- | --- | --- |
| Auth (all) | 6 | 0 | 0 | 0 | 0 | 6 |
| Operator | 11 | 0 | 0 | 0 | 0 | 11 |
| Supervisor | 0 | 4 | 6 | 0 | 0 | 10 |
| QA | 0 | 0 | 0 | 5 | 0 | 5 |
| Loading (concept) | 0 | 0 | 1 | 1 | 0 | 2 |
| Admin | 0 | 0 | 0 | 4 | 0 | 4 |
| Management | 0 | 0 | 0 | 0 | 2 | 2 |
| Auditor | 0 | 0 | 0 | 3 | 0 | 3 |
| **Total** | **17** | **4** | **7** | **13** | **2** | **43** |

**Note:** This count includes only one representative state per screen. Multiple states (loading, error, empty, success) will increase frame count. Estimate ~2–3 frames per screen for key states → **estimated total: 80–120 frames** for Phase 01C high-fidelity screens.

---

## Responsive design notes

### Mobile (360px)
- **Priority:** Operator screens
- **Layout:** Single-column, stacked cards
- **Touch targets:** Min 48px (operator-critical: 56px)
- **Navigation:** Bottom nav (3–5 items) or hamburger menu
- **Typography:** 16px body minimum (iOS/Android readability)
- **Images/Evidence:** Responsive thumbnails (tap to full-screen)

### Mobile (430px)
- **Priority:** Supervisor mobile fallback
- **Layout:** Single-column, slightly more comfortable spacing
- **Touch targets:** Min 48px
- **Navigation:** Bottom nav or tab bar
- **Typography:** 16px body
- **Images/Evidence:** Larger thumbnails

### Tablet (768px)
- **Priority:** Supervisor, QA fallback
- **Layout:** Two-column where appropriate (e.g., SV-QUE list + detail preview)
- **Touch targets:** Min 48px
- **Navigation:** Sidebar (persistent) or top tabs
- **Typography:** 16–18px body
- **Images/Evidence:** Inline preview panels
- **Tables:** Multi-column tables for queues (vs. cards on mobile)

### Desktop (1024px)
- **Priority:** QA, Admin, Auditor
- **Layout:** Multi-column (sidebar + main + detail panel where applicable)
- **Touch targets:** Min 44px (keyboard-focused UX)
- **Navigation:** Persistent sidebar or top nav
- **Typography:** 16–18px body
- **Images/Evidence:** Inline preview panels + full-screen modal
- **Tables:** Full-width tables with sorting/filtering

### Desktop (1440px)
- **Priority:** Management dashboards
- **Layout:** Grid-based KPI cards, multi-column tables
- **Touch targets:** Min 44px
- **Navigation:** Persistent sidebar
- **Typography:** 16–18px body
- **Charts:** Full-width or multi-column charts
- **White space:** Generous padding for readability

---

## Responsive component behavior

| Component | Mobile (360) | Tablet (768) | Desktop (1024+) |
| --- | --- | --- | --- |
| **Navigation** | Bottom nav (3–5 items) or hamburger | Sidebar (collapsible) or tabs | Persistent sidebar |
| **Forms** | Single-column, full-width | Single-column, max-width 600px centered | Two-column where appropriate |
| **Tables/Queues** | Card list (vertical stack) | Table (3–5 columns) | Table (5+ columns) |
| **Modals** | Full-screen sheet (bottom-up) | Centered modal (max-width 600px) | Centered modal (max-width 800px) |
| **Images/Evidence** | Thumbnail (tap → full-screen) | Inline preview (tap → modal) | Inline preview (tap → modal or full-screen) |
| **Status banners** | Full-width, top | Full-width, top | Full-width or inline within section |
| **Action buttons** | Bottom-sticky or inline | Inline at form end | Inline at form end |

---

## Figma frame organization

Organize Figma frames by persona and breakpoint:

**Page structure:**
- **06 Operator Mobile** → All OP-* screens at 360px (+ selected 430px variants)
- **07 Supervisor Mobile and Tablet** → All SV-* screens at 430px and 768px
- **08 QA Console** → All QA-* screens at 1024px
- **09 Administration** → All AD-*, AU-*, LD-* screens at 1024px
- **10 Management Dashboard** → All MG-* screens at 1440px

**Frame naming:**
- `{page-number}/{persona}/{screen-id}/{breakpoint}`
- Example: `06/operator/OP-HOME/360`
- Example: `07/supervisor/SV-REV/768`
- Example: `08/qa/QA-VER/1024`

---

## Responsive testing checklist

Before Phase 01C approval:

- [ ] All required frames (✅) designed at specified breakpoints
- [ ] Responsive components (navigation, forms, tables, modals) adapt correctly
- [ ] Touch targets meet minimums (48px general, 56px operator-critical)
- [ ] Typography readable at all breakpoints (min 16px body)
- [ ] Images/evidence scale appropriately
- [ ] Navigation patterns consistent per device class (bottom nav mobile, sidebar desktop)
- [ ] Forms single-column on mobile, max-width centered on tablet, multi-column optional on desktop
- [ ] Tables convert to cards on mobile, multi-column on tablet/desktop
- [ ] Modals full-screen on mobile, centered on tablet/desktop

---

## Next steps

1. Build required frames (✅) per breakpoint in Figma
2. Test responsive component behavior within Figma prototypes
3. Review with stakeholders at each breakpoint
4. Phase 01C approval before implementation

---

**Document status:** Draft pending owner review  
**Approval required before:** Figma high-fidelity build completion  
**Related approval form:** [PHASE_01C_HIGH_FIDELITY_APPROVAL.md](../approvals/PHASE_01C_HIGH_FIDELITY_APPROVAL.md)
