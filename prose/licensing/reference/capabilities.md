---
title: Capability catalog
slug: licensing/reference/capabilities
category: reference
audience: mmpworks-operator, sales, customer-IT
reading-level: high-school (target = "no glossary needed")
since: 2.1
status: published
last-reviewed: 2026-05-19
source-of-truth: data/licensing/capabilities/*.json
related:
  - prose/licensing/operator-runbook/02-issuing-a-license.md
  - prose/licensing/explanation/how-licensing-works.md
  - docs/_wip/capability-composition-plan-v1.md
---

# Capability catalog

A license decides what a customer's installation is allowed to do. Until
now the decision was a single label: Pro, Enterprise, or TesseraSeal.
Starting in 2.1, the license carries a list of **capabilities**. Each
capability is a small, named permission the customer's installation
reads to know which features it can turn on.

The label is still there. A customer who buys "Pro" still picks Pro on
the order form. Behind the scenes, Pro expands into the capability list
the license actually carries. And a customer who wants Pro plus one
extra feature can have exactly that, without paying for the whole
Enterprise tier.

This page lists every capability the catalog ships with, what it lets
the customer do, and where it normally lives in the SKU lineup.

> :bulb: **Quick picture.** Think of a license as a key ring instead of
> a single key. The Pro ring has three keys on it. The Enterprise ring
> has seven. The catalog below is the list of every key that exists and
> what door each one opens. Most customers take a pre-built ring off
> the shelf (the Pro or Enterprise preset). The few who need a custom
> set get exactly the keys they want. Same shape, same locks, just a
> different selection.

## How the catalog is used

Three audiences read this same list:

- **The operator portal** turns every entry below into a checkbox. The
  operator picks a preset (Pro, Enterprise, TesseraSeal) and the right
  boxes light up. They can tick extras on or off before saving.
- **The customer's installation** reads the same list to know which
  features it's allowed to turn on. The list lives inside the license
  file the customer received.
- **Sales and the documentation site** read this page to explain what
  each capability does in plain English.

All three reads come from one file per capability in
`data/licensing/capabilities/`. Edit the JSON once; the portal checkbox
text, the C# code that enforces the capability, and this page all
regenerate.

> :bulb: **Why one source.** When the same fact lives in three places,
> two of them go out of date. Keeping the capability description in one
> file and rendering everything else from it removes that drift
> problem. Herald uses the same pattern for its sink catalog and
> configuration reference. It is CUPID's Composable property applied to
> documentation: the entries are the parts, and the renders are the
> compositions.

## The 12 capabilities

The catalog ships with 12 capabilities. The columns are the same shape as
the portal's checkbox list: a plain-English name, a one-line summary, and
the tier where the capability normally lives.

### Basic features

#### Pro features

`pro-base`. Normally a **Pro** capability.

Lets the customer use the Pro pipeline features that ship with every
paid Pro license.

Turns on the standard Pro toolset: advanced filtering, premium template
options, and the richer pipeline configuration the free tier doesn't
include. This is the floor every Pro license starts from. If the
customer asked for "Pro," this is the box that gets checked first. The
other Pro-adjacent boxes layer on top.

#### Advanced event editing

`event-processing-pro`. Normally a **Pro** capability.

Lets the customer redact, rename, or transform log events as they pass
through the pipeline.

Turns on the editors that change what an event looks like before it
leaves the pipeline. Common uses: hiding credit card numbers, renaming
fields to match a customer's existing format, or splitting one event
into two. Customers with privacy or formatting requirements need this.
Customers happy with logs as-they-come don't.

### Resilience

#### Keep working when things break

`resilience-decorators`. Normally a **Pro** capability.

Lets the customer add automatic retry, circuit-break, and
buffer-to-disk protections to their log pipeline.

Think of it as a safety net for the log pipeline. When a downstream
system gets slow or stops responding, this turns on the protections
that retry, slow down, or temporarily save events to disk instead of
dropping them. Customers running production workloads almost always
want this on. Customers running a quick demo usually don't need it.

#### Advanced pipeline shapes

`advanced-strategies`. Normally an **Enterprise** capability.

Lets the customer use the high-performance and special-purpose pipeline
arrangements (fast path, flight recorder, custom orderings).

Turns on the pipeline arrangements that go beyond the standard "events
in, events out" shape. The fast path makes the hot route as quick as
possible. The flight recorder keeps a rolling buffer of recent events
so the team can replay what happened during an incident. Custom
orderings let the customer reshape the pipeline to match an unusual
workflow. Customers running heavy production workloads or doing
incident-response work usually want this on.

### Multi-tenancy

#### Serve multiple customer organizations

`multi-tenant`. Normally an **Enterprise** capability.

Lets one installation handle logging for several separate customer
organizations at the same time, keeping each one's data isolated.

> :bulb: **Quick picture.** Think of an apartment building. One
> building, but each unit is fully sealed off from the others.
> Different keys for different doors, mailboxes that don't connect, no
> shared anything. This turns on the same shape for log pipelines: one
> server installation can serve many customer organizations and keep
> each one's events, settings, and dashboards isolated. Almost always
> what providers (MSPs) need. Rarely what a single-company customer
> needs.

### Audit and compliance

#### Audit chain and regulated-industry protections

`compliance-overlay`. Normally a **Compliance Pack** add-on.

Lets the customer turn on the audit-chain and personal-information
protections that regulated industries require.

> :bulb: **Quick picture.** Think of a chain-of-custody log at a
> hospital pharmacy. Every handoff is signed. The chain can't be edited
> without leaving a mark. This turns on the same shape for log events,
> plus the personal-information redactions that SOC2, HIPAA, FINRA, and
> PCI customers need to pass an audit. Customers in regulated
> industries almost always need this. Everyone else can leave it off.
> This is the Compliance Pack add-on box.

Compliance Pack is an add-on, not a license on its own. Customers buy
Pro Team, Pro Fleet, or Pro Enterprise and attach this capability. The
parent license keeps working unchanged. This box just turns on the
extras.

#### Banking audit-chain format

`ffiec-chain`. Normally a **TesseraSeal** capability.

Lets the customer produce audit chains in the FFIEC chain-of-custody
format banks and bank examiners expect.

> :bulb: **Quick picture.** Think of a tamper-evident envelope a bank
> courier uses. Sealed at the source. Every handoff signed. Opening it
> without a record is impossible. FFIEC is the specific shape of that
> envelope U.S. bank examiners look for. This turns on the matching
> audit-chain output. Customers in banking, credit unions, or anyone
> the FFIEC examines need this. Everyone else can leave it off.

Turning this on also turns on `compliance-overlay` automatically. You
can't produce FFIEC chains without the audit-chain machinery
underneath.

#### Audit data feed for Python tools

`audit-aggregation-py`. Normally a **TesseraSeal** capability.

Lets a separate Python aggregator pull audit data out of the customer's
audit pipeline.

Customers running the Python audit aggregator (a separate tool that
bundles audit chains into reports for regulators) need this box checked
so the aggregator is allowed to read the audit feed. If the customer
isn't using the Python aggregator, leave this off. It doesn't do
anything else.

#### Tag events with audit profiles

`tesseraseal-audit-profiles`. Normally a **TesseraSeal** capability.

Lets the customer mark events with audit profiles (SOC2, HIPAA, FINRA,
PCI) and have the runtime enforce the matching rules.

> :bulb: **Quick picture.** Think of color-coded folders in a filing
> cabinet. Red for HIPAA, blue for PCI, green for SOC2. And a rule that
> says "red folders never leave the building." This turns on the
> matching shape for log events: developers tag the events that belong
> to a regulated profile, and the runtime enforces the rules for that
> profile (where it can go, how long it lives, who can read it).
> Customers running mixed-workload systems where some events are
> regulated and most aren't need this. Single-profile customers usually
> don't.

Turning this on also turns on `compliance-overlay` automatically.

### Premium destinations

#### Premium destination types

`premium-sinks`. Normally an **Enterprise** capability.

Lets the customer send logs to the premium destinations (Splunk,
Datadog, the cloud-only sinks).

Turns on the destinations that need extra licensing or a paid
integration on the receiving side. Splunk, Datadog, and similar
enterprise-only systems live behind this box. The standard destinations
(files, common cloud storage, OpenTelemetry) work without it. If the
customer asks "can I send logs to Splunk?" this is the box that answers
yes.

### Provider features

#### Manage licenses for downstream customers

`msp-billing`. Normally a **Pro Provider** capability.

Lets a managed-service provider issue and bill for licenses on behalf
of the customer organizations they serve.

For Provider customers (the MSPs who resell our product to their own
customers). This turns on the reporting and billing-handoff features
they need so the licenses they hand to their customers get tracked back
to the Provider's account. Direct customers (companies running their
own logging) never need this. Only check it for Provider segment
licenses.

This capability goes hand-in-hand with the MSP Terms of Service
click-through during onboarding. If `msp-billing` is checked but the
TOS isn't accepted, the portal blocks the mint. See operator-runbook
article 10.

### Developer mode

#### Stamp every event with a Demo tag

`demo-watermark`. Normally a **Pro Developer** capability. **Sentinel.
Not a customer-facing feature.**

Turns on the Demo watermark the free Pro Developer tier carries.

Internal sentinel. When present, the customer's instances stamp every
log event with a `LicenseTier: Demo` property as it leaves the
pipeline. That's the shape of the free Pro Developer tier. It's how
customers and downstream tools tell free-tier traffic apart from paid
traffic. Don't check this on a paid license. It would tag the
customer's production events with the Demo marker.

The portal hides this row by default. It appears only when the operator
picks the Pro Developer preset. That preset checks the box
automatically and locks it. If a customer asks "how do I get rid of the
Demo tag?" the answer is "upgrade to Pro Team," which mints a token
without `demo-watermark`.

## The presets

A preset is a pre-built capability list the operator can pick with one
click. Eight presets ship today; more can be added as new SKUs land.

| Preset | What's in the box |
|---|---|
| **Pro** (no segment) / **Pro Team** | `pro-base`, `resilience-decorators`, `event-processing-pro` |
| **Pro Developer** | Pro + `demo-watermark` |
| **Pro Fleet** | Same as Pro Team (segment is for billing, not capabilities) |
| **Pro Provider** | Pro + `msp-billing` |
| **Pro Enterprise** | Same as the Enterprise preset below. The full set. |
| **Enterprise** | Pro + `multi-tenant` + `advanced-strategies` + `premium-sinks` + `compliance-overlay` |
| **TesseraSeal** | `compliance-overlay` + `ffiec-chain` + `audit-aggregation-py` + `tesseraseal-audit-profiles` |
| **Pro + Compliance Pack** | Pro preset + `compliance-overlay`. The add-on case, checked manually. |

> :bulb: **Why Pro Enterprise carries the full Enterprise cap-set.**
> The $50K+ Pro Enterprise tier is priced at the same level as
> Enterprise. Customers buying it expect every capability Enterprise
> customers get. The difference between the two SKUs is the
> contracting and support shape, not the feature list.

## How the catalog stays consistent

Operators and sales don't have to think about this part. The shape
matters anyway, because it's how the catalog stays trustworthy.

```mermaid
flowchart LR
    src[data/licensing/capabilities/*.json<br/>data/licensing/presets/*.json]
    schema[schemas/licensing/*.schema.json]

    src -.validates against.-> schema

    src --> minter[Minter<br/>MMP.Licensing<br/>server side]
    src --> verifier[Verifier<br/>MMP.Licensing.Contracts<br/>client side]
    src --> portal[Operator portal<br/>MMP.Licensing.Portal<br/>checkbox UI]
    src --> docs[This page<br/>customer-facing reference]
    src --> manifest[/api/system/capabilities<br/>per-build manifest endpoint/]

    minter --> token[Signed license token<br/>caps[] claim]
    verifier --> gates[HeraldCapabilityGate.Require]
    portal --> ux[Operator picks preset<br/>+ extras]
    manifest --> dashboard[Dashboard mismatch warnings]
```

All five reads (minter, verifier, portal, this page, manifest) pull
from the same JSON files under `data/licensing/`. A capability that
gets renamed, retired, or added shows up everywhere at once. A
capability that exists in one place but not another is a build-time
failure. The schema validator catches it before the renderer runs.

The C# side (`EditionCapabilityPresets.cs` in `MMP.Licensing.Contracts`)
is regenerated from the same JSON during the licensing build. Glenn
maintains the generator. The catalog files are the source.

## Adding or retiring a capability

Adding a capability is a small PR. The discipline matters because the
catalog is closed by default. Only capabilities listed here are valid
in a license. Letting it grow without review is how the portal turns
into a 50-checkbox feature-flag screen no operator wants to read.

The procedure:

1. Open a PR that adds a new JSON file under
   `data/licensing/capabilities/`. The schema validates the shape.
2. The display name, summary, and tooltip must follow the no-jargon
   discipline. IT operators read these, not Herald developers.
3. Bump the minor version of `MMP.Licensing.Contracts`.
4. Steve reviews and merges.
5. The renderer regenerates the portal data, this page, and the C#
   preset table on the next build.

Retiring a capability follows the same shape with `status: "deprecated"`
and a `replacedBy:` pointer. The portal renders deprecated rows with a
strikethrough. Existing tokens carrying the deprecated capability keep
working. Removal waits for the next major version of
`MMP.Licensing.Contracts`.

## What's NOT a capability

Some things look like they could be capabilities but deliberately
aren't:

- **Instance count.** That's a limit, carried in the `lim` claim, a
  separate part of the license. Capabilities are yes/no. Limits are
  numbers.
- **Term length.** That's the expiry date on the license. Not a
  capability.
- **Per-tenant overlays.** "Tenant A has compliance-overlay but Tenant
  B doesn't" is a 2.x roadmap item, not a v1 shape. The catalog grants
  apply at the process level today.
- **Region restrictions.** "This license works in the EU but not the
  US" would be a separate kind of claim. Not on the roadmap.

If a future feature request looks like it might be a capability, the
test is: does it answer the question *can this customer use this
feature, yes or no?* Answer yes, it's a capability. Answer "kind of"
or "depending on," it's something else, and trying to model it as a
capability would muddy the catalog.
