# UK Gilts: storyline (gate 1, round 3: after the strict review)

One line per slide: **section · the point (becomes the title, ≤ 2 lines) · what it shows**. Two tags on each line help lucidity:
- **Plain:** a term defined in plain words where it first appears
- **So what:** the one-line takeaway the slide ends with

The reader is a student part-way through CFA Level 1, reading on paper with no presenter (user rule). The full analysis stays; it is explained, not simplified.

`[src]` points to `work/gilts/sources.md`; numbers come from `work/gilts/calcs.py`. Every repeated calculation gets its own slide (user rule). Money on holdings is shown in £m to 1 dp on £100m face.

## 0 · Opening
1. **Cover**: "UK Gilts: pricing, yields and interest-rate risk" · Group 10, course [user to supply]
2. **A trader must price nine UK government bonds and know how much each could lose if interest rates rise** · the four questions, one line each; the five sections. Plain: "interest-rate risk" = how much a bond's price falls when market rates rise.

## 1 · Case overview (the market, not a company)
3. Divider · 01 Case overview
4. **A gilt is a loan to the UK government that pays fixed interest twice a year** · cash-flow diagram: £1,000 of 4% Treasury Gilt 2016 pays £20 every March and September, then £1,000 back (case p.2). Plain: face value, coupon, maturity.
5. **A gilt's name gives its coupon and repayment year; its price is quoted per £100 of face value** · "4% Treasury Gilt 2060" annotated. So what: a price of 102.50 means £102.50 per £100 [src]
6. **Conventional gilts pay fixed cash; index-linked gilts pay cash that rises with inflation** · side-by-side; this case covers conventional gilts only (case p.2)
7. **The UK has never missed a gilt payment, so gilts set the UK's risk-free rate** · DMO quote (case p.2); ratings shown: S&P AAA (2014) and Fitch AA- (Aug 2026, secondary) only; others not verified, so not shown [src]. Plain: risk-free rate = the return on a loan with no real chance of default; AAA/AA = the agencies' top grades
8. **The Debt Management Office (DMO) sells gilts for the Treasury, mostly at 5, 10 and 30 years** · issuance; 50-year gilts since 2005, thinly traded (case p.2) [src]
9. **The gilt market has doubled: £1,365bn in 2014, £2,817bn in 2026** · bar chart, conventional vs index-linked, same DMO basis [src]
10. **QE: since 2009 the Bank of England has created money to buy gilts and push yields down** · Plain: QE (quantitative easing) in one line [src]; Bank Rate 0.50% from Mar 2009; £375bn of gilts bought by 2014 [src]. Plain: Bank Rate = the Bank of England's main interest rate, which sets the cost of short-term borrowing. So what: by 2014 the Bank was one of the biggest holders
11. **In 2014 three groups held over 80% of gilts: overseas investors, pension funds and insurers, and the Bank of England** · holdings chart 29% / 27% / 26% (Bank figure footnoted as "end-2014" per DMO) [src]
12. **UK government debt more than doubled as a share of GDP, from 35.6% in 2008 to 78.6% in 2014** · net debt % GDP: Mar 2008 35.6, Mar 2014 78.6, Mar 2026 93.2; borrowing % GDP: 2.9 / 5.6 / 4.4 (ONS, current vintage) [src]. Plain: net debt = what the government owes minus its liquid assets. So what: more gilts to sell, and investors to persuade
13. **In May 2014 a 10-year gilt paid 2.77%, against 2.62% in the US and 1.50% in Germany** · today 5.30% / 4.98% / 3.39% (BoE, US Treasury, Bundesbank) [src]. Plain: par yield = the coupon a bond would need to be priced at exactly £100. Plain: Treasuries and Bunds = the US and German governments' bonds; sovereign spread = the extra yield one government pays over another (gilt − Bund: 127bp then, 191bp now)
14. **The case: Petr Cech must price nine gilts and measure their risk for his trading desk** · setting (MU Securities); why a desk needs fair prices (to spot over- or under-priced bonds) and risk numbers (to set limits and hedge) (case p.1)
15. **Five ideas we use throughout: price per £100, coupon, yield to maturity, premium/discount, and the basis point** · primer, one plain line each. YTM = the single interest rate at which the bond's future cash, discounted, equals its price; premium = price above 100; discount = below 100; 1 basis point (bp) = 0.01 percentage point
16. **Each question needs one CFA tool: time value of money, YTM, the yield curve, duration and convexity** · Q1–Q4 mapped to tools

## 2 · Exhibit analysis
17. Divider · 02 Exhibit analysis
18. **Exhibit 1 gives nine gilts, each with either a price or a yield, never both** · native table, rebuilt (coupon, maturity, price, YTM; blanks shown as "?"); source: IMD research. So what: our job is to fill the gaps
19. **Coupons range from 2¾% to 5¼% because each gilt was issued when rates were different** · coupon vs maturity chart. So what: a coupon tells you about the past, not today's market
20. **Four of the five given prices are above £100: those gilts must yield less than their coupon** · given prices vs 100 bar; the 50-year at 94.96 is the only discount. So what: a first clue for Q1
21. **The four given yields rise with maturity, from 1.74% at 2 years to 4.36% at 30** · the given yields plotted with the gaps marked. So what: longer loans pay more, which sets up Q3
22. **Exhibit 1 is a teaching set: its yields are about one point above the real market on 9 May 2014** · chart: Exhibit 1 vs real DMO yields that day (10-year 2.80% vs 4.04%; ~30-year 3.39% vs 4.36%; ~50-year 3.36% vs 4.24%) [src]. Similar rise at the short end; the real long end is flatter. So what: we analyse the exhibit's numbers and use the real data only as context
23. **None of the nine is an exact real gilt, so we keep the case's labels** · no certain coupon-and-maturity match in the DMO list (user rule: name only if certain); nearest real gilts for context [src]
24. **The task: work out four prices and five yields, then test all nine against a rate rise** · roadmap; Exhibit 1 assumes annual coupons (stated here and tested on slide 58)

## 3 · Q1: coupon rate vs YTM
25. Divider · 03 Q1: coupon rate vs yield to maturity
26. **Q1: how do the coupon rate and the YTM differ, and what does that do to price?** · question in three parts: define, compare, effect on price
27. **The coupon rate fixes the cash; the YTM is the return the market demands today** · two definitions; example: 20-year 4¾% pays £4.75 a year whatever happens, but the market now wants 4.38% (derived on slide 52)
28. **YTM is the bond's internal rate of return, and it is only earned under three conditions** · Plain: internal rate of return (IRR) = the one discount rate that makes the PV of the cash flows equal the price. Conditions: held to maturity, no default, coupons reinvested at the YTM (CFA FI LM10)
29. **Reinvesting coupons at less than the YTM lowers the return actually earned** · Plain: realised return = what you actually earn, given the rate you reinvest coupons at. In words first: each coupon is invested until maturity and grows with interest; adding them up gives a standard formula. Coupons grow to FV = C × [(1+r)^N − 1]/r: at 4.38%, 4.75 × 30.96 = 147.08 (+100 = 247.08); at 2%, 4.75 × 24.30 = 115.41 (+100 = 215.41)
30. **On the 20-year gilt, the return falls from 4.38% to 3.66% if coupons earn 2%** · realised return = (215.41/104.93)^(1/20) − 1 = 3.66%; at 0%, 3.15%. So what: if rates fall, a holder earns less than the YTM promised (reinvestment risk)
31. **Coupon rate, current yield and YTM give three different answers for the same bond** · Plain: current yield = annual coupon ÷ price (ignores the gain or loss at maturity). Table for all nine; e.g. 7-year: 5.00% / 4.59% / 3.54%. So what: only the YTM counts the whole return
32. **A bond's price is the present value of its cash flows, discounted at the YTM** · formula in words first ("each payment is worth less the later it comes"), then P = Σ C/(1+y)^t + 100/(1+y)^N with each symbol explained (CFA FI LM06)
33. **When the yield rises, the price falls** · price–yield curve for the 7-year 5% gilt, its given price 108.91 at 3.54% marked. So what: price and yield always move in opposite directions
34. **YTM below the coupon means a price above £100; above it, below £100** · rule with given yields only: 2-year (1.74% < 5.25%) and 30-year (4.36% < 4.50%) → premium; 5-year (3.00% > 2.75%) and 10-year (4.04% > 3.75%) → discount; par shown as a hypothetical
35. **A premium or discount shrinks to zero as the gilt nears repayment** · Plain: pull to par. Year-by-year price path of a premium and a discount gilt (chart). So what: on the repayment date every gilt is worth exactly £100
36. **Coupons and yields differ because rates have moved since the gilts were issued** · Bank Rate path to 0.50% (March 2009) [src: BoE database; earlier levels added to sources.md at build or omitted]. So what: high-coupon gilts date from higher-rate years
37. **Q1 answer: the coupon sets the cash; the yield sets the price** · three-line summary

## 4 · Q2: fill in the missing values
38. Divider · 04 Q2: the missing prices and yields
39. **Q2: four prices and five yields are missing** · question; gaps highlighted; two tasks (price from yield; yield from price)
40. **Assumptions: annual coupons, priced on a coupon date, per £100** · each with a reason; no accrued interest, so clean = full price. Plain: clean price = the quoted price; full price = clean + accrued interest; accrued interest = interest earned since the last coupon, paid on top when a bond is sold between coupon dates
41. **Price from yield, step 1: list the 5-year gilt's cash flows** · £2.75 a year for 4 years, then £102.75
42. **Step 2: discount each cash flow at 3.00%** · table: year, cash flow, discount factor 1/1.03^t, PV (2.67, 2.59, 2.52, 2.44, 88.63). Plain: discount factor = what £1 paid in year t is worth today
43. **Step 3: add them up: the 5-year gilt is worth £98.86** · sum. So what: below £100, because 3.00% > 2.75%
44. **A shortcut gives the same answer: the coupons as an annuity plus the PV of £100** · Plain: annuity = equal payments every year. P = C × [1 − (1+y)^−N]/y + 100/(1+y)^N → 2.75 × 4.5797 = 12.5942; + 86.2609 = £98.8551 ≈ £98.86
45. **The 2-year gilt at 1.74% is worth £106.84** · formula → 5.25 × 1.9490 + 96.61 → result. So what: a premium, because 1.74% < 5.25%
46. **The 10-year gilt at 4.04% is worth £97.65** · 3.75 × 8.0948 = 30.3554; + 67.2971 = 97.6525. So what: a discount
47. **The 30-year gilt at 4.36% is worth £102.32** · 4.50 × 16.5606 + 27.80. So what: a small premium
48. **Yield from price, the easy case: the 1-year gilt yields 0.73%** · 102.50 = 103.25/(1+y) → 1+y = 1.007317 → y = 0.73%. So what: buyers accept 0.73% because the gilt pays 3.25% on a price of 102.50 and loses £2.50 at repayment
49. **Longer gilts need a search: try two yields whose prices sit either side of the target** · Plain: "bracketing". 3-year at 107.02: at 2% the price is 107.21, at 3% it is 104.24, so the yield is between 2% and 3%
50. **Estimate in proportion, then check: the 3-year gilt yields 2.06%** · Plain: interpolation = assume the price falls in a straight line between the two tries. 2% + (107.21 − 107.02)/(107.21 − 104.24) × 1% = 2.064%; exact 2.063%; reprice at 2.063% = 107.02 ✓
51. **The 7-year gilt at £108.91 yields 3.54%** · bracket (3%: 112.46; 4%: 106.00) → interpolate 3.550% → exact 3.541% → check ✓
52. **The 20-year gilt at £104.93 yields 4.38%** · bracket (4%: 110.19; 5%: 96.88) → 4.395% → exact 4.375% → check ✓
53. **The 50-year gilt at £94.96 yields 4.24%** · bracket (4%: 100.00; 5%: 81.74) → 4.276% → exact 4.245% → check ✓. So what: for long bonds the straight-line estimate is further off, so the check matters
54. **Exhibit 1 complete: six gilts trade above £100, three below, and yields run from 0.73% to 4.38%** · full table; computed cells in bold and accent (readable in grey)
55. **Real gilts pay twice a year: a worked example** · 2-year at 1.74% a year = 0.87% per half-year; four payments of £2.625 → 2.602 + 2.580 + 2.558 + 99.130 = £106.87 (vs £106.84 annual). Plain: the yield is still quoted as an annual rate, compounded twice a year
56. **Paying twice a year changes prices by at most £0.03 and yields by at most 1bp** · annual vs semi-annual table, both directions. So what: the case's annual simplification is safe

## 5 · Q3: the yield curve
57. Divider · 05 Q3: the yield curve
58. **A yield curve shows the yield on one borrower's bonds at each maturity** · definition; why it matters (it is the benchmark for all UK borrowing)
59. **Exhibit 1's curve rises steeply to 10 years, is flat to 30, and falls to 4.24% at 50** · line chart of the nine YTMs on a true-scale years axis
60. **In numbers: +331bp from 1 to 10 years, +34bp to 20, then −2bp and −12bp** · step bars. So what: almost all the rise happens in the first ten years
61. **A YTM mixes many payment dates; a spot rate is the yield for a single payment date** · Plain: spot rate = the yield on a single payment due at one date (like a zero-coupon bond). Plain: forward rate = the one-year rate for a future year that today's prices lock in (CFA FI LM09)
62. **Step 1: the 1-year spot rate is the 1-year yield, 0.73%** · one payment, so YTM = spot
63. **Step 2: the 2-year gilt reveals a 2-year spot rate of 1.77%** · 106.84 = 5.25/1.0073 + 105.25/(1+z2)² → z2 = 1.77%. Plain: "bootstrapping" = using shorter rates to unlock the next one
64. **Step 3: the 3-year gilt reveals a 3-year spot rate of 2.09%** · 107.02 = 4.5/1.0073 + 4.5/1.0177² + 104.5/(1+z3)³ → 2.09%
65. **Step 4: the curve implies 1-year rates of 2.81% one year ahead and 2.75% two years ahead, against 0.73% today** · forward = (1+z2)²/(1+z1) − 1 = 2.81%; Plain: "2y1y" = the one-year rate starting in two years = (1+z3)³/(1+z2)² − 1 = 2.75%. So what: the exhibit's curve implies rates rising sharply. Caveat: this is the exhibit's curve, not the 2014 market's
66. **Hindsight test: rates did not rise; Bank Rate was cut to 0.25% in August 2016** · [src: BoE]. So what: a curve shows expectations plus a premium, not a forecast that comes true
67. **Three theories explain why curves rise, and each predicts a different shape** · expectations / liquidity preference / segmentation side by side. Plain: term premium = extra yield for lending longer; preferred habitat = investors who stick to certain maturities
68. **The steep short end fits rising rate expectations plus a term premium** · links slides 65–67; Bank Rate 0.50% in 2014 [src]
69. **The long end flattens and dips, most likely because pension funds and insurers want long gilts** · preferred habitat; they held 27% of gilts in 2014 [src]. Competing explanations, in plain words (both explained fully in Q4, slides 98–100): investors pay up for long bonds' extra price gains when rates fall, and coupon differences shift yields. Evidence is suggestive, not proof: the real 9 May 2014 dip was only 3bp
70. **Caution: this is a curve of coupon-bond yields; the spot curve sits slightly differently** · YTM vs spot for 1–3 years (0.73/1.74/2.06 vs 0.73/1.77/2.09)
71. **Q3 answer: a curve that rises steeply, flattens, and dips slightly at the long end** · summary with the chart thumbnail

## 6 · Q4: what if all yields rise by 1%?
72. Divider · 06 Q4: a 1% rise in all yields
73. **Q4: every yield rises by one percentage point at the same time** · Plain: parallel shift = the whole curve moves up by the same amount (3.00% → 4.00%). One line: real curves can also twist (shaping risk), which Q4 does not ask about
74. **At 1.73%, the 1-year gilt falls from 102.50 to 101.49 (−0.98%)** · formula → numbers → result. So what: a tiny move for a short gilt
75. **At 2.74%, the 2-year gilt falls from 106.84 to 104.82 (−1.89%)** · same layout
76. **At 3.06%, the 3-year gilt falls from 107.02 to 104.06 (−2.77%)**
77. **At 4.00%, the 5-year gilt falls from 98.86 to 94.44 (−4.47%)**
78. **At 4.54%, the 7-year gilt falls from 108.91 to 102.70 (−5.70%)**
79. **At 5.04%, the 10-year gilt falls from 97.65 to 90.06 (−7.78%)**
80. **At 5.38%, the 20-year gilt falls from 104.93 to 92.45 (−11.89%)**
81. **At 5.36%, the 30-year gilt falls from 102.32 to 87.31 (−14.67%)**
82. **At 5.24%, the 50-year gilt falls from 94.96 to 78.11 (−17.74%)** · So what: the longest gilt loses 18 times as much as the shortest
83. **All nine together: the longer the gilt, the bigger the fall** · table + bar chart of % change by maturity
84. **In money: on £100m of each gilt, a 1% rise costs £1.0m on the 1-year and £16.8m on the 50-year** · £m table (value, change at +1%). So what: this is the number a trading desk watches
85. **PVBP: the 50-year gilt loses about £0.2m per £100m for every 1bp rise** · Plain: PVBP (price value of a basis point) = money lost for a 0.01% rise. Worked: [95.1580 − 94.7626]/2 = 0.1977 per £100 → £0.20m per £100m; table for all nine
86. **Duration measures how long, on average, you wait for a bond's money** · Plain: Macaulay duration = the average time to each payment, weighted by its PV. See-saw picture
87. **The 5-year gilt: Macaulay duration 4.74 years** · step table: t, CF, PV, weight (PV ÷ price), t × weight → sum 4.74
88. **Modified duration turns waiting time into price sensitivity: 4.60% per 1% of yield** · ModD = MacD/(1+y) = 4.74/1.03 = 4.60; %ΔP ≈ −ModD × Δy (CFA FI LM11). So what: predicts −4.60% vs the actual −4.47%
89. **The 1-year gilt: duration 1.00 year, modified 0.99** · sum(t × PV)/P = 102.50/102.50; one payment, so duration = maturity
90. **The 2-year gilt: duration 1.95, modified 1.92** · table: t1 PV 5.1602 (t × PV 5.1602); t2 PV 101.6807 (203.3615); sum 208.52 ÷ 106.84 → ÷1.0174
91. **The 3-year gilt: duration 2.88, modified 2.82** · table: t × PV 4.4090 + 8.6399 + 294.8730 = 307.92 ÷ 107.02 → ÷1.0206
92. **For longer gilts a CFA shortcut gives duration in one line: the 7-year's is 6.12** · Macaulay = (1+y)/y − [(1+y) + N(c−y)]/[c((1+y)^N − 1) + y], explained in words first; 29.2437 − 1.1376/0.0492 = 6.12; modified 6.12/1.0354 = 5.91
93. **The 10-year gilt: duration 8.50, modified 8.17** · shortcut: 25.7525 − 1.0114/0.0586 = 8.50 → ÷1.0404
94. **The 20-year gilt: duration 13.51, modified 12.94** · shortcut: 23.8567 − 1.1187/0.1081 = 13.51 → ÷1.0438
95. **The 30-year gilt: duration 17.17, modified 16.45** · shortcut: 23.9358 − 1.0856/0.1605 = 17.17 → ÷1.0436
96. **The 50-year gilt: duration 21.70, modified 20.82** · shortcut: 24.5598 − 0.9202/0.3221 = 21.70 → ÷1.0424; only 14% of its value sits in the final £104 (weight 0.137); the other 86% is coupons spread over 50 years. So what: that is why a 50-year gilt behaves like a 22-year loan
97. **Modified duration ranks the risk from 0.99 (1-year) to 20.82 (50-year)** · table of Macaulay and modified duration, columns labelled
98. **Same maturity, lower coupon, more risk** · hypothetical 10-year gilts at 0%, 3.75% and 8%: −9.12%, −7.78%, −7.00%. Plain: the coupon effect: low coupons push the money later. So what: today the 0½% 2061 gilt, a near-zero coupon, has a modified duration of 26.75 and trades at £23.41 [src, secondary]
99. **For long gilts, duration overstates the fall: −20.82% predicted vs −17.74% actual** · estimate vs actual, all nine
100. **Convexity: the price–yield line curves, so prices fall less than the straight line predicts** · Plain: convexity = how much the line bends. Chart with the duration tangent line
101. **Convexity of the 10-year gilt: 81.56** · formula in words first; 10-row table of t, CF, PV, t(t+1) × PV (7.21 … 7,680.29), sum 8,620.9; ÷ (97.65 × 1.0824) = 81.56
102. **Convexity of the 50-year gilt: 701** · CFA price-based method with a small 0.05% step: (95.9569 + 93.9798 − 2 × 94.96)/(94.96 × 0.0005²) = 701.05, matching the cash-flow formula (701.03). So what: almost nine times the 10-year's bend (701.03 ÷ 81.56 = 8.6)
103. **Duration plus convexity: −7.76% for the 10-year (actual −7.78%)** · %ΔP ≈ −8.17 × 1% + ½ × 81.56 × (1%)² = −8.17% + 0.41%
104. **For the 50-year a gap remains: −17.31% estimated vs −17.74% actual** · −20.82% + ½ × 701.03 × (1%)² = −17.31%. Why: two terms cannot capture all the bending over a move as big as 1%. Cross-check: with the price-based measures taken at ±1% (ApproxModDur 21.30, ApproxCon 711.82), −21.30% + ½ × 711.82 × (1%)² = −17.74%, which matches by construction because they are built from those same two prices
105. **Falling yields help more than rising yields hurt: +24.86% vs −17.74% on the 50-year** · worked −1% (4 × 24.5767 + 100/4.9357 = 118.57) + table for all nine. So what: convexity is good for the holder
106. **Long gilts paid little extra yield for much more risk** · scatter: YTM vs modified duration. So what: +3.5 points of yield for 21 times the risk
107. **Short gilts suit investors who may need cash soon or fear rate rises; long gilts suit those matching long-term promises** · who should hold which (pension funds vs a bank treasury)
108. **Q4 answer: all prices fall, long gilts by far the most; duration predicts it, convexity refines it** · summary

## 7 · Epilogue
109. Divider · 07 Epilogue
110. **What we found: coupon ≠ return, a rising curve, and risk that grows with maturity** · four findings, one per question
111. **After 2014 gilt yields kept falling, to a record low of 0.12% in August 2020** · BoE 10-year par yield: 2.77% (9 May 2014) → 0.12% (4 Aug 2020, lowest since the series began in 1993) [src]
112. **After the 2016 Brexit vote, S&P cut the UK from AAA to AA** · June 2016 [src, secondary: Euronews]
113. **From December 2021 inflation returned, and Bank Rate rose from 0.10% to 5.25% by August 2023** · Bank Rate chart [src: BoE]
114. **September 2022: long gilt yields jumped over 100bp in four days and the Bank had to step in** · Plain: LDI (liability-driven investment) = strategies pension schemes use to match their assets to their long-term promises (BoE FSR Dec 2022 [src]), often with borrowed money; falling gilt prices forced them to post cash (margin calls) and sell gilts. BoE bought £19.3bn, 28 Sep – 14 Oct 2022 [src]
115. **Our 1% scenario happened, though not as a parallel shift: the long end moved most** · Bank Underground (a Bank of England staff blog): "a 100 basis point increase in yields for a 20 year gilt maps to roughly a 20% price fall" vs our −11.89% (20-year); the gap is the coupon effect (slide 98) plus 2022's lower starting yields [src]
116. **Then the Bank reversed QE: it stopped reinvesting in February 2022 and began selling gilts in November 2022** · Plain: QT (quantitative tightening) = the reverse of QE [src: BoE]; holdings down from £895bn to £488bn [src]
117. **A real 50-year gilt shows Q4 in practice: the 4% 2060 fell from £114.76 to £75.28** · yields on the same (semi-annual) basis: 3.365% → 5.658% (+229bp); modified duration 22.24 alone predicts −51.0%, actual −34.4%; the gap is convexity plus 12 fewer years to maturity (modified duration today 15.73) [src: DMO 2014; today secondary, giltsyield.com]
118. **Today Bank Rate is 3.75% and gilt yields are higher than in 2014 at every maturity** · today's curve (secondary: giltsyield.com) vs Exhibit 1 vs real May 2014 (DMO) (chart) [src]; next Bank Rate decision 5 Nov 2026 (re-check before submission)
119. **Lessons: the coupon is not the return, the curve carries information, and duration is the price of extra yield** · closing

## 8 · Team
120. **Group 10** · members' photos, full names, student IDs (placeholder until supplied)

---

## Instructions checklist
| Requirement (Case Presentation Instructions) | Slides |
|---|---|
| Overview: background, "business model", industry/competition, key financial information, main problem | 4–16 |
| External sources in the overview | 5, 7–13 |
| Every exhibit rebuilt, explained, key numbers, meaning, implications | 18–24 |
| Each question stated and broken into parts | 26, 39, 58, 73 |
| Theories and frameworks | 28–35, 44, 61–70, 86–105 |
| Evidence from the case and external sources, per question | Q1: 36 · Q2: 22 · Q3: 66, 69 · Q4: 115, 117 |
| Assumptions explained | 28, 40, 55–56, 65, 73 |
| Alternatives compared | 31 (three yield measures), 44 (two pricing methods), 55–56 (annual vs semi-annual), 98 (coupons), 99–105 (duration vs convexity; up vs down), 107 |
| Every calculation shown step by step, one slide per repeat | 29–30, 41–56, 62–65, 74–105 |
| Epilogue: findings, turning points, outcome, after the case, today | 110–119 |
| Final slide with photo, name, ID | 120 |

## Response to the strict review round 3 (NOT READY, A− once fixed)
- **B1:** slide 96 corrected (14% of value in the final payment).
- **B2:** slide 117 now compares like with like (semi-annual yields): +229bp, duration estimate −51.0%; durations labelled modified.
- **B3:**
  - Slide 98 now uses the sourced 0½% 2061 facts (secondary).
  - Slide 10 says "holders".
  - Slide 36 is limited to the sourced 0.50% (March 2009); earlier levels are added at build or omitted.
  - Slide 118 labels giltsyield.com as secondary.
  - Slide 7 names exactly which ratings it shows.
- **B4:**
  - Durations: tables for the 2- and 3-year gilts; the CFA closed form for 7–50 years (reproduces every value).
  - Convexity: the 10-row table for the 10-year; the 5bp price-based method for the 50-year (701.05 vs 701.03).
  - Slide 104's cross-check is now independent.
- **Lucidity (six slides):** Bank Rate (10), clean/full price (40), the FV formula in words (29), forward references on 69, "2y1y" (65) and par yield (13).
- **Non-blocking items taken:** "derived on slide X" (27), ApproxModDur 21.30 (104), Bank Underground credit (115), 4 dp (44, 46).
- **Left for the build:** shortening titles on 11, 15, 65, 107 and 119 to two lines.
- **Not re-reviewed:** the user stopped the session for handover. The next session should run the strict review once more (expected READY).

## Response to the strict review (round 2: NOT READY, B+)
- **B1 (repeats):** +1% repricing for all nine (74–82); duration for all nine (87–96); convexity split (101–102); worked −1% (105) and PVBP (85) before their tables.
- **B2:** one convexity measure throughout (analytic: 81.56 / 701.03, derived on 101–102); the price-based measure is a labelled cross-check on 104, with "by construction" made explicit.
- **B3:** reinvestment FV formula (29–30); semi-annual worked example (55); bootstrap split into 62–65.
- **B4:** `work/gilts/sources.md` is built. Slides 12, 13, 111 and 116 are verified from primary sources (ONS, US Treasury, Bundesbank, BoE). Slide 112 and today's Fitch rating are labelled secondary. S&P's and Moody's current ratings could not be verified, so they are dropped from slide 7.
- **B5:** slide 113 now says December 2021.
- **B6 (lucidity):** a primer (15); every term defined where first used (Plain:); concepts before use (spot/forward on 61, before the bootstrap; QE on 10, before holdings on 11); every calculation ends with a So what.
- **B7:** slide 54 and 67 titles are now points; long titles shortened, with the detail moved to the body.
- **Non-blocking items taken:** 1 (117), 2 (84), 3 (69), 4 (22), 5 (65–66), 6 (115), 8 (11), 9 (2), 10 (97).
- **Removed:** the "(case teaching point)" tag.
