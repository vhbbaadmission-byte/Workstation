# Jaguar Land Rover: storyline (gate 1, round 3: after the strict review)

One line per slide: **section · the point (becomes the title, ≤ 2 lines, about 15 words or fewer) · what it shows**. Two tags on each line help lucidity:
- **Plain:** a term defined in plain words where it first appears
- **So what:** the one-line takeaway the slide ends with

The reader is a student part-way through CFA Level 1, reading on paper with no presenter (user rule). The full analysis stays; it is explained, not simplified.

`[src]` points to `work/jaguar/sources*.md`; numbers come from `work/jaguar/calcs.py`. All bond maths in US$, converted once at 1.50 (user rule). The case's maturity date, 15 May 2021, is used, plus one note slide (user rule). Every repeated calculation gets its own slide (user rule). The deck never refers to a teaching note.

## 0 · Opening
1. **Cover**: "Jaguar Land Rover: did refinancing at half the rate create value?" · Group 10, course [user to supply]
2. **JLR halved its interest rate in 2015; can that be a free lunch in an efficient market?** · the case's question; the four questions, one line each; the sections

## 1 · Case overview
3. Divider · 01 Case overview
4. **Two British brands, a century old, owned by Ford and then Tata** · timeline: Jaguar 1922 (Swallow Sidecar), Land Rover 1948 [src: JLR]; Ford bought Jaguar in 1989 and Land Rover from BMW in 2000 (€3bn) [src, secondary]; Tata 2008 [src: JLR]; earlier British Leyland/BMW years only as background (not sourced to primary)
5. **Tata bought JLR from Ford in June 2008 for US$2.3bn, as the crisis hit** · deal facts [src]; volumes −32% in 10 months, FY2009 loss £402.4m (case p.2)
6. **Three years later JLR made £1,115m before tax on £9.9bn of revenue** · FY2011: wholesales 243,621 (+26%), revenue £9,871m (+51%), PBT £1,115m vs £51m [src]; profit after tax £1,035.9m (case p.2)
7. **JLR sold 462,209 vehicles in FY2015; China was its biggest market** · by region: China 115,969, Europe 87,863, UK 86,750, North America 78,372, Asia Pacific 26,619, other 66,636; Changshu plant with Chery opened Oct 2014 (130,000 capacity) [src: JLR FY2015 report, release]
8. **Premium carmakers grew on SUVs and China, while the EU set a 95g CO2/km target for 2020** · Land Rover brand +8.9% in FY2015 to 385,279 [src: JLR]; EU Regulation 333/2014 [src]. Plain: CO2 g/km target = the average emissions limit per car sold
9. **JLR sold about a quarter as many cars as BMW, Audi or Mercedes-Benz** · 2014: BMW 1,811,719 (secondary), Audi 1,741,129 (secondary), Mercedes-Benz 1,650,010, Porsche 189,849; JLR 462,209 (FY2015) [src]
10. **JLR is Tata Motors' cash engine: over 80% of its automotive revenue** · and the only source of consolidated operating profit in FY2014 (case p.2)
11. **JLR borrows in pounds and dollars to match where it earns** · Plain: natural hedge = borrowing in the currency you earn in, so currency moves hit both sides; ~17% of revenue each from the UK and North America (case p.2)
12. **JLR's credit improved: Moody's upgraded it to Ba2 in 2013 and outlooks turned positive in 2014** · Plain: credit rating = an agency's grade of default risk; Ba/BB = "high yield" (below investment grade) (case p.2) [src]
13. **But heavy spending lay ahead: £3.6–3.8bn of capex planned for FY2016** · Moody's expected free cash flow to turn negative (case p.2). Plain: capex = spending on plants and equipment
14. **In early 2015 the Fed was at zero, but high-yield spreads had widened to about 460bp** · Fed funds 0–0.25% until Dec 2015 [src]; high-yield spreads 330bp (2014) → ~460bp (Mar 2015) [src, secondary]. So what: the market was not getting easier; JLR still borrowed at only 193bp over Treasuries
15. **JLR refinanced twice in two months: sterling in February, dollars in March 2015** · Feb: £400m 3.875% 2023 replaces £500m 8.25% 2020; Mar: US$500m 3.5% 2020 replaces US$410m 8.125% 2021 [src; case p.1]
16. **Holders could sell their notes back, swap into the new issue, or keep them without covenant protection** · Plain: tender offer = the issuer offers to buy its own bonds; consent solicitation = asking holders to vote away the covenants (the promises that protect them); early premium = an extra US$30 per US$1,000 for answering by 16 March [src]
17. **The deal in one picture: US$500m raised, US$472m spent buying back old notes, US$28m left before fees** · flow diagram, every arrow labelled with the money and what it is

## 1b · Bond toolkit (concepts used in the rest of the deck)
18. **A bond's price is quoted per 100 of face value; JLR's notes pay coupons twice a year** · Plain: face value = the amount repaid at maturity; coupon = the fixed interest (8.125% a year = US$40.625 per US$1,000 every six months)
19. **A basis point (bp) is one hundredth of a percentage point** · 1bp = 0.01%; 8.125% − 3.50% = 4.625 points = 462.5bp
20. **Money paid later is worth less today: present value and discounting** · Plain: PV = future cash ÷ (1 + rate)^time; one-bond example. So what: every valuation in this deck is this one idea
21. **Yield to maturity: the single rate that makes the PV of a bond's cash equal its price** · higher yield → lower price
22. **A company's yield = a Treasury yield + a credit spread** · Plain: credit spread = the extra yield investors want for the company's default risk (CFA FI LM07); two-layer picture
23. **A call option lets JLR repay early at a set price; investors then look at yield to call and yield to worst** · Plain: yield to call = the yield if repaid on the call date; yield to worst = the lower of the two. So what: a callable bond's price is capped near its call price
24. **Between coupon dates a buyer pays the price plus the interest earned so far** · Plain: clean price = quoted price; accrued interest = coupon earned since the last payment; full price = clean + accrued (CFA FI LM06)

## 2 · Exhibit analysis
25. Divider · 02 Exhibit analysis
26. **Exhibit 1: JLR owed £2.4bn at end-2014, almost all in six fixed-rate notes** · native table, rebuilt, source line
27. **Notes are 92% of borrowing; the £1,485m credit line is completely unused** · composition chart. Plain: revolving facility = a pre-agreed credit line
28. **The two oldest notes cost most, 8.125% and 8.25%, and both become callable in 2016** · notes ranked by coupon, with call dates
29. **Those two notes cost £34.5m a year more than JLR's 2015 rates** · at 1.50: US$410m = £273.3m × (8.125 − 3.5)% = £12.6m; £500m × (8.25 − 3.875)% = £21.9m. So what: a clear target for refinancing
30. **JLR's spread over Treasuries fell from 497bp in 2011 to 189bp in 2015, with one small rise in 2014** · spread at each US$ issue: 497 (May 2011) → 362 (Jan 2013) → 260 (Dec 2013) → 272 (Oct 2014) → 189 (Mar 2015) [src: Treasury CSVs; issue dates partly approximate]
31. **Repayments are spread from 2018 to 2023, so there is no single wall of debt** · maturity ladder (£m per year)
32. **Exhibit 1 converts dollars at about 1.56; the case tells us to use 1.50 for March 2015** · 410/263 = 1.559; £263m vs £273.3m. So what: we keep the bond maths in dollars and convert once
33. **Exhibit 2: the market valued the 8.125% notes at 111.28, an 11% premium** · native table; plain notes on its jargon (two ISIN lines = the same bond sold to US and non-US investors; "i" = indicative price, no trade that day); price dated 4 Feb 2015, before the offer; second line stale (Aug 2014)
34. **At 111.28 the notes yielded 5.94% to 2021 but only 2.28% to the 2016 call** · calc both. So what: the market already priced the bond as if JLR would repay it in 2016
35. **The sterling 8.25% notes told the same story at 110.94** · the second old bond, refinanced in February [src]
36. **The new 2015 notes trade at 100, so their coupons equal JLR's market yield** · 3.5% 2020 and 3.875% 2023 rows
37. **Exhibit 3: from 2011 to 2015, long Treasury yields fell a lot; short ones barely moved** · rebuilt chart from Treasury data (axis titles, units)
38. **The 10-year Treasury fell 105bp, the 5-year only 26bp** · change-by-maturity bars; the 14-month Treasury that priced the tender (0.395%) marked. So what: lower Treasury yields explain little of JLR's lower 5-year rate
39. **Exhibit 4: revenue grew 43% and profit before tax 69% in two years** · native table; growth bars FY2012–FY2014 (FY2015 shown as 9 months)
40. **EBITDA margin rose from 14.8% to 18.0%** · Plain: EBITDA = profit before interest, tax, depreciation and amortisation (a cash-earnings proxy). Step by step each year: PBT + D&A + finance expense − finance income − FX gain
41. **Capitalised development costs equal 38–51% of profit before tax** · Plain: capitalising = recording R&D as an asset instead of an expense, which lifts this year's profit. So what: profit quality needs care
42. **The tax rate jumped from 1% to 27%: FY2012 profit was flattered by tax credits** · effective tax rate by year
43. **Exhibit 5: operations brought in £2.4–3.4bn of cash a year** · native table; CFO bars. Plain: CFO = cash from operations
44. **Free cash flow stayed positive but thin, and Moody's expected it to turn negative** · Plain: FCF = CFO − capex. £1,090m, £580m, £1,066m, £540m (9 months); after cash interest and dividends £962m, £251m, £647m, £293m
45. **Cash interest is small next to earnings: EBITDA covers it 12 to 30 times** · EBITDA ÷ cash finance paid (not the P&L figure, which nets off capitalised interest)
46. **Exhibit 6: equity more than doubled, from £2.9bn to £6.8bn** · native table; equity bars
47. **JLR held more cash than debt: net cash rose from £456m to £1,604m** · cash + deposits − debt, by year
48. **Debt/equity halved, from 0.68 to 0.36** · ratio table by year
49. **The exhibits together: a stronger borrower, expensive callable notes, and a market already pricing the call** · synthesis linking each exhibit to Q1–Q4

## 3 · Q1: why could JLR borrow at less than half the 2011 rate?
50. Divider · 03 Q1
51. **Q1: what let JLR's coupon fall from 8.125% to 3.5%?** · three candidate causes: Treasury rates, the bond's length and features, JLR's credit. Assumptions: issued at par; Treasuries matched to each note's length
52. **2011: 8.125% = 3.15% Treasury + 497bp spread** · 10-year Treasury, 16 May 2011
53. **2015: 3.50% = 1.57% Treasury + 193bp spread** · 5-year Treasury, 16 Mar 2015
54. **Two thirds of the 462bp fall came from a narrower credit spread** · waterfall: spread 304bp (66%); Treasury level and shorter length 158bp (34%). Plain: the 304bp also includes the value of the 2011 notes' call feature
55. **At the same 5-year length, Treasuries fell only 26bp** · 1.83% → 1.57%
56. **Test 1: the same bond's yield fell from 8.125% at issue to 2.28% to the call in 2015** · Exhibit 2
57. **Test 2: across five dollar issues, JLR's spread fell by 308bp** · 497 → 362 → 260 → 272 → 189bp (slide 30's data), tenor-matched
58. **Test 3: market-wide high-yield spreads fell about 40bp; JLR's fell 304bp** · Plain: high-yield index spread = the average spread of all below-investment-grade bonds; ~502bp (May 2011) vs ~460bp (Mar 2015), different indices and dates, indicative only [src, secondary]. So what: about 260bp is JLR-specific
59. **The reason: JLR became a far safer borrower** · dashboard from Exhibits 4–6 (EBITDA margin, net cash, debt/equity, cover) + ratings
60. **The 2015 notes are also shorter, and the 2011 notes' call had to be paid for** · Plain: tenor effect = shorter loans usually cost less; 2011 notes sold as "callable after five years" [src]; the 2020 notes' early-repayment terms were not found, so no claim is made
61. **Q1 answer: mostly JLR's better credit; lower rates and a shorter term explain the rest** · summary with the waterfall

## 4 · Q2: what price would bondholders accept?
62. Divider · 04 Q2
63. **Q2: what price makes holders give up their 8.125% notes?** · holders' choices: sell in the market, keep (and be repaid in 2016), tender early or late, swap into the new notes
64. **The cash still due: US$40.625 every May and November, then US$1,000** · timeline to 2021
65. **JLR can repay these notes from 15 May 2016 at 104.0625%** · call terms [src]; why 104.0625 (par + half a coupon; it reproduces the actual tender price)
66. **With 8.125% to pay and 3.5% available, JLR will certainly repay in 2016** · so the notes behave like a 14-month bond. So what: value them to May 2016, not 2021
67. **Accrued interest at 17 March 2015: 122 days → US$27.53 per US$1,000** · 30/360 in words (every month counts as 30 days, a year as 360); 122/180 × 40.625; 31 March: 136 days → US$30.69 [src: matches JLR's payments]
68. **Step 1: discount the three payments to May 2016 at the 14-month rate** · discount rate choice in words: a holder's required yield for 14 months of JLR risk
69. **The market's 14-month rate for JLR was about 2.28%** · from Exhibit 2's price (yield to call)
70. **At 2.28%, the notes are worth 110.61** · step table: 4.0625, 4.0625, 108.125 → discount factors → full price → − accrued 2.75 = clean 110.61
71. **The value to call ranges from 112.85 at 0.5% to 109.11 at 3.5%** · sensitivity table. So what: the lower the 14-month rate, the more holders can ask
72. **JLR priced its offer the same way: to the 2016 call, at the May 2016 Treasury yield + 0.50%** · Plain: reference Treasury = the government bond whose yield sets the price; fixed spread = a set margin added to it. The 0.25% coupon note yielded 0.395% on 16 March [src]
73. **At 0.895% the price is 112.35, JLR's offer to within US$0.01 per US$1,000** · step table: discount factors → full 115.10 − accrued 2.75 = 112.35
74. **Early tenders got US$1,123.52 per US$1,000, late ones US$1,093.52, both plus accrued interest** · early premium US$30 [src]
75. **A callable bond is worth the plain bond minus JLR's option to repay** · Plain: CFA rule callable = straight − call option; picture of the price capped near the call price (called "negative convexity")
76. **The naive view ignores the call: discounting to 2021 at 3.5% gives 125.43** · why 3.5% (JLR's new borrowing cost), cash-flow table, 1 of 2
77. **The naive view, continued: full 128.18 − accrued 2.75 = clean 125.43** · result
78. **So JLR's option to repay was worth about 14 points** · 125.43 − 111.28 (approximate: different dates and yields). So what: paying 125 would hand holders ~US$54m for an option JLR owns
79. **JLR's filings date the maturity 15 November 2021; that moves only the naive value, to 127.26** · case date used throughout (user rule); filing quoted [src]
80. **Five values side by side: 109.11, 110.61, 111.28, 112.35 and 125.43** · reconciliation chart, each labelled with its method, rate and date
81. **Q2 answer: about 111–112 per 100 plus accrued interest, US$456–461m for the whole issue** · summary; consent solicitation as an extra push to tender

## 5 · Q3: incremental cash flows and savings
82. Divider · 05 Q3
83. **Q3: does buying back all the notes at 112.35 save JLR money?** · split: accounting saving vs economic value; before and after tax
84. **How we judge it: net present value of the change in cash flows** · Plain: incremental cash flow = cash with the deal minus cash without it; NPV = PV of those differences; positive = JLR better off
85. **Assumptions** · all US$410m bought at 112.35 (the actual early price; our Q2 range's top) on 17 Mar 2015; funded with new 3.5% debt; tax 21% on the premium (deal year), 20% after; fees ignored, then noted
86. **JLR needs US$471.9m to buy the notes, leaving US$28.1m from the US$500m before fees** · 410 × (112.35 + 2.75)%
87. **The accounting view: interest falls by US$16.8m a year on the same funding** · US$33.3m (8.125% × 410) vs US$16.5m (3.5% × 471.9)
88. **But JLR pays US$50.6m above face value up front, three years of savings** · premium, including the US$12.3m early premium
89. **New debt borrowed at the market rate adds no value by itself** · PV at 3.5% of the new-debt payments = US$472.0m ≈ the US$471.9m borrowed. So what: the NPV is simply the value of old debt avoided minus cash paid
90. **Naive baseline, 2015–2017: old payments avoided, discounted at 3.5%** · table: date, cash flow, discount factor, PV
91. **Naive baseline, 2018–2021, continued** · same columns; total PV US$525.5m
92. **Against keeping the notes to 2021, the NPV looks like +US$53.6m** · 525.5 − 471.9. So what: this is the illusion, because JLR would never keep 8.125% debt it can repay
93. **Realistic baseline: JLR repays in May 2016, valued at the market's 2.28%** · table: 3 payments, discount factors, PV US$464.8m
94. **Against the realistic baseline, the NPV is −US$7.1m** · 464.8 − 471.9. So what: JLR paid a little more than the debt was worth
95. **At the offer's own 0.895% rate, the NPV is zero** · PV US$471.9m. So what: the offer was priced at fair value for a near-risk-free 14-month claim
96. **After tax, step 1: the premium is tax-deductible, saving US$10.6m at 21%** · after-tax cash paid US$461.3m
97. **After tax, step 2: old interest after tax, discounted at the after-tax rate** · Plain: after-tax rate = rate × (1 − tax rate), because interest cuts tax; 2.28% × 0.8 = 1.82% (realistic); 3.5% × 0.8 = 2.80% (naive)
98. **After tax, the answer holds: −US$7.3m realistic, +US$43.0m naive** · results
99. **The answer depends on the baseline, and the realistic one shows no saving** · comparison table: naive / realistic at 2.28% / at 0.895% / vs market (−US$4.4m), pre- and after-tax
100. **Q3 answer: a real cash-interest saving, but no economic saving; JLR paid the gain away up front** · summary

## 6 · Q4: other benefits, and who gains?
101. Divider · 06 Q4
102. **Q4: what else does JLR gain, and who wins: JLR, the bondholders or Tata Motors?** · question split; assumptions
103. **In an efficient market, swapping debt at fair prices creates no value** · Plain: market efficiency = prices already reflect public information; Modigliani–Miller = financing choices don't change a firm's value (before taxes and costs) (CFA CI LM06, EQ LM03)
104. **JLR's choices: do nothing, wait and repay in 2016, buy notes in the market, or tender now** · each with its cost (market 111.28; call 104.0625 + coupons; tender 112.35)
105. **Tendering locked in 3.5% before the Fed's first rate rise, at the cost of paying about 8 points early** · Fed raised rates in Dec 2015 [src]
106. **Reported profit rises: interest falls US$16.8m a year after a one-off US$50.6m charge** · P&L effect
107. **Holders who stayed lost their covenant protection** · what covenants restrict, and why removing them helps JLR [src]
108. **US$28m of extra cash is small next to £3.6–3.8bn of capex** · liquidity
109. **Moving repayment from 2021 to 2020 adds refinancing risk** · trade-off; foreshadows 2020 (epilogue)
110. **The deal signals confidence to investors and rating agencies** · signalling theory (CFA)
111. **JLR as a firm: roughly no value created, as theory predicts** · tie to Q3; a lower coupon also means a slightly smaller tax saving on interest
112. **Holders who tendered gained 1.08 per 100 over the market, US$4.4m in total** · and 1.74 per 100 (US$7.1m) over waiting to be repaid in 2016; those who stayed were repaid at 104.0625 in May 2016
113. **Tata Motors, the only shareholder, ends up slightly worse off** · who pays the holders' gain, plus fees
114. **Q4 answer: soft benefits for JLR, a small gain for bondholders, nothing for Tata Motors** · who-gains table

## 7 · Epilogue
115. Divider · 07 Epilogue
116. **What we found** · four findings, one per question
117. **79.61% of the notes were tendered, almost all early, for US$375.7m including interest** · results [src]
118. **The remaining US$83.6m was repaid in May 2016, the first call date** · [src: Tata Motors 20-F FY2016]
119. **Sales rose for three years to a record 614,309 in FY2018, then fell for three** · retail: 462,209 (FY15), 521,571, 604,009, 614,309, 578,915, 508,659, 439,588 (FY21) [src: JLR]
120. **FY2019: a £3.6bn loss, including a £3.1bn write-down, and the Project Charge savings plan** · Project Charge £2.5bn target, later £5bn; COVID shut all plants for two months; the chip shortage [src: JLR]
121. **Hindsight: 3.5% was cheap. When the notes fell due in March 2020, JLR was paying 5.875–7.75% on new debt** · repaid from cash in March 2020; €500m 5.875% 2024 and €500m 6.875% 2026 (Nov/Dec 2019), US$700m 7.75% 2025 (Oct 2020); ratings fell to S&P B+, Moody's B1 [src: JLR]. So what: the 2015 deal locked in cheap money, but brought repayment forward into a crisis
122. **2021: "Reimagine" turns Jaguar into an all-electric brand from 2025** · £1.5bn of exceptional charges; FY2021 loss before tax £861m [src: JLR]
123. **S&P rated JLR investment grade in August 2024; Moody's sits one notch below** · S&P BBB- (20 Aug 2024), Moody's Ba1 (13 Jun 2025) [src: JLR]; after the cyber-attack Moody's outlook turned negative (Sep 2025) and S&P's too (May 2026) [src, secondary]
124. **2025: a cyber-attack stopped production for five weeks** · impact [src]
125. **Today JLR is barely profitable: Q1 FY2027 revenue £6.0bn, profit before tax £109m** · adjusted EBIT margin 2.8%; FY2026 revenue £22.9bn; owned by Tata Motors Passenger Vehicles after the Oct 2025 demerger (secondary) [src]
126. **The lesson: better credit cuts the cost of new debt, but buying back old debt at a fair price creates no value** · closing

## 8 · Team
127. **Group 10** · members' photos, full names, student IDs (placeholder until supplied)

---

## Instructions checklist
| Requirement | Slides |
|---|---|
| Overview: history, business model, industry and competition, financials, main problem | 4–17 |
| External, current information | 4–9, 12, 14–16, 117–125 |
| All 6 exhibits rebuilt, explained, key numbers, meaning, implications | 26–49 |
| Each question stated and broken into parts | 51, 63, 83, 102 |
| Theories and frameworks | 18–24, 54, 75, 84, 89, 97, 103, 110 |
| Evidence (case + external) | 56–60, 65, 72–74, 105, 107 |
| Assumptions explained | 51, 66, 68, 85, 102 |
| Alternatives compared | 70/73/76/80 (four valuations), 92–99 (baselines, pre- and after-tax), 104 |
| Every calculation shown step by step, one slide per repeat | 29, 32, 34, 40–48, 52–58, 64–80, 86–99, 112 |
| Chronological sequence | 4–17, 117–125 |
| Epilogue: findings, turning points, outcome, after the case, today | 116–126 |
| Final slide | 127 |

## Sources round 3 applied (2026-10-30)
- Slides 4, 7–9, 30, 57 and 119–125 now carry sourced figures. Secondary sources are labelled.
- Unverified history (BMW and British Leyland dates) stays as background only.
- Industry-wide premium SUV growth was not found; Land Rover's own growth is used instead.
- **Not re-reviewed:** the user stopped the session for handover. The next session should run the strict review (round 3) on this plan.

## Response to the strict review (round 2: NOT READY, B+)
- **B1 (lucidity):** a bond toolkit (18–24) before the exhibits; an NPV concept slide (84); MM and market efficiency (103); a "Plain:" definition and a "So what" on each slide the review listed.
- **B2:** the realistic baseline is now valued at 2.28% (the market's 14-month yield) and at 0.895% (the offer's rate); 3.5% is kept only for the naive 2021 view. New figures: −US$7.1m / 0; after tax −US$7.3m; holders +1.74 over the call (112).
- **B3:** PV tables with discount factors (90–95); a proof that NPV = PV avoided − cash paid (89); after-tax split into 96–98, with the 21%/20% timing stated.
- **B4:** slide 30 retitled; 123 corrected (S&P investment grade, Moody's not); the 2011 B1 rating removed (12); 1.08 (112).
- **B5:** sources for 4, 7–9 and 119–125 are being fetched by a strict helper. Any fact still unsourced comes off its slide. Slide 14 reframed (spreads widened).
- **B6:** Q2 now leads with the call-aware value (64–74); the naive value follows (76–78). Slide 29 uses 1.50.
- **B7:** titles shortened to about 15 words or fewer; labels turned into points.
- **Non-blocking items taken:** 1 (54), 4 (78), 5 (81), 7 (104), 8 (38), 10 (58).
