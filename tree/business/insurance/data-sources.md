---
title: Insurance Lead Data Sources (OSINT + Commercial)
description: The source catalog for the `osint-signals-researcher` agent. For each signal in
tags: ['insurance']
created: 2026-08-28
last_updated: 2026-08-28
source_path: /Users/teaglebuilt/github/teaglebuilt/aiconfig/context/knowledge/insurance/data-sources.md
---
# Insurance Lead Data Sources (OSINT + Commercial)

## When to Use

The source catalog for the `osint-signals-researcher` agent. For each signal in
`lead-signals.md`, this tells you *where* it lives, how to access it, cost, and — most
importantly — the **legality/permitted-use class**. Always cross-check `compliance.md`
before acting on anything sourced here.

## Permitted-Use Classes (read first)

Every source below is tagged with a class. The class, not the availability, decides what
you may do with the data.

- **PUBLIC-RECORD** — government public record. Free to observe. Contacting the person is still governed by TCPA/DNC/CAN-SPAM.
- **FCRA** — if used to decide *eligibility/underwriting*, it is a consumer report; triggers permissible purpose + adverse-action rules. Marketing use has a narrow "prescreen"/firm-offer path with strict rules. Do not blur these.
- **NON-FCRA-MARKETING** — vendor certifies data is for marketing only; you may *not* use it for eligibility decisions.
- **CONSENTED-LEAD** — the consumer submitted their info; check the consent scope and whether it names you specifically (see compliance TCPA 1:1 note).
- **TOS-RESTRICTED** — scraping/automated collection may violate the platform's terms (and possibly CFAA). Manual, human review of a public profile is lower risk than automated scraping.
- **PROHIBITED-PRETEXT** — obtaining financial data by pretexting is illegal under GLBA. Never.

---

## Home & Property Sources

| Source | Signal | Class | Access | Notes |
|--------|--------|-------|--------|-------|
| County recorder / register of deeds | Deed transfers, mortgages, lis pendens | PUBLIC-RECORD | County portal, bulk data, or aggregator | The single richest, cleanest home signal. Many counties sell bulk feeds. |
| County assessor | Owner, value, property characteristics | PUBLIC-RECORD | Portal / bulk | Good for replacement-cost & appreciation signals |
| ATTOM Data / CoreLogic / First American | Nationwide property + transaction | NON-FCRA-MARKETING | Paid API | Normalizes county data nationally; expensive but turnkey |
| PropertyRadar | Transactions, foreclosures, equity | NON-FCRA-MARKETING | Paid | Popular with agents/investors; good filtering |
| MLS / IDX feeds | Pending & sold listings | TOS-RESTRICTED | Broker/agent access or licensed IDX | Requires MLS membership or a licensed feed; scraping Zillow/Redfin violates ToS |
| USPS NCOALink (via Melissa, Experian, Anchor) | New movers | NON-FCRA-MARKETING | Licensed processor only | You cannot get raw NCOA; must go through a licensed vendor |
| Municipal building permits | New build / additions / roofs | PUBLIC-RECORD | City portals, BuildZoom, Shovels API | Signals changed exposure |

## Life Insurance Sources

| Source | Signal | Class | Access | Notes |
|--------|--------|-------|--------|-------|
| County marriage records | Marriage | PUBLIC-RECORD | County/state vital records | Availability varies by state; some restrict marketing use |
| Secretary of State business filings | New business formation | PUBLIC-RECORD | State portal / bulk | Key-person & SBA-loan life needs |
| LinkedIn (manual review) | Job change, promotion | TOS-RESTRICTED | Human review of public profile | Automated scraping violates ToS; Sales Navigator is the sanctioned path |
| Mortgage recordings | New debt / family formation | PUBLIC-RECORD | County recorder | Proxy for life need; overlaps home signal |
| Obituaries (legacy.com, local) | Surviving spouse | PUBLIC-RECORD | Public | Grief-sensitive; most agents should skip cold outreach here |
| First-party SF book | Existing customer, no life | CONSENTED-LEAD | Your own CRM | Best source, period. Already consented, high trust, zero acquisition cost |

## Annuity & Retirement Sources

| Source | Signal | Class | Access | Notes |
|--------|--------|-------|--------|-------|
| DOL Form 5500 filings | Employer plan size, terminations | PUBLIC-RECORD | EFAST2 / DOL bulk datasets | Terminated plans = rollover opportunity; fully public |
| State WARN Act notices | Mass layoffs | PUBLIC-RECORD | State labor dept sites | Money-in-motion (severance + rollover) signal |
| Secretary of State | Business dissolution / sale | PUBLIC-RECORD | State portal | Liquidity events |
| Age/demographic append | Pre-retiree (52–65) | NON-FCRA-MARKETING | Data broker | Marketing use only; never eligibility |
| Professional licensing boards | High-income professionals | PUBLIC-RECORD | State boards | HNW targeting |
| First-party SF book age 50+ | Existing customer near retirement | CONSENTED-LEAD | Your CRM | Preferred given suitability rules |

## Commercial Data Brokers & Append (cross-line)

| Vendor | Use | Class | Caution |
|--------|-----|-------|---------|
| Experian / Acxiom / Epsilon / TransUnion | Demographic + contact append | NON-FCRA-MARKETING (default) | Same vendor also sells FCRA products — contract must state marketing-only use |
| LexisNexis / Verisk | Insurance-specific data, C.L.U.E. | FCRA | C.L.U.E. loss history is FCRA — eligibility use only, with permissible purpose |
| Spokeo / BeenVerified / TruePeopleSearch | Contact lookup | NON-FCRA-MARKETING | Explicitly *not* for FCRA purposes; accuracy varies |

## Intent & Digital Lead Sources

| Source | Class | Notes |
|--------|-------|-------|
| Your own website form fills / quote-start | CONSENTED-LEAD | Capture consent language + timestamp + IP; strongest TCPA footing |
| Google Ads / Meta lead ads | CONSENTED-LEAD | Own the consent disclosure on the form |
| Aggregators: EverQuote, QuoteWizard, MediaAlpha, SmartFinancial | CONSENTED-LEAD | **Captive SF agents: verify State Farm's policy on buying third-party leads before purchasing.** Also confirm consent is 1:1 / names you (see compliance.md) |
| Comparison-shopping referrals | CONSENTED-LEAD | Vet the upstream consent trail |

---

## Sourcing Rules of Thumb

1. **First-party beats third-party** on cost, trust, and compliance. Mine the existing SF book before buying anything.
2. **Public record ≠ permission to call.** Observation is legal; outreach is separately gated by TCPA/DNC.
3. **Never cross FCRA and marketing.** Pick the product class up front; document the permitted use.
4. **Prefer manual review over scraping** for ToS-restricted platforms. It does not scale, but it does not violate terms or CFAA.
5. **Log provenance** for every lead: source, class, timestamp, consent state. This is your defense if challenged.
6. **No pretexting, ever** for financial data (GLBA).
