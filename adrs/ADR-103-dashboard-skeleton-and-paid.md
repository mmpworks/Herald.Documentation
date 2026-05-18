# ADR-103 — Two dashboards (DashboardOSS skeleton + Dashboard.Paid with runtime capability gating)

- **Status:** Proposed
- **Date:** 2026-05-18
- **Stage:** 3
- **Mirrors:** umbrella `herald` (Modules/Dashboard)

## Context

`Modules/Dashboard` today is a Vue 3 / Pinia / Vite SPA. It already
carries runtime license awareness — `LicenseBanner.vue`,
`LicenseStatusPanel.vue`, `useLicenseStatus.js`, `useLicenseBanner.js`.
Steve's vision is one OSS skeleton plus one paid binary that runtime-gates
Pro versus Enterprise features.

Plan v2 designed the carve assuming DashboardOSS might be pointed at
a paid server (and vice versa). Plan v2.2 collapsed that: OSS is
always self-hosted by ServerOSS (ADR-102), so DashboardOSS never has
to discover its server URL and never lands at a paid server. The
mismatched-server screen, the first-load URL config dialog, and the
401 / wrong-tier degradation surface all move to Dashboard.Paid scope.

The IP framing has to stay honest. Paid components ship in the paid
bundle and are visible to browser devtools regardless of which
capabilities the runtime advertises. The capability list gates UX
politely; it does not protect IP. IP protection happens server-side.

## Decision

### 1. Boundary — what lives in DashboardOSS

- `components/pipeline/*` and `components/sinkconfig/*` carve
  mechanically. Nancy verified: zero `tenant | RBAC | admin | replay |
  PluginTrust | oidc` references.
- `App.vue`, `AppHeader.vue`, `stores/herald.js`, `composables/useAuth.js`
  are **chokepoints requiring designed seams, not file copies**. Nancy
  owns the seam design as a Stage 3 sub-deliverable — see ADR-103.1.
- Live log viewer needs an OSS variant (no `useAuth` import). Clean
  separation; both variants honor `[[feedback_eventsource_onerror_close]]`.
- License banner sourced from `/api/system/license`. The OSS payload
  `{ edition, metaItems: [] }` is a structural subset of the paid
  payload — paid extends; banner degradation works in either direction.
- Theme, font, and preferences (`useTheme.js`, `useFontScale.js`,
  `PreferencesPopup.vue`) — straight copy.

### 2. What stays paid

Tenant switcher, RBAC user / role admin UI, replay browser,
plugin-trust UI, OAuth / OIDC login flow, compliance / audit panels,
and the raw-JSON pipeline editor (gated by the `pipeline-edit-raw-json`
capability key).

### 3. License-token gating: runtime, server-driven capability list

Build-time feature flags would require two npm builds; runtime gating
keeps one paid bundle.

- Dashboard.Paid extends the OSS skeleton Vue app at build time via
  additive imports. **Working assumption per Nancy's Vite spike:
  `import.meta.glob` over a `paid-components/` directory present only
  in the paid repo (option B).** Pinned to ADR-103.1 contingent on
  the Stage -1 30-minute verification.
- At runtime, the SPA calls `GET /api/system/capabilities`. Paid views
  register behind a capability key; routes and menu entries render
  only if the capability is present.
- OSS skeleton ships a stub `useCapabilities.js` returning `[]`;
  paid-mounted components degrade to "not available."

### 4. Capability key list (initial)

- `pipeline-edit` — advertised on every tier (ServerOSS, Pro,
  Enterprise). Gates the builder-shape pipeline editor view.
- `pipeline-edit-raw-json` — advertised on Pro and Enterprise only.
  Gates the raw-JSON pipeline editor view. This is the dashboard
  reflection of the ADR-102 endpoint-input gradient: the dashboard
  surfaces what the server accepts.

Per the IP-honesty stance below, the capability key gates UX. The
server-side enforcement is the input validation on
`PUT /api/pipelines/{name}`, not the capability list.

### 5. IP honesty

Paid components ship in the paid bundle and are visible to browser
devtools regardless of capability state. **The capability list
enforces UX politeness, not IP. IP protection happens server-side:
paid endpoints reject unauthorized requests.** The ADR says this
plainly so reviewers do not form the wrong mental model. Adopting
this framing has zero cost — the architecture is already what it is.

### 6. OSS skeleton hosting contract

The OSS skeleton declares **minimal hosting shape**: capability key
namespace conventions, the registration protocol (what
`paid-components/index.js` must export), Vue plugin slot names. The
OSS skeleton does **not** know which paid components will load, but
it does declare the shape of "a thing that loads." That is IP-clean
and accurate — it is the contract a third-party Vue plugin could
target without revealing what we plug into it.

### 7. Bundle / build pipeline and versioning

Dashboard.Paid consumes the OSS skeleton as an npm dependency
(`@mmpworks/herald-dashboard-oss`) published from the OSS repo.
**Version-range pinning:** paid pins `^X.Y.Z` of OSS. OSS ships
ahead independently. Paid optionally bumps the floor when it wants
new capabilities. The Plan v1 idea of a lockstep
`release-dashboard-pair.sh` is rejected as the wrong default.

### 8. DashboardOSS / paid-server scenarios — moved to paid

Plan v2 introduced `MismatchedServerScreen.vue` for the case where
DashboardOSS gets pointed at a paid server. Plan v2.2 dropped it
from OSS scope — same-origin hosting means OSS can't be pointed at
a different server. The screen, the first-load URL config dialog,
and the 401 / unreachable / wrong-tier capability-degradation
scenarios all move to Dashboard.Paid surface. If the same-origin
server isn't responding, the browser shows its own connection-failed
page before the SPA boots.

`useCapabilities` still returns `[]` for OSS and the stub stays for
forward-compat. The capability degradation scenarios that remain in
OSS scope are component-mount-without-capability and capability fetch
200-but-empty.

### 9. prefers-reduced-motion

`prefers-reduced-motion` is not honored anywhere in the dashboard
today. Stage 3 seeds the discipline: every new component in
DashboardOSS honors `prefers-reduced-motion`. Existing components
migrated to DashboardOSS get the audit pass. Nancy owns. Documented
in the DashboardOSS contributor guide.

### 10. wwwroot copy in cheat-mode

`cheat-mode.ps1` and `cheat-mode.sh` gain a `--dashboard oss|paid`
CLI flag with edition-default fallback (matches the existing
`--edition` flag pattern). Max specs and ships.

### 11. Release workflow as GitHub Actions

The OSS skeleton publish plus the paid version-range floor bump
happen in `.github/workflows/dashboard-release.yml` rather than a
bash script — observability over scripting convenience.

## Alternatives considered

### Build-time feature flags

Two npm builds, one for OSS and one for paid, gated by environment
flags. **Rejected** — doubles the build matrix, doubles the QA
surface, and makes a runtime tier upgrade impossible without
redeploying the bundle. Runtime gating against a server-driven
capability list keeps one paid bundle.

### Server-side rendering of capability-gated views

Render the dashboard server-side and omit paid components from the
HTML entirely. **Rejected** — the OSS skeleton is a Vue SPA; SSR is
a separate framework decision that this ADR is not the place to
make. The IP-honesty framing makes SSR moot: bundle visibility was
never the IP control anyway.

### Lockstep release of OSS skeleton + Dashboard.Paid

Plan v1's `release-dashboard-pair.sh`. **Rejected.** Version-range
pinning lets OSS ship ahead independently and lets paid bump the
floor only when it wants new capabilities. The lockstep release
couples the two cadences for no operational gain.

## Consequences

**Positive.** One paid bundle. OSS skeleton stays small and
Composable. Capability list is server-authoritative. Version-range
pinning means OSS releases do not gate on paid coordination.

**Negative.** Stage 3 carries DashboardOSS tests, capability-degradation
tests, Vitest scaffolding, the `prefers-reduced-motion` audit, and
Nancy's ADR-103.1 spike. **2-3 weeks does not absorb this. Stage 3
lengthened to 3-4 weeks.** Test surface shift per v2.2: ServerOSS
loses CORS variation tests; Dashboard.Paid gains URL config dialog,
MismatchedServerScreen, CORS preflight, credentialed-origin, and
capability 401 / wrong-tier degradation tests.

R3 (Vite composition mechanism) softens after Stage -1 spike — the
DashboardOSS first-load shape collapsed with v2.2's same-origin
decision, so the spike is smaller.

## Quick picture

> Imagine a museum that runs a public gallery (free admission) and
> a members-only gallery (paid). The public gallery has the same
> floor plan and the same coat check; the members-only gallery adds
> new rooms behind a member-only door. We don't build two museums.
> We build one museum and the door reads the membership card. The
> dashboard is the museum; the capability list is the membership
> card. The paid rooms are still on the floor plan a curious visitor
> might trace — but the door is what controls access, and the door
> is server-side.

## Rationale tied to CUPID + DRY

Runtime capability gating is the CUPID *Composable* call. The OSS
skeleton declares a hosting contract; Dashboard.Paid composes
against it as a Vue plugin. The skeleton has no knowledge of paid
components; the paid components have no knowledge of the skeleton's
private state. Both sides change independently as long as the
contract holds.

The decision also removes a near-DRY violation that build-time
feature flags would have introduced: every component would have
needed `if (FEATURE_PRO)` branches, scattered across the bundle.
Runtime gating concentrates the "is this capability available?"
check in one place (`useCapabilities`) and every consumer asks
the same composable.

## References

- Plan v2 ADR-103 (original design)
- Plan v2.1 §3 (`pipeline-edit-raw-json` capability key)
- Plan v2.2 §ADR-103 (first-load dialog + MismatchedServerScreen
  moved to paid)
- ADR-103.1 (build-time composition mechanism)
- ADR-102 (same-origin hosting decision)
- ADR-105 (cross-origin dashboard hosting as paid feature)
- `[[feedback_eventsource_onerror_close]]`
- `[[feedback_localstorage_tab_namespace]]`
