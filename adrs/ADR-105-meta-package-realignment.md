# ADR-105 — Post-reorg shape of Herald.Pro, Herald.Enterprise meta-packages plus license-tier MSBuild mechanism

- **Status:** Proposed
- **Date:** 2026-05-18
- **Stage:** 5
- **Mirrors:** umbrella `herald`, `Herald.RestApi`

## Context

Pre-reorg `Herald.Pro` and `Herald.Enterprise` meta-packages exist.
After Stages 1 through 4 the dependency closures change substantially:
RestApi splits 3 OSS / 6 paid, three new server binaries appear,
DashboardOSS / Dashboard.Paid split, Sci lifts to a standalone repo.

The Stage 5 meta-package realignment locks the closures and ships
the MSBuild mechanics that v1 hand-waved:

- A license-tier warning mechanism (consuming project's license token
  doesn't match the meta's claimed tier).
- A conflict marker if both `Herald.Pro` and `Herald.Enterprise` are
  installed in the same project.

Plan v2.2 added one feature line: cross-origin dashboard hosting is
paid-tier only, advertised in both meta-package descriptions.

## Decision

### 1. Herald.Pro transitive closure (post-Stage 5)

- `Herald.OSS`
- `MMP.Herald.RestApi.Contracts` (OSS post Stage 1)
- `MMP.Herald.RestApi.Host` (OSS post Stage 1)
- `MMP.Herald.RestApi.Auth.Bearer` (paid)
- `MMP.Herald.Server.Pro` (paid)
- `MMP.Herald.Server.Paid.Common` (paid, transitive from Server.Pro)
- `MMP.Herald.Dashboard.Paid` (paid)
- Paid addons: `MMP.Herald.Observability`, `MMP.Herald.LogAnalysis`,
  `MMP.Herald.LogQuality`, `MMP.Herald.Receivers.Otlp`
- `MMP.Licensing` source-linked (NOT a NuGet dep — see ADR-100)
- **Excludes:** `MMP.Herald.RestApi.Contracts.Enterprise` trio

### 2. Herald.Enterprise = Pro closure plus Enterprise additions

- Everything in Pro **except** `MMP.Herald.Server.Pro` (replaced by
  Enterprise)
- `MMP.Herald.Server.Enterprise` (paid)
- `MMP.Herald.RestApi.Contracts.Enterprise` trio (Contracts,
  Testing, Conformance)
- `MMP.Herald.Compliance` (renamed to `MMP.Herald.Audit` in Stage 6
  — see ADR-106)

### 3. OSS deployment recipe — no meta-package

OSS users install three packages directly, one command each:

```
dotnet add package Herald.OSS
dotnet add package Herald.ServerOSS
dotnet add package Herald.DashboardOSS
```

No `Herald.OSS.All` meta. Escalation #2 from v1 closed: deferred to
Steve, default no. Transitive resolution from `Herald.ServerOSS` does
most of the work (per ADR-102.5, the dashboard asset package is a
transitive dep of ServerOSS) — the three-command install is the
documented path for users who want explicit control.

### 4. License-tier MSBuild warning mechanism

Per-paid-package `build/Herald.Pro.targets` payload, shipped via:

```xml
<None Include="build\Herald.Pro.targets" Pack="true" PackagePath="build\" />
```

MSBuild property names cannot contain dots — the sidecar property
is `HeraldLicensePath`, not `Herald.License.Path`. The consuming
project ships:

- The JWT license token at the path `HeraldLicensePath` points to.
- A sidecar `<license>.license.json` alongside the JWT, carrying the
  parsed tier and expiry. **MSBuild cannot parse JWT at build time;**
  the sidecar is the parsed form.

The targets file reads the sidecar. Mismatch (consumer ships a Pro
sidecar but installs `Herald.Enterprise`) produces an MSBuild warning.
Sidecar generation is documented in customer onboarding.

### 5. Pro-vs-Enterprise conflict marker

Each meta ships `build/` targets defining a property:

```
HeraldServerTierClaim=Pro     (Herald.Pro)
HeraldServerTierClaim=Enterprise  (Herald.Enterprise)
```

If both metas are installed, MSBuild evaluates both targets. A second
target setting `HeraldServerTierClaim` to a different value produces
an MSBuild **error** via an `<Error>` task gated on a condition
check. Without this, `dotnet restore` happily installs both, both
module initializers run, first-write-wins on `SetEdition` silently
picks one. Echo writes a CI test that installs both metas in a probe
project and asserts the MSBuild error fires.

### 6. Cross-origin dashboard hosting — paid tier upsell

Add to both `Herald.Pro` and `Herald.Enterprise` meta-package
descriptions:

> Includes cross-origin dashboard hosting support (configurable CORS
> plus a separately-hosted SPA option).

This is the **tier upsell narrative** from the same-origin OSS
hosting decision (ADR-102). Heather quotes it on the public-docs
server-comparison page; the exact wording lives here as the canonical.

### 7. Naming convention reconciliation

Per the locked rule (`[[project_herald_package_naming_convention]]`):

- **Customer-facing top-level:** `Herald.OSS`, `Herald.ServerOSS`,
  `Herald.DashboardOSS`, `Herald.Sci`, `Herald.Pro`, `Herald.Enterprise`
  (bare prefix).
- **MMPWorks-authored intermediates:** `MMP.Herald.<Component>.<Tier?>`
  (vendor prefix, tier in suffix or via csproj license metadata).
- **Third-party sinks:** `<Vendor>.Herald.Sinks.<Name>`.

### 8. Stage 6 carry-through

Stage 5 ships with `MMP.Herald.Compliance` in the Enterprise closure.
Stage 6 renames the package to `MMP.Herald.Audit`; a transitional
`MMP.Herald.Compliance` shim stays published with deprecation metadata
for one release cycle. **Docs use Audit wording from Stage 1 forward**
— Stage 6 is a package rename, not a doc migration. See ADR-106.

## Consequences

**Positive.** Clear tier-to-package mapping. Conflict marker is a
real MSBuild primitive, not a wish. The sidecar `.license.json`
approach acknowledges that MSBuild and JWT live in different worlds
and bridges them honestly.

**Negative.** Sidecar `.license.json` is a customer-visible artifact
that requires onboarding docs. Heather produces the customer
decision flowchart ("which meta-package do I want?") and the
sidecar-format reference page.

## Quick picture

> Picture buying a season ticket to a theatre. The ticket says "Pro
> tier" or "Enterprise tier." The usher checks the ticket against
> the seat — if you have a Pro ticket and you sit in an Enterprise
> seat, the usher politely flags it. If you somehow have both
> tickets, the gate doesn't let you through at all — that's the
> conflict marker. The sidecar `.license.json` is the ticket itself
> in a form the usher can read without needing a cryptographic
> decoder ring at the door.

## Rationale tied to CUPID + DRY

The meta-package closures are CUPID *Domain-based*: customers reason
about tiers (`Pro`, `Enterprise`), not about individual packages
(`MMP.Herald.Server.Pro` plus `MMP.Herald.RestApi.Auth.Bearer` plus
six addons). The meta-package is the domain-level install target;
the package list inside it is implementation.

The MSBuild conflict marker removes a near-DRY ambiguity: without
it, the system has two implicit "which tier am I?" answers (the two
installed metas) and `SetEdition` silently picks one. The conflict
marker forces the question to be answered at install time.

## References

- Plan v2 ADR-105
- Plan v2.2 §ADR-105 (cross-origin dashboard hosting line)
- ADR-100 (`MMP.Licensing` source-linked, not packaged)
- ADR-102 (server binaries)
- ADR-103 (dashboards)
- ADR-106 (Compliance to Audit rename, deferred)
- `[[project_herald_package_naming_convention]]`
- `[[project_pro_sku_lineup_locked]]`
