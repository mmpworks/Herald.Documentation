---
title: Licensing legal documents - index
slug: licensing/legal/README
category: reference
audience: counsel, sales, customer-procurement, runtime-implementers (Glenn), portal-implementers (Nancy)
reading-level: mixed (legal sections are formal; this index is plainspoken)
since: 2.1
status: draft
last-reviewed: 2026-05-19
source-of-truth: prose/licensing/legal/README.md
related:
  - prose/licensing/reference/capabilities.md
  - data/licensing/nag-templates/manifest.json
  - docs/_wip/capability-composition-plan-v1.md
counsel-review-required: true
---

> **FIRST DRAFT - COUNSEL REVIEW REQUIRED BEFORE DEPLOYMENT.** All
> documents indexed here are draft-quality starting points for
> counsel-led drafting. Nothing in this subtree is authorized for
> production use until counsel signs off. Steve-ratified facts
> (jurisdiction, venue, liability cap multiple, AS-IS SLA posture,
> Compliance Posture / no-Business-Associate stance, DPA scope, BAA
> removal, indemnification carve-outs) were folded into the drafts
> on 2026-05-19; only counsel-language review remains.

# Licensing legal documents

This page is the single index for every legal artifact in the Herald
licensing surface. Eleven artifacts live here today: two signed
agreements, four runtime nag templates, a JSON manifest that ties
the runtime templates to the wording counsel reviews, the JSON
Schema the manifest validates against, and two package-banner
templates (LICENSE.txt + README.md) plus their index, embedded in
every paid `MMP.*` NuGet package MMPWorks publishes.

The discipline is docs-as-database. Each artifact has one canonical
source. The runtime, the operator portal, the public docs, and
counsel review all read the same file. Edit the canonical file once;
every consumer surface picks up the change.

## What lives where

| Artifact | Path | Voice | Counsel review |
|---|---|---|---|
| Pro License Agreement | `prose/licensing/legal/agreements/pro-license-agreement.md` | Formal legal | Required |
| Enterprise License Agreement | `prose/licensing/legal/agreements/enterprise-license-agreement.md` | Formal legal | Required |
| Nag template - issued demo | `data/licensing/nag-templates/issued-demo.txt` | Friendly | Required (banner) |
| Nag template - soft reminder (day 1-30) | `data/licensing/nag-templates/expired-paid-day-1-30.txt` | Soft reminder | Required (banner) |
| Nag template - stern legal notice (day 32-60) | `data/licensing/nag-templates/expired-paid-day-32-60.txt` | Stern legal | **Required (load-bearing)** |
| Nag template - revoked | `data/licensing/nag-templates/revoked.txt` | Stern legal | **Required (load-bearing)** |
| Nag template manifest | `data/licensing/nag-templates/manifest.json` | n/a (metadata) | Counsel-aware (links templates to agreement clauses) |
| Nag template schema | `schemas/licensing/nag-template.schema.json` | n/a (metadata) | n/a |
| Package-banner LICENSE.txt template | `prose/licensing/legal/package-banners/LICENSE.txt.template` | Formal legal | **Required (load-bearing)** |
| Package-banner README.md template | `prose/licensing/legal/package-banners/README.md.template` | Plainspoken (install-surface) | Required |
| Package-banner index | `prose/licensing/legal/package-banners/README.md` | Plainspoken | Required |

## How the artifacts fit together

The two agreements are the contracts the customer signs. The four
nag templates are the operator-facing notices the runtime renders
during the license lifecycle. The two stern-legal-notice templates
(day 32-60 and revoked) restate clauses from the signed agreement
in the customer's operations console; that is the link between the
signed contract and the runtime warning the operator sees.

> :bulb: **Quick picture.** Think of the License Agreement as the
> deed to a house and the nag templates as the notices a courier
> tapes to the door. The deed has the full terms. The door notice
> reminds the resident that the terms apply right now — pay the
> assessment, the closing date has passed, the property has been
> condemned. The door notice does not replace the deed. It restates
> the part of the deed that applies in this moment, in language
> someone reading it on a phone can act on.

The manifest at `data/licensing/nag-templates/manifest.json` carries
the metadata that links each template to (a) the lifecycle trigger
the runtime evaluates, (b) the variables the runtime substitutes,
and (c) the agreement clause the template restates. When counsel
reviews the stern templates, the `restatesClauseFrom` field on each
manifest entry points to the exact agreement section that must
remain consistent.

The package-banner templates at
`prose/licensing/legal/package-banners/` are the third axis. Every
paid `MMP.*` NuGet package embeds a `LICENSE.txt` and a `README.md`
rendered from those templates. Counsel reviews the canonical
templates once; every paid package picks up the approved wording
at publish time. See the package-banners
[index](package-banners/README.md) for the substitution contract,
adoption status, and the workflow Glenn follows when bumping a
package's banner version.

## Roles and responsibilities

**Counsel** owns the wording of the two agreements and the two
stern-legal-notice templates. Wording changes to these four
artifacts trip mandatory counsel review.

**Heather** (documentation agent) owns the structure: schema, layout,
cross-references, and the renderers that produce consumer surfaces
from the canonical artifacts. Heather drafts initial wording for
counsel to review; counsel rewrites freely.

**Glenn** (migration-shepherd) hardcodes the runtime gate primitives
that select and render the nag templates per Richard's
capability-composition-plan-v1 ADR-211. Glenn reads
`data/licensing/nag-templates/manifest.json` to discover which
template to render in which lifecycle state.

**Nancy** (internal-SPA engineer) consumes the manifest in the
operator portal to render template previews and to display the
canonical template names alongside the corresponding agreement
clauses.

**Dawn** (herald-website-maintainer) does not own this subtree.
Public marketing copy about licensing lives elsewhere; the legal
artifacts here are not for the marketing site.

## Workflow for changing a legal artifact

1. Edit the canonical file (the `.md` for agreements, the `.txt`
   for nag templates, or `manifest.json` for metadata).
2. If the change touches wording on an agreement or a stern legal
   notice, set the manifest entry's `status` to `counsel-review`
   and notify counsel.
3. Counsel reviews and either approves or returns with edits.
4. On counsel approval, set `status` to `published` and clear the
   COUNSEL REVIEW REQUIRED banner from the affected file(s).
5. Re-run the renderers so the operator portal and the public docs
   pick up the new wording.

The renderers preserve the banner on any artifact whose `status` is
anything other than `published`. The banner is a forcing function:
no consumer surface ships unapproved legal wording.

## Steve-ratified facts (folded 2026-05-19)

The nine ambiguities flagged in the first-draft index have all been
resolved by Steve and folded into the agreements. Counsel review of
the resulting wording is still required, but no further fact
gathering from MMPWorks is needed.

| # | Item | Steve's answer | Where it lives |
|---|---|---|---|
| 1 | Jurisdiction | Texas | Pro 12.1, Enterprise 11.1 |
| 2 | Venue | Williamson County, Texas | Pro 12.1, Enterprise 11.1 |
| 3 | Enterprise liability cap multiple | 24 months of fees | Enterprise 8.2 |
| 4 | Schedule A - SLA terms | AS-IS uptime; no SLA, no service credit | Enterprise 5, Schedule A |
| 5 | Schedule B - Compliance posture | Customer-operated software; MMPWorks does not host or process Customer Data; no Business Associate / Processor role | Enterprise 4.3, Schedule B |
| 6 | FFIEC representation | Auditable via Herald's own technical capabilities (HMAC + Merkle + HSM) | Enterprise 4.1, Schedule B |
| 7 | DPA scope | Not applicable; MMPWorks does not host or process Customer Data | Enterprise 7.1 |
| 8 | BAA template | Removed; MMPWorks does not act as a Business Associate | Enterprise 7.2, Schedule B |
| 9 | Enterprise cap carve-outs | Confidentiality, Customer indemnification, MMPWorks indemnification, third-party amounts | Enterprise 8.3 |

## What counsel still does

Counsel reviews the wording of the two agreements and the two
stern-legal-notice templates and either approves or returns edits.
The facts above are settled; counsel is free to rewrite the
language that expresses them, but no further fact-gathering is
required from MMPWorks before review.

## Status of each artifact

All eight artifacts in this subtree are currently `status: draft`.
None are authorized for production use. The runtime (Glenn's gate
primitives) may reference the canonical paths to read the templates
during development; the COUNSEL REVIEW REQUIRED banner shall remain
visible at runtime on any installation that ships before counsel
approval.
