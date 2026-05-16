---
title: Website Integration Pilot — Herald.Documentation → herald-website
slug: website-integration-pilot
status: draft (alpha)
created: 2026-05-16
author: Heather (documentation agent)
collaborators:
  - Dawn (herald-website-maintainer)
related-repos:
  - Herald.Documentation
  - herald-website
last-reviewed: 2026-05-16
---

# Website Integration Pilot — Herald.Documentation → herald-website

The goal of this pilot is to prove the data-transfer pipeline that
moves prose and structured records out of Herald.Documentation and
onto the public website. Nothing in the user-facing site changes.
A hidden `/documentation/herald-oss/` route — only we know it exists —
renders a small set of alpha pages so we can verify the round trip end
to end.

If the pipeline works, we widen it. If it breaks, we fix the seam
before any of the bigger content waves go through it.

## Round 2 corrections applied (2026-05-16)

Richard reviewed the round-1 producer + consumer proposals together at
`herald-website/docs/design-notes/documentation-pilot-architecture-review.md`.
Verdict: YELLOW (mechanism green-lit, 12 corrections required). The
user resolved the one escalated question: no version gate, always
`main`, no `since:` frontmatter behavior.

Items that changed on this producer side:

- **URL prefix locks to `/documentation/herald-oss/<slug>`** (Richard
  item 3). Round-1 §3's URL table assumed `/documentation/<slug>` and
  said the `herald-oss/` segment was deferred to round 2. Overruled.
  The product segment is part of the URL contract from day one.
  Internal markdown links in the three alpha pages stayed correct
  because every cross-page link was already relative — the renderer
  resolves them under whatever prefix the website mounts.
- **`draft: true` frontmatter is the in-progress gate** (Richard item
  11, replaces the round-1 `website-alpha` branch idea). The website
  skips any page whose frontmatter sets `draft: true`. The alpha
  pages are not drafts. Documented in
  `documentation-guidance/herald-oss/herald-oss-documentation-plan.md`
  as a one-line note.
- **No version gate, ever** (resolves §10 open question #2). The
  website renders whatever is on `main`. Pages do not gate on
  `since:`. The `since:` field stays in frontmatter as metadata the
  reader can see, not as a render-time gate.
- **Branch contract is `main`** (resolves §10 open question #3). The
  `website-alpha` branch idea is dropped. The website's fetch script
  clones `main`. In-progress drafts hide behind `draft: true`, not
  behind a branch.
- **Manifest file is not part of the contract** (Richard item 2, was
  Dawn's proposal). The producer does not author or maintain a
  `prose/_manifest.json`. The sync script walks the tree and infers
  what to render from frontmatter alone.
- **No remote fetch fallback** (Richard divergence #2, was Dawn's
  proposal). The website always clones the docs repo at build time;
  there is no `raw.githubusercontent.com` fallback. Doesn't affect
  what the producer authors — listed here so the round-2 reader has
  the full picture.

The rest of the proposal stands. SVG diagram support is in scope from
day one (Richard item 10) because the alpha explanation page already
references one. Frontmatter shape, sync seam, test plan, and failure
modes all carry over from round 1.

---

## 1. Mechanism — recommendation

**Recommendation: shallow git clone at build time, then file-copy
into `web/src/content/herald-docs/`. Mirror the MRM-spec pattern
already running in the website.**

The website's MRM-spec pipeline solved this exact problem six months
ago. It is already in production. The shape is:

1. `scripts/fetch-spec-if-missing.cjs` does a `git clone --depth 1`
   of the public spec repo if the sibling directory is missing.
2. `scripts/sync-mrm-spec.cjs` walks the source, copies markdown
   into `web/src/content/mrm-spec/`, and writes an `_index.json`
   catalogue.
3. Vite's `import.meta.glob` pulls every file in `src/content/`
   into the bundle at build time.
4. The runtime page (`SpecDocPage.vue`) loads the matching slug from
   the glob and renders it with `markdown-it`.

We add a sibling pair of scripts pointing at Herald.Documentation,
a sibling destination at `web/src/content/herald-docs/`, and a
single new route `/documentation` with a `DocumentationLayout.vue`
that mirrors `MrmLayout.vue`. That is the whole change on the
website side.

### Why this beats the alternatives

| Option | Verdict |
|---|---|
| **Shallow git clone at build (recommended)** | One precedent in the repo. No GitHub auth needed for public content. Idempotent across local and CI. Fails loudly if the clone fails. |
| Raw-content fetch via `raw.githubusercontent.com` | Works for one file at a time but loses the directory walk. We'd reinvent the index file by hand and re-author the sync script around `fetch()`. No win over `git clone`. |
| GitHub API at build | Rate-limited to 60/hr without a token. The website builds run on Cloudflare Pages too — one missing token and the build breaks. Strictly worse than `git clone` for a public repo. |
| Git submodule | Couples the website's branch state to Herald.Documentation's commit. Every doc change becomes a website commit. We want the two repos to release on independent cadences, not to lockstep. |
| Manual sync (copy script run by a human) | Works exactly until someone forgets. Drift becomes the steady state. |

CUPID property this choice favors: **Composable**. The website
already knows how to pull a sibling repo and render its markdown.
The Herald.Documentation source becomes another instance of the
same shape — no new subsystem, no new tool, no new mental model.
DRY is the other beneficiary: we are not duplicating the fetch +
sync + glob pattern. We are reusing it.

### Where the seam lands in the website build

```
npm run dev / npm run build
  └── prebuild
       ├── fetch-spec-if-missing.cjs        (existing — MRM)
       ├── sync-mrm-spec.cjs                (existing — MRM)
       ├── fetch-herald-docs-if-missing.cjs (NEW — clone or update)
       ├── sync-herald-docs.cjs             (NEW — walk + copy + index)
       └── gen-og-png.cjs                   (existing)
  └── build
       └── vite build
            └── import.meta.glob picks up src/content/herald-docs/
                and src/content/mrm-spec/ alike
```

Both new scripts are pure Node (no shell-out beyond `git clone`),
cross-platform, and idempotent. Local devs check out
Herald.Documentation as a sibling directory; CI clones it fresh on
each build.

## 2. Alpha content surface

Three pages, all markdown-with-frontmatter (the prose data model).
Schema-driven records are deferred to round 2 — this pilot proves
the prose path first.

| Page | Diátaxis | Lives at | Demonstrates |
|---|---|---|---|
| `tutorials/first-pipeline.md` | Tutorial | `prose/herald-oss/tutorials/` | Callout analogy, Mermaid sequence, CUPID rationale |
| `explanation/kernel-vs-chain.md` | Explanation | `prose/herald-oss/explanation/` | Callout analogy, hand-authored SVG (architecture-page style), DRY rationale |
| `quickstart.md` | Top-level entry | `prose/herald-oss/` | Frontmatter routing, related-page links, no diagram |

This set exercises:

- **Frontmatter the website needs to read** (title, slug, category,
  audience, related, last-reviewed, since).
- **Markdown body with embedded Mermaid** (fenced code block,
  language `mermaid`).
- **Markdown body referencing an SVG asset** (relative path under
  `diagrams/herald-oss/`).
- **Cross-doc links** (`quickstart.md` links into both the tutorial
  and the explanation; the link rewriter has to resolve `./` and
  `../` paths correctly).

One callout analogy per page, one CUPID/DRY rationale per page.
Voice and reading level held at the project standard.

### Page-by-page intent

**`quickstart.md`.** The five-minute landing for a new adopter.
"You have a console app, you want a logger, here is the smallest
useful pipeline." Links into the longer tutorial and the
explanation for readers who want more.

**`tutorials/first-pipeline.md`.** A Diátaxis tutorial. Walks one
specific adopter from a blank `Program.cs` to a working logger
that prints `Info` and `Warn` events to console. Two `dotnet` CLI
commands, three lines of code, one screenshot's-worth of output. A
Mermaid sequence diagram shows the accept-path flow so the reader
ends with a mental model, not just a working snippet.

**`explanation/kernel-vs-chain.md`.** The "what is the kernel fast
path and why does it exist" page from the doc plan. This one earns
a hand-authored SVG in the herald-website architecture-page style
because it has a comparison story (kernel path vs chain path) and
color semantics carry weight. The prose names the DRY violation
the kernel avoids (one delegate, not N decorator layers) and the
CUPID property the design favors (Predictable — same call shape,
same cost shape, every time).

## 3. Data contract for Dawn

What URLs return what, what shape the files take, how to handle
renames.

### URL shape (after the sync runs)

The sync script mirrors the source layout under `prose/herald-oss/`
into `web/src/content/herald-docs/herald-oss/`. For example:

| Source path (Herald.Documentation) | Destination (website) | URL |
|---|---|---|
| `prose/herald-oss/quickstart.md` | `src/content/herald-docs/herald-oss/quickstart.md` | `/documentation/herald-oss/quickstart` |
| `prose/herald-oss/tutorials/first-pipeline.md` | `src/content/herald-docs/herald-oss/tutorials/first-pipeline.md` | `/documentation/herald-oss/tutorials/first-pipeline` |
| `prose/herald-oss/explanation/kernel-vs-chain.md` | `src/content/herald-docs/herald-oss/explanation/kernel-vs-chain.md` | `/documentation/herald-oss/explanation/kernel-vs-chain` |

The product segment is part of the URL from day one (Richard
correction #3). When more products land (Compliance, Lean, etc.),
they slot in alongside herald-oss at the same prefix depth.

### Frontmatter the website must read

Every prose file starts with YAML frontmatter. The website parses
it with `js-yaml` (already a dependency). Fields the renderer
relies on:

```yaml
---
title: Quickstart — Herald.OSS         # used for <title>, h1, breadcrumb
slug: quickstart                        # used to match URL (== filename minus .md)
category: tutorial | howto | reference | explanation | landing
audience: new-adopter | advanced | plugin-author | contributor
since: 0.2.2                            # version where the page first applies
last-reviewed: 2026-05-16               # surfaced as "Last reviewed" footer
related: [other-slug, another-slug]     # rendered as a sidebar list
related-records: []                     # round-2; ignore for alpha
---
```

Unknown frontmatter fields are preserved but ignored. The website
must not error on a frontmatter field it doesn't recognise — the
docs repo will grow fields the website is not yet wired to render.

### Diagram assets

Two patterns:

- **Mermaid.** Embedded as a fenced code block. The website's
  existing `mermaid` dependency handles it. No extra file.
- **Hand-authored SVG.** Lives at `diagrams/herald-oss/<slug>.svg`
  in Herald.Documentation. The sync script copies the SVG to
  `web/src/content/herald-docs/diagrams/herald-oss/<slug>.svg`. The
  markdown references it with a relative path: `![alt](../diagrams/herald-oss/<slug>.svg)`.

The SVG follows the architecture-page style sheet (Cascadia Code
font, the blue/red/green/yellow palette, 75 px rounded rectangles)
so it sits visually alongside `/herald/architecture` without a
re-skin.

### Renames

The slug is the contract, not the file path. If a page moves,
update the slug only if the URL must change; keep the slug stable
otherwise.

When a slug must change:

1. Add a `redirected-from: [old-slug]` field to the new file's
   frontmatter.
2. The website builds a redirect map from `redirected-from` and
   serves 301s.

The pilot does not implement the redirect map (no renames yet).
The mechanism is reserved for round 2.

## 4. Test plan

Local end-to-end test. Five steps.

1. **Author or edit a page locally.** Pick any file under
   `prose/herald-oss/`. Change a heading. Save.
2. **Run the website locally.**
   ```bash
   cd E:/dev/herald-website
   npm run dev
   ```
   The `predev` hook runs the new fetch + sync scripts. If
   `Herald.Documentation` is a sibling on disk (the dev case), no
   clone happens — the sync reads directly from the local working
   copy.
3. **Navigate to the page.** Open `http://localhost:5173/documentation/<slug>`.
4. **Verify the change appears.** The heading you edited is visible.
5. **Verify nothing else changed.** Open three or four existing
   pages (`/herald/architecture`, `/mrm`, `/`). They render
   unchanged.

CI end-to-end test (after we push the alpha). The Cloudflare Pages
build does its own `git clone` of Herald.Documentation (the
sibling directory is not in the website's repo), runs the sync,
and produces the same `dist/` as local. We verify by visiting
`<preview-url>/documentation/quickstart` after the build.

The route is hidden — no nav link, no sitemap entry, no robots.txt
change. Only people who type the URL find it. That is the "only we
know about it" constraint.

### What success looks like

- A push to `Herald.Documentation:main` triggers no website rebuild
  on its own (the docs repo doesn't know about the website). That
  is correct — the website rebuilds on its own schedule.
- The next website build picks up the docs change.
- The hidden `/documentation` URL renders the new content.
- Nothing about the existing site changed.

### What failure modes we are looking for

- The Cloudflare runner can't clone the docs repo (auth, network,
  rate limit). The new `fetch-herald-docs-if-missing.cjs` must
  fail loudly with a clear error.
- Frontmatter parses wrong on a page the docs team wrote
  intuitively but didn't match the schema. We need a lenient
  parser that surfaces a friendly error and keeps building.
- Mermaid syntax error in a doc page breaks the markdown render.
  Need to confirm `markdown-it` and the Mermaid plugin degrade
  gracefully (render the fenced block as text, not throw).
- Two pages claim the same slug. The sync script must detect
  duplicates and fail the build.

## 5. What we are not doing this round

- No schema-driven content. The structured-record pipeline (sinks
  matrix, API reference, capability matrix) ships in round 2 after
  the prose pipeline is proven.
- No nav link. Hidden until the user says go.
- No multi-product URL prefix. Round 2 adds `/<product>/` when the
  second product lands.
- No redirects, no `redirected-from`. Reserved.
- No website-side search index for the docs corpus. Round 2.
- No translation pipeline. Round 3 if a need shows up.

## Questions for Richard

These are the architectural choices we want Richard to weigh in on
before the pilot ships:

1. **Where exactly does the sync slot in if the website moves off
   Vite?** The current sync writes into `web/src/content/herald-docs/`
   so `import.meta.glob` picks it up. If the website ever switches
   to Astro or Nuxt the glob seam changes. Should the sync write
   to a tool-agnostic intermediate (e.g. `web/public/herald-docs/`
   served as static assets) so the rendering tool is the only thing
   that swaps?

2. **Release-cadence drift between the two repos.** Herald.Documentation
   will release on its own pace. The website does the same. When a
   doc page is updated to describe a feature that hasn't shipped
   in Herald.OSS yet, the website would render it the moment the
   docs repo merges the change. Do we want a `since: x.y.z` gate on
   the renderer that hides pages whose `since` exceeds the
   currently-shipped Herald.OSS version, and how does the website
   learn what "currently shipped" is — a pinned version constant in
   the docs repo's root manifest, or a check against the NuGet feed?

3. **Branch contract for the alpha.** Should the website's
   `fetch-herald-docs-if-missing.cjs` clone `main`, or should we
   tag a `website-alpha` branch in Herald.Documentation that the
   website pins to until the pilot is reviewed? Pinning to a branch
   protects the live site from in-progress doc drafts but
   complicates the local-dev story (which checks out `main`).

4. **What does the website do if the docs repo is unreachable at
   build time?** Fail the build (current MRM behavior), or build
   with last-known-good cached content? The MRM pattern fails
   loudly; that may not be what we want for a hidden alpha that
   should not block a deploy.

5. **Cross-doc links into the rest of the website.** A docs page
   may link to `/herald/architecture` or `/mrm/spec/...`. Should
   those be plain markdown links the website resolves at render
   time, or should we route through a manifest the docs repo
   maintains so the link is type-checked at build (broken-link
   detection without a crawler)?

Resolve these with the user as needed; the pilot can ship with
defaults on each (1 = stay on Vite for now, 2 = no version gate yet,
3 = clone `main`, 4 = fail loudly, 5 = plain markdown) and revisit
when the questions become real.

---

## Appendix — file map of the alpha

Authored this session, **uncommitted** under
`E:\dev\Herald.Documentation\`:

```
documentation-guidance/pilots/
  website-integration-pilot.md          (this file)

prose/herald-oss/
  quickstart.md
  tutorials/
    first-pipeline.md
  explanation/
    kernel-vs-chain.md
```

Pending Dawn's work on the website side:

```
herald-website/web/scripts/
  fetch-herald-docs-if-missing.cjs       (NEW — mirror MRM script)
  sync-herald-docs.cjs                   (NEW — mirror MRM script)

herald-website/web/src/
  content/herald-docs/                   (generated; gitignored)
  layouts/DocumentationLayout.vue        (NEW — mirror MrmLayout.vue)
  pages/documentation/
    DocumentationLandingPage.vue         (NEW)
    DocumentationPage.vue                (NEW — renders one markdown file)
  router/index.ts                        (one new route block under /documentation)
```

After the user reviews and approves, `git push` from
Herald.Documentation lights up the pilot. The website side is
Dawn's to land — this proposal is the handoff.
