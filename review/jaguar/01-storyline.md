# Jaguar Land Rover: storyline (gate 1)

One line per slide: **section · the point (becomes the title) · what it shows**. `[src]` = external fact with a source line (in `work/jaguar/sources*.md`). Numbers are from `work/jaguar/calcs.py`. All bond maths in US$; £ only at 1.50 (user decision).

## 0 · Opening
1. **Cover**: "Jaguar Land Rover: did refinancing at half the rate create value?" · Group 10, course [user to supply]
2. **What this deck answers**: the question the case poses ("can a positive-sum game exist in an efficient market?"), the four questions, the sections

## 1 · Case overview
3. Divider · 01 Case overview
4. **JLR today: Britain's largest carmaker, owned by India's Tata Motors** · snapshot numbers: latest revenue, retail sales, employees, plants [src]
5. **Two British brands with a century of history and many owners** · timeline: Jaguar 1922, Land Rover 1948, British Leyland, BMW/Ford, Ford 1989/2000, Tata 2008 [src; case p.1]
6. **Tata bought JLR from Ford in 2008 for US$2.3bn, just as the crisis hit** · deal facts; volumes −32% in 10 months; FY2009 loss £402.4m (case p.2)
7. **By FY2011 JLR had turned around to a £1,035.9m profit** · loss-to-profit chart FY2009–FY2014 (case p.2, Exhibit 4)
8. **JLR sells premium SUVs and luxury cars worldwide from British plants** · business model: brands/products, regions (UK, North America, China, Europe), manufacturing footprint [src]
9. **It competes with BMW, Mercedes-Benz, Audi and Porsche in the premium segment** · competitor comparison (volumes or revenue) [src]
10. **JLR is Tata Motors' cash engine: over 80% of automotive revenue in FY2014** · share of Tata Motors' revenue and operating profit (case p.2) [src for figures]
11. **JLR borrows in both pounds and dollars to match where it earns** · natural hedge explained; ~17% of revenue each in UK and North America (case p.2, Exhibit 1 note)
12. **Credit improved fast: Moody's upgraded JLR to Ba2 in 2013 and outlooks turned positive in 2014** · rating path 2011–2015 (case p.2) [src for dates/agencies]
13. **But heavy investment lay ahead: £3.6–3.8bn of capex planned for FY2016** · capex plan and Moody's free-cash-flow concern (case p.2)
14. **Early 2015 was a good time to borrow: low Treasury yields and strong demand for high-yield bonds** · context [src]
15. **March 2015: JLR sells US$500m of 5-year notes at 3.5% to buy back its 8.125% notes** · the deal in a diagram: new notes in, old notes out; Feb 2015 sterling refinancing as the "first of two" (case p.1) [src]
16. **Holders could sell their old notes to JLR or roll them into the new issue by 30 March** · tender-offer mechanics, early vs final deadline (case p.1) [src]
17. **The question: if JLR halves its interest rate, who pays for it?** · the case's framing: a free lunch in an efficient market?
18. **How we answer it** · Q1–Q4, each with its CFA concept (spreads and credit; bond valuation with a call; NPV of refinancing; MM and market efficiency)

## 2 · Exhibit analysis
19. Divider · 02 Exhibit analysis
20. **Exhibit 1: JLR's debt at 31 December 2014** · native table, rebuilt, with source line
21. **Six bond issues make up 92% of borrowing; the £1,485m revolver is completely undrawn** · composition chart (notes vs factoring vs undrawn)
22. **The two 2011–12 notes carry the highest coupons (8.125% and 8.25%), and both become callable in 2016** · notes ranked by coupon, with call dates
23. **Repayments are spread from 2018 to 2023, so there is no maturity wall** · maturity ladder chart (£m per year)
24. **Implication: the expensive callable notes are the obvious ones to refinance** · link to the case decision
25. **Exhibit 2: JLR bonds on the Luxembourg exchange** · native table (coupon, ISIN, dates, last price), "i" = indicative
26. **The 8.125% 2021 notes traded at 111.28, an 11% premium to face value** · the price explained per US$1,000; second ISIN's price is stale (Aug 2014)
27. **At 111.28 the market yield was 5.94% to maturity but only 2.28% to the 2016 call: the market already priced in the call** · YTM vs yield to call (calc from calcs.py; CFA yield-to-worst)
28. **New 2015 issues priced at par (100), so their coupons equal market yields** · the 3.5% 2020 and 3.875% 2023 rows; implication for Q1
29. **Exhibit 3: the US Treasury curve, May 2011 vs March 2015** · rebuilt line chart from Treasury's official data (axis titles, units)
30. **Long Treasury yields fell a lot (10-year −105bp), but the 5-year fell only 26bp** · change-by-maturity bar chart
31. **Implication: Treasuries explain little of JLR's lower 5-year rate** · sets up Q1
32. **Exhibit 4: income statements FY2012–FY2015 (9 months)** · native table
33. **Revenue grew 43% in two years and profit before tax 69%** · revenue and PBT bars (FY2015 annualised, method stated)
34. **Margins held up: EBITDA margin [x]% → [y]%** · EBITDA calculation (PBT + D&A + net finance − FX) shown step by step, by year
35. **Interest is tiny next to profit: interest cover above [x] times** · interest cover calc
36. **Implication: a much stronger borrower than in 2011** · link to credit spreads
37. **Exhibit 5: cash flow statements** · native table
38. **Operations generate about £3bn a year, but investment absorbs almost all of it** · CFO vs capex + intangibles chart
39. **Free cash flow is thin and turning negative** · FCF calculation per year (CFO − PPE − intangibles), with dividends
40. **Implication: JLR still needs debt markets, so lower borrowing costs matter** · link to the decision
41. **Exhibit 6: balance sheets** · native table
42. **Equity more than doubled, from £2.9bn to £6.8bn** · equity bars; retained profits
43. **JLR holds more cash than debt: net cash of £[x]m** · cash + deposits vs short- and long-term debt, calc by year
44. **Leverage fell: debt/equity [x] → [y]** · ratio table (debt/equity, debt/capital, current ratio)
45. **What the exhibits tell us together** · one-page synthesis: better credit, low Treasuries only at the long end, expensive callable notes, a market that already priced the call

## 3 · Q1: why could JLR borrow at less than half the 2011 rate?
46. Divider · 03 Q1
47. **Q1 asks what let JLR's coupon fall from 8.125% to 3.5%** · question stated; split into: market rates, maturity, JLR's own credit
48. **A corporate bond's yield is a benchmark Treasury yield plus a credit spread** · CFA FI LM07: yield = benchmark + spread; picture of the two layers
49. **2011: 8.125% = 3.15% Treasury + 497bp spread** · calc with the 10-year Treasury on 16 May 2011
50. **2015: 3.50% = 1.57% Treasury + 193bp spread** · calc with the 5-year Treasury on 16 Mar 2015
51. **Two thirds of the 462bp fall came from JLR's credit spread** · waterfall: 304bp credit (66%), 158bp Treasury level and shorter maturity (34%)
52. **Like for like at 5 years, Treasury yields fell only 26bp** · 1.83% → 1.57%; the teaching point
53. **Why the spread narrowed: JLR became a far safer borrower** · ratio dashboard from Exhibits 4–6 (profit, margin, net cash, leverage) and rating upgrades [src]
54. **Why the spread narrowed: investors wanted high-yield bonds in 2015** · market context [src]
55. **Why the spread narrowed: a 5-year note is less risky than a 10-year** · tenor and credit term structure (CFA)
56. **Answer to Q1** · summary: credit (two thirds), rates and maturity (one third)

## 4 · Q2: what price would bondholders accept?
57. Divider · 04 Q2
58. **Q2 asks what price would make holders give up their 8.125% notes** · question; holder's options: sell in the market, keep, tender
59. **A bond's price has two parts: the clean price and the interest accrued since the last coupon** · CFA definitions, formula
60. **Accrued interest on 17 March 2015: 122 days → US$27.53 per US$1,000** · step calc (30/360); matches the actual payment [src]
61. **Valuing the notes, step 1: list the remaining cash flows** · coupon US$40.625 per US$1,000 every May/Nov to May 2021, then US$1,000
62. **Method A: discount to 2021 at JLR's new rate (3.5%) → 125.43** · formula, the 13 cash flows discounted (table split if needed), clean = full − accrued; a 25% premium
63. **But no holder will get 125: JLR can call the notes in May 2016** · what a call option is; the call schedule [src]
64. **When the coupon is far above market rates, the issuer will call: the bond behaves like a 14-month bond** · CFA yield-to-call and yield-to-worst; the issuer's choice
65. **Method B: discount to the May 2016 call at 3.5% → 109.11** · 3 cash flows + call price, step table, result
66. **The right discount rate for 14 months is lower than 3.5%** · JLR's short-term credit risk is small; sensitivity table, clean value to call at 0.5%–3.5% (112.85 → 109.11)
67. **The market agreed: 111.28 implies a 2.28% yield to the call** · Exhibit 2 check
68. **The actual tender priced the notes to the 2016 call at a Treasury yield plus a fixed spread** · tender formula from the offer documents [src]; step table at 0.89% → 112.35
69. **Early tenders got US$1,123.52 per US$1,000 (incl. a US$30 early premium); late tenders US$1,093.52** · [src]; plus accrued US$27.53 / US$30.69
70. **Four answers, one picture: 109.11, 111.28, 112.35 and 125.43** · reconciliation bar chart, each labelled with its method
71. **Why the teaching benchmark of 25–29% is too high** · it values the notes to 2021 and ignores the call; a 125 bid would hand holders ~US$54m for nothing
72. **Answer to Q2** · holders would accept about 111–112 per 100 clean (US$457–461m for the issue), plus accrued interest

## 5 · Q3: incremental cash flows and savings
73. Divider · 05 Q3
74. **Q3 asks whether refinancing saves JLR money if it buys all the notes at the Q2 price** · question; split: accounting saving vs economic value
75. **Assumptions** · all US$410m bought at 112.35 on 17 Mar 2015; funded with new 3.5% debt; US$; fees ignored at first (then shown)
76. **The accounting view: interest falls by US$19.0m a year** · US$33.3m (8.125%) → US$14.4m (3.5%) on US$410m; £12.6m at 1.50
77. **But JLR pays a US$50.6m premium up front, 2.7 years of those savings** · premium calc (incl. US$12.3m early premium)
78. **Incremental cash flows, 2015–2017** · table: old coupons avoided, new coupons paid, net (split over slides 78–80, readable)
79. **Incremental cash flows, 2018–2019**
80. **Incremental cash flows, 2020–2021** · new debt repaid Mar 2020; old principal avoided May 2021
81. **If the old notes would have run to 2021, the NPV is +US$53.5m** · NPV at 3.5% step summary; this is the teaching note's view
82. **But JLR would have called them in 2016; against that, the NPV is −US$13.4m at 3.5%** · same table, old path ending in the May 2016 call
83. **At market prices the deal is roughly break-even: about −US$4m** · value avoided (111.28) − price paid (112.35), × US$4.10m
84. **The deal NPV depends on what you compare it with** · comparison table: vs hold to 2021, vs call 2016, vs market; sensitivity to the discount rate
85. **Answer to Q3** · real cash-interest saving, but no economic saving: JLR paid away the gain up front, as an efficient market predicts

## 6 · Q4: other benefits, and who gains?
86. Divider · 06 Q4
87. **Q4 asks what else JLR gains and who wins: the firm, the bondholders or the shareholders** · question split into three
88. **Reported profit rises: lower interest expense and higher interest cover** · P&L effect (after a one-off loss on the premium)
89. **JLR swaps tight 2011 junk-bond covenants for the terms of a stronger borrower** · covenant comparison [src]
90. **It raises US$90m of extra cash ahead of £3.6–3.8bn of capex** · liquidity
91. **It brings the maturity forward to 2020 and lowers the cost of its benchmark curve** · maturity profile before/after
92. **It signals confidence to investors and rating agencies** · signalling (CFA capital structure)
93. **Costs: the premium, the early-tender payment and issue fees** · cost list
94. **The firm: about zero value created, as Modigliani–Miller and market efficiency predict** · MM in plain words; tie to Q3 NPV
95. **Bondholders gain: US$1.07 per 100 above the market price, US$3.24 above the value to call** · gain calc × US$4.10m
96. **Shareholders: about neutral, slightly negative after fees and the premium** · who pays the bondholders' gain
97. **Answer to Q4** · who-gains table (firm, bondholders, shareholders) and the soft benefits

## 7 · Epilogue
98. Divider · 07 Epilogue
99. **What we found** · four findings, one per question
100. **79.6% of holders tendered (US$326.4m) and were paid up to US$366.7m plus accrued interest** · tender results; 326.42 × 112.352 if all tendered early [src]
101. **The rest of the notes were called in 2016** · redemption date and price [src]
102. **2015–2018: record sales, then trouble: China, diesel and Brexit** · sales and profit chart FY2015–FY2019 [src]
103. **2019–2021: big losses and a turnaround plan** · Project Charge, COVID, chip shortage [src]
104. **2021: "Reimagine" bets on electric luxury cars** · strategy [src]
105. **Recovery: record profit in FY2024 and investment-grade ratings** · results and rating upgrades [src]
106. **2025: a cyber-attack stopped production for weeks** · impact [src]
107. **Where JLR stands today** · latest results, net debt, ratings, ownership [src]
108. **What the case teaches** · better credit lowers new borrowing costs, but buying back old debt at a fair price does not create value

## 8 · Team
109. **Group 10** · members' photos, full names, student IDs (placeholder until the user supplies them)

---

## Instructions checklist
| Requirement (Case Presentation Instructions) | Slides |
|---|---|
| Overview: background and history | 4–7 |
| Business model, products | 8 |
| Industry and competition | 9 |
| Major financial or operational information | 7, 10–13 |
| Main problem or decision | 15–17 |
| External, current information in the overview | 4, 5, 8, 9, 12, 14 |
| All 6 exhibits inserted (rebuilt), explained, key numbers, meaning, implications | 20–45 |
| Each question stated and broken down | 47, 58, 74, 87 |
| Theories and frameworks | 48, 55, 59, 63–64, 94, 92 |
| Evidence from case and external sources | 53–54, 63, 68–69, 89 |
| Assumptions explained | 60, 66, 75 |
| Alternatives compared | 62/65/67/68/70 (four valuations), 81–84 (three baselines), 95–96 |
| Calculations shown step by step on slides | 27, 34–35, 39, 43–44, 49–52, 60–70, 76–84, 95 |
| Chronological sequence | overview timeline 5–16; epilogue 100–107 |
| Epilogue: findings, turning points, outcome, after the case, today | 99–108 |
| Final slide with photo, name, ID | 109 |
