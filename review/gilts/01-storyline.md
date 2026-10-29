# UK Gilts: storyline (gate 1, revised after grader review)

One line per slide: **section · the point (becomes the title) · what it shows**. `[src]` = external fact with a source line (in `work/gilts/sources*.md`). Numbers are from `work/gilts/calcs.py`. Grader report: `01-grader-report.md`; my response at the end.

## 0 · Opening
1. **Cover**: "UK Gilts: pricing, yields and interest-rate risk" · Group 10, course [user to supply]
2. **A trader must price nine gilts and know how much each could lose if rates rise** · the deck's question in one line, the four case questions, the five sections

## 1 · Case overview (the market, not a company)
3. Divider · 01 Case overview
4. **A gilt is a loan to the UK government that pays a fixed coupon twice a year** · cash-flow diagram for £1,000 of 4% Treasury Gilt 2016 (£20 each Mar/Sep, £1,000 back) (case p.2)
5. **A gilt's name tells you its coupon and maturity; prices are quoted per £100** · anatomy of "4% Treasury Gilt 2060" (case p.2, DMO [src])
6. **Conventional gilts pay fixed cash; index-linked gilts pay cash that rises with inflation** · side-by-side; this case is conventional only (case p.2)
7. **The UK has never missed a gilt payment, so gilts set the UK's risk-free rate** · DMO quote (case p.2); UK ratings 2014 vs today [src]
8. **The Debt Management Office issues gilts for HM Treasury, mostly at 5, 10 and 30 years** · issuance; 50-year gilts since 2005, thinly traded (case p.2) [src]
9. **The gilt market was £[x]bn in 2014 and is £[y]bn today** · bar chart [src]
10. **The Bank of England, pension funds and insurers, and overseas investors own most gilts** · holdings breakdown [src]
11. **The UK borrowed heavily after 2008: debt rose from [x]% to [y]% of GDP** · public debt and deficit 2007–2014 vs today [src]
12. **Gilts compete with US Treasuries and German Bunds for global savings** · 10-year yields of the three in May 2014 and today; sovereign spreads [src]
13. **In May 2014 Bank Rate had been 0.5% for five years and QE held £375bn of gilts** · timeline 2008–2014 [src]
14. **The case: Petr Cech must price nine gilts and measure their rate risk for his trading desk** · setting (MU Securities); why a desk needs fair prices (spot rich/cheap bonds) and risk numbers (limits, hedging) (case p.1)
15. **Each question needs one CFA tool: TVM, yield to maturity, the yield curve, duration and convexity** · Q1–Q4 mapped to concepts

## 2 · Exhibit analysis
16. Divider · 02 Exhibit analysis
17. **Exhibit 1: nine gilts, each with a price or a yield but never both** · native table, rebuilt (coupon, maturity, price, YTM; blanks "?"), source IMD research
18. **Coupons from 2¾% to 5¼% show the gilts were issued when rates were at different levels** · coupon vs maturity chart; high coupons = earlier, higher-rate years (with real issue years only where names are certain) [src]
19. **Four of the five given prices are above 100, so those gilts yield less than their coupon** · given prices vs 100; 50-year at 94.96 is the only discount (first clue for Q1)
20. **The four given yields rise with maturity, from 1.74% at 2 years to 4.36% at 30 years** · given YTMs plotted, gaps marked (sets up Q3)
21. **Exhibit 1 is a teaching set: its yields sit above the real gilt market of May 2014** · Exhibit 1 vs the actual BoE/DMO gilt curve on 9 May 2014 (chart, source line); what that means: we analyse the exhibit's numbers and use real data only for context [src] *(wording depends on the data)*
22. **The real gilts behind Exhibit 1** · case bond → real gilt name/maturity, only certain matches (user rule) [src] *(merged into 18 if few match)*
23. **The exhibit asks us to solve four prices and five yields, then stress-test all nine** · roadmap; annual-coupon simplification flagged

## 3 · Q1: coupon rate vs YTM
24. Divider · 03 Q1: coupon rate vs yield to maturity
25. **Q1 asks how the coupon rate and the YTM differ and what that does to price** · question stated; three parts: define, compare, effect on price
26. **The coupon rate fixes the cash; the YTM is the return the market wants today** · two definitions, 20-year 4¾% example
27. **YTM is the bond's internal rate of return, and it holds only under three conditions** · held to maturity, no default, coupons reinvested at the YTM (CFA FI LM10); IRR picture
28. **Reinvest the 20-year gilt's coupons at 2% instead of 4.38% and the return falls to 3.66%** · £104.93 grows to £247.08 at 4.38% (return 4.38%), £215.41 at 2% (3.66%), £195.00 at 0% (3.15%)
29. **Coupon rate, current yield and YTM give three different answers for the same bond** · table for all nine; e.g. 7-year 5%: 5.00% / 4.59% / 3.54%; which one measures what
30. **A bond's price is the present value of its cash flows at the YTM** · P = Σ C/(1+y)^t + 100/(1+y)^N, each symbol explained (CFA FI LM06)
31. **Higher yield, lower price: the price–yield curve slopes down** · chart for the 7-year 5% gilt (a given price, 108.91 at 3.54% marked)
32. **YTM below the coupon means a premium; above means a discount; equal means par** · rule shown with the given yields only: 2-year (1.74% < 5.25%), 30-year (4.36% < 4.50%) → premium; 5-year (3.00% > 2.75%), 10-year (4.04% > 3.75%) → discount; par case shown as a hypothetical
33. **A premium or discount shrinks to zero by maturity (pull to par)** · price paths of a premium and a discount gilt year by year (chart)
34. **Coupon and YTM differ because rates have moved since the gilts were issued** · link to issue eras; external anchor: Bank Rate path [src]
35. **Q1 answer: the coupon sets the cash, the YTM sets the price** · three-line summary

## 4 · Q2: fill in the missing values
36. Divider · 04 Q2: the missing prices and yields
37. **Q2: four prices and five yields are missing** · question, gaps highlighted, two tasks
38. **Assumptions: annual coupons, priced on a coupon date, per £100** · reasons; no accrued interest so clean = dirty price (one line on clean vs dirty)
39. **Price from yield, step 1: list the 5-year gilt's cash flows** · £2.75 × 4, then £102.75
40. **Step 2: discount each cash flow at 3.00%** · table: year, cash flow, 1/1.03^t, PV (2.67, 2.59, 2.52, 2.44, 88.63)
41. **Step 3: add them up: the 5-year gilt is worth £98.86** · sum; discount because 3.00% > 2.75%
42. **A shortcut gives the same answer: annuity of coupons plus the PV of £100** · P = C × [1 − (1+y)^−N]/y + 100/(1+y)^N → 2.75 × 4.5797 + 86.26 = 98.86
43–45. **The 2-, 10- and 30-year gilts: 106.84, 97.65, 102.32** · formula → numbers plugged in → result (*one slide each, or one combined: user's choice*)
46. **Yield from price, the easy case: the 1-year gilt yields 0.73%** · 102.50 = 103.25/(1+y) → y = 0.73%
47. **Longer bonds need a search: bracket the 3-year yield between 2% and 3%** · price at 2% = 107.21, at 3% = 104.24; target 107.02
48. **Interpolate, then check: the 3-year yield is 2.06%** · 2% + (107.21 − 107.02)/(107.21 − 104.24) × 1% = 2.064%; exact 2.063%; reprice at 2.063% = 107.02 ✓
49–51. **The 7-, 20- and 50-year yields: 3.54%, 4.38%, 4.24%** · bracket → interpolate → exact → reprice check (*one slide each, or one combined: user's choice*)
52. **Exhibit 1 completed** · full table, computed cells marked (bold + accent, readable in grey)
53. **Paying coupons twice a year changes prices by at most 0.03 and yields by at most 1bp** · annual vs semi-annual table, price change for YTM-given bonds, bp change for price-given bonds

## 5 · Q3: the yield curve
54. Divider · 05 Q3: the yield curve
55. **A yield curve plots yield against maturity for one issuer's bonds** · definition; why it matters (benchmark for all UK borrowing)
56. **Exhibit 1's curve rises steeply to 10 years, is flat to 30, and falls 14bp at 50** · line chart of the nine YTMs (years on a true-scale axis)
57. **The slope in numbers: +331bp from 1 to 10 years, +34bp to 20, −2bp to 30, −12bp to 50** · step-change bars
58. **The short end implies rising rates: the 1-year rate one year ahead is 2.81%, against 0.73% today** · bootstrap: z1 0.73%, z2 1.77%, z3 2.09%; forwards 1y1y 2.81%, 2y1y 2.75% (CFA FI LM09)
59. **Three theories explain a curve's shape** · expectations, liquidity preference, segmentation/preferred habitat side by side, what each predicts
60. **Applied here: expected rate rises explain the steep short end, a term premium the slope to 10 years** · link to slide 58 and Bank Rate 0.5% [src]
61. **The long end bends down because pension funds and insurers buy long gilts, even though the 50-year is illiquid** · preferred habitat; illiquidity should raise its yield, yet 4.24% is the lowest long yield → demand dominates [src]
62. **Caution: this is a curve of coupon-bond yields, not spot rates** · YTM vs spot (coupon effect), our z-rates vs YTMs for 1–3 years
63. **Q3 answer: an upward curve that flattens and bends down at the long end** · summary + chart thumbnail

## 6 · Q4: what if all yields rise by 1%?
64. Divider · 06 Q4: a 1% rise in all yields
65. **Q4: every yield moves up by one percentage point at once** · parallel shift picture; "+1%" means 3.00% → 4.00%
66–68. **Repricing the 1-, 10- and 50-year gilts at their new yields** · formula, plugged in, result: 102.50 → 101.49 (−0.98%); 97.65 → 90.06 (−7.78%); 94.96 → 78.11 (−17.74%) (*one slide each, or one combined: user's choice*)
69. **Every gilt falls, and the 50-year falls 18 times as much as the 1-year** · results table, all nine
70. **On a £1m holding, the 50-year loses £168,478; the 1-year £10,076** · money loss and PVBP (value of one basis point) table
71. **Duration measures how long, on average, you wait for a bond's cash** · Macaulay duration concept, see-saw picture
72. **Macaulay duration of the 5-year gilt: 4.74 years** · step table: t, PV(CF), weight, t × weight → sum
73. **Modified duration turns that into price sensitivity: 4.60% per 1% of yield** · ModD = MacD/(1+y) = 4.74/1.03; %ΔP ≈ −ModD × Δy (CFA FI LM11)
74. **The 10-year gilt: Macaulay 8.50, modified 8.17** · second worked example, short form
75. **Duration ranks the risk: 0.99 (1-year) to 20.82 (50-year)** · Macaulay and modified duration table (columns labelled)
76. **Same maturity, different coupon: a lower coupon means more rate risk** · hypothetical 10-year at 0%, 3.75%, 8%: −9.12%, −7.78%, −7.00% (coupon effect)
77. **For long bonds duration overstates the fall: −20.82% estimated vs −17.74% actual** · estimate vs actual, all nine
78. **Convexity: the price–yield line curves, so prices fall less than the straight line says** · chart with the duration tangent
79. **Measuring convexity from prices: 81.65 for the 10-year, 711.82 for the 50-year** · ApproxCon = (P₋ + P₊ − 2P₀)/(P₀ × Δy²), numbers plugged in (CFA FI LM12)
80. **Duration plus convexity: −7.76% for the 10-year (actual −7.78%)** · %ΔP ≈ −ModD·Δy + ½·C·(Δy)² plugged in
81. **For the 50-year, even this leaves a gap at a full 1% move: −17.31% vs −17.74%** · higher-order effects; the price-based measures (ApproxModDur 21.30, ApproxCon 711.82) give −17.74% exactly
82. **Falling yields help more than rising yields hurt: +24.86% vs −17.74% for the 50-year** · −1% vs +1% table (convexity asymmetry)
83. **Long gilts paid little extra yield for much more risk** · scatter: YTM vs modified duration
84. **Short gilts suit investors who may need cash or fear rate rises; long gilts suit those matching long liabilities or betting on falling rates** · when to hold which (case teaching point)
85. **Q4 answer: all prices fall, long gilts by far the most; duration predicts it, convexity refines it** · summary

## 7 · Epilogue
86. Divider · 07 Epilogue
87. **What we found: coupon ≠ return, a rising curve, and rate risk that grows with maturity** · four findings, one per question
88. **After 2014, gilt yields kept falling, to record lows in 2020** · 10-year gilt yield 2014–2021 [src]
89. **Turning points: the 2016 Brexit vote and the UK's rating downgrade** · [src]
90. **From 2022, inflation returned and Bank Rate rose from 0.1% to 5.25%** · Bank Rate chart [src]
91. **September 2022: long gilts crashed and the Bank of England had to step in** · mini-budget, 30-year yield jump, BoE action (date, size) [src]
92. **Our Q4 numbers in real life: a [x]bp rise × 50-year duration ≈ the actual loss** · apply our duration/convexity to the 2022 move and compare with the real fall in a long gilt [src]
93. **The Bank then reversed QE and began selling gilts (QT)** · [src]
94. **What happened to our nine gilts** · redeemed ones and dates; any still trading, then vs now [src]
95. **Today (October 2026): Bank Rate [x]% and a gilt curve that [shape]** · today's curve vs Exhibit 1 curve and the real May 2014 curve (chart) [src]
96. **Lessons for an investor: the coupon is not the return, the curve carries information, and duration is the price of extra yield** · closing slide

## 8 · Team
97. **Group 10** · members' photos, full names, student IDs (placeholder until supplied)

---

## Instructions checklist
| Requirement (Case Presentation Instructions) | Slides |
|---|---|
| Overview: background, "business model", industry/competition, key financial information, main problem | 4–15 (12 = competing sovereigns; 11 = fiscal position) |
| External sources in the overview | 5, 7–13 |
| Every exhibit inserted (rebuilt), explained, key numbers, meaning, implications | 17–23 |
| Each question stated and broken into parts | 25, 37, 55, 65 |
| Theories and frameworks | 27, 30–33, 42, 58–62, 71–81 |
| Evidence from the case and external sources, per question | Q1: 34 · Q2: 21 (exhibit vs real) · Q3: 60–61 · Q4: 92 |
| Assumptions explained | 27, 38, 53, 62, 65 |
| Alternatives compared | 29 (three yield measures), 42 (two pricing methods), 53 (annual vs semi), 76 (coupons), 77–82 (duration vs convexity, up vs down), 84 |
| Calculations shown step by step on the slides | 39–53, 58, 66–82 |
| Epilogue: findings, turning points, outcome, after the case, today | 87–96 |
| Final slide with photo, name, ID | 97 |

## Response to the grader (B+ as it stood)
**Done:**
- **1:** slide 21 compares the exhibit with the real May 2014 curve; slides 60–61 and 95 reworded to match. The wording waits for the BoE data.
- **2:** 27–28.
- **3:** 29.
- **4:** 19 and 32 now use only given numbers; the par case is labelled hypothetical.
- **5:** 42.
- **6:** 47–48.
- **7:** 72–74 and 79–81, including why the 50-year gap remains.
- **9:** 58, with the forwards computed.
- **10:** 59, 61.
- **11:** 56–57.
- **12:** 70.
- **13 (part):** −1% on slide 82; the coupon effect on 76.
- **14:** 84.
- **15:** 11–12.
- **16:** 89, 92, 93, 95.
- **17:** all titles are now points.
- **18:** 19, 32 and 33 each do a different job.
- **20:** 53.
- **21:** checklist row.
- Nice-to-haves also done: 38, 75, 83, 14.

**Decided later:**
- **19:** slides 18 and 22 depend on the gilt-name research. If few bonds match, they merge.

**Not done:**
- **13, the non-parallel shift:** CFA Level 1 only names shaping risk, and a numeric twist scenario would add slides without answering Q4, which asks about a parallel move. We mention it in one line on slide 65.
- **8:** grader recommends the full version; **this is the user's choice** (see the gate question).
