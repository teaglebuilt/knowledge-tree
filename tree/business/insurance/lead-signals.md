---
title: Insurance Lead Signals (State Farm: Life, Home, Annuity)
description: Reference when deciding *who* is a good prospect and *why now*. Maps observable
tags: ['insurance']
created: 2026-08-28
last_updated: 2026-08-28
source_path: /Users/teaglebuilt/github/teaglebuilt/aiconfig/context/knowledge/insurance/lead-signals.md
---
# Insurance Lead Signals (State Farm: Life, Home, Annuity)

## When to Use

Reference when deciding *who* is a good prospect and *why now*. Maps observable
life/financial events to the product line they create demand for, and to a rough
intent tier. Pair with `data-sources.md` (where to find the signal) and
`compliance.md` (whether/how you may act on it).

## Core Principle: Trigger Events Beat Demographics

Insurance is bought at moments of change, not on a schedule. A 34-year-old is a weak
lead; a 34-year-old who *closed on a house last week* is a high-intent lead for both
home (mandatory) and life (new debt + family formation). Score on **recency of a
qualifying event**, not static demographics.

Intent tiers used below:
- **T1 (mandatory/imminent)** — event forces a purchase on a deadline (e.g. escrow requires home insurance). Highest conversion, shortest window.
- **T2 (high-propensity)** — event strongly correlates with need; buyer is receptive but not forced.
- **T3 (nurture)** — demographic/latent fit; long cycle, low per-touch conversion.

---

## Home & Property Insurance

| Signal | Tier | Why it converts | Window |
|--------|------|-----------------|--------|
| Deed transfer / home purchase closing | T1 | Lender/escrow requires bound policy before closing | Days — must reach *before* close |
| Purchase agreement / pending sale (MLS status change) | T1 | Buyer shopping insurance now to satisfy lender | 2–6 weeks |
| New mortgage / refinance recording | T2 | Refi may reset escrow, opens bundling conversation | Weeks |
| USPS change-of-address / new-mover | T2 | Renters → renters policy; owners → new dwelling policy | 1–3 months |
| Building permit (new build, addition, pool, roof) | T2 | Changes replacement cost / liability exposure | 1–3 months |
| Rental listing → lease signed | T2 | Renters insurance often lease-required | Weeks |
| Auto policy already with SF, no home policy | T2 | Bundle gap; ~$1,273 avg bundle savings is the hook | Anytime (retention play) |
| Home value appreciation / underinsurance | T3 | Coverage-gap review | Annual |

Best single home signal: **pending/closed property transaction** — it is public,
recent, and the purchase is effectively mandatory.

---

## Life Insurance

Life sales follow **family-formation and debt-acquisition** events — moments where
someone new depends on the prospect's income, or new debt would burden survivors.

| Signal | Tier | Why it converts | Window |
|--------|------|-----------------|--------|
| New mortgage / home purchase | T2 | Large new debt + often a growing household | 1–2 months |
| Marriage record | T2 | New dependent; classic coverage trigger | 1–3 months |
| New child (baby registry, but births are largely private now) | T2 | Strongest emotional trigger; hard to source cleanly | 0–6 months |
| New job / promotion (income jump) | T2 | Affordability rises; often loses/changes group life | 1–3 months |
| Leaving an employer (group life lapses) | T2 | Coverage gap the moment they leave | Weeks |
| Business formation (Secretary of State filing) | T2 | Key-person / buy-sell / SBA-loan life needs | 1–3 months |
| Existing SF auto/home customer, no life policy | T2 | Trusted-relationship cross-sell; lowest CAC | Anytime |
| Age band 25–45, homeowner, no life | T3 | Latent term-life fit | Long nurture |
| Recent obituary (surviving spouse) | T3 | Real need but grief-sensitive; handle with extreme care or skip | N/A |

Best single life signal for a captive SF agent: **existing home/auto book with no life
policy**. Lowest acquisition cost, highest trust, fully first-party (no OSINT needed).

---

## Financial Annuities & Retirement

Annuities follow **retirement-horizon and money-in-motion** events. Note the heavier
regulatory load (see `compliance.md` — NAIC best-interest / suitability; variable
annuities are securities under FINRA).

| Signal | Tier | Why it converts | Window |
|--------|------|-----------------|--------|
| Age 52–65 (pre-retiree) | T2 | Core annuity demographic; rollover planning | Multi-year |
| Job change / retirement / layoff (WARN Act notice) | T2 | 401(k) rollover decision = money in motion | 1–6 months |
| Orphaned / terminated employer plan (Form 5500 signals) | T2 | Rollover into an annuity/IRA | Months |
| Business sale / liquidity event | T2 | Lump sum needs tax-aware placement | 1–6 months |
| Maturing CD / low-yield holder | T3 | Rate-shopping into fixed/indexed annuity | Rate-cycle dependent |
| Existing SF life/home customer, age 50+ | T2 | Trusted cross-sell into retirement planning | Anytime |
| Inheritance / probate filing | T3 | Lump sum placement; sensitive | Months |

Best single annuity signal: **near-retirement existing customer** or a **documented
rollover event**. Because suitability/best-interest rules bite hard here, prefer
first-party and consented sources over cold OSINT.

---

## Lead Scoring Model (starter)

Score = (Signal tier weight) x (Recency decay) x (Reachability) x (Compliance-clear flag)

- Signal tier weight: T1=1.0, T2=0.6, T3=0.25
- Recency decay: 1.0 within window, halve each equivalent window elapsed
- Reachability: has a compliant contact channel (see compliance.md consent state)
- Compliance-clear flag: **hard 0/1 gate** — if not clear to contact, score is 0 regardless of fit. Never let a hot signal override a compliance block.

## Product Bundling Logic

- Home purchase → lead for **home (T1) + life (T2, new debt) + auto bundle**
- New job/retirement → **annuity (T2) + life review**
- Existing single-line SF customer → cross-sell the *missing* lines first (cheapest, most compliant, highest trust)
