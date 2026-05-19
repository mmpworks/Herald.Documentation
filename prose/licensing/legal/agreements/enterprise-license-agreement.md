---
title: Herald Enterprise License Agreement (Draft)
slug: licensing/legal/agreements/enterprise-license-agreement
category: legal
audience: counsel, sales, customer-procurement, customer-legal
reading-level: formal-legal (NOT high-school - this is a contract)
since: 2.1
status: draft
last-reviewed: 2026-05-19
source-of-truth: prose/licensing/legal/agreements/enterprise-license-agreement.md
related:
  - prose/licensing/legal/agreements/pro-license-agreement.md
  - data/licensing/nag-templates/manifest.json
  - docs/_wip/capability-composition-plan-v1.md
counsel-review-required: true
jurisdiction: Texas (Steve-ratified 2026-05-19). Williamson County venue (per Pro Agreement Section 12.1).
sla-posture: AS-IS, no service-level agreement (Steve-ratified 2026-05-19). Schedule A states the no-SLA stance in formal-legal voice.
compliance-posture: Customer-operated software; MMPWorks does not host or process Customer Data. Schedule B states the no-Business-Associate / no-Processor stance verbatim per Steve 2026-05-19.
---

> **FIRST DRAFT - COUNSEL REVIEW REQUIRED BEFORE DEPLOYMENT.** This
> document has not been reviewed by licensed legal counsel and is not
> authorized for production use. Use only as a starting point for
> counsel-led drafting. Steve-ratified facts (jurisdiction, venue,
> liability cap multiple, AS-IS SLA posture, no-Business-Associate
> compliance posture, DPA scope, BAA removal, indemnification
> carve-outs) have been folded into the draft as of 2026-05-19;
> counsel-language review is still required.

# Herald Enterprise License Agreement

This Herald Enterprise License Agreement (the "**Enterprise
Agreement**") is entered into as of the Effective Date by and
between **MMPWorks LLC**, a Texas limited liability company
("**MMPWorks**"), and the entity identified on the applicable Order
Form (the "**Customer**"). MMPWorks and Customer are each a
"**Party**" and collectively the "**Parties**".

---

## 1. Incorporation of Pro License Agreement

1.1 **Incorporation by reference.** Except as expressly modified or
superseded by this Enterprise Agreement, the terms of the Herald Pro
License Agreement published at
`prose/licensing/legal/agreements/pro-license-agreement.md` (the
"**Pro Agreement**") are hereby incorporated into this Enterprise
Agreement by reference and shall apply to Customer's licensed use of
the Software.

1.2 **Order of precedence.** In the event of any conflict between
this Enterprise Agreement and the Pro Agreement, this Enterprise
Agreement shall control with respect to the conflicting term. The
Order Form shall control over both this Enterprise Agreement and the
Pro Agreement with respect to any term expressly addressed on the
Order Form (such as fees, Capability Set, Tier, Segment, and
Initial Term).

1.3 **Defined terms.** Capitalized terms used but not defined in
this Enterprise Agreement have the meanings set forth in the Pro
Agreement.

1.4 **Tier.** For purposes of this Enterprise Agreement, the
permitted Tier value encoded in the License Token's `prd` claim is
`enterprise`.

---

## 2. Enterprise Capability Set

2.1 **Capability Set.** The Capability Set for an Enterprise Tier
license shall include, at minimum, all Capabilities mapped to the
Enterprise preset in the Catalog, and any additional Capabilities
expressly set forth on the Order Form.

2.2 **Application of Pro Section 2.3 (Contract Year invariant).**
The Contract Year invariant in Section 2.3 of the Pro Agreement
applies with full force to this Enterprise Agreement. MMPWorks shall
not, during an active Contract Year, remove, revoke, or restrict any
Capability that was granted to Customer at the start of that
Contract Year.

2.3 **Application of Pro Section 2.2 (Capability composition).**
The additive-expansion provision in Section 2.2(b) of the Pro
Agreement applies with full force to this Enterprise Agreement.
Capability additions published to the Catalog during the Contract
Year shall be made available to Customer at no additional charge.

---

## 3. Multi-Tenant Rights

3.1 **Tenant-level capability resolution.** Customer is granted the
right to operate the Software in multi-tenant mode, in which
Customer's installations resolve Capability Sets per tenant rather
than per installation. The technical mechanism for tenant-level
resolution is set forth in the Documentation.

3.2 **Tenant-level audit.** MMPWorks's audit cooperation right under
Section 3.2 of the Pro Agreement extends, in this Enterprise
Agreement, to tenant-level configuration, License Token allocation
across tenants, and tenant-level Capability Set assignment.

3.3 **Customer responsibility for tenants.** Customer is solely
responsible for (a) the lawful operation of the Software with
respect to each of Customer's tenants, (b) any agreements between
Customer and its tenants, and (c) any costs, fees, charges, or
liabilities arising from the operation of the Software on behalf of
Customer's tenants. The cost-overrun acknowledgement in Section 8.1
of the Pro Agreement (as restated in Section 8 below) applies in
full to tenant-attributable costs.

---

## 4. FFIEC and Compliance Representations

4.1 **FFIEC chain-of-custody representation.** Where Customer
licenses the Compliance Pack add-on or the TesseraSeal product
alongside this Enterprise Agreement, MMPWorks represents that the
Software supports the production of audit chains in the chain-of-
custody format described in the Federal Financial Institutions
Examination Council ("**FFIEC**") canonical strings specification
published in the Documentation. MMPWorks further represents that the
audit chains produced under such configuration are verifiable
against the FFIEC canonical strings using the verifier tooling
shipped with the Software. The FFIEC-conformance representations in
this Section 4.1 are auditable using the technical capabilities
described in Schedule B (Compliance Posture), including HMAC
integrity tagging, Merkle-tree sealing, and Hardware Security Module
integration.

4.2 **No certification.** Notwithstanding Section 4.1, MMPWorks
does not represent that the Software is itself FFIEC-certified,
examiner-approved, or audit-ready out of the box. Customer is
responsible for engaging its own auditors and examiners and for
ensuring that the Software, as configured by Customer, satisfies
Customer's regulatory obligations.

4.3 **Compliance posture.** MMPWorks's representations regarding
Customer's compliance with SOC 2, HIPAA, GDPR, CCPA, FFIEC guidance,
PCI DSS, and any other regulatory framework are set forth in
Schedule B (Compliance Posture). Customer acknowledges that MMPWorks
does not host or process Customer Data and that Customer is solely
responsible for its own compliance status under each such framework.

---

## 5. Service Level Agreement

5.1 **AS-IS uptime; no service-level agreement.** The Software is
provided to Customer on an AS-IS basis with respect to uptime,
availability, and response performance. Herald is software operated
by Customer on Customer's own hardware or cloud account. MMPWorks
LLC provides no uptime guarantee, no response-time service level
agreement, and no service credit. The full statement of MMPWorks's
service-level posture is set forth in Schedule A.

5.2 **No SLA remedies.** Customer acknowledges that no service
credits, refunds, or other SLA-based remedies are available under
this Enterprise Agreement. Any commitments regarding uptime,
response time, or service credits must be set forth in a separately
executed Service Order signed by both Parties; absent such Service
Order, no such commitments exist.

---

## 6. Support

6.1 **Premium support.** During the Term, MMPWorks shall provide
Customer with premium support in accordance with the support terms
set forth in **Schedule A** or in a separately executed Service
Order, including without limitation channel availability, response
time targets, and named technical contact.

6.2 **Excluded from support.** Items excluded from premium support
shall be set forth in Schedule A and shall include, at minimum, (a)
issues caused by Customer's modification of the Software, (b)
issues caused by Customer's use of the Software in violation of
this Enterprise Agreement, (c) issues attributable to third-party
software, services, or infrastructure not provided by MMPWorks, and
(d) issues attributable to Customer's hardware, cloud account,
network, or operating environment, which are Customer's sole
responsibility.

---

## 7. Data Processing

7.1 **Data Processing Addendum not applicable.** A Data Processing
Addendum is not applicable to this Enterprise Agreement. MMPWorks
does not host or process Customer Data. Customer operates the
Software on Customer's own hardware or cloud account, and all
processing of Customer Data occurs on infrastructure controlled by
Customer. The compliance posture set forth in Schedule B applies.

7.2 **No Business Associate role.** MMPWorks does not act as a
Business Associate under HIPAA. Customer is responsible for any
required Business Associate Agreements with its own infrastructure
providers and downstream vendors.

---

## 8. Restatement and Modification of Limitation of Liability

8.1 **Restatement of Pro Section 8.1.** The cost-overrun
acknowledgement in Section 8.1 of the Pro Agreement applies in full
to this Enterprise Agreement. Customer expressly acknowledges and
agrees that all costs, fees, charges, and liabilities arising from
continued event dispatch by the Software during the Grace Period or
following revocation of a License Token — **including without
limitation** cloud service usage, network egress, storage charges,
third-party API consumption, vendor billing of any kind, and any
other costs, damages, or claims incurred during such continued
operation — are **solely and exclusively the responsibility of
Customer**. MMPWorks shall have no liability whatsoever for any
such costs, damages, or claims. This Section 8.1 applies on a
per-tenant basis where Customer operates the Software in multi-
tenant mode.

8.2 **Enterprise liability cap.** Section 8.3 of the Pro Agreement
(cap on liability) is hereby modified for this Enterprise Agreement
to provide: each Party's aggregate liability arising out of or
related to this Enterprise Agreement shall not exceed the fees paid
by Customer to MMPWorks under this Enterprise Agreement during the
**twenty-four (24) months** immediately preceding the event giving
rise to the claim. All other provisions of Section 8 of the Pro
Agreement (including the exclusion of consequential damages and the
restatement-in-operator-notices clause) apply without modification.

8.3 **Carve-outs from Enterprise cap.** The liability cap in
Section 8.2 above shall not apply to (a) a Party's breach of
Section 7 (Confidentiality) of the Pro Agreement, (b) Customer's
indemnification obligations under Section 9.3 of the Pro Agreement,
(c) MMPWorks's indemnification obligations under Section 9.1 of the
Pro Agreement, or (d) liability for amounts payable to unaffiliated
third parties pursuant to indemnification obligations.

---

## 9. Term and Termination

9.1 **Initial Term.** The Initial Term of this Enterprise Agreement
shall be as set forth on the applicable Order Form and shall be
twelve (12) months unless otherwise specified on the Order Form.

9.2 **Renewal.** Section 10.1 of the Pro Agreement (automatic
renewal) applies; provided, however, that the non-renewal notice
period for this Enterprise Agreement shall be **sixty (60) days**
(rather than thirty (30) days as in the Pro Agreement) prior to the
end of the then-current term.

9.3 **Effect of termination on Schedule A.** Upon termination or
expiration of this Enterprise Agreement, the service level and
support commitments in Schedule A cease, and MMPWorks shall have no
further obligation to provide premium support or service credits.
All other survival provisions in Section 10.5 of the Pro Agreement
apply, together with the survival of Sections 4 (FFIEC and
Compliance Representations), 8 (this Section 8, including the
modified cap), and this Section 9.3.

---

## 10. Order of Precedence; Conflict Resolution

10.1 **Hierarchy of documents.** In the event of conflict, the
following hierarchy controls (highest to lowest): (a) Order Form;
(b) separately executed Service Order, where any exists; (c) this
Enterprise Agreement; (d) Schedule A (Service-Level Posture); (e)
Schedule B (Compliance Posture); (f) Pro Agreement.

10.2 **Schedule incorporation.** All Schedules referenced in this
Enterprise Agreement are incorporated herein by reference upon
execution by both Parties. An unexecuted Schedule does not bind
either Party.

---

## 11. Miscellaneous

11.1 **Governing law and venue.** Section 12.1 of the Pro Agreement
applies without modification. This Enterprise Agreement is governed
by the laws of the State of Texas, and the Parties consent to the
exclusive jurisdiction of the state and federal courts located in
Williamson County, Texas.

11.2 **All other Pro Agreement miscellaneous provisions.** Sections
12.2 through 12.10 of the Pro Agreement (Notices, Assignment, Entire
Agreement, Amendment, Severability, Waiver, Force Majeure,
Independent Contractors, and Counterparts) apply to this Enterprise
Agreement without modification.

---

**END OF ENTERPRISE AGREEMENT**

---

## Schedule A - Service-Level Posture

**AS-IS uptime; no service-level agreement.** Herald is software
operated by the Customer on the Customer's own hardware or cloud
account. MMPWorks LLC provides no uptime guarantee, no response-time
service-level agreement, and no service credit.

MMPWorks does not operate the infrastructure on which the Software
runs, does not control the network or operating environment, and
does not have access to Customer's deployment. Uptime,
availability, response performance, and capacity are therefore
under Customer's exclusive control. Any service-level commitment
must be set forth in a separately executed Service Order signed by
both Parties; absent such Service Order, no such commitment exists.

Premium support, where available, is provided on a commercially
reasonable basis and is not a service-level commitment.

---

## Schedule B - Compliance Posture

Herald is software whose function is to transport, transform, and
persist Customer log and event data between the Customer's data
sources and the Customer's chosen sinks. MMPWorks LLC ships Herald
Pro and Herald Enterprise for the Customer to install and operate
on the Customer's own hardware or cloud account. MMPWorks does not
host, operate, route, store, or otherwise process Customer Data on
its own infrastructure.

Accordingly, the Customer is solely responsible for compliance with
all laws and regulations applicable to its data and its operations,
including without limitation HIPAA, GDPR, CCPA, FFIEC guidance, PCI
DSS, SOC 2 controls, and any other regulatory framework. MMPWorks
LLC makes no representation, warranty, or certification regarding
the Customer's compliance status under any such framework.

Herald Enterprise provides technical capabilities — including
FFIEC-canonical chain-of-custody construction, HMAC integrity
tagging, Merkle-tree sealing, and Hardware Security Module
integration — that the Customer may use to support its own
compliance posture. These capabilities are tools; their correct
use, sufficiency for the Customer's specific regulatory obligations,
and audit-readiness are the Customer's responsibility.

MMPWorks does not act as a Business Associate under HIPAA, a Data
Processor or Sub-Processor under GDPR, or comparable roles under
any regulatory framework, because MMPWorks does not host or access
Customer Data.

---

> **FIRST DRAFT - COUNSEL REVIEW REQUIRED BEFORE DEPLOYMENT.**
