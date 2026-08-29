---
title: Insurance Lead-Gen Compliance
description: The hard-gate reference for the `insurance-compliance-officer` agent, and a required
tags: ['insurance']
created: 2026-08-28
last_updated: 2026-08-28
source_path: /Users/teaglebuilt/github/teaglebuilt/aiconfig/context/knowledge/insurance/compliance.md
---
# Insurance Lead-Gen Compliance

## When to Use

The hard-gate reference for the `insurance-compliance-officer` agent, and a required
cross-check for any lead-gen workflow. If a signal is hot (`lead-signals.md`) and a
source is available (`data-sources.md`) but the outreach fails a rule here, the lead is
**dead until remediated**. This is not legal advice — it flags where a licensed
compliance/legal review is mandatory before launch.

## The Non-Negotiable Gates

Every outbound contact must clear, in order:
1. **Channel-consent gate** (TCPA / CAN-SPAM) — do you have the right consent for this channel?
2. **Suppression gate** (DNC federal + state + internal) — is this number/contact suppressed?
3. **Data-use gate** (FCRA / GLBA / privacy) — are you using the data within its permitted class?
4. **Product-conduct gate** (licensing / suitability / anti-rebating / carrier rules) — are you allowed to recommend/solicit this product this way?

---

## 1. Channel Consent

### TCPA (calls & texts)
- Autodialed or prerecorded **marketing** calls/texts to a **wireless** number require **prior express written consent (PEWC)**.
- Consent must be clear, retained, and revocable; honor revocation promptly (FCC 2024 rules tightened revocation — treat any reasonable opt-out method as valid, act within a reasonable time, generally ≤10 business days).
- **1:1 consent rule status (verify current):** The FCC's "one-to-one" lead-gen consent rule was **vacated by the 11th Circuit in early 2025 (IMC v. FCC)**, so the strict single-seller consent requirement is not in force federally — but treat single-seller, unambiguous consent as best practice and **re-verify the current state** before relying on shared/aggregator consent.
- Manual, non-autodialed calls to numbers not on DNC lists have a lower bar but still face state mini-TCPA laws.

### State mini-TCPA
- **Florida (FTSA)**, **Oklahoma**, **Washington**, **Maryland**, and others impose stricter consent/curfew rules than federal. Check the prospect's state, not just yours.

### CAN-SPAM (email)
- Accurate headers/subject, valid physical postal address, clear opt-out honored within 10 business days, no harvesting.

### Calling curfews
- Federal TSR: no telemarketing before 8am / after 9pm prospect local time. Some states narrower.

---

## 2. Suppression / Do-Not-Call

- **National DNC Registry** — scrub before every campaign. Registration is permanent.
- **EBR exemption** — an *established business relationship* (existing customer, or inquiry within 3 months) permits some calls, but does **not** override an entity-specific DNC request.
- **Internal DNC list** — you must maintain your own and honor it indefinitely.
- **State DNC lists** — some states maintain separate registries; scrub those too.
- **Wireless / reassigned numbers** — check the FCC Reassigned Numbers Database to avoid calling a number that changed hands after consent.

---

## 3. Data Use (privacy & fair reporting)

### FCRA
- Data used to **decide eligibility, rates, or underwriting** = a consumer report → needs a permissible purpose; adverse actions require notice.
- **C.L.U.E. loss-history and credit-based insurance scores are FCRA.** Do not use FCRA data to *build marketing lists* except via the narrow, compliant prescreen/firm-offer-of-credit-or-insurance path.
- Keep marketing (NON-FCRA) and underwriting (FCRA) data streams separate and documented.

### GLBA
- Non-public personal financial information is protected; provide privacy notices; honor opt-outs on sharing.
- **Pretexting to obtain financial info is a federal crime.** Never source data that way.

### State privacy (CCPA/CPRA, and the growing state patchwork)
- Insurance transactions have partial carve-outs, but **marketing data and cold prospect data generally are covered.** Provide notice-at-collection, honor deletion/opt-out of sale/sharing, and respect Global Privacy Control signals where applicable.

---

## 4. Product Conduct

### Licensing
- Soliciting or recommending insurance generally requires a state producer license. Lead-gen that merely advertises and hands off may be exempt, but **"steering" or advice crosses into solicitation.** Variable annuities additionally require **FINRA registration (Series 6/7 + 63)** and a broker-dealer relationship.

### Suitability / best interest
- **Annuities:** NAIC **Suitability in Annuity Transactions** model reg (best-interest standard) is adopted in ~45 states — document the basis for any recommendation. Variable annuities also fall under **SEC Reg BI**.
- **Life:** replacement regulations and suitability apply; extra disclosure when replacing an existing policy.

### Anti-rebating & inducements
- Most states prohibit offering anything of value (cash, gifts above de-minimis, free services) to induce a purchase. Watch "refer-a-friend" incentives and lead-purchase arrangements.

### RESPA (referral partnerships)
- Home-insurance referral deals with realtors/lenders can trip **RESPA anti-kickback** rules. Paid-per-lead arrangements with settlement-service providers are high risk.

### State Farm captive-agent rules
- SF is an **exclusive/captive** model. Agents are independent contractors but bound by SF's marketing, brand, and compliance standards.
- **Trademark use is restricted** — "State Farm," the logo, and slogans have usage rules.
- **Third-party lead purchases (aggregators) may be restricted or prohibited by SF policy** — confirm with SF agency compliance before buying leads.
- Advertising must not misrepresent products, pricing, or the SF relationship.

---

## Pre-Launch Checklist (attach to every campaign)

- [ ] Consent type documented per channel (PEWC for autodial/text, opt-in for email)
- [ ] National + applicable state + internal DNC scrub run, dated
- [ ] Reassigned-number check for aged consent
- [ ] Prospect-state mini-TCPA + curfew rules checked
- [ ] Data source permitted-use class verified; FCRA/marketing not blended
- [ ] Privacy notice / opt-out mechanism live
- [ ] Product recommendation logic passes suitability/best-interest (esp. annuities)
- [ ] Licensing/registration covers the states + products in scope
- [ ] No anti-rebating/RESPA exposure in referral or incentive structure
- [ ] State Farm brand + third-party-lead policy reviewed with SF compliance
- [ ] Provenance + consent log retained per lead
- [ ] Licensed compliance/legal sign-off on the campaign

> Flag for human counsel whenever: buying third-party/aggregator leads, using any FCRA
> data, running autodialed/prerecorded outreach, or recommending annuities.
