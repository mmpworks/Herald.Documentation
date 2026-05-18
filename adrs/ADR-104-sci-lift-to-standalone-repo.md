# ADR-104 — Promote Herald.Sci to mmpworks/Herald.Sci standalone OSS repo

- **Status:** Proposed
- **Date:** 2026-05-18
- **Stage:** 4
- **Mirrors:** umbrella `herald`; eventually mmpworks/Herald.Sci (at first commit)

## Context

`Modules/Herald.Sci/` already exists as a self-contained project in
the umbrella tree. Lifting it to a standalone OSS repo validates the
ecosystem story Stages 2 and 3 set up (Herald.OSS plus Herald.ServerOSS
plus Herald.DashboardOSS, each as its own published repo) and
decouples Sci's release cadence from the umbrella's quarterly rhythm.

Sci is small enough to lift cleanly. The umbrella has no external
consumers — every reference to `Herald.Sci` lives inside the same
solution. The friction is in the day-one repo scaffolding and the
friend-grants survival.

## Decision

1. **Mechanical lift.** `Modules/Herald.Sci/` moves to a new
   `mmpworks/Herald.Sci` repo. Reuse the `Herald.OSS` repo scaffold
   (Apache 2.0 LICENSE, NOTICE, README, CONTRIBUTING with DCO,
   SECURITY, CoC, `docs/adrs/` index stub). The lift commit is the
   first commit on the new repo's `main`.
2. **Friend-grants.** `Herald.Sci` is currently on Herald.OSS's
   `InternalsVisibleTo` list. That grant survives the lift as long
   as Herald.Sci's strong-name public key is pinned in the qualifier
   added in Stage 0. If the key changes during the lift, R17 (key
   rotation runbook) applies.
3. **DCO not CLA** per `[[feedback_herald_sinks_dco]]`. Reuse the
   Herald.Sinks DCO scaffold; do not introduce CLA infrastructure.
4. **Day-one new-repo artifact set** must exist at first commit:
   LICENSE (Apache 2.0), NOTICE, README, CONTRIBUTING (with DCO
   sign-off instructions), SECURITY, CoC, `docs/adrs/` index stub
   referencing this ADR as a mirror. "We will document later" repos
   become permanently undocumented; the scaffold prevents that.
5. **No parallelism with Stages 2 or 3.** Heather's lane is
   saturated by Stages 2 and 3 back-to-back. Stage 4 runs serial
   after Stage 3 close. Escalation #4 from v1 closed: no parallel
   execution.
6. **Stage 5 consumes Sci as a PackageReference.** Post-lift, the
   Stage 5 `Herald.Pro` and `Herald.Enterprise` meta closures pull
   `Herald.Sci` from nuget.org rather than the umbrella's
   `Modules/Herald.Sci`. The umbrella drops the project from its
   curated build loop in the same commit.

## Consequences

**Positive.** Clean OSS release demonstrating the ecosystem story.
Sci's release cadence decouples from the umbrella. Third-party
contributors have a small, focused repo to land PRs against.

**Negative.** One new repo to scaffold plus day-one artifact set.
The lift commit has no rollback past the umbrella delete commit;
treat the same as `Modules/Core` retirement (ADR-100) and tag
`pre-sci-lift` before the umbrella delete.

**Herald.Gaming note.** Plan v1 grouped Gaming with Sci as
candidates for the standalone-OSS lift. Steve flagged Gaming as a
special case — different licensing posture, different consumer
audience — and deferred its disposition. Gaming is not part of this
ADR.

## Quick picture

> Picture moving a self-contained workshop out of a shared garage
> into its own building. The workshop already has its own tools,
> its own bench, its own door — it just shares the garage's address
> and electricity. Moving it out means a separate address, a
> separate utility bill, and a sign on the door. Nothing inside the
> workshop changes; what changes is who can reach it from the
> street.

## Rationale tied to CUPID + DRY

The lift is a CUPID *Domain-based* call: `Herald.Sci`'s domain
(scientific notation, physics units, statistical processors) is
distinct enough from the kernel that consumers should be able to
reach for it without pulling the umbrella's dependency closure.
Standalone OSS repos are the cleanest expression of that domain
boundary.

No DRY tension here — the lift removes nothing from the umbrella's
duplication picture; it just relocates a project that was already
self-contained.

## References

- Plan v2 ADR-104
- `[[feedback_herald_sinks_dco]]`
- ADR-100 (Stage 0 friend-grant transplant covers Sci too)
- Plan v2 risk matrix entries R7, R17
