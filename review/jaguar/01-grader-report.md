# Grader report: Jaguar storyline (gate 1)

Judged against the Case Presentation Instructions, the case text, and the four assigned questions. This covers content only, not formatting or exact numbers.

## Grade estimate: B+ as planned. A is within reach.

The structure is right. All six exhibits are covered, and Q2 (the call option) and Q3 (the choice of baseline) are well above a typical class answer. Four things hold it below an A:
- Q3 leaves out taxes and sizes the new debt inconsistently.
- Q1 asserts its credit-spread story instead of testing it against the market.
- Two slides cite a teaching note.
- A few titles claim things the exhibit numbers don't support.

---

## Must-fix

1. **Slides 71 and 81 cite the "teaching benchmark" / "teaching note's view".** Students aren't supposed to have a teaching note, and a professor who sees it cited will mark the deck down at once.
   - **Fix:** reframe both as the *naive hold-to-maturity valuation*. For example, slide 71 becomes "Valuing the notes as if they ran to 2021 overstates their worth by about 13 points". Keep the argument and drop any reference to where the benchmark came from.

2. **Q3 has no taxes (slides 75–84).** The textbook refunding analysis uses after-tax cash flows: interest and the call/tender premium are tax-deductible, and you discount at the after-tax cost of new debt. A finance professor will expect at least the after-tax version.
   - **Fix:** state the UK corporation tax rate for 2015 [src]. Show pre-tax and after-tax incremental cash flows and NPV side by side, and add one line on how the premium is treated for tax.

3. **The size of the new debt doesn't match Q3's own assumption (slides 75, 76, 90).** Slide 75 says the buyback is "funded with new 3.5% debt", but slide 76 charges 3.5% on US$410m. Buying at 112.35 plus accrued interest costs about US$472m, so the new debt that funds it is about US$472m, not US$410m.
   - Slide 90 has a related error: "US$90m of extra cash" is 500 − 410 face value. It ignores the premium and accrued interest, so the real surplus is about US$28m before fees.
   - **Fix:** take the size of the new debt from the actual cash outlay (price + accrued + fees). Show the 3.5% interest on that amount, and correct slide 90.

4. **Q1 asserts the credit-spread story instead of testing it (slides 51–54).** "Two thirds came from JLR's credit spread" lumps together three effects:
   - market-wide changes in high-yield spreads
   - JLR's own credit improvement
   - the tenor and call effects (10-year non-call-5 vs 5-year)

   **Fix:**
   - (a) Add a benchmark: the BB / high-yield index spread in May 2011 vs March 2015 [src, e.g. ICE BofA BB OAS on FRED]. Then split the spread change into a market-wide part and a JLR-specific part.
   - (b) Use Exhibit 1 itself. JLR's coupons from each issue (8.125% 2011, 8.25% 2012, 5.625% / 4.125% / 4.25% / 5.0% 2013–14, 3.5% / 3.875% 2015) make a ready-made chart of the spread falling issue by issue, plotted against the matching Treasury.
   - (c) Use the 2021 notes' own yield in 2015. The same issuer and the same bond now yield 2.28% to the call (5.94% to maturity), against 8.125% at issue. That is direct evidence for the credit case.
   - (d) Add the **call feature** as a Q1 factor. The 2011 notes were callable, so investors were paid for the option they sold, and that sits inside the 8.125%. Check [src] whether the 3.5% 2020 notes carry only a make-whole call. If so, part of the coupon gap is option value, not credit.

   Slide 55 (tenor) is then a clean third leg instead of overlapping slide 51.

5. **Slide 39's title is not supported by Exhibit 5.**
   - Free cash flow (CFO − PPE − intangibles) is about £1,090m, £580m and £1,066m for FY2012–14, and about £540m for 9M FY2015. It is positive every year.
   - "Turning negative" is Moody's *forecast*, not what the exhibit shows.
   - **Fix:** retitle along the lines of "Free cash flow stayed positive but thin; Moody's expects it to turn negative as capex rises to £3.6–3.8bn". Also show FCF after cash interest (£97–269m) and dividends (£150m).

6. **Slide 35's interest cover is misleading.** P&L finance expense (net £13–185m) is after capitalised borrowing costs. Exhibit 5 shows cash "finance expenses and fees paid" of £128–269m.
   - **Fix:** calculate cover on cash interest (EBITDA ÷ cash finance paid), or show both and explain the gap. Otherwise the title "interest is tiny" overstates the point.

7. **The "wait and call in May 2016" alternative isn't modelled properly (slide 82).** This is the real alternative to tendering now. JLR could pay 112.35 today or, 14 months later, pay the call price (104.06 [src]) plus coupons. But the "call 2016" baseline stops in 2016, while the new notes run to 2020 and the old ones would have run to 2021.
   - **Fix:** state what JLR does after the call: it refinances in May 2016 at an assumed rate, either today's forward rate or a stated scenario. Line up the horizons, including the 2020–2021 gap between the new and old maturities, explicitly on the slide. Then argue the timing choice on one slide in Q4:
     - locking in rates ahead of the expected Fed rise (the Fed did raise rates in December 2015 [src])
     - against paying about 8 points early.

---

## Should-fix

8. **The market benchmark is stale (slides 26, 67, 83).** The 111.28 last traded on 4 February 2015, a month before the 3 March announcement.
   - Say this on slide 26.
   - On slide 83, state the price date and that the comparison of −US$4m mixes dates. This is the comparison that carries the "roughly break-even" conclusion, so it needs the caveat most.

9. **Separate the call option's value explicitly (slides 63–66).** CFA Level 1: callable bond value = straight bond value − value of the call.
   - Show 125.43 (straight, to 2021) − about 109–113 (to the call) ≈ the value of the issuer's call.
   - Add the negative-convexity idea, that prices of callable bonds get squeezed near the call price.

   This is the theory that explains why the market price is 111 and not 125.

10. **Slide 58 leaves out an option.** The case says holders could also **roll their notes into the new issue**. Add it, and compare it with selling in the market, holding (and being called in 2016) and tendering early or late.

11. **Q3's assumptions don't say why 112.35 is "the price worked out in Q2" (slide 75).** Slide 72 answers Q2 with a range (111–112). Say why Q3 uses the actual tender price, and point to the sensitivity on slide 84 for the low end of the range.

12. **The discount-rate choices need a reason on the slides (slides 62, 66, 81–84).**
   - Slide 62 applies a 5-year new-issue rate (3.5%) to a 6-year bond. Slide 66's range starts at 0.5%.
   - Explain each choice on the slide: the issuer's cost of debt vs the holder's required yield, pre-tax vs after-tax, and which maturity each rate is for.

13. **Q4: equity-holders = Tata Motors (slide 96).** JLR is wholly owned, so "equity-holders" means Tata Motors and, through it, Tata Motors' listed shareholders. Name them.
   - Add the MM-with-taxes point: a lower coupon cuts the interest tax shield slightly.
   - In Q4 itself, compare holders who tendered with holders who stayed in and were called in 2016. This is currently only in the epilogue (slide 101).

14. **Slide 91 frames a cost as a benefit.** Moving the maturity *forward* from 2021 to 2020 increases refinancing risk.
   - **Fix:** retitle it as a trade-off. The epilogue proves the point: the 3.5% notes fell due in March 2020, just as COVID hit and JLR's credit was at its weakest [src].

15. **The epilogue doesn't close the loop on the deal (slides 100–107).** Add one hindsight slide: what it cost JLR to refinance the 3.5% 2020 notes in 2019–20, against the 3.5% locked in in 2015, with the coupons and ratings at the time [src]. That ties the "turning points" requirement to the decision in the case.
   - "Where JLR stands today" (slide 107) should cover ownership after Tata Motors' demerger (2025) [src].

16. **The opening is repetitive (slides 2, 17, 18).** Three slides set up the question and the plan.
   - **Fix:** merge slide 2 into slides 17–18, or cut slide 18 to a short roadmap. Slide 4 ("JLR today") and slide 107 also overlap. Keep the detailed "today" view for the epilogue and give slide 4 a short hook.

17. **Slide 14's framing conflicts with the deck's own thesis.** "A good time to borrow: low Treasury yields" goes against slides 30–31 and 52, which say Treasuries explain little. Reframe it as strong demand for high-yield bonds and tight spreads, with Treasury yields low at the long end only.

18. **Slide 7 sources.** Exhibit 4 covers only FY2012–FY2015, so the FY2009–FY2011 points need external sources [src]. Also avoid showing Exhibit 4 data in the overview before the exhibit is analysed, so it isn't repeated on slide 33.

19. **The industry slide is thin (slide 9).** "Industry and competitive environment" needs more than a competitor league table.
   - Add 2015 industry drivers [src]: growth in China, the premium SUV boom, emissions and diesel regulation, and how much the industry needs to invest.
   - These set up the epilogue's China and diesel turning point.

20. **Some titles state no point.** The table slides 20, 25, 29, 32, 37 and 41 ("Exhibit N: …") and the answer slides 56, 72, 85 and 97 ("Answer to Qn") only label the slide. Put the finding in the title, for example:
   - "Q2 answer: holders would accept about 111–112 clean, plus accrued interest"
   - "Exhibit 1: £2.4bn drawn, mostly fixed-rate notes, with £1.5bn of the facilities undrawn".

21. **Exhibit analysis that is missing.**
   - **Exhibit 4:** capitalised development costs (£751–1,030m) inflate profit, a quality-of-earnings point. The tax rate jumps from 1% (FY2012) to 27%.
   - **Exhibit 3:** the 1-year / 14-month point. The tender's reference Treasury was the 0.25% note due May 2016, so this is the rate that matters for Q2, and slide 30 should show it.
   - **Exhibit 1:** the implied US$/£ rate (410/263 ≈ 1.56 at 31 December 2014) against the 1.50 used, as a reason for the FX assumption.
   - **Exhibit 2:** the 8.25% sterling notes at 110.94, which tie to the February sterling refinancing (slide 15).

22. **Thin "Implication" slides (24, 31, 36, 40).** As one-liners they will read as slides that say little. Either fold each into its analysis slide as a closing "so what" box, or give each a number that links it to the decision. For example, slide 24: "the 8.125% and 8.25% notes cost £[x]m a year in interest above what the 2015 coupons would cost".

## Nice-to-have

23. **Depth against the brief.** 109 slides is acceptable, but the brief says 150–200 and the benchmark deck is 268. Most of the gap should come from real analysis, not padding:
   - must-fix items 2, 4 and 7
   - a full discounting table for Method A (slide 62)
   - per-year ratio derivations (slides 43–44)
   - a Q1 chart of the spread on each issue.
24. **Q1 corroboration.** The February 2015 sterling refinancing (3.875% 2023 replacing 8.25% 2020) shows the same pattern in a second currency.
25. **Q1 / Q4 credit context.** Add the full rating path from 2011 to 2015 (B1 → Ba3 → Ba2, with outlooks) [src], not just the 2013 upgrade.
26. **Q4 alternatives.** One slide on what else JLR could have done: do nothing, wait and call, buy notes in the open market, or use cash on hand (net cash of about £1.6bn), each with its trade-off.
27. **Assumptions slides for Q1 and Q4.** Q1 assumes the 2011 notes were issued at par and uses tenor-matched Treasuries. The checklist cites assumptions only for Q2 and Q3.
28. **Tender mechanics.** Check [src] whether the tender came with a consent solicitation (to strip covenants), which is common in US high-yield tenders. If it did, it belongs on slides 16 and 89.

---

## Strongest parts
- Q2 treats the call option correctly and reconciles four valuations (109.11 / 111.28 / 112.35 / 125.43) on one chart. That is the analytical centre of the deck.
- Q3 shows that the NPV depends on the baseline (hold to 2021, call in 2016, market price). This tests the "free lunch" claim instead of asserting it.
- Every exhibit has a native rebuild, key numbers and an implication, plus a synthesis slide (45) that links the exhibits to the questions.
- The epilogue is well researched and runs from the outcome of the tender to the 2025 cyber-attack.
- Clean clean-vs-dirty and accrued-interest handling (slides 59–60, 69).
