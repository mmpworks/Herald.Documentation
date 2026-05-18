# ADR-101 — Herald.RestApi packages split across Apache 2.0 and closed-IP

- **Status:** Proposed
- **Date:** 2026-05-18
- **Stage:** 1
- **Mirrors:** `Herald.RestApi`

## Context

`E:\dev\Herald.RestApi\` today ships nine packages under one solution.
Per the locked naming rule, every one of them stays under the
`MMP.Herald.*` vendor prefix — these are MMPWorks-authored intermediates
that customers pull transitively via `Herald.Pro` or `Herald.Enterprise`,
not front-door packages anyone types into `dotnet add package`. The
licensing axis (Apache 2.0 vs proprietary) is signaled per-csproj via
`<PackageLicenseExpression>`, not in the package ID.

Stage 2 of the vertical split needs `Herald.ServerOSS` to consume the
OSS contracts and host packages as PackageReferences. That requires
the contracts surface to be unambiguously OSS, and the auth-aware
helpers to be unambiguously paid, with no source-side leakage between
them.

Plan v2 framed this as a 4-OSS / 4-paid split. Plan v2.1 refined it
in two ways. First, Steve closed the Conformance OSS audit by deciding
Conformance is paid — third-party server implementations get Contracts
plus generic Testing and write their own verification. Second, the
Testing concept itself splits: generic helpers are OSS, auth-aware
helpers move to a new `Testing.Commercial` package. The license line
runs through the middle of "testing," not between testing and
conformance.

## Decision

### Package matrix (3 OSS + 6 paid)

| Package | License | Notes |
|---|---|---|
| `MMP.Herald.RestApi.Contracts` | Apache 2.0 | The contracts surface. Unchanged. |
| `MMP.Herald.RestApi.Host` | Apache 2.0 | The hosting primitives. Unchanged. |
| `MMP.Herald.RestApi.Contracts.Testing` | Apache 2.0 | **Scope tightened.** Generic helpers only: fake HTTP clients, request-builder utilities, response-shape assertion helpers for the OSS Contracts surface. No auth concepts. No multi-tenant. No RBAC. |
| `MMP.Herald.RestApi.Contracts.Testing.Commercial` | paid | **New package.** Auth-aware test helpers — JWT bearer mocks, RBAC role fixtures, tenant-context helpers, Enterprise response-shape assertions. Catches anything that would otherwise leak into the OSS Testing package. |
| `MMP.Herald.RestApi.Contracts.Conformance` | paid | **Moved to paid.** Steve's call. Third-party implementations write their own verification against the OSS Contracts surface. |
| `MMP.Herald.RestApi.Auth.Bearer` | paid | JWT bearer middleware. Unchanged. |
| `MMP.Herald.RestApi.Contracts.Enterprise` | paid | Enterprise contract additions. Unchanged. |
| `MMP.Herald.RestApi.Contracts.Enterprise.Testing` | paid | Enterprise testing helpers. Unchanged. |
| `MMP.Herald.RestApi.Contracts.Enterprise.Conformance` | paid | Enterprise conformance suite. Unchanged. |

### Decision points

1. **Single repo, mixed licensing.** `E:\dev\Herald.RestApi\` stays one
   repo with one solution. Per-csproj license metadata is the only
   signal that distinguishes OSS from paid; the repo's root LICENSE
   covers the Apache 2.0 packages, NOTICE clarifies the mixed posture.
2. **The OSS / closed-IP line falls inside the Testing concept.**
   Generic helpers live OSS so third-party server authors can write
   their own verification suites. Auth-aware and Enterprise-aware
   helpers live in `Testing.Commercial` because they would otherwise
   surface JWT, RBAC, and tenant shapes that belong to the paid
   product. This is the load-bearing call of the v2.1 amendment.
3. **Conformance is paid.** Third-party server implementations get
   `Contracts` and `Contracts.Testing` and assemble their own
   verification. The Conformance package's test names enumerate
   product behaviors that include Enterprise spec; keeping it paid
   removes the leakage surface entirely. R19 closes.
4. **Friend-grant audit — tightened.** Pre-commit grep across all
   nine csproj for `InternalsVisibleTo` and across all source files
   for `[assembly: InternalsVisibleTo]`. Any grant from an
   OSS-promoted package to a closed-IP package is a violation; such
   grants are inverted or removed. The audit must specifically verify
   that no symbol in `Contracts.Testing` reaches into anything
   `Contracts.Enterprise` or `Auth.Bearer` exposes. Any helper that
   does, moves to `Testing.Commercial`.
5. **Stage 2 consumption contract.** Herald.ServerOSS PackageReferences
   `MMP.Herald.RestApi.Contracts` and `MMP.Herald.RestApi.Host` from
   nuget.org. Stage 1 publish must precede Stage 2 first build by at
   least 60 minutes — outside contributors and our own CI runners
   fail on stale feed otherwise (R16). The Stage 2 CI lane carries a
   stale-feed retry guard.

## Consequences

**Positive.** Herald.ServerOSS ships the day Stage 1 closes without
needing a Conformance audit on the critical path. Third-party server
implementations have a clean OSS surface to build against — Contracts
plus generic Testing — and can publish their own conformance suites
without paying for ours. The Testing-package split catches the exact
leakage the old 4+4 framing left ambiguous.

**Negative.** Heather writes two README headers and a per-package
license matrix. The new `Testing.Commercial` package adds one csproj
to the solution and a new CI lane. R22 names the source-drift risk
between `Testing` and `Testing.Commercial`: `Testing.Commercial`
PackageReferences `Testing` at a pinned major, and CI runs a smoke
build of `Testing.Commercial` against the latest `Testing` minor and
fails on type-load errors.

R19 (Conformance IP leakage) closes with this decision. The remaining
Stage 1 risks are R16 (NuGet propagation timing) and R22 (the new
testing-package drift watch).

## Quick picture

> Picture a hardware store that sells both lumber and prebuilt kits.
> Anyone walking in can buy lumber and build their own shed. The
> prebuilt kits — with custom hinges, latches, and locking mechanisms
> — sit behind the counter. The store's testing department writes
> two manuals: one for the lumber ("here's how to measure a board, how
> to check for warp") and a separate one for the kits ("here's how to
> verify the latch engages, how to test the lock"). Our split mirrors
> that. The OSS Testing package is the lumber manual; `Testing.Commercial`
> is the kit manual.

## Rationale tied to CUPID + DRY

The Testing-package split is a CUPID *Composable* call. Two packages
with disjoint dependency closures (`Testing` reaches only `Contracts`;
`Testing.Commercial` reaches `Contracts` plus `Auth.Bearer` plus
`Contracts.Enterprise`) let consumers pull exactly what they need. A
third-party OSS server consumer never accidentally pulls JWT machinery.

The decision also avoids a DRY violation that the v2 framing
masked: had we kept a single Testing package with conditional helpers,
the auth-aware helper code would have either lived in OSS (leaking
paid shape) or been duplicated across `Testing` and a private internal
copy. Splitting the package removes the duplication question entirely.

## References

- Plan v2 ADR-101 (original 4+4 framing — superseded)
- Plan v2.1 §1 (Testing-package split, Conformance moved to paid)
- Plan v2 risk matrix entries R16, R19 (closed), R22 (new)
- `[[project_herald_package_naming_convention]]`
- `[[project_rest_api_scope]]`
