---
title: Package-banner templates - index
slug: licensing/legal/package-banners/README
category: reference
audience: counsel, package-publishers (Glenn), runtime-implementers
reading-level: mixed (template bodies are formal-legal; this index is plainspoken)
since: 2.1
status: draft
last-reviewed: 2026-05-19
source-of-truth: prose/licensing/legal/package-banners/README.md
related:
  - prose/licensing/legal/agreements/pro-license-agreement.md
  - prose/licensing/legal/agreements/enterprise-license-agreement.md
  - prose/licensing/legal/README.md
counsel-review-required: true
---

> **FIRST DRAFT - COUNSEL REVIEW REQUIRED BEFORE DEPLOYMENT.** The
> templates in this directory have not been reviewed by licensed
> legal counsel and are not authorized for production embedding in
> any shipped NuGet package. Use only as a starting point for
> counsel-led drafting. The first concrete instance — `MMP.Licensing`
> and `MMP.Licensing.Contracts` 2.1.1 — was Steve-ratified on
> 2026-05-19; counsel-language review is still required before
> Glenn re-packs and re-publishes.

# Package-banner templates

This directory holds the canonical `LICENSE.txt` and `README.md` templates
embedded in every paid `MMP.*` NuGet package MMPWorks publishes. Adopting
the same template across every paid package keeps the IP banner consistent
and removes the per-package wording-drift risk that landed `MMP.Licensing`
2.1.0 on nuget.org with no license declared.

## What lives here

| Artifact | Path | Voice | Counsel review |
|---|---|---|---|
| Package LICENSE.txt template | `prose/licensing/legal/package-banners/LICENSE.txt.template` | Formal legal | **Required (load-bearing)** |
| Package README.md template | `prose/licensing/legal/package-banners/README.md.template` | Plainspoken (install-surface metadata) | Required |
| Index (this file) | `prose/licensing/legal/package-banners/README.md` | Plainspoken | Required |

## The substitution contract

Both templates are mechanical-substitution starting points. Two
tokens are required, one is optional.

**Required tokens:**

- `{packageName}` — the NuGet package id. Examples: `MMP.Licensing`,
  `MMP.Licensing.Contracts`, `MMP.Herald.Pro`, `MMP.Herald.Enterprise`.
- `{packageRole}` — one paragraph (one to three sentences) describing
  what the package is for, in plainspoken language a NuGet consumer
  reads on the package detail page. Example for `MMP.Licensing`:
  > "Ed25519 license verifier for MMPWorks's paid Herald products.
  > The package contains the cryptographic verifier, the v2 token
  > wire format, the locator that resolves a license token from
  > environment or file, and the gate primitives the paid packages
  > call at registration time."

**Optional token:**

- `{companionPackage}` — the NuGet id of a paired package that ships
  alongside this one under the same license terms. Example: when
  rendering `MMP.Licensing`'s banner, the companion is
  `MMP.Licensing.Contracts`; when rendering Contracts, the companion
  is `MMP.Licensing`. Most paid packages have no companion and leave
  this token unfilled.

**How the optional token renders.** Both templates wrap the
companion-package sentence in an HTML-comment fence:

```
<!-- IF companionPackage -->
... sentence body referencing {companionPackage} ...
<!-- ENDIF -->
```

The publisher's substitution step does one of two things on each
fenced block:

- When `{companionPackage}` is filled, replace the token with the
  companion package id and remove the surrounding `<!-- IF -->` /
  `<!-- ENDIF -->` markers. The sentence renders.
- When `{companionPackage}` is empty, delete the entire fenced
  block including the markers. No dangling reference remains in
  the rendered file.

The legal clauses do not change per package. The package-role
description changes per package. The companion-package sentence is
present or absent per package. The token-replacement step is
mechanical and lives in the package publisher's workflow
(Glenn's lane).

## Why this is one template, not many

The docs-as-database discipline applies. Editing the legal clauses in
one place and rendering them into every package's `LICENSE.txt` removes
the failure mode where one package's banner drifts from the others
during a clause update. Counsel reviews the canonical templates here;
every paid `MMP.*` package picks up the approved wording at publish time.

> **Quick picture.** Think of the templates as the master deed
> language a title office stamps on every property in a development.
> The street address and lot number change per property; the deed
> language is uniform. When the development's lawyer updates the
> easement clause, every new deed picks up the change automatically.
> The alternative — hand-editing each deed — is how wording drifts
> across properties and how disputes start.

This is DRY applied to legal text. One canonical clause, rendered
into every paid package's install-surface artifact at publish time.

## Concrete adoption examples

| Package | Status | Banner version | First-shipped under banner |
|---|---|---|---|
| `MMP.Licensing` | Draft (this dispatch) | 2.1 template | 2.1.1 (pending) |
| `MMP.Licensing.Contracts` | Draft (this dispatch) | 2.1 template | 2.1.1 (pending) |
| `MMP.Herald.Pro` | Future | 2.1 template | TBD |
| `MMP.Herald.Enterprise` | Future | 2.1 template | TBD |

When a new paid `MMP.*` package goes through its first publish, the
publisher copies both templates into the package source tree, runs the
two-token substitution, and references the resulting files from the
package's `.csproj` via `<PackageLicenseFile>` and `<PackageReadmeFile>`.
No further drafting is required for the per-package legal text.

## Workflow for changing a template

1. Edit the canonical template file in this directory.
2. If the change touches a load-bearing legal clause, set the
   `status` in this index to `counsel-review` and notify counsel.
3. Counsel reviews and either approves or returns with edits.
4. On counsel approval, set `status` to `published` and clear the
   COUNSEL REVIEW REQUIRED banner from the affected file(s).
5. Coordinate with Glenn to bump the banner version on every paid
   `MMP.*` package at the next publish.

## Relationship to the Product License Agreements

The package-banner `LICENSE.txt` template is **not** a Product License
Agreement. It governs the NuGet package itself (installation, internal
redistribution, CI references). The right to use the underlying paid
Herald product comes from the separately-signed Herald Pro, Herald
Enterprise, or TesseraSeal license agreement. The template makes that
distinction explicit and cross-references the canonical agreements:

- `prose/licensing/legal/agreements/pro-license-agreement.md`
- `prose/licensing/legal/agreements/enterprise-license-agreement.md`
- TesseraSeal license agreement (forthcoming)

This separation keeps the package-banner language short — a NuGet
consumer can read it in one sitting — while leaving the heavy contract
machinery in the canonical agreements where counsel-led editing already
lives.
