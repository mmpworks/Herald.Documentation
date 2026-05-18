# Architecture Decision Records

This directory is the canonical home for Herald ecosystem ADRs.

Every ADR here is the source of truth. Per-repo mirrors live at
`<repo>/docs/adrs/ADR-NNN-slug.md` and carry a thin pointer back to
this canonical version. Mirrors are never hand-edited. When the
canonical text changes, the mirrors regenerate from it.

## Numbering

ADRs are numbered in the order they are decided, not the order they
are executed. A decision that produces a sub-ADR uses a dotted suffix:
ADR-102 covers the three-binary server carve, ADR-102.1 covers the
endpoint mapper sub-decision underneath it.

The Herald.OSS repo carries its own internal ADRs (currently ADR-001)
that predate this canonical home and remain there. Ecosystem-spanning
ADRs start at ADR-100 to keep the two namespaces from colliding.

## Index

| # | Title | Status | Stage |
|---|-------|--------|-------|
| ADR-100 | Retire Modules/Core in favor of Herald.OSS as canonical upstream | Proposed | 0 (Detour C) |
| ADR-101 | Herald.RestApi packages split across Apache 2.0 and closed-IP | Proposed | 1 |
| ADR-102 | Three server binaries (ServerOSS / Server.Pro / Server.Enterprise) | Proposed | 2 |
| ADR-102.1 | ServerOSS endpoint mapper carve — clean 8-endpoint reimplementation | Proposed | 2 |
| ADR-102.5 | OSS server packaging composition (four-package vs fat NuGet) | Proposed | 2 |
| ADR-103 | Two dashboards (DashboardOSS skeleton + Dashboard.Paid runtime gating) | Proposed | 3 |
| ADR-103.1 | Dashboard.Paid build-time composition mechanism | Proposed (pending spike) | 3 |
| ADR-104 | Herald.Sci lift to mmpworks/Herald.Sci standalone OSS repo | Proposed | 4 |
| ADR-105 | Post-reorg shape of Herald.Pro, Herald.Enterprise meta-packages | Proposed | 5 |
| ADR-106 | Herald.Compliance to Herald.Audit rename | Deferred (placeholder) | 6 |

## Per-repo mirror convention

Each ADR names the repos that need a stub mirror. Mirrors are short:
title, status, one-line summary, link back to canonical. The discipline
is "stubs never deviate from canonical." A renderer script is on the
roadmap; until then the first author hand-writes the stubs to match.

If a target repo doesn't exist yet (Herald.ServerOSS, Herald.DashboardOSS,
Herald.Sci), the stub lands at the repo's first commit. The canonical
ADR notes which repos are pending.

## License

Apache 2.0, inherited from the Herald.Documentation repo root.
