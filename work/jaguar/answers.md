# Jaguar Land Rover: answers (gate 1)

All numbers come from `work/jaguar/calcs.py` (run it to see every step). Inputs: `work/jaguar/exhibits.csv`, `work/jaguar/sources.md`, `work/jaguar/sources_research.md`.

## Conventions and assumptions
- **Currency:** bond maths in **US$** (the notes' currency); £ only at the case's **1.50** (user decision). Exhibit 1's £263m implies 1.559 (31 Dec 2014 rate).
- **Prices:** per 100 face; semi-annual coupons (15 May / 15 Nov); **30/360** day count; clean = full − accrued (CFA FI LM06).
- **Settlement:** 17 Mar 2015 (early settlement); 31 Mar 2015 for late tenders. Source: JLR releases.
- **Call:** first call 15 May 2016 at **104.0625** (par + half coupon). The 2015 offering memorandum prints "104.663%", but only 104.0625 reproduces the published tender price (to within US$0.01 per US$1,000), so 104.663 is treated as a misprint.
- **Maturity:** the case says **15 May 2021**; Tata Motors' SEC filing says **15 Nov 2021**. Waiting for the user's decision; this only affects the hold-to-maturity value (125.43 vs 127.26).
- **Tax:** UK main corporation tax rate 20% from 1 Apr 2015 (Finance Act 2013 s.6); premium and interest deductible (assumption).

## Q1. Why could JLR borrow at less than half the 2011 coupon? — *solid* (numbers) / *debatable* (weights)
- 2011: 8.125% = 3.15% (10-year UST, 16 May 2011) + **497bp**. 2015: 3.50% = 1.57% (5-year UST, 16 Mar 2015) + **193bp**.
- The total fall of **462bp** splits into:
  - credit spread **304bp (66%)**
  - Treasury level and shorter maturity **158bp (34%)**. How these 158bp divide depends on the order of the split: our order gives 105bp level + 53bp tenor; the checker's gives 26bp + 132bp. Both are valid, so the deck shows the 158bp as one block.
- Like for like at 5 years, the UST fell only **26bp** (1.83% → 1.57%).
- Same-bond evidence: the old 8.125% notes traded at 111.28 (4 Feb 2015) = **2.28% yield to call**, 5.94% to maturity.
- Drivers of the narrower spread:
  - credit metrics (Exhibits 4–6): EBITDA margin 14.8% → 18.0%, net cash £456m → £1,604m, D/E 0.68 → 0.36, EBITDA/cash interest 12–30×
  - ratings (Ba3 → Ba2 in 2013; positive outlooks in 2014)
  - shorter tenor (5 vs 10 years)
  - the 2011 notes' call feature (investors were paid for it in the 8.125%)
  - market demand for high-yield bonds (market-wide spread data still being sourced)

## Q2. Price holders would accept — *solid*
| Method | Discount rate (why) | Clean price | Premium |
|---|---|---|---|
| A: hold to May 2021 (naive) | 3.50% (JLR's new 5-year cost) | 125.43 | 25.4% |
| B: to May 2016 call | 3.50% | 109.11 | 9.1% |
| Market (Exhibit 2, 4 Feb 2015) | implied 2.28% to call | 111.28 | 11.3% |
| Actual tender (early) | 0.395% UST May-2016 + 0.50% = 0.895%, to call | 112.35 | 12.4% |
| Actual tender (late) | early price − US$30 early premium | 109.35 | 9.4% |

- Accrued interest: 122 days → **US$27.53** per US$1,000 (17 Mar); 136 days → **US$30.69** (31 Mar). Both match JLR's payments.
- **Answer:** about **111–112 clean** per 100 (US$456–461m for the issue), plus accrued interest. Holders won't accept less than the market price (111.28) and can't expect more than the value of the notes to the call at a near-risk-free 14-month rate (~112.4–112.9).
- The hold-to-maturity value (125) ignores the call. The issuer's option is worth about **14 points** (125.43 − 111.28).

## Q3. Incremental cash flows and savings — *solid* (numbers) / *debatable* (choice of baseline)
- Cash needed: 410 × (112.352 + 2.754)% = **US$471.9m**. New issue US$500m → surplus **US$28.1m** before fees.
- Accounting view:
  - interest US$33.3m/yr (8.125% × 410) → US$16.5m/yr (3.5% × 471.9), a saving of **US$16.8m/yr**
  - premium above face **US$50.6m** (incl. US$12.3m early premium) ≈ 3 years of savings
- The full dated incremental table is in the calcs output (old coupons avoided May/Nov to 2021; new coupons Mar/Sep to 2020).

| Baseline | Pre-tax NPV @3.50% | After-tax NPV @2.80% |
|---|---|---|
| Old notes held to 2021 | +US$53.5m | +US$44.8m |
| Old notes called May 2016 (realistic) | −US$13.4m | −US$10.4m |
| Market value (111.28) | −US$4.4m | — |

- **Answer:** there is a real cash-interest saving but no economic saving. Against the realistic baseline (the call), JLR paid slightly more than the debt was worth. The "saving" only appears if you assume JLR would have kept 8.125% debt to 2021, which it would not.

## Q4. Other benefits; who gains — *debatable*
- **Benefits to JLR:**
  - higher reported profit and interest cover after a one-off charge
  - covenants stripped through the consent solicitation
  - US$28m of extra liquidity
  - locked in 3.5% before the Fed's first rise (Dec 2015)
  - signalling
- **Costs:** the premium, the early-tender payment, fees, and refinancing risk from the maturity moving to 2020.
- **Firm:** about zero value (MM; efficient market). A lower coupon means a slightly smaller interest tax shield.
- **Bondholders who tendered:** +1.07 per 100 over the market price (US$4.4m on US$410m), +3.24 over being called (US$13.3m).
- **Tata Motors (sole shareholder):** about neutral to slightly negative.

## Independent check (sonnet helper, case only, no teaching note) — `work/jaguar/check/`
| Item | Ours | Checker | Why they differ |
|---|---|---|---|
| Q1 spread change | 304bp | 304bp | — |
| Q1 level/tenor split | 105 + 53 | 26 + 132 | order of decomposition; both valid; deck shows the 158bp combined |
| Q2 headline | 111–112 (to call; market and tender anchors) | 110.44 (to call at 2.24%, settle 31 Mar) | the checker used JLR's 5-year spread over the 1-year Treasury and a later settlement date; it is inside our band |
| Q2 to maturity | 125.43 | 124.11 (at 3.69%) | the checker used a 6-year yield (3.69%) instead of 3.5% |
| Q3 NPV vs hold | +53.5 | +53.8 | the checker included a 1.25% fee and different funding; same conclusion |
| Q3 NPV vs call | −13.4 | −13.1 | same |
| Conclusion | no economic saving | "little or no value created once compared with the call" | same |

## Teaching note comparison (for checking only; never cited on slides)
- Its Q2 answer is a 25–29% premium. That is our Method A (25.4%; its variant 2 uses a different discounting schedule). The difference from our answer (11–12%) is **the call option**, which the teaching note ignores. The actual tender (12.35%) and the market (11.3%) both support our answer. User decision at gate 0: lead with the call-aware value.
- It uses £263m (Dec-2014 FX) for the old notes and £333m (1.50) for the new notes. We stay in US$.
- Its NPV of 0.00 (variant 1) is zero by construction: it prices the notes at the same rate it discounts at.
- Its accrued interest of US$25.92 (to 15 Mar) vs ours of US$27.53 (to 17 Mar): different date. Ours matches the actual payment.
