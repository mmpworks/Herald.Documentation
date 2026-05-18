# ADR-100 — Retire Modules/Core in favor of Herald.OSS as canonical upstream

- **Status:** Proposed
- **Date:** 2026-05-18
- **Stage:** 0 (Detour C closure)
- **Mirrors:** umbrella `herald`, `Herald.OSS`

## Context

The umbrella `herald` repo carries `Modules/Core/` — the historical home
of the Herald kernel. The sibling `Herald.OSS` repo holds the same kernel
under Apache 2.0, with an active research lane and the published NuGet
identity. Until now both trees have been kept warm in parallel, and
paid modules under `Modules/` have depended on `Modules/Core` via
ProjectReference.

This is duplication with no upside. Every kernel change has to land
twice. Friend-grants and `InternalsVisibleTo` declarations have to be
mirrored across both trees. Bench numbers drift between the two
because inlining behavior changes when a kernel ships as a package
versus a ProjectReference. The umbrella's curated `--all` loop already
excludes the consumers blocked by the Detour-C divergence; the
exclusions are accumulating and the umbrella build is getting harder
to reason about.

Steve has named Herald.OSS as the canonical kernel going forward.
Stage 0 of the vertical-split plan is the mechanical work that turns
that decision into reality.

## Decision

1. **Herald.OSS is the canonical kernel.** Every paid module in
   `Modules/` repoints its kernel dependency from
   `Modules/Core/Herald.Core.csproj` to a PackageReference on the
   published `Herald.OSS` NuGet identity.
2. **Modules/Core is deleted from the umbrella tree** at the end of
   the Stage 0 shadow window. The delete is its own commit, tagged
   `pre-core-delete` immediately before, so a rollback is a `git
   reset` away if the shadow window missed something.
3. **MMP.Licensing is source-linked, not packaged.** Paid csprojs
   include `MMP.Licensing` source files via MSBuild `<Compile Include>`
   patterns rather than via a NuGet package. There is no internal
   feed. There is no published `MMP.Licensing` package. The source
   tree is organised so the includes are clean.
4. **HeraldEdition + SetEdition land on Herald.OSS.** The sibling adds
   a public `HeraldEdition` enum (`Community`, `Pro`, `Enterprise`,
   `Dev`), a `HeraldVersion.CurrentEdition` accessor defaulting to
   `Community`, and an install hook `HeraldVersion.SetEdition` called
   from paid module initializers. The hook is first-write-wins under
   concurrency.
5. **Two-week shadow window with a real exercise harness.** The
   shadow window is the period between the sibling-repoint commit
   and the `Modules/Core` delete. A daily cron exercises every module
   initializer, every `/api/system/license` response shape (Community
   empty, Pro populated, Enterprise populated), a `SetEdition` race
   fixture under xUnit parallel runner, and a curated umbrella build
   against sibling-as-package. Without the harness, the shadow window
   passes meaninglessly; with it, the window is the gate.
6. **Friend-grant transplant.** Every `[assembly: InternalsVisibleTo]`
   declaration in `Modules/Core` source files migrates to the sibling
   with the public-key qualifier applied. Linked-source MSBuild
   includes that cross project boundaries either become explicit
   PackageReferences or migrate to the new owning csproj. The Stage -1
   audit produces the spreadsheet; Stage 0 applies it.
7. **ApiCompat baselines committed before Stage 0 active work.** The
   Stage -1 prerequisite lays down baselines for `Herald.OSS`,
   `MMP.Herald.RestApi.Contracts`, and `MMP.Herald.RestApi.Host`. The
   Stage 0 exit check diffs against those baselines; surface drift
   surfaces as a CI failure, not a manual review note.

## Consequences

**Positive.** One kernel. One bench floor. One friend-grant inventory.
The umbrella curated loop loses its accumulating exclusion list. Every
paid module rebuilds against the published OSS package the day Stage 0
closes — the package boundary is the contract, and bench drift across
that boundary is the signal we want.

**Negative.** `Modules/Core` deletion has no clean rollback past the
2-week shadow window. R12 in the v2 risk matrix names this and
mitigates with the `pre-core-delete` tag plus the rollback runbook at
`docs/runbooks/core-rollback.md`. Bench calibration has to be redone
against PackageReference-as-floor rather than ProjectReference; the
new floor lives at `docs/benchmarks/baselines/v11-package-ref-floor.json`
and every subsequent stage-boundary check diffs against it.

The friend-grant transplant is broader than the v1 plan assumed (R2).
Source-side `[assembly:]` declarations, xmldoc `<see cref>` references
that resolve against the moved exception type, and linked-source
include declarations all need to move in the same commit as the
rename. The Stage -1 audit names every site; Glenn applies them
mechanically.

## Quick picture

> Imagine two warehouses storing the same inventory. Every shipment
> has to be packed twice; every recall has to be processed twice. The
> warehouses drift because the cataloguers use slightly different
> labels. The fix isn't more discipline at the cataloguers — it's
> closing one warehouse. Herald.OSS becomes the only warehouse;
> `Modules/Core` ships its last truck and the doors close.

## Rationale tied to CUPID + DRY

Two parallel kernel trees is a textbook DRY violation: the same fact
(the kernel implementation) lives in two places, and every change
costs twice. Collapsing to one canonical upstream is the minimum
change that removes the duplication.

The decision also supports CUPID's *Composable* property. With
`Modules/Core` retired, paid modules compose against a published
package boundary. The boundary is the same contract a third-party
consumer sees, so the paid composition story and the OSS composition
story stop diverging.

## References

- Plan v2, "Stage 0 reaffirmation"
- Plan v2 risk matrix entries R2, R12, R17
- `[[project_detour_c_umbrella_unblock_2026_05_18]]`
- `[[project_herald_package_naming_convention]]`
- Runbooks: `docs/runbooks/core-rollback.md`, `docs/runbooks/strong-name-key-rotation.md`
