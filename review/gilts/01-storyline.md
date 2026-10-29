# UK Gilts: storyline (gate 1)

One line per slide: **section · the point (becomes the title) · what it shows**. `[src]` = external fact with a source line (in `work/gilts/sources*.md`). Numbers are from `work/gilts/calcs.py`.

## 0 · Opening
1. **Cover**: "UK Gilts: pricing, yields and interest-rate risk" · Group 10, course [user to supply]
2. **What this deck answers**: the four questions, each in one line, plus the five sections (overview → exhibit → analysis → epilogue → team)

## 1 · Case overview (the market, not a company)
3. Divider · 01 Case overview
4. **A gilt is a loan to the UK government that pays a fixed coupon twice a year** · plain definition; diagram of cash flows on a £1,000 holding of 4% Treasury Gilt 2016 (£20 each Mar/Sep, £1,000 back) (case p.2)
5. **Gilts are priced per £100 of face value and quoted with coupon and maturity** · anatomy of a gilt name "4% Treasury Gilt 2060": coupon, issuer, maturity (case p.2, DMO [src])
6. **Two kinds: conventional gilts (fixed cash) and index-linked gilts (cash rises with inflation)** · side-by-side comparison; this case covers conventional only (case p.2)
7. **The UK has never missed a gilt payment, which is why gilts are the UK's risk-free benchmark** · quote from DMO (case p.2), UK rating in 2014 vs today [src]
8. **The Debt Management Office issues gilts for HM Treasury, mostly at 5, 10 and 30 years** · how issuance works; 50-year gilts since 2005 (case p.2, DMO [src])
9. **The gilt market is large: £[x]bn in 2014, £[y]bn today** · bar chart of gilts in issue [src]
10. **Who owns gilts: the Bank of England (QE), pension funds and insurers, and overseas investors** · holdings breakdown [src]
11. **In May 2014 Bank Rate had been 0.5% for five years and QE held £375bn of gilts** · timeline 2008–2014 [src]
12. **The case: Petr Cech must price nine gilts and measure their rate risk** · the setting (MU Securities, maturities 1–50 years) and the task (case p.1)
13. **The four questions and how we answer them** · Q1–Q4, each with the CFA concept it uses (TVM, YTM, yield curve, duration/convexity)

## 2 · Exhibit analysis
14. Divider · 02 Exhibit analysis
15. **Exhibit 1: nine gilts, each with a price or a yield but never both** · native table, rebuilt (coupon, maturity, price, YTM; blanks shown as "?"), source IMD research
16. **Coupons from 2¾% to 5¼% show these gilts were issued in different rate eras** · coupon vs maturity dot chart; high coupons = pre-2008 issues [src for issue years if names certain]
17. **Prices above 100 already tell us the yield is below the coupon** · the five given prices vs 100 (premium/discount bar), first hint for Q1
18. **The four given yields rise with maturity: 1.74% at 2 years to 4.36% at 30 years** · the given YTMs plotted, curve still has gaps (sets up Q3)
19. **The real gilts behind Exhibit 1** · table: case bond → real gilt name and maturity date, only certain matches (user rule) [src]
20. **What Exhibit 1 means for the analysis: we must solve for four prices and five yields, then stress-test all nine** · roadmap linking the exhibit to Q2–Q4; note the annual-coupon simplification

## 3 · Q1: coupon rate vs YTM
21. Divider · 03 Q1: coupon rate vs yield to maturity
22. **Q1 asks how the coupon rate and the YTM differ and what that does to price** · question stated, broken into 3 parts (define, compare, effect on price)
23. **The coupon rate fixes the cash; the YTM is the return the market wants today** · two definitions side by side, with 20-year 4¾% example
24. **A bond's price is the present value of its cash flows at the YTM** · formula P = Σ C/(1+y)^t + 100/(1+y)^N with each symbol explained (CFA FI LM06)
25. **When the YTM rises, the price falls** · price–yield curve for the 10-year 3¾% gilt (chart), marked at 4.04%
26. **YTM below coupon means a premium, above means a discount, equal means par** · rule with three exhibit examples: 1-year (0.73% < 3.25% → 102.50), 10-year (4.04% > 3.75% → 97.65), par case
27. **Most of our gilts trade at a premium because rates fell after they were issued** · premium/discount for all nine (bar vs 100), linked to the coupon/issue era
28. **A premium or discount shrinks to zero as the bond nears maturity (pull to par)** · price path of a premium and a discount bond over time (chart)
29. **Answer to Q1** · three-line summary

## 4 · Q2: fill in the missing values
30. Divider · 04 Q2: the missing prices and yields
31. **Q2: four prices and five yields are missing** · question, the gaps highlighted on Exhibit 1, the two tasks (price from yield; yield from price)
32. **Assumptions: annual coupons, priced on a coupon date, per £100** · assumption list with reasons (Exhibit 1 simplification; real gilts semi-annual → slide 41)
33. **Price from yield, step 1: list the 5-year gilt's cash flows** · timeline: £2.75 × 4, then £102.75
34. **Step 2: discount each cash flow at 3.00%** · table: year, cash flow, 1/1.03^t, PV (2.67, 2.59, 2.52, 2.44, 88.63)
35. **Step 3: add them up: the 5-year gilt is worth £98.86** · sum, result large; discount because 3.00% > 2.75%
36. **The same method prices the 2-, 10- and 30-year gilts** · formula + plugged-in line + result for each (106.84, 97.65, 102.32) — *display option, see below*
37. **Yield from price, the easy case: the 1-year gilt yields 0.73%** · 102.50 = 103.25/(1+y) → y = 0.73%, solved in three lines
38. **Longer bonds need trial and error: the 3-year gilt yields 2.06%** · table of trial yields (2.00% → 107.21; 2.10% → 106.91; 2.063% → 107.02), with a picture of closing in
39. **The same search gives the 7-, 20- and 50-year yields** · equation + result for each (3.54%, 4.38%, 4.24%) — *display option*
40. **Exhibit 1 completed** · full table, computed cells highlighted (accent + bold, readable in grey)
41. **Paying coupons twice a year, as real gilts do, changes the answers by at most 0.03 in price** · annual vs semi-annual table (user decision: one comparison slide)

## 5 · Q3: the yield curve
42. Divider · 05 Q3: the yield curve
43. **Q3: a yield curve plots yield against maturity for bonds of the same issuer** · definition; why it matters (benchmark for all UK borrowing)
44. **The gilt curve rises steeply to 10 years, flattens, then dips beyond 20 years** · line chart of our nine YTMs, maturity axis in years, labelled points
45. **The slope in numbers: +331bp from 1 to 10 years, +34bp to 20 years, −13bp to 50 years** · step-change bars between maturities
46. **Short yields were low because Bank Rate was 0.5% and markets expected it to rise** · expectations theory + term premium, with 2014 Bank Rate [src]
47. **Long yields were held down by pension funds and insurers buying long gilts** · preferred habitat / segmentation; UK pension demand [src]
48. **Caution: this is a curve of coupon-bond yields, not spot rates** · YTM vs spot curve in plain words (CFA FI LM09)
49. **Answer to Q3** · summary with the chart thumbnail

## 6 · Q4: what if all yields rise by 1%?
50. Divider · 06 Q4: a 1% rise in all yields
51. **Q4: every yield moves up by one percentage point at once** · parallel-shift picture (two curves), what "+1%" means (3.00% → 4.00%)
52. **Repricing the 10-year gilt at 5.04% drops its price from 97.65 to 90.06** · formula, plugged-in line, result (−7.78%)
53. **Every gilt falls, and the 50-year falls 18 times as much as the 1-year** · results table: price before, after, % change for all nine
54. **The longer the maturity, the bigger the fall** · bar chart of % change by maturity
55. **Duration measures how far, on average, a bond's cash comes back** · Macaulay duration concept (weighted average time) with a see-saw picture
56. **Calculating duration for the 5-year gilt: 4.74 years** · step table: t, PV(CF), weight, t × weight → sum
57. **Modified duration turns that into a price sensitivity: 4.60% per 1% of yield** · ModD = MacD/(1+y), %ΔP ≈ −ModD × Δy (CFA FI LM11)
58. **Duration ranks the risk: from 0.99 (1-year) to 20.82 (50-year)** · table of MacD and ModD for all nine
59. **For long bonds duration overstates the fall: −20.82% estimated vs −17.74% actual** · comparison table (estimate vs actual)
60. **Convexity explains the gap: prices fall less than the straight line predicts** · price–yield curve with the duration tangent line (chart)
61. **Adding convexity brings the 50-year estimate to −17.31%** · formula %ΔP ≈ −ModD·Δy + ½·C·(Δy)², plugged in for the 10-year and 50-year (CFA FI LM12)
62. **Longer gilts paid little extra yield for far more risk** · scatter: YTM vs modified duration (yield per unit of risk)
63. **Answer to Q4** · summary: who loses most and why; investor implication

## 7 · Epilogue
64. Divider · 07 Epilogue
65. **What we found** · four findings, one per question
66. **After 2014 gilt yields kept falling, to record lows in 2020** · 10-year gilt yield 2014–2021 [src]
67. **Then inflation returned and Bank Rate rose from 0.1% to 5.25%** · Bank Rate chart 2020–2023 [src]
68. **September 2022: long gilts crashed and the Bank of England had to step in** · mini-budget, 30-year yield jump, BoE intervention date and size [src]
69. **That crash was Q4 in real life: long duration meant huge losses** · e.g. 0.5% 2061 gilt price fall [src]; link to our 50-year result
70. **What happened to our nine gilts** · redeemed ones with dates; the 4% 2060 (if certain) then and now [src]
71. **Where gilts stand today: Bank Rate [x]% and a curve that slopes up again** · today's curve vs our 2014 curve (chart) [src]
72. **Lessons for an investor** · coupon ≠ return; the curve's shape is information; duration is the price of yield

## 8 · Team
73. **Group 10** · members' photos, full names, student IDs (placeholder until the user supplies them)

---

## Instructions checklist
| Requirement (Case Presentation Instructions) | Slides |
|---|---|
| Overview: background, business model, industry, key data, main problem | 4–13 |
| Overview uses reliable external sources | 7–11 |
| Every exhibit inserted (rebuilt), explained, key numbers, meaning, implications | 15–20 |
| Each question stated | 22, 31, 43, 51 |
| Broken into sub-questions | 22, 31, 51 |
| Theories and frameworks applied | 24–28, 43–48, 55–61 |
| Evidence from case and external sources | 46–47, 66–71 |
| Assumptions explained | 32, 41, 48, 51 |
| Alternatives compared | 41 (annual vs semi), 59–61 (duration vs convexity), 62 |
| Calculations shown step by step on the slides | 33–41, 52, 56–61 |
| Epilogue: findings, turning points, outcome, after the case, today | 65–72 |
| Structure intro → exhibits → analysis → epilogue | sections 1–7 |
| Charts, tables, diagrams | 9, 10, 16–18, 25, 27–28, 44–45, 54, 60, 62, 66–67, 71 |
| Final slide with photo, name, ID | 73 |
| Body text ≥ 18pt, no overcrowding, consistent design | gate 2/3 checks |

## Display option for repeated calculations (user to choose)
Slides 36, 39 and 53 repeat a method already shown in full. See the question at the gate.
