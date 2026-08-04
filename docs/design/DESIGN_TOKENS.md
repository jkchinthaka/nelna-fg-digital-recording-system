# Design Tokens — Phase 01B

**Document status:** Proposed token system for design review — not a brand or certification claim  
**Phase:** 01B — Design tokens and component system  
**Last updated:** 2026-08-04  
**Depends on:** Phase 01A approved baseline

This specification defines Figma variables and implementation-facing token names for later Django/Tailwind mapping. It does **not** invent Nelna operational limits or claim production UI readiness. Hex values are **PROPOSED** until design review.

Visual direction: operational factory-floor clarity — cool neutral surfaces, strong semantic status, high contrast, no decorative purple/indigo marketing theme, no cream/terracotta editorial theme.

---

## Token layers

| Layer | Purpose |
| --- | --- |
| Primitive | Raw palette, type sizes, space scale |
| Semantic | Role-based usage (text, surface, border, status, focus) |
| Component | Optional aliases bound inside components |

Figma: create variable collections `primitive`, `semantic` (mode: Light only for 01B; Dark deferred).

---

## Colour — primitives (PROPOSED)

| Token | Value | Notes |
| --- | --- | --- |
| `color.neutral.0` | `#FFFFFF` | |
| `color.neutral.50` | `#F5F7F8` | App background |
| `color.neutral.100` | `#E8EEF0` | Subtle panels |
| `color.neutral.200` | `#D0DADF` | Borders quiet |
| `color.neutral.300` | `#A8B8C0` | Disabled borders |
| `color.neutral.500` | `#5B6B73` | Secondary text |
| `color.neutral.700` | `#2F3B41` | Body text |
| `color.neutral.900` | `#12181C` | Primary text / icons |
| `color.brand.600` | `#0F6B5C` | Primary actions (teal-green operational) |
| `color.brand.700` | `#0B5347` | Primary pressed |
| `color.brand.100` | `#D8F0EB` | Primary soft fill |
| `color.status.pass.600` | `#1B7A3D` | Pass / success |
| `color.status.pass.100` | `#E4F6EA` | |
| `color.status.warn.700` | `#8A5A00` | Warning text (contrast-safe) |
| `color.status.warn.100` | `#FFF3D6` | |
| `color.status.critical.700` | `#9B1C1C` | Critical / fail / blocked |
| `color.status.critical.100` | `#FDE8E8` | |
| `color.status.info.700` | `#1E4F8C` | Informational |
| `color.status.info.100` | `#E7F0FB` | |
| `color.status.sync.700` | `#4A5560` | Offline/sync neutral emphasis |
| `color.status.sync.100` | `#EDF1F3` | |
| `color.focus.ring` | `#0F6B5C` | Visible focus |
| `color.overlay.scrim` | `#12181C99` | Modal scrim (~60%) |

Do not use status colour alone — pair with text + icon + pattern (DES-005).

---

## Colour — semantic (PROPOSED)

| Token | Maps to |
| --- | --- |
| `sem.surface.app` | `neutral.50` |
| `sem.surface.card` | `neutral.0` |
| `sem.surface.muted` | `neutral.100` |
| `sem.text.primary` | `neutral.900` |
| `sem.text.secondary` | `neutral.500` |
| `sem.text.inverse` | `neutral.0` |
| `sem.border.default` | `neutral.200` |
| `sem.border.strong` | `neutral.300` |
| `sem.action.primary.bg` | `brand.600` |
| `sem.action.primary.bg.pressed` | `brand.700` |
| `sem.action.primary.text` | `neutral.0` |
| `sem.action.secondary.bg` | `neutral.0` |
| `sem.action.secondary.border` | `neutral.300` |
| `sem.action.danger.bg` | `status.critical.700` |
| `sem.status.pass.*` | pass primitives |
| `sem.status.warn.*` | warn primitives |
| `sem.status.critical.*` | critical primitives |
| `sem.status.info.*` | info primitives |
| `sem.status.sync.*` | sync primitives |
| `sem.focus.ring` | `focus.ring` |

### Critical / loading-block pattern (non-colour)

| Token / style | Spec |
| --- | --- |
| `pattern.critical.hatch` | 45° diagonal hatch overlay on banner edge |
| `pattern.blocked.stripe` | Alternating strong stripe on LOADING BLOCKED bar |

---

## Typography (PROPOSED)

Sinhala-capable stacks are mandatory for operator UI.

| Token | Value | Use |
| --- | --- | --- |
| `font.family.sans` | `"Noto Sans Sinhala", "Noto Sans", system-ui, sans-serif` | Default UI |
| `font.family.mono` | `"Noto Sans Mono", ui-monospace, monospace` | Codes, IDs, measurements |
| `font.size.100` | 12px | Meta / timestamps |
| `font.size.200` | 14px | Secondary |
| `font.size.300` | 16px | Body default |
| `font.size.400` | 18px | Operator emphasis |
| `font.size.500` | 20px | Section titles (mobile) |
| `font.size.600` | 24px | Page titles |
| `font.size.700` | 28px | Critical banner title |
| `font.weight.regular` | 400 | |
| `font.weight.medium` | 500 | |
| `font.weight.semibold` | 600 | Actions, status |
| `font.weight.bold` | 700 | Critical only |
| `line.height.tight` | 1.25 | Titles |
| `line.height.normal` | 1.45 | Body (Sinhala-friendly) |
| `line.height.relaxed` | 1.6 | Help text |

Licensing: use SIL-licensed Noto (or owner-approved equivalent). Do not embed unlicensed brand fonts.

---

## Spacing (PROPOSED)

4px base scale:

| Token | Value |
| --- | --- |
| `space.0` | 0 |
| `space.1` | 4px |
| `space.2` | 8px |
| `space.3` | 12px |
| `space.4` | 16px |
| `space.5` | 20px |
| `space.6` | 24px |
| `space.8` | 32px |
| `space.10` | 40px |
| `space.12` | 48px |
| `space.14` | 56px |

---

## Sizing — touch and controls (PROPOSED)

| Token | Value | Rule |
| --- | --- | --- |
| `size.touch.min` | 48px | WCAG-oriented minimum |
| `size.touch.operator` | 56px | Recommended primary operator controls |
| `size.icon.sm` | 20px | Inline |
| `size.icon.md` | 24px | Default |
| `size.icon.lg` | 32px | Status / critical |
| `size.input.height` | 48px | Default fields |
| `size.button.height` | 48px | Default; operator primary 56px |

---

## Radius and elevation (PROPOSED)

Operational UI: modest radius; avoid heavy multi-shadow chrome.

| Token | Value |
| --- | --- |
| `radius.sm` | 4px |
| `radius.md` | 8px |
| `radius.lg` | 12px |
| `radius.pill` | 999px | **Avoid** for primary factory actions; reserved for rare chips |
| `elevation.0` | none |
| `elevation.1` | `0 1px 2px rgba(18,24,28,0.08)` |
| `elevation.2` | `0 4px 12px rgba(18,24,28,0.12)` | Modals/sheets only |

---

## Motion (PROPOSED)

| Token | Value | Use |
| --- | --- | --- |
| `motion.fast` | 120ms | Pressed states |
| `motion.normal` | 200ms | Panels |
| `motion.slow` | 320ms | Rare |
| `motion.easing.standard` | cubic-bezier(0.2, 0, 0, 1) | |

Respect `prefers-reduced-motion`: disable non-essential motion.

---

## Breakpoint tokens (align with responsive doc)

| Token | Value (PROPOSED) |
| --- | --- |
| `bp.phone.sm` | 320px |
| `bp.phone.lg` | 390px |
| `bp.tablet` | 600px |
| `bp.laptop` | 1024px |
| `bp.desktop` | 1280px |

---

## Implementation mapping (later phases)

| Design token | Likely CSS / Tailwind approach |
| --- | --- |
| `sem.*` | CSS variables on `:root` |
| Spacing/type | Tailwind theme extension |
| Status | Utility classes + icon components — never colour-only |

Do not commit binary font files without license review.

---

## Open token decisions

| ID | Topic | Status |
| --- | --- | --- |
| TOK-001 | Final brand primary hue vs proposed teal | [DECISION REQUIRED] if brand guidelines exist |
| TOK-002 | Dark mode | Deferred |
| TOK-003 | Exact Sinhala webfont hosting | [DECISION REQUIRED] IT |
| TOK-004 | Compact density mode for desktop admin | Proposed optional later |
