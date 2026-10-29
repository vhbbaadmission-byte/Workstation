# Jaguar Land Rover: gate 0 brief

## The case in plain words
March 2015. JLR (owned by Tata Motors since 2008) sells **US$500m of new 5-year notes at 3.5%** and uses the money to buy back its **US$410m 8.125% notes due May 2021**, issued in May 2011 when JLR was a weaker credit. Holders could tender their notes (deadline 30 March 2015) or roll them into the new issue. On paper JLR "halves its interest cost". The case asks whether that is a free lunch in an efficient bond market: if JLR has to pay bondholders a fair price for the old notes, the coupon saving is paid away up front. The twist is that the lower rate came from **better credit, not lower Treasury yields**: the 5-year Treasury fell only 26bp (1.83% → 1.57%) between the two dates.

## Exhibits (6), all numbers in `work/jaguar/exhibits.csv`
| # | What it is | What it's for in the deck |
|---|---|---|
| 1 | Financing at 31 Dec 2014: 6 senior notes (£ and US$) + £1,485m undrawn revolver + factoring; £3,965m facilities, £2,448m drawn | The debt stack; the 8.125% 2021 note is JLR's most expensive US$ debt; first calls in 2016 |
| 2 | Luxembourg prices of 8 JLR bonds (two ISINs per note: 144A and Reg S) | 8.125% 2021 indicative at **111.276** (4 Feb 2015): the market's price for what we must value |
| 3 | US Treasury curve, 16 May 2011 vs 16 Mar 2015 (chart only) | Rebuilt from Treasury's official data (matches the two chart labels exactly). Rates fell at the long end but only **26bp at 5 years** |
| 4 | Income statements FY2012–FY2015 (9 months) | Revenue £13.5bn → £19.4bn; PBT £1.5bn → £2.5bn: the credit story |
| 5 | Cash flow statements | Strong operating cash; capex/intangibles rising fast; FCF thinning (Moody's concern) |
| 6 | Balance sheets | Equity £2.9bn → £6.8bn; cash £2.9bn + deposits £1.1bn vs £2.4bn debt: low net leverage |

Extraction: two helpers extracted independently. **Every value agreed** (the only differences were labels). Every subtotal and total ties in all four periods, and the balance sheet balances.

## Questions (4)
1. What enabled JLR to raise new debt at less than half the 2011 coupon?
2. At what price would existing bondholders surrender their notes?
3. If JLR buys all old notes at that price, what are the incremental cash flows, and does it save money?
4. What other benefits? Does it add value to the firm, the old bondholders, the shareholders?

## CFA concepts we'll use (Level 1)
- Bond valuation: PV of cash flows, **flat vs full price, accrued interest (30/360)**, semi-annual YTM (FI LM06, LM07)
- **Callable bonds: yield-to-call, yield-to-worst**; the issuer's call caps the price (FI LM01, LM07)
- Yield = benchmark + **spread** (G-spread); credit risk, ratings, credit ratios (FI LM07, LM14, LM16)
- Time value of money, NPV of the refinancing (QM LM02), the term structure (FI LM09)
- Capital structure and MM: refinancing at a fair price does not create value (CI LM06); market efficiency (EQ LM03)
- Ratio analysis on Exhibits 4–6: margins, leverage, interest cover, FCF (FSA LM11)

## Our one-line answers (first pass; solved fully at gate 1)
1. **Credit, mostly.** Like for like at 5 years, Treasuries fell only 26bp. The rest is a much tighter credit spread: 2011 coupon 8.125% vs 10-year UST 3.15% (≈497bp) and 2015 coupon 3.50% vs 5-year UST 1.57% (≈193bp). Behind it: the turnaround (profit ×1.3, equity ×2.3 in 3 years), rating upgrades (Ba3 → Ba2, positive outlooks), a shorter 5-year tenor, and strong demand for high-yield bonds in 2015.
2. **About 109–112 per 100, not 125.** Valued to maturity at JLR's new 3.5% rate, the old notes are worth ≈125 (clean). But JLR can call them in **May 2016**, so no holder can expect 125; valued to the call they are worth ≈109. The market had them at 111.28. The actual tender paid **112.35** (early) / **109.35** (late), plus accrued interest of **US$27.53** / **US$30.69** per US$1,000, which we reproduce exactly with 30/360.
3. **The accounting saving is real; the economic saving is close to zero.** On the same US$410m face, coupons fall from US$33.3m (8.125%) to US$14.4m (3.5%) a year, but the premium paid up front (≈US$50m on US$410m) roughly equals the PV of those savings at today's rates. The NPV is about zero, and slightly negative if JLR paid above the bonds' fair value.
4. **The firm gains little value. Bondholders gain a premium over the market price. Shareholders are about neutral.** The real gains are softer: higher reported profit and interest cover, looser covenants, an earlier and cheaper maturity profile, and a signal of credit strength. Tagged *debatable* until gate 1.

## Traps found
- **The call option is the crux of Q2.** The teaching note values the notes to 2021 at 3.5% and gets a 25–29% premium. That ignores the May 2016 call and doesn't match the market (111) or the actual tender (112). See question 1 below.
- The case names the **May 2016 Treasury as the "reference security"**. That is the standard way a tender on a callable bond is priced: discount to the first call date at that Treasury's yield plus a fixed spread. A law firm's deal note confirms "a fixed spread over a defined government security yield". We'll find the exact spread in the tender notices.
- **FX mixing:** Exhibit 1 converts US$410m at the Dec-2014 rate (£263m, i.e. 1.559). The case says to use **1.50** for March 2015 (£273.3m). The teaching note uses £263m for the old notes and £333m (at 1.50) for the new: two rates in one NPV. We'll do the bond maths in **US$** (no FX needed) and convert once at 1.50.
- **Mismatched tenors:** old 10-year vs new 5-year. Comparing the coupons directly overstates the gain from credit. Use the spread over the matching Treasury.
- **Gross vs net:** US$500m raised vs US$410m face. The extra US$90m is new borrowing, not refinancing.
- **FY2015 is 9 months.** Annualise it or compare like periods.
- FY2012 D&A is **465** in Exhibit 4 but **466** in Exhibit 5 (a source rounding difference, noted).
- Exhibit 2: the second 8.125% ISIN last traded in **Aug 2014** (111.583), so it's stale. Use 111.276 (Feb 2015).
- Only **79.61%** (US$326.42m) was tendered (teaching note, to be verified at source). Q3 assumes 100%. The epilogue covers the remaining ~20% (likely called in 2016; to be checked).
- Clean vs dirty: the tender paid accrued interest separately; our prices are clean, and we'll say so on every price.

## Research plan (gate 1; helpers gather, I check)
- Bourse de Luxembourg notices (Avis 46246, 46518) and the tender offer documents: price, spread, results. The 2011 offering memo: the call schedule.
- JLR/Tata annual reports and press releases: the 2011 and 2015 issues, the Feb 2015 3.875% notes (the "first refinancing").
- Moody's / S&P rating history 2011 → today.
- Epilogue: what happened to the 2021 notes; JLR since 2015 (Brexit, the 2018–19 losses and Project Charge, Reimagine/EV, the return to profit, investment-grade ratings, the 2025 cyber-attack); where it stands today (latest results, debt, ratings).
- Overview: history (Ford → Tata 2008), brands, markets, competitors (BMW, Mercedes, Audi, Porsche), the 2015 high-yield market.
- Tools: web search and fetch both work (fetch after you opened the network). The Claude Slides artifact can be created.

## Questions for you (answered 2026-10-29)
- **Q2:** call-aware value first; the teaching note's ~125 is shown as the naive upper limit and reconciled to the market and tender prices.
- **Currency:** all bond maths in US$, converted to £ once at 1.50.

### As asked
1. **Q2: how should we treat the teaching note's 25–29%?** Our answer differs by much more than rounding.
   - **A (recommended):** lead with the call-aware value (≈109–112). Show the teaching note's to-maturity value (≈125) as the naive upper bound, explain why holders can't get it (the call), and reconcile to the market (111.28) and the actual tender (112.35). This also answers the "explain the gap" trap in CLAUDE.md.
   - **B:** follow the teaching note's method as the main answer and add the call as a caveat.
   - **C:** only the market/tender view.
2. **Currency:** OK to do all bond maths in **US$** and convert to £ only once, at 1.50, when linking to JLR's £ statements? (The alternative is the teaching note's £ throughout, which needs two FX rates.)
