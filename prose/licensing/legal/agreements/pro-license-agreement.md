---
title: Herald Pro License Agreement (Draft)
slug: licensing/legal/agreements/pro-license-agreement
category: legal
audience: counsel, sales, customer-procurement
reading-level: formal-legal (NOT high-school - this is a contract)
since: 2.1
status: draft
last-reviewed: 2026-05-19
source-of-truth: prose/licensing/legal/agreements/pro-license-agreement.md
related:
  - prose/licensing/legal/agreements/enterprise-license-agreement.md
  - data/licensing/nag-templates/manifest.json
  - docs/_wip/capability-composition-plan-v1.md
counsel-review-required: true
jurisdiction: Texas (Steve-ratified 2026-05-19). Williamson County venue.
---

> **FIRST DRAFT - COUNSEL REVIEW REQUIRED BEFORE DEPLOYMENT.** This
> document has not been reviewed by licensed legal counsel and is not
> authorized for production use. Use only as a starting point for
> counsel-led drafting. Steve-ratified facts (jurisdiction, venue,
> liability cap multiple, indemnification carve-outs) have been
> folded into the draft as of 2026-05-19; counsel-language review is
> still required.

# Herald Pro License Agreement

This Herald Pro License Agreement (the "**Agreement**") is entered
into as of the Effective Date by and between **MMPWorks LLC**, a
Texas limited liability company with its principal place of business
in Texas ("**MMPWorks**"), and the entity identified on the
applicable order form, schedule, or online purchase record (the
"**Customer**"). MMPWorks and Customer are each a "**Party**" and
collectively the "**Parties**".

---

## 1. Definitions

The following capitalized terms have the meanings set forth below.
Other capitalized terms are defined inline where they first appear.

1.1 "**Capabilities**" means the discrete, named functional
permissions enumerated in the capability catalog published at
`https://herald.dev/licensing/capabilities` (the "**Catalog**"),
each of which represents a specific permitted use of the Software.

1.2 "**Capability Set**" means the set of Capabilities granted to
Customer under this Agreement, as encoded in the License Token's
`caps` claim and, where applicable, expanded from the `prd` and
`seg` claims pursuant to the Catalog. The initial Capability Set is
set forth in the applicable Order Form.

1.3 "**Contract Year**" means each successive twelve (12) month
period beginning on the Effective Date and on each anniversary
thereof during the Term.

1.4 "**Documentation**" means the user and operator documentation
for the Software made available by MMPWorks at
`https://mmpworks.com/herald/docs` or any successor location.

1.5 "**Effective Date**" means the date set forth on the applicable
Order Form, or, if no date is specified, the date on which Customer
first receives a License Token from MMPWorks.

1.6 "**Grace Period**" means the sixty (60) day period commencing on
the day immediately following the expiration date of the License
Token, during which the Software continues to operate in Demo Mode
as described in Section 4.4.

1.7 "**License Token**" means the cryptographically signed token
issued by MMPWorks pursuant to this Agreement that encodes
Customer's Capability Set, Tier, Segment, expiration, and other
license metadata.

1.8 "**Order Form**" means the ordering document, online purchase
record, or quote signed or accepted by Customer that references this
Agreement and identifies the Tier, Segment, Capability Set, and
fees.

1.9 "**Segment**" means the customer-facing segment identifier
encoded in the License Token's `seg` claim. Permitted Segment values
are: Developer, Team, Fleet, Provider, and Enterprise.

1.10 "**Software**" means Herald Pro and any updates, upgrades,
patches, and modifications thereto made available to Customer by
MMPWorks during the Term.

1.11 "**Tier**" means the product tier identifier encoded in the
License Token's `prd` claim. Permitted Tier values for this
Agreement are: pro.

1.12 "**Term**" has the meaning set forth in Section 10.1.

---

## 2. Grant of License

2.1 **License grant.** Subject to Customer's payment of all fees
when due and Customer's compliance with the terms of this Agreement,
MMPWorks hereby grants to Customer a non-exclusive,
non-transferable, non-sublicensable license, during the Term, to
install and use the Software solely for Customer's internal business
purposes, in the Tier and Segment, and subject to the Capability
Set, set forth on the applicable Order Form.

2.2 **Capability composition.** Customer acknowledges and agrees
that:

(a) the license granted under this Agreement is defined by the
Capability Set encoded in the License Token, and not by any tier
name, marketing description, or general representation;

(b) MMPWorks may at any time during the Term **additively expand**
the Capability Set associated with Customer's Tier and Segment by
publishing additions to the Catalog, and any such additions shall be
made available to Customer at no additional charge for the remainder
of the then-current Contract Year; and

(c) the canonical Capability Set in effect at any time is the
Capability Set encoded in the most recently issued License Token,
as expanded by the Catalog version pinned thereto.

2.3 **Contract Year invariant.** MMPWorks shall not, during an
active Contract Year, remove, revoke, or restrict any Capability
that was granted to Customer at the start of that Contract Year.
Removal of a Capability from Customer's Capability Set may occur
only at the boundary of a Contract Year and only upon notice to
Customer at or before renewal. This Section 2.3 is a material
commitment of MMPWorks to Customer and shall survive any change to
the Catalog or to the Software.

2.4 **Permitted use.** The license granted under this Section 2 is
limited to:

(a) installation of the Software on the number of installations or
cloud virtual machines (each an "**Instance**") corresponding to
Customer's Tier and Segment, as set forth on the applicable Order
Form;

(b) use of the Capabilities encoded in Customer's Capability Set;
and

(c) use solely for Customer's internal business purposes, except
where Customer's Segment is Provider, in which case use on behalf of
Customer's end customers is permitted subject to Section 2.5.

2.5 **Provider Segment.** Where Customer's Segment is Provider,
Customer may operate the Software on behalf of Customer's end
customers solely pursuant to a managed-service provider terms of
service separately executed between Customer and MMPWorks. Absent
such terms of service, the Provider Segment is not licensed.

---

## 3. Restrictions

3.1 **Customer shall not:**

(a) copy, modify, adapt, translate, or create derivative works of
the Software, except as expressly permitted by this Agreement or
applicable law;

(b) reverse engineer, decompile, disassemble, or otherwise attempt
to derive the source code, structure, sequence, or organization of
the Software, except to the extent such restriction is expressly
prohibited by applicable law;

(c) rent, lease, lend, sell, sublicense, assign, distribute,
publish, transfer, or otherwise make available the Software to any
third party, except as expressly permitted under Section 2.5
(Provider Segment);

(d) remove, alter, or obscure any proprietary notices (including
copyright and trademark notices) of MMPWorks or its suppliers on the
Software or any copy thereof;

(e) use the Software in any manner that exceeds Customer's
Capability Set, Tier, Segment, or Instance count, or that
circumvents any technical limitation or license verification
mechanism of the Software;

(f) use the Software to develop a product or service that competes
with the Software; or

(g) use the Software in violation of any applicable law or
regulation.

3.2 **Audit cooperation.** Customer shall, on no fewer than thirty
(30) days' written notice, cooperate with MMPWorks's verification
that Customer's use of the Software conforms to the Tier, Segment,
Instance count, and Capability Set licensed under this Agreement.
Where Customer's Segment is Team, Fleet, or Provider, such
verification may include MMPWorks's review of License Token
check-in records for the Instances licensed to Customer. Audits
shall be conducted during normal business hours and shall not
unreasonably interfere with Customer's business operations.

---

## 4. License Token, Expiration, and Grace Period

4.1 **Issuance.** MMPWorks shall issue Customer a License Token
upon execution of this Agreement and upon each renewal. Customer
shall install the License Token on each Instance.

4.2 **Verification.** The Software shall periodically verify the
License Token against MMPWorks's licensing service. The cadence and
mechanism of such verification are set forth in the Documentation
and may be updated by MMPWorks from time to time.

4.3 **Expiration.** Each License Token includes an expiration date.
Upon expiration, the License Token enters the Grace Period.

4.4 **Grace Period - Demo Mode.** During the Grace Period, the
Software shall continue to operate; provided, however, that:

(a) the Software shall stamp each emitted event with a
"`LicenseTier: Demo`" property, signaling to downstream sinks and
dashboards that the Software is operating under an expired license;

(b) the Software shall display the operator notice set forth in
`data/licensing/nag-templates/expired-paid-day-1-30.txt` (the
"**Soft Reminder**") on each day of the Grace Period from Day 1
through Day 31; and

(c) from Day 32 through Day 60 of the Grace Period, the Software
shall display the operator notice set forth in
`data/licensing/nag-templates/expired-paid-day-32-60.txt` (the
"**Stern Notice**"), which incorporates the acknowledgements and
waivers set forth in Section 8 below.

4.5 **Termination of Grace Period.** On Day 61 following expiration,
the Software shall cease publishing events to all configured sinks
on each affected Instance until a valid License Token is installed.

4.6 **Continued operation at Customer's risk.** Customer
acknowledges that continued operation of the Software during the
Grace Period is at Customer's sole risk and that the limitations of
liability set forth in Section 8 apply with full force during the
Grace Period.

---

## 5. Fees and Payment

5.1 **Fees.** Customer shall pay the fees set forth in the
applicable Order Form. Fees are payable in U.S. dollars and are
non-refundable except as expressly provided herein.

5.2 **Taxes.** Fees are exclusive of any taxes, levies, duties, or
similar governmental assessments, including value-added,
sales-and-use, or withholding taxes. Customer is responsible for all
such taxes, except for taxes based on MMPWorks's net income.

5.3 **Late payment.** Any amounts not paid when due shall accrue
interest at the lesser of one and one-half percent (1.5%) per month
or the maximum rate permitted by applicable law.

5.4 **Suspension for non-payment.** MMPWorks may suspend the
License Token if any fee is more than thirty (30) days past due,
following written notice and a reasonable cure opportunity.
Suspension under this Section 5.4 shall trigger the Revoked-state
notice procedures of Section 10.4.

---

## 6. Intellectual Property

6.1 **Ownership.** MMPWorks and its licensors retain all right,
title, and interest in and to the Software, including all
intellectual property rights therein. No rights are granted to
Customer hereunder other than the limited license expressly set
forth in Section 2.

6.2 **Feedback.** If Customer provides MMPWorks with any
suggestions, ideas, or feedback regarding the Software ("**Feedback**"),
Customer hereby grants MMPWorks a perpetual, irrevocable, worldwide,
royalty-free license to use, modify, and incorporate such Feedback
into the Software without restriction or attribution.

---

## 7. Confidentiality

7.1 **Confidential Information.** "Confidential Information" means
non-public information disclosed by one Party (the "**Discloser**")
to the other (the "**Recipient**") that is marked confidential or
that a reasonable person would understand to be confidential given
the nature of the information and the circumstances of disclosure.
MMPWorks's pricing, License Token internals, and non-public portions
of the Software are Confidential Information of MMPWorks.

7.2 **Obligations.** The Recipient shall (a) use the Confidential
Information solely to exercise its rights and perform its
obligations under this Agreement, and (b) protect the Confidential
Information using the same degree of care it uses to protect its own
confidential information of similar nature, but in no event less
than reasonable care.

7.3 **Exclusions.** Confidential Information does not include
information that (a) is or becomes publicly available without breach
of this Agreement, (b) was known to the Recipient prior to
disclosure without obligation of confidence, (c) is independently
developed by the Recipient without use of the Discloser's
Confidential Information, or (d) is rightfully received from a third
party without obligation of confidence.

7.4 **Compelled disclosure.** The Recipient may disclose
Confidential Information to the extent required by law or court
order, provided that the Recipient provides the Discloser with prompt
written notice (where legally permissible) and reasonable cooperation
in seeking a protective order.

---

## 8. Limitation of Liability

8.1 **Acknowledgement of cost-overrun risk during Grace Period and
following Revocation.** Customer expressly acknowledges and agrees
that all costs, fees, charges, and liabilities arising from
continued event dispatch by the Software during the Grace Period or
following revocation of a License Token — **including without
limitation** cloud service usage, network egress, storage charges,
third-party API consumption, vendor billing of any kind, and any
other costs, damages, or claims incurred during such continued
operation — are **solely and exclusively the responsibility of
Customer**. MMPWorks shall have no liability whatsoever for any such
costs, damages, or claims.

8.2 **Exclusion of consequential damages.** IN NO EVENT SHALL
MMPWORKS BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL,
CONSEQUENTIAL, PUNITIVE, OR EXEMPLARY DAMAGES, INCLUDING WITHOUT
LIMITATION LOST PROFITS, LOST REVENUES, LOST DATA, LOSS OF GOODWILL,
OR BUSINESS INTERRUPTION, ARISING OUT OF OR RELATED TO THIS
AGREEMENT OR THE SOFTWARE, WHETHER IN CONTRACT, TORT (INCLUDING
NEGLIGENCE), STRICT LIABILITY, OR ANY OTHER THEORY, EVEN IF MMPWORKS
HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

8.3 **Cap on liability.** EXCEPT FOR LIABILITY ARISING FROM (A) A
PARTY'S BREACH OF SECTION 7 (CONFIDENTIALITY), (B) CUSTOMER'S
INDEMNIFICATION OBLIGATIONS UNDER SECTION 9.2, OR (C) MMPWORKS'S
INDEMNIFICATION OBLIGATIONS UNDER SECTION 9.1, EACH PARTY'S
AGGREGATE LIABILITY ARISING OUT OF OR RELATED TO THIS AGREEMENT
SHALL NOT EXCEED THE FEES PAID BY CUSTOMER TO MMPWORKS UNDER THIS
AGREEMENT DURING THE TWELVE (12) MONTHS IMMEDIATELY PRECEDING THE
EVENT GIVING RISE TO THE CLAIM.

8.4 **Restatement in operator notices.** The acknowledgements and
waivers in this Section 8 are restated, in summary form, in the
Stern Notice and the Revoked-state notice rendered by the Software.
Such operator notices are intended to remind Customer of the
acknowledgements and waivers set forth herein and shall be construed
as supplementing, and not replacing, this Section 8.

8.5 **Allocation of risk.** Customer acknowledges that the
limitations and exclusions in this Section 8 are a material basis of
the bargain reflected in this Agreement and that MMPWorks would not
have entered into this Agreement on the agreed-upon fees absent such
limitations and exclusions.

---

## 9. Indemnification

9.1 **MMPWorks indemnification.** MMPWorks shall defend Customer
against any third-party claim that the Software, as provided by
MMPWorks and used by Customer in accordance with this Agreement,
infringes a valid United States patent, copyright, or trademark, or
misappropriates a trade secret, of such third party (an
"**Infringement Claim**"), and shall pay any final judgment or
settlement of such Infringement Claim approved by MMPWorks.
MMPWorks's obligations under this Section 9.1 are conditioned on
Customer (a) providing MMPWorks with prompt written notice of the
Infringement Claim, (b) giving MMPWorks sole control over the
defense and settlement, and (c) providing reasonable cooperation at
MMPWorks's expense.

9.2 **Exclusions to MMPWorks indemnification.** MMPWorks shall have
no obligation under Section 9.1 to the extent the Infringement Claim
arises from (a) Customer's modification of the Software, (b)
Customer's use of the Software in combination with non-MMPWorks
products where the Infringement Claim would not have arisen but for
such combination, (c) Customer's use of the Software in violation
of this Agreement, or (d) Customer's continued use of the Software
after notice of an alleged or actual infringement.

9.3 **Customer indemnification.** Customer shall defend MMPWorks
against any third-party claim arising from (a) Customer's use of the
Software in violation of this Agreement or applicable law, (b)
Customer's misuse of the Software, **(c) any cost, fee, charge, or
liability described in Section 8.1 arising from continued event
dispatch by the Software during the Grace Period or following
revocation of a License Token**, or (d) Customer's violation of any
agreement between Customer and any third party arising from
Customer's use of the Software, and shall pay any final judgment or
settlement of such claim approved by Customer.

9.4 **Sole remedy.** This Section 9 states each Party's sole
liability and the other Party's sole remedy for any third-party
claim covered by this Section 9.

---

## 10. Term and Termination

10.1 **Term.** This Agreement commences on the Effective Date and
continues for the subscription period set forth on the applicable
Order Form (the "**Initial Term**"), and shall thereafter
automatically renew for successive periods equal to the Initial Term
(each a "**Renewal Term**", and together with the Initial Term, the
"**Term**") unless either Party provides written notice of
non-renewal at least thirty (30) days prior to the end of the
then-current term.

10.2 **Termination for cause.** Either Party may terminate this
Agreement for cause upon thirty (30) days' written notice of a
material breach if such breach remains uncured at the end of such
notice period.

10.3 **License revocation.** MMPWorks may revoke a License Token,
without prior notice, upon (a) Customer's material breach of this
Agreement, (b) non-payment more than thirty (30) days past due
following the cure opportunity in Section 5.4, (c) Customer's
disputed charges that remain unresolved more than sixty (60) days
following dispute initiation, (d) suspected fraud, (e) suspected
abuse or violation of applicable law, or (f) any other ground set
forth in this Agreement. Revocation under this Section 10.3 shall
trigger the operator notice set forth in
`data/licensing/nag-templates/revoked.txt`.

10.4 **Effect of revocation.** Upon revocation, the Software shall
cease operation immediately on the next License Token verification
cycle on each affected Instance. Customer's obligation to pay fees
accrued through the date of revocation survives revocation.

10.5 **Effect of termination.** Upon termination or expiration of
this Agreement, (a) the license granted under Section 2 immediately
ceases, (b) Customer shall cease all use of the Software and shall
either return or destroy all copies of the Software in Customer's
possession or control, and (c) Sections 1, 3, 5 (for accrued
amounts), 6, 7, 8, 9, 10.4, 10.5, 11, and 12 shall survive.

---

## 11. Warranties and Disclaimers

11.1 **Mutual warranty.** Each Party represents and warrants that
(a) it has the full power and authority to enter into this
Agreement, and (b) its execution and performance of this Agreement
do not violate any other agreement to which it is a party.

11.2 **DISCLAIMER.** EXCEPT FOR THE EXPRESS WARRANTIES IN SECTION
11.1, THE SOFTWARE IS PROVIDED "AS IS" AND MMPWORKS HEREBY DISCLAIMS
ALL WARRANTIES, WHETHER EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE,
INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE, AND
NON-INFRINGEMENT. MMPWORKS DOES NOT WARRANT THAT THE SOFTWARE WILL
BE UNINTERRUPTED, ERROR-FREE, OR FREE OF HARMFUL COMPONENTS.

---

## 12. Miscellaneous

12.1 **Governing law and venue.** This Agreement shall be governed
by and construed in accordance with the laws of the State of Texas,
without regard to its conflict of laws principles. The Parties
consent to the exclusive jurisdiction of the state and federal
courts located in Williamson County, Texas for any action arising
out of or related to this Agreement.

12.2 **Notices.** All notices under this Agreement shall be in
writing and shall be deemed given when delivered by hand, by
nationally recognized overnight courier, or by certified mail
(return receipt requested) to the addresses set forth in the
applicable Order Form, or by email with confirmation of receipt to
the email addresses identified by the Parties for notice purposes.

12.3 **Assignment.** Neither Party may assign this Agreement
without the other Party's prior written consent, except that either
Party may assign this Agreement, without consent, to a successor in
connection with a merger, acquisition, reorganization, or sale of
substantially all of its assets, provided that the assignee assumes
all obligations hereunder.

12.4 **Entire agreement.** This Agreement, together with all Order
Forms and any documents incorporated by reference, constitutes the
entire agreement between the Parties with respect to its subject
matter and supersedes all prior agreements, understandings, and
communications, whether oral or written.

12.5 **Amendment.** No amendment to this Agreement is effective
unless in writing and signed by an authorized representative of each
Party. Click-through acceptance of an updated Agreement at the time
of License Token issuance or renewal shall constitute Customer's
signed amendment.

12.6 **Severability.** If any provision of this Agreement is held
invalid or unenforceable, that provision shall be reformed to the
minimum extent necessary to render it enforceable, and the remaining
provisions shall continue in full force and effect.

12.7 **Waiver.** No failure or delay by either Party in exercising
any right under this Agreement shall operate as a waiver thereof.

12.8 **Force majeure.** Neither Party shall be liable for any
failure to perform its obligations under this Agreement (other than
payment obligations) caused by events beyond its reasonable control.

12.9 **Independent contractors.** The Parties are independent
contractors. This Agreement does not create any agency, partnership,
joint venture, or employment relationship.

12.10 **Counterparts.** This Agreement may be executed in
counterparts, each of which shall be deemed an original, and all of
which together shall constitute one and the same instrument.

---

**END OF AGREEMENT**

> **FIRST DRAFT - COUNSEL REVIEW REQUIRED BEFORE DEPLOYMENT.**
