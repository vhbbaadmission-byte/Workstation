# UK Gilts: grader report on the gate 1 storyline

Reviewed as the professor would grade the finished deck. I read only the grading brief, the case and its four questions, and `01-storyline.md`.

## Likely grade: B+ as planned (A− to A if the must-fix items are done)
The structure, theory and Q4 depth are strong. The plan is held back by four things. It treats a stylised exhibit as the real 2014 market. It leaves out the YTM assumptions and the closed-form formulas a Level 1 class expects. Convexity is used but never derived. At 73 slides it is light against a brief that explicitly mentions 150–200 slides, with only one fully worked example per method.

---

## Must-fix

1. **Slides 44, 46, 47, 71 (and 11, 16, 27) → Exhibit 1's yields are treated as the real May 2014 gilt market, but they don't look like it.** Check this, but the actual 10-year gilt yield in May 2014 was about 2.6–2.7%, against 4.04% in the exhibit, and the 2-year was under 1%, against 1.74%. Slides 46–47 explain the curve's shape with real 2014 causes (Bank Rate 0.5%, pension demand), and slide 71 compares "our 2014 curve" with today's. If the exhibit is illustrative ("IMD research"), that reasoning doesn't hold, and a demanding grader will notice. **Fix:** add a slide in the exhibit section or Q3 that plots Exhibit 1's curve against the actual BoE/DMO nominal curve on the case date (9 May 2014), with a source line. State plainly whether the exhibit is stylised. Then set up 46–47 as "why a 2014 gilt curve slopes this way", and apply it to both curves where they agree. Label slide 71's comparison correctly.

2. **Q1 (slides 23–29) → The YTM's assumptions and its link to IRR are missing.** A CFA L1 grader expects YTM to be defined as the IRR of the bond's cash flows, valid only if the bond is held to maturity, there is no default, and every coupon is reinvested at the YTM. Without this, "coupon vs YTM" is half answered, and reinvestment risk, which ties into Q4, never appears. **Fix:** add one slide, "YTM is the bond's IRR, and it holds only under three assumptions", with a small reinvestment example. The teaching concepts list NPV/IRR explicitly.

3. **Q1 (slides 23, 26) → No alternatives are compared.** The brief asks for alternatives, and the checklist lists none for Q1. **Fix:** compare the three yield measures side by side for one gilt: coupon rate, current yield (coupon ÷ price) and YTM. Example: 7-year 5% at 108.91 gives coupon 5.00%, current yield 4.59% and YTM 3.54%. This also makes the premium-bond relationship visible: coupon > current yield > YTM.

4. **Slides 26–27 → Q1 uses Q2 results before they are derived.** Slide 26's 10-year price of 97.65 and slide 27's "all nine" premium/discount both rely on the pricing done in slides 33–39. **Fix:** answer Q1 from what Exhibit 1 already gives. The five given prices show premium or discount directly (for example, the 50-year at 94.96 is below 100, so its YTM is above 4%). For the four given yields, compare the YTM with the coupon (for example, 5-year 3.00% > 2.75%, so it trades at a discount) without pricing it. Alternatively, put "computed in Q2, slide 35" on the slide. Slide 26 promises a "par case", but none of the nine gilts trades at par. Say it is a hypothetical example.

5. **Q2 (slides 24, 33–39) → The annuity (closed-form) bond formula is missing.** Summing 30 or 50 discounted terms on a slide is impractical, and "the same method" (slides 36, 39) hides the working. **Fix:** after the 5-year PV table, introduce P = C × [1 − (1+y)^−N] / y + 100 / (1+y)^N. Show that it gives the same 98.86, then plug it in with every number written out for each of the other eight gilts. That satisfies "show every step" without 50-row tables.

6. **Slide 38 (and 39) → The yield-from-price search is not reproducible.** "Trial yields … closing in" doesn't show how 2.063% is reached. **Fix:** show the linear interpolation between the two trial yields as an equation with numbers. Then **verify** every solved yield by repricing it, for example "at 4.24%, the 50-year prices at 94.96 ✓". Do this for 7-, 20- and 50-year as well, not only the 3-year.

7. **Slide 61 (and 58) → Convexity and the nine durations are used but never derived.** The convexity value C for the 10-year and 50-year comes from nowhere, and slide 58's table has only one worked example (slide 56). **Fix:** show convexity with the CFA approximation, C ≈ (P₋ + P₊ − 2P₀) / (P₀ × Δy²), with the numbers plugged in for the 10-year and 50-year (you already have P₊ from slide 53, so add P₋). For slide 58, state the method and show at least the 10-year and 50-year duration workings. Also explain why the 50-year convexity-adjusted estimate (−17.31%) now overshoots the actual fall (−17.74%): the higher-order terms omitted from a two-term approximation at a large Δy.

8. **Display option (slides 36, 39, 53) → Choose the full display, not the compressed one.** The brief says 150–200 slides "if necessary" and the benchmark decks are step by step. A grader comparing this with G1 will see one worked example and three "same method" slides as thin. **Fix:** give one slide per bond for the eight missing values (formula plugged in, result, premium/discount check), and keep the results table as the summary. For Q4, write at least the 1-, 10- and 50-year repricings in full, and give the formula plugged in for the rest. That takes the deck to about 90–100 slides of real content, not padding.

---

## Should-fix

9. **Slide 46 → "Markets expected it to rise" is asserted, not shown.** **Fix:** bootstrap spot rates from the 1-, 2- and 3-year gilts (the annual coupons make this easy). Then compute the implied 1-year forward rates (1y1y, 2y1y) and show that they are above today's 1-year rate. That turns expectations theory into numbers. It also fills out slide 48, which currently says only in words that YTM differs from spot.

10. **Slides 46–47 → Term-structure theories are applied but not compared.** **Fix:** add one slide comparing pure expectations, liquidity preference and market segmentation/preferred habitat. For each, give what it predicts for this curve's shape and whether the evidence supports it. Fold in the case's own fact that the 50-year has low secondary-market liquidity. A liquidity premium should push its yield *up*, yet it is the lowest long yield (4.24%). Explain the tension: pension-fund demand outweighs illiquidity.

11. **Slide 44 → "Dips beyond 20 years" leans on a 2bp gap.** The 20-year (4.38%) and 30-year (4.36%) are effectively flat. **Fix:** say "flat from 20 to 30 years, then 14bp lower at 50". Point out that the curve is built from bonds with different coupons (the coupon effect), so small kinks are not signals.

12. **Q4 (slides 53–63) → There is no money impact or implication for the case's decision-maker.** **Fix:** turn the percentages into money on a holding, for example £10m nominal of each gilt, or a sample MU Securities book: "a 1% rise costs £x on the 50-year vs £y on the 1-year". Add PVBP/money duration (CFA L1) to give a basis-point figure.

13. **Q4 → The only alternative is duration vs convexity.** **Fix:** add a −1% scenario next to +1% to show the asymmetry convexity creates: gains exceed losses. Add one non-parallel case (steepening) as a sentence or a small table to show the limit of the parallel-shift assumption. Compare two gilts of similar maturity and different coupon (for example, the 5-year 2¾% and the 7-year 5%) to show that coupon also drives duration.

14. **Slide 62–63 → "Long vs short: when to hold which" is missing.** This is a listed teaching concept. **Fix:** add a slide saying who should hold long gilts (pension and insurance liability matching, investors expecting rates to fall) and who should hold short (expecting rises, liquidity needs). Back it with the numbers on slide 62.

15. **Overview (slides 4–13) → It covers gilt mechanics but not the issuer's finances or the "competitive environment".** The brief asks for financial information and industry context. **Fix:**
   - Add the UK's 2014 fiscal position (deficit, debt/GDP, the DMO's 2014-15 gross financing remit) against today's.
   - Compare May 2014 10-year sovereign yields: gilts vs US Treasuries vs Bunds vs a periphery market. This covers "sovereign bond spreads", another listed teaching concept.
   - Add a line on the risk-free rate and sovereign risk.

16. **Epilogue (slides 65–72) → It tells market history but never closes the loop on the case's analysis.** **Fix:**
   - Add one slide applying your own duration numbers to a real move. For example, the change in the 30-year yield from early 2022 to the October 2022 peak × your ModD gives a predicted loss, set against the actual price fall of a long gilt.
   - Add the Brexit-vote rating downgrade (2016) and the switch from QE to active QT gilt sales (from November 2022) as turning points.
   - "Where gilts stand today" needs a dated October 2026 figure for Bank Rate and the 10-/30-year yields.

17. **Weak titles that state no point: slides 2, 19, 29, 40, 49, 63, 65, 70, 72.** "Answer to Q1", "What we found", "Lessons for an investor" and "Exhibit 1 completed" are labels, not claims. **Fix:** write each as the claim, for example slide 40: "Five of the nine gilts trade above par; the 7-year is the richest at 108.91". Slide 63: "A 1% rise costs the 50-year 17.7% but the 1-year only 1.0%; maturity is the main driver of the gap, with coupon and yield also playing a part".

18. **Slides 17, 26, 27 → The premium/discount point is made three times.** **Fix:** keep slide 17 as a one-line observation in the exhibit section. Make slide 26 the rule and slide 27 the cause (issue era). Don't restate the same comparison each time.

19. **Slides 16, 19, 27 → They rest on matching the exhibit's bonds to real gilts.** "High coupons = pre-2008 issues" and "rates fell after they were issued" are causal claims. If the exhibit is stylised (see item 1) and only some bonds can be matched with certainty, these slides could end up thin or speculative. **Fix:** decide now. If fewer than about half can be matched, merge 19 into 16 and phrase the issue-era point as reasoning from the coupons, not fact.

20. **Slide 41 → The semi-annual comparison covers only prices.** For the five gilts where the price is given, semi-annual compounding changes the *yield*, not the price. **Fix:** show both columns, Δprice for the four priced gilts and Δyield (in bp) for the five yield-solved gilts. State that the semi-annual yield is quoted as a bond-equivalent annual rate.

21. **Instructions checklist → "Evidence from external sources" maps only to Q3.** **Fix:** give each question at least one external anchor: Q1 the DMO definition of coupon and yield; Q2 an actual DMO closing price for a real gilt next to the model price; Q4 the 2022 episode as a forward reference. Update the checklist rows for "alternatives" and "evidence" so each question has slide numbers.

---

## Nice-to-have

22. **Slides 2 and 13 → The four questions are listed twice.** Keep slide 2 as a short agenda, and keep slide 13 because it maps each question to a concept.
23. **Slide 32 → Pricing on a coupon date means clean = dirty.** Add a line on clean vs dirty price and accrued interest (how gilts actually trade), so the class sees why the assumption matters.
24. **Slide 58 → Label the column as modified duration.** "0.99 to 20.82" are modified durations; the 1-year's Macaulay duration is exactly 1.00. Label both columns so the table doesn't read as inconsistent with slide 56.
25. **Slide 62 → Put the yield-per-risk point in numbers in the title.** For example, "Moving from 10 to 50 years adds 20bp of yield but more than doubles the duration".
26. **Slide 12 → Explain why a trading desk prices these.** Add one line on why MU Securities needs prices, yields and rate sensitivity: mark-to-market, finding rich or cheap bonds, risk limits. This is the "main decision" the overview brief asks for.
27. **Q2 relative value.** Once the curve is complete, flag any gilt that looks rich or cheap against its neighbours (for example, the 20-year yields more than the 30-year). This ties back to the case's goal of finding the "appropriate price".

---

## Strengths
- **Clear structure and flow.** The structure is overview → one exhibit → Q1–Q4 → epilogue, and each question opens with the question stated and broken into parts.
- **Q2 teaches both directions.** It works the 5-year as a full PV table and the 1-year algebraically, then deals with trial and error. That is the right teaching order.
- **Q4 is the strongest section.** It goes from repricing to duration to the limits of duration to convexity. It uses the 50-year's actual-vs-estimate gap to motivate convexity, and it plots yield against risk. This is the depth the brief asks for.
- **The 2022 LDI/mini-budget crisis as "Q4 in real life".** This is an excellent epilogue choice that links the analysis to what happened after the case.
- **The annual-coupon simplification is named and tested** (slides 20, 32, 41), not hidden.
