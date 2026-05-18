# ADR-102 — Three server binaries (ServerOSS / Server.Pro / Server.Enterprise) plus shared paid scaffolding

- **Status:** Proposed
- **Date:** 2026-05-18
- **Stage:** 2
- **Mirrors:** umbrella `herald` (three new server projects under `Modules/`)

## Context

`Modules/Server` today is single-binary: multi-tenant, JWT-authenticated
admin server with full RBAC and the Enterprise feature surface.
Steve's vision is three distinct binaries instead of one:

- **Herald.ServerOSS** — Apache 2.0, single-tenant, no JWT, no admin.
  A reference server you can run with `dotnet add package` and one
  command. The OSS dashboard's API contract.
- **Herald.Server.Pro** (NuGet ID `MMP.Herald.Server.Pro`) — single-tenant,
  JWT-authenticated, single-org RBAC, paid feature surface.
- **Herald.Server.Enterprise** (NuGet ID `MMP.Herald.Server.Enterprise`) —
  today's `Modules/Server`, renamed. Multi-tenant, full admin, full
  replay, cluster coordination.

The vision rejects a shared-binary-with-license-token approach because
that puts paid IP into the OSS binary closure. The license shape can
gate UX, but the bits on disk still ship with the binary; a single
shared binary would expose Pro and Enterprise mechanisms to anyone
running the OSS tier.

Plan v1 deferred a `Paid.Common` extraction to a Stage 5 amendment.
Plan v2 brings it in from Stage 2 start because three Program.cs plus
three appsettings plus three Dockerfiles is duplication before any
business logic.

Plan v2.2 simplified further: ServerOSS always serves DashboardOSS
from its own `wwwroot/` — same origin, no CORS, no SPA URL discovery,
no first-load config dialog. Cross-origin dashboard hosting becomes
a paid-tier feature. The OSS scope shrinks accordingly.

## Decision

### 1. Three csproj, three Program.cs, plus one shared paid scaffolding package

Plus **one `MMP.Herald.Server.Paid.Common`** internal package carrying:

- Shared Program.cs scaffolding (host builder, scope policies, OTLP
  gRPC kestrel config)
- Shared `appsettings.json` defaults (overridden per-binary)
- Shared Dockerfile base layer
- Shared `IClusterCoordination` no-op for Pro (Enterprise overrides)
- **Not shared:** endpoint mapping (each binary maps its own),
  `HeraldTenantContext` (no-op for Pro, real for Enterprise), license
  validation (per-tier).

ServerOSS does **not** depend on `Paid.Common`. That is the IP wall.
ServerOSS reimplements its tiny shell from scratch.

### 2. Herald.ServerOSS minimum surface — 8 endpoints

ServerOSS publishes seven business endpoints plus `/health`. The
scoped-group convention (read/write/admin route groups) does **not**
survive into ServerOSS — there is no auth, so no scope split.
ServerOSS uses one ungated route group. The per-line keep/delete
decision against the current 2,530-line endpoint mapper is **ADR-102.1**.

The endpoint set:

- `GET /api/pipelines` — list configured pipelines
- `GET /api/pipelines/{name}` — read one pipeline (state + components)
- `PUT /api/pipelines/{name}` — modify a pipeline
- `POST /api/sinks` — register a sink
- `GET /api/sinks` — list registered sinks
- `GET /api/system/license` — returns `{ edition: "Community", metaItems: [] }`
- `GET /api/system/capabilities` — returns `[]`
- `GET /health` — kept verbatim

### 3. Per-edition request-body shape on PUT /api/pipelines/{name}

**OSS / ServerOSS** accepts **builder-shape JSON only**. The request
body is a `QuickLogBuilder`-shaped description
(`{ sinks: [...], processors: [...], strategy: ... }`). Server
validates against the builder's schema, runs
`QuickLogBuilder.BuildJsonConfig`, applies the result to the kernel.
Raw canonical-JSON payloads are rejected with a clear error shape:

```json
{
  "error": "Raw JSON pipeline editing requires Herald.Server.Pro or higher",
  "documentation": "https://..."
}
```

**Pro / Enterprise** accepts builder-shape OR raw canonical JSON.
Content-type signals which; a sibling endpoint
`PUT /api/pipelines/{name}/json` accepts raw only. The raw surface
lets paid customers express things the builder doesn't surface —
custom processors, hand-tuned strategies, edge-case configurations
the builder validation rejects.

Same kernel, same canonical JSON downstream. The HTTP-shape distinction
is purely **what request shapes the endpoint accepts**, gated by
edition. The architecture already supports this split (the builder
produces JSON, JSON drives construction); the ADR names where the
gate sits at the HTTP layer.

**The OSS/Pro endpoint-input gradient is the load-bearing product
differentiator between server tiers.** ServerOSS is the safe, validated
front door. Pro+ unlocks the full kernel surface. The
product-narrative paragraph in §"Canonical product wording" below
must appear (verbatim or substantially) in ADR-102 readers, the
public-docs server-comparison page, and the `Herald.ServerOSS` README.

### 4. ServerOSS always self-hosts DashboardOSS

**Dropped** in v2.2:

- The `ServeStaticDashboard` config flag — ServerOSS always serves
  the bundle. No toggle, no mode.
- The `AllowedOrigins` config from OSS — same-origin removes the
  CORS surface entirely.
- The loud "CORS permissive" startup banner.

**Replaced** by a single-line startup banner:

> Herald.ServerOSS — no authentication; reverse-proxy expected for
> production exposure.

That is the OSS deployment expectation, stated once at startup. The
HTTP middleware stack is concrete: `MapStaticAssets()` -> API endpoint
mappings -> `MapFallbackToFile("index.html")` for SPA deep-link
refresh. Standard ASP.NET Core SPA hosting; nothing exotic. Glenn
needs the shape named so the carve is mechanical.

Packaging composition (four-package vs fat NuGet) is **ADR-102.5**.

### 5. Herald.Server.Pro shape

ServerOSS endpoint set plus:

- JWT bearer middleware (`MMP.Herald.RestApi.Auth.Bearer`)
- Single-org RBAC
- `Modules/Server/ManagementApi/PluginTrust/*` endpoints
- Real `/api/system/license` that validates the Pro license token at
  startup and returns `{ edition: "Pro", metaItems: [...] }`
- `/api/system/capabilities` returns the Pro capability list,
  including `pipeline-edit-raw-json`

Multi-tenant code paths excluded; `HeraldTenantContext` is a no-op
via `Paid.Common`.

### 6. Herald.Server.Enterprise = today's Modules/Server, renamed

NuGet ID `MMP.Herald.Server.Enterprise`. Multi-tenant, full RBAC,
full admin, full replay, full plugin-trust, OTLP ingest, cluster
coordination. Project file rename:

```
Modules/Server/Herald.Server.csproj
  -> Modules/Herald.Server.Enterprise/Herald.Server.Enterprise.csproj
```

**No transitional shim package.** `Herald.Server` was never published;
zero installs exist outside the umbrella. The rename is free.

### 7. Carve order (mechanical)

1. Create `MMP.Herald.Server.Paid.Common` first, with the shared
   scaffolding lifted from current `Modules/Server`.
2. Copy `Modules/Server/` to `Modules/Herald.ServerOSS/`.
3. Strip ServerOSS per ADR-102.1.
4. Copy `Modules/Server/` to `Modules/Herald.Server.Pro/`. Strip
   multi-tenant code paths; depend on `Paid.Common`.
5. Rename `Modules/Server/Herald.Server.csproj` ->
   `Modules/Herald.Server.Enterprise/Herald.Server.Enterprise.csproj`;
   add dep on `Paid.Common`. Delete `Modules/Server/` in the same
   commit.
6. Update `build.sh` curated loop per the per-stage `HERALD_ALL_PROJECTS`
   diff (10 -> 13 net).
7. Echo barrier-fixture coverage (R20) lands in the ServerOSS test
   project before Stage 2 close.

### 8. Recurring re-convergence step (drift audit)

Stage 2 produces three diverging codebases. To prevent first-CVE
re-forking, a **quarterly drift audit** runs `diff` across ServerOSS,
Server.Pro, and Server.Enterprise on a published delta-budget. If
duplication grows above the budget, scaffolding from `Paid.Common`
absorbs the drift. Owner: Richard. First audit: Stage 5 close + 90
days. Audit calendar at `docs/cadences/server-drift-audit.md`.

### 9. Naming reconciliation

`Herald.ServerOSS` versus `MMP.Herald.Server.Pro` is not an
inconsistency — it is the naming rule:

- OSS top-level customer-facing install targets carry the bare
  `Herald.*` prefix with `OSS` as a suffix.
- Paid binaries are intermediate vendor-namespace packages reached
  via the meta-package — `MMP.Herald.Server.<Tier>`.

Heather documents the rule in customer onboarding.

### 10. Runtime config-key migration

`MMP.Herald.Server.Enterprise` reads BOTH the legacy `Herald.Server`
configuration section and the new `Herald.Server.Enterprise` section.
Legacy-key detection emits a one-time startup warning. The dual-read
removes after two release cycles. This covers R15.

## Alternatives considered

### Shared binary with license-token gating

A single `Herald.Server` binary whose feature surface activates from
the license token at startup. **Rejected** — the bits ship with the
binary regardless of which feature flags are flipped. Anyone running
the OSS tier ends up with Pro and Enterprise machinery on disk. The
IP wall has to be a binary boundary, not a flag boundary.

### Deferring Paid.Common to Stage 5

Plan v1 carried this. **Rejected** by v2 — three Program.cs plus
three appsettings plus three Dockerfiles is duplication before any
business logic. Standing up the shared scaffolding from Stage 2 start
costs one extra csproj and saves the deferred refactor.

### Keep ServerOSS's CORS surface configurable

Plan v2 specified a permissive-by-default CORS posture for ServerOSS.
**Replaced** in v2.2 by same-origin hosting. The CORS attack surface
collapses entirely. Cross-origin dashboard hosting becomes a paid-tier
feature (ADR-105).

## Consequences

**Positive.** OSS users get a clean reference server without paid
middleware. Paid binaries share scaffolding via `Paid.Common` so
first-CVE updates touch one Program.cs instead of two. Each binary
stays Composable. The OSS deployment story collapses to one line:
"run `Herald.ServerOSS` on a port, open the port in a browser."

**Negative.** Four csprojs total (three binaries plus `Paid.Common`),
three CI lanes. Quarterly drift audit calendar cost. **Cognitive cost
in marketing** — "which server do I want?" — Heather produces a
decision flowchart. The CUPID-Composable trade is explicitly accepted:
we duplicate Program.cs across three binaries because the alternative
is paid IP in the OSS closure. The trade is named here so readers
learn CUPID by meeting it.

## Quick picture

> Imagine a kitchen that needs to serve three menus — diner, bistro,
> and fine-dining. You could try one kitchen that switches menus by
> flipping a sign on the door, but the bistro's truffle station and
> the fine-dining sommelier's cellar still sit in the room. Or you
> could build three kitchens that share the same loading dock, the
> same dishwasher pit, and the same walk-in for the staples. The
> shared infrastructure goes in `Paid.Common`; the three menus are
> the three Program.cs files. The diner gets its own clean room
> without truffles or wine on the premises.

## Canonical product wording

The following paragraph is the canonical product framing for the
ServerOSS / Pro / Enterprise gradient. It must appear (verbatim or
substantially) in this ADR, the public-docs server-comparison page,
and the `Herald.ServerOSS` README:

> Herald.ServerOSS exposes the canonical Herald pipeline over REST
> in `QuickLogBuilder` shape — the same fluent, validated builder API
> customers know from the SDK, served as endpoint input. Pro and
> Enterprise add the raw-JSON manipulation surface for customers who
> need to express pipeline shapes the builder doesn't expose (custom
> processors, hand-tuned strategy chains, edge-case configurations).
> Both tiers drive the same kernel; the OSS tier is the safe,
> validated front door, and the paid tiers unlock the full kernel
> surface.

## Rationale tied to CUPID + DRY

`MMP.Herald.Server.Paid.Common` is the CUPID *Composable* call. The
two paid binaries compose against the shared scaffolding without
inheriting from a common base class; Program.cs in each binary calls
into `Paid.Common` for the parts it shares and writes the parts it
doesn't. The shared scaffolding stays small and the binaries stay
independently runnable.

The decision also names a DRY trade-off honestly: ServerOSS reimplements
its tiny shell from scratch rather than depending on `Paid.Common`,
because the alternative is paid IP in the OSS closure. The duplication
is intentional and bounded — ServerOSS's shell is ~150 LoC against
`Paid.Common`'s scaffolding. Naming the trade in the ADR is more
honest than papering over it with a comment in Program.cs.

## References

- Plan v2 ADR-102 (Paid.Common from start)
- Plan v2.1 §2 (endpoint-input gradient on PUT /api/pipelines)
- Plan v2.2 §ADR-102 (same-origin hosting, CORS dropped from OSS)
- ADR-102.1 (endpoint mapper carve)
- ADR-102.5 (packaging composition)
- ADR-103 (DashboardOSS hosting)
- Plan v2 risk matrix entries R9, R15, R20, R21
- `[[feedback_json_is_source_of_truth]]`
- `[[project_herald_package_naming_convention]]`
