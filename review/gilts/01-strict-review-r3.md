NOT READY. Grade estimate A− in substance, held back by four small blocking items: one false statement (slide 96), one yield-convention mix (slide 117), four unsourced or wrong external claims (10, 36, 98, 118), and sums on the duration and convexity slides that the reader cannot trace. Each is a short fix, and none needs new analysis.

# UK Gilts: strict review of the gate 1 storyline, round 3

Reviewed: `review/gilts/01-storyline.md` (120 slides). I checked it against the grading brief, the case text (`case-layout.txt`), CLAUDE.md, DESIGN.md, PROGRESS.md (user feedback and decisions), the live output of `python3 work/gilts/calcs.py`, `work/gilts/sources.md` and `work/gilts/sources_research.md`. I also ran my own checks: the closed-form Macaulay duration, approximate convexity at 1bp and 5bp, and the yield conventions for the 4% 2060 gilt. I did not take the "Response to the strict review" on trust; each claim in it was checked against the plan.

## 1. Verdict
**NOT READY. Grade estimate A− once the blocking items below are fixed (B+/A− as it stands).** Three hard requirements fail: H3, H4 and H7/H8 (one blocking item each, plus a fourth). All six quality scores are 4 or above. Round 2's B1–B7 are substantially resolved (section 7). The new failures were introduced by the rewrite or left by it.

## 2. Hard requirements

| # | Result | Evidence |
|---|---|---|
| H1 Structure | PASS | Opening 1–2; overview 3–16; exhibits 17–24; Q1 25–37; Q2 38–56; Q3 57–71; Q4 72–108; epilogue 109–119; team placeholder 120. |
| H2 Every exhibit | PASS | The case has one exhibit (case p.3, "Source: IMD research"). Slide 18 rebuilds it natively, with blanks shown as "?". Slides 19–21 cover what it shows and the key numbers (coupon range 2¾–5¼%, 4 of 5 given prices above 100, given yields 1.74 → 4.36%; all checked against the case). Slide 22 covers what it means (a teaching set about 1 point above the 9 May 2014 DMO yields: 2.803 / 3.393 / 3.365, confirmed in sources.md). Slides 23–24 cover the implication. |
| H3 Every question, all seven elements | **FAIL (narrow)** | All four questions are stated (26, 39, 58, 73), broken into parts, given theory, assumptions (40, 55–56, 65, 73) and alternatives (31, 44, 55–56, 98–105). The calculation traceability is incomplete. The duration slides for the 7-, 10-, 20-, 30- and 50-year gilts (92–96) plug in a total, "Σ(t × PV)" = 666.55 / 830.03 / 1,417.35 / 1,756.98 / 2,060.94, that is never derived; the 2- and 3-year slides (90–91) do the same, though their 2–3 rows would fit easily. The convexity slides (101–102) plug in Σ[t(t+1) × PV] = 8,620.9 and 72,340.5, also with no derivation. These are the headline Q4 numbers, and a reader with a calculator cannot reproduce them. That breaks "formula → numbers plugged in → result" and the user's one-slide-each rule. Secondary gaps: slide 65 gives 2y1y = 2.75% with no formula, and slides 44 and 46 show intermediate values that do not add up at the precision displayed (12.59 + 86.26 = 98.85, not 98.86; 30.36 + 67.30 = 97.66, not 97.65). |
| H4 External sourced facts | **FAIL** | Slide 98: "why the zero-coupon-like 2061 gilt fell so far in 2022 (slide 117)". `sources_research.md` line 206 says the 2022 price of the 0½% 2061 is **NOT FOUND**, and slide 117 is about the 4% 2060, not the 2061. Slide 10: "in 2014 the Bank was one of the biggest buyers". The sources show £375bn bought (complete by 2012) and **holdings** of 26.4%; nothing supports "buyers" in 2014, and QE purchases had stopped by then. Slide 36: "Bank Rate history 2007 → 2014 [src]". sources.md logs Bank Rate only from `05 Feb 09 | 1.00`, so the 2007–08 levels are not logged. Slide 118: today's curve comes from giltsyield.com (sources.md section F, SECONDARY), but the slide tags only "[src: BoE, sources.md]" with no secondary label. Slide 7: "ratings: 2014 vs today, only those verified" does not pin down which ratings. Fitch's 2014 AA+ rests on a search snippet ("snippet only; re-verify", sources.md line 77), so it cannot appear on the slide as written. Everything else checks out: 9, 11, 12, 13, 111, 112 (labelled secondary), 113, 114, 116 and the 117 figures. |
| H5 No teaching note | PASS | No citation, quotation or concept-list tag. Our numbers were derived independently in calcs.py. The "(case teaching point)" tag has been removed. "Teaching set" on slide 22 describes the exhibit, not the note. |
| H6 Titles: points, ≤ 2 lines | PASS (watch length) | Every content title is now a finding; slide 54 and 67 are fixed. Five titles run 110–119 characters (11: 116, 107: 119, 65: 109, 15: 110, 119: 110) and may hit 3 lines at headline size. Trim them at build time (non-blocking item 5). |
| H7 Finance correct at CFA L1 | **FAIL (one statement)** | **Slide 96: "most of its value sits in the final £104 (weight 0.137 × 50 years)" is false.** calcs.py gives the final payment's PV weight as 0.1370, so 13.7% of the value sits there and 86% sits in the coupons. That is exactly why duration (21.70) is far below 50. As written, the slide teaches the reverse of the concept. Everything else is correct: the YTM conditions (28), price as PV (32), the premium/discount rule (34), annual ModD = MacD/(1+y) (88), analytic convexity Σt(t+1)PV/[P(1+y)²] (101), the duration-plus-convexity estimate (103–104), "by construction" made explicit (104), the bootstrap (63–64) and forwards (65). Two imprecisions are non-blocking (items 2 and 3): slide 104's 1%-step "CFA price-based" cross-check, and slide 115's gap attributed only to the coupon effect. |
| H8 Numbers right | **FAIL (one number)** | **Slide 117: "yield 3.36% → 5.74% (+237bp)"** mixes conventions. 3.365% is the DMO's semi-annual yield (2014 reference prices). 5.738% is giltsyield's "Gross yield", which is the annual-effective equivalent: (1 + 5.658%/2)² − 1 = 5.738%. The same row gives the DMO-convention yield as 5.658%. Like for like, the move is **+229bp**, and the duration-only estimate is −22.24 × 2.29% = **−51.0%**, not −52.8%. The conclusion (duration alone overshoots −34.4% by a wide margin) still holds. 34 other numbers match calcs.py or the sources (table in section 4). Formats follow the project rule. |
| H9 User decisions | PASS (with a caveat) | Annual coupons plus one semi-annual comparison (55–56); gilt names only when certain (23); every Q2 value, every +1% repricing (74–82) and every duration (87–96) on its own slide. Caveat: current yield (31), semi-annual (56), −1% (105), PVBP (85) and money (84) are one worked example plus a table. Round 2 asked for exactly this, but it is still a reading of "one slide each". Name it in one line at the gate so the user is not surprised. |
| H10 Known traps | PASS | Annual-coupon simplification stated (24, 40) and tested (55–56); per £100 (5, 15, 40); duration and convexity explain the +1% shift (86–105). |
| H11 Lucidity | PASS (marginal) | A part-way Level 1 reader would stumble on 6 slides, each a one-line fix (B6 below). That is about a handful, against round 2's ~20. The biggest leftover: **Bank Rate is never defined**, although round 2's B6.4 asked for it and the response claims B6 is done. It is used on 10, 36, 66, 68, 113 and 118. |

## 3. Quality scores

| | Score | Reason |
|---|---|---|
| Q1 Depth | 5 | Goes well past the four questions and tests its claims: the reinvestment FV, three yield measures, bootstrapped forwards with a hindsight test (66), the coupon effect, convexity asymmetry, the exhibit against the real 2014 curve, and a real 4% 2060 test of Q4 (117). |
| Q2 Logic and flow | 4 | Clean arc, and concepts now come before use (primer 15, spot/forward 61). Remaining breaks: Q1 slides 27, 30, 31 and 33 use yields (4.38%, 3.54%) that are only derived in Q2 (51–52), with no "derived on slide X" note; slide 69 uses "convexity value" and "the coupon effect" before slides 98 and 100 define them; two cross-references are wrong (24 → "slide 58" should be 55–56; 98 → "slide 117" is a different gilt). |
| Q3 Evidence | 4 | Strong primary sources: ONS, US Treasury, Bundesbank, BoE IUDMNPY, DMO GAR and reference prices, BoE notices. Held back by the four H4 items and a thin source for slide 113's "inflation returned" (no inflation figure is logged). |
| Q4 Lucidity | 4 | Glosses ("Plain:") and a so-what are on nearly every slide. Six slides still leave the reader short (B6). Slides 75–81 say "same layout" without writing their so-what lines; write them into the plan so the builders do not leave them empty. |
| Q5 Calculations | 4 | Q2 is exemplary, with bracket → interpolate → exact → reprice check. The +1% repricing and the duration ratios are complete. Docked for the untraceable Σ totals (92–96, 101–102), the missing 2y1y formula (65), and displayed sums that do not add (44, 46). |
| Q6 Overview and epilogue | 4 | Current to 29 Oct 2026, with Bank Rate, ONS debt, the curve and the 2060 gilt. Well tied back to the case through 115 and 117. Docked for 117's convention mix, 118's unlabelled secondary source, and 115 calling the BoE staff blog "BoE". |

## 4. Number spot-check (calcs.py run 2026-10-30; sources.md)

| Number | Slide | Source | Match |
|---|---|---|---|
| FV factor 30.96 → 147.08 → 247.08; 24.30 → 115.41 → 215.41 | 29 | calcs "STRICT REVIEW ADDITIONS" | yes |
| Realised return 3.66%; 3.15% at 0% | 30 | calcs reinvestment | yes |
| 7-year: 5.00 / 4.59 / 3.54% | 31 | calcs current yield | yes |
| PVs 2.67 / 2.59 / 2.52 / 2.44 / 88.63 → 98.86 | 42–43 | calcs example A | yes |
| 2.75 × 4.5797 + 86.26 = 98.86 | 44 | calcs annuity | yes (but 12.59 + 86.26 shows as 98.85; give 3 dp) |
| 106.84; 97.65; 102.32 | 45–47 | calcs Q2 | yes (slide 46: 30.36 + 67.30 = 97.66 on display) |
| 1 + y = 1.007317 → 0.73% | 48 | calcs example B | yes |
| 107.21 / 104.24 → 2.064% / 2.063% | 49–50 | calcs interpolation | yes |
| 3.550 / 3.541; 4.395 / 4.375; 4.276 / 4.245 | 51–53 | calcs | yes |
| Semi-annual 2.602 + 2.580 + 2.558 + 99.130 = 106.87 | 55 | calcs | yes |
| Max £0.03, 1bp | 56 | calcs semi-annual block | yes |
| +331 / +34 / −2 / −12bp | 60 | calcs Q3 | yes |
| z2 1.77%, z3 2.09% | 63–64 | calcs; my recomputation from the displayed inputs | yes |
| 1y1y 2.81%, 2y1y 2.75% | 65 | calcs | yes (from rounded displayed inputs 1y1y gives 2.82%; show 4 dp) |
| +1% prices 101.49 / 104.82 / 104.06 / 94.44 / 102.70 / 90.06 / 92.45 / 87.31 / 78.11 | 74–82 | calcs Q4 | yes, all nine |
| % changes −0.98 / −1.89 / −2.77 / −4.47 / −5.70 / −7.78 / −11.89 / −14.67 / −17.74 | 74–82 | calcs Q4 | yes, all nine |
| "18 times" (17.74 / 0.98) | 82 | calcs | yes |
| −£1.0m (1y), −£16.8m (50y) on £100m | 84 | calcs £100m block | yes |
| PVBP [95.1580 − 94.7626]/2 = 0.1977 → £0.20m | 85 | calcs; my P(±1bp) = 95.158036 / 94.762630 | yes |
| MacD 5y 4.74 (t × weight sum 4.7377), ModD 4.60 | 87–88 | calcs | yes |
| MacD/ModD 1.00/0.99, 1.95/1.92, 2.88/2.82, 6.12/5.91, 8.50/8.17, 13.51/12.94, 17.17/16.45, 21.70/20.82 | 89–96 | calcs; my closed-form MacD 6.120 / 8.500 / 13.508 / 17.172 / 21.703 | yes, all eight |
| "weight 0.137" (50y final payment) | 96 | calcs t=50 weight 0.1370 | number yes, **statement no** (13.7% is not "most") |
| −9.12 / −7.78 / −7.00% coupon effect | 98 | calcs | yes |
| Convexity 81.56 = 8,620.9/(97.65 × 1.0824) | 101 | calcs; my ApproxCon at 1bp 81.56 | yes (Σ not derived on the slide) |
| Convexity 701.03 = 72,340.5/(94.96 × 1.0867); ratio 8.6 | 102 | calcs; my ApproxCon at 1bp 701.03, at 5bp 701.05 | yes (Σ not derived on the slide) |
| −7.76% (10y), −17.31% (50y) | 103–104 | calcs | yes |
| ApproxCon 711.82 matches −17.74% | 104 | calcs: needs ApproxModDur 21.30 as well | yes, but 21.30 is missing from the plan (with ModD 20.82 the reader gets −17.26%) |
| 4 × 24.5767 + 100/4.9357 = 118.57, +24.86% | 105 | calcs | yes |
| "+3.5 points of yield for 21 times the risk" | 106 | 4.24 − 0.73; 20.82/0.99 | yes |
| 35.6 / 78.6 / 93.2%; 2.9 / 5.6 / 4.4% | 12 | sources 1a–1f (ONS) | yes |
| 2.77 / 2.62 / 1.50%; 5.30 / 4.98 / 3.39%; 127bp / 191bp | 13 | sources 2a–2d, 3b | yes (UK figure dated 27 Oct, US/DE 29 Oct; label the dates) |
| £1,365bn / £2,817bn, same basis | 9 | sources 7a–7c | yes |
| 29 / 27 / 26% | 11 | DMO GAR 2013-14 29.2 / 26.6 / 26.4 | yes |
| 0.12% on 4 Aug 2020, lowest since 1993 | 111 | sources 3a | yes |
| £19.3bn, 28 Sep – 14 Oct 2022 | 114 | sources section E | yes |
| £895bn → £488bn | 116 | APF letter, 17 Sep 2026 | yes |
| 4% 2060: 114.76 → 75.28 = −34.4%; ModD 22.24 → 15.73 | 117 | sources 8a, 8b | yes |
| 4% 2060: 3.36% → 5.74%, +237bp, −52.8% | 117 | sources 8a: DMO-convention 5.658% | **no**: like for like it is +229bp, −51.0% |
| Bank Rate 0.10 → 5.25% (16 Dec 21 – 3 Aug 23); 3.75% today; 0.25% Aug 2016 | 66, 113, 118 | BoE database | yes |

## 5. Blocking items (exact fixes)

**B1. H7, slide 96: false explanation of the 50-year duration.**
Replace "most of its value sits in the final £104 (weight 0.137 × 50 years)" with: "Only 14% of its value sits in the final £104 (weight 0.137); the other 86% is coupons, many paid early, so the average wait is 21.7 years, not 50." Keep the so-what.

**B2. H8, slide 117: one yield convention.**
Use the DMO-convention yield for both dates: 3.365% → 5.658%, **+229bp** (sources 8a, "DMO yield" column). Duration alone: −22.24 × 2.29% = **−51.0%**, against an actual −34.4%. Label 22.24 and 15.73 as **modified** duration, and keep today's figures labelled secondary (giltsyield.com). If the slide keeps 5.74%, say it is the annual-compounding equivalent and convert the 2014 yield the same way: (1 + 3.365%/2)² − 1 = 3.393%, so the move is +235bp.

**B3. H4: external claims not backed by sources.md.**
- **Slide 98:** delete "why the zero-coupon-like 2061 gilt fell so far in 2022 (slide 117)". The 2022 price is NOT FOUND. Replace it with a sourced fact: "Today the 0½% 2061 trades at £23.41 with modified duration 26.75, against 15.73 for the 4% 2060 that matures 21 months earlier: same maturity, lower coupon, more risk" (sources_research line 206 and sources 8a, both secondary: label them).
- **Slide 10:** "in 2014 the Bank was one of the biggest buyers" → "in 2014 the Bank was one of the biggest **holders** (26%, slide 11)". Purchases of the £375bn were already complete.
- **Slide 36:** log the 2007–08 Bank Rate rows (the same BoE database page, e.g. the July 2007 peak) in sources.md with an exact quote, or start the chart at `05 Mar 09 | 0.50` and the rows already logged.
- **Slide 118:** tag the today curve "[src: giltsyield.com, secondary; BoE for the 10-year]". Use the DMO-yield column, consistent with B2.
- **Slide 7:** name the exact ratings on the slide. Allowed: 2014 S&P AAA (PTI, secondary) and Moody's Aa1 (since Feb 2013, Motley Fool, secondary); today Fitch AA− (secondary). Drop Fitch 2014 AA+ unless the Bloomberg page is opened and quoted. It is a snippet only.

**B4. H3/Q5, slides 90–96 and 101–102: make the Σ totals traceable.**
- **Duration, 7- to 50-year (92–96):** show the CFA Level 1 closed-form Macaulay duration with numbers plugged in, explained in words first. MacD = (1+r)/r − [1 + r + N(c − r)] / [c((1+r)^N − 1) + r]. The 50-year: 24.559 − 0.92015/0.32213 = 24.559 − 2.857 = **21.70** (I verified this exactly; it also gives 6.12, 8.50, 13.51 and 17.17). Keep Σ(t × PV)/P as the cross-check.
- **Duration, 2- and 3-year (90–91):** show the 2–3 row t × PV table. It fits.
- **Convexity, 10-year (101):** show the 10-row t(t+1) × PV table (two slides if 18pt needs it), summing to 8,620.9.
- **Convexity, 50-year (102):** derive it from three prices with the CFA L1 price-based formula at a small step, in words first: "price if the yield falls 0.05%, price if it rises 0.05%". ApproxCon = (P₋ + P₊ − 2P₀)/(P₀ × Δy²) = (95.9569 + 93.9798 − 2 × 94.96)/(94.96 × 0.0005²) ≈ **701.05**. Show the prices to 4 dp. This matches the analytic 701.03, needs no 50-row table, and turns slide 104's circular cross-check into a real one.

**B6 (part of H11; required at build, not separately blocking): six slides that would lose a part-way Level 1 reader.**
1. **Slide 10 (first use of Bank Rate):** "Plain: Bank Rate = the interest rate the Bank of England pays banks on their deposits with it; it anchors short-term UK rates" (sources 9d).
2. **Slide 40:** define clean and full price before "clean = full price": clean = the quoted price; full (dirty) = clean + accrued interest.
3. **Slide 29:** say in words what C × [(1+r)^N − 1]/r is ("what 20 equal coupons are worth at year 20 if each one earns r until then") before plugging in. The annuity idea is only introduced on 44.
4. **Slide 69:** either define "convexity value" and "the coupon effect" in one line each, or point forward ("explained on slides 98 and 100").
5. **Slide 65:** gloss "2y1y" ("the 1-year rate starting two years from now") and show its formula (1+z3)³/(1+z2)² − 1 with numbers.
6. **Slide 13:** "fitted par yields" in the source line: add "par yield = the coupon at which a bond would price at exactly 100", or drop the term from the body.

## 6. Non-blocking improvements (most valuable first)
1. **Q1 forward references (27, 30, 31, 33):** add "(derived on slide 51/52)" wherever a Q2 result is used early, or use given values only, as slide 34 already does.
2. **Slide 104:** if the 1%-step cross-check stays, state ApproxModDur 21.30 next to ApproxCon 711.82, so the reader can reproduce −17.74%. With 20.82 they get −17.26%. Note that CFA uses a small step (B4 makes the point).
3. **Slide 115:** the BoE staff blog's "~20% per 100bp for a 20-year gilt" against our −11.89%. The coupon effect explains most of the gap: a 20-year zero at 4.38% falls about 17.4%. The rest comes from the lower starting yields of 2022 (lower yield, longer duration). Say both. Credit "Bank Underground (BoE staff blog)", not "BoE".
4. **Slides 44 and 46 (and 29, 65):** show intermediate values to 3–4 dp so the displayed numbers add up on paper (12.594 + 86.261 = 98.855 → 98.86).
5. **Titles 11, 107, 65, 15, 119:** trim to about 100 characters to stay within 2 lines. "Duration is the price of extra yield" (119) is unclear; try "extra yield comes with much more rate risk".
6. **Slide 73:** add the second Q4 assumption: the shift is instantaneous (no time passes, so no pull to par).
7. **Slides 75–81:** write each so-what into the plan (e.g. 80: "the 20-year loses about 12 times what the 1-year loses").
8. **Slides 13 / 22 / 111:** the 10-year May 2014 yield appears as 2.77% (BoE par yield) and 2.80% (DMO, 2¾% 2024). Footnote that they are two measures, or a careful reader will think one is a typo.
9. **Slide 113:** "inflation returned" has no logged figure. Add a BoE/ONS CPI datum with a quote, or reword to "Bank Rate rose to bring inflation down" with a BoE MPC quote.
10. **Fix cross-references:** 24 → "tested on slides 55–56"; 98 → the new sourced 2061 fact (B3).

## 7. Round 2 blocking items: resolution check

| Item | Status | Evidence |
|---|---|---|
| B1 Q4 repeats | Resolved, with a gap | +1% for all nine (74–82), duration for all nine (87–96), convexity split (101–102), worked −1% (105) and PVBP (85). The Σ totals are not traceable: new B4. |
| B2 one convexity measure | Resolved | Analytic 701.03 is used throughout, and "by construction" is explicit (104). The cross-check still omits 21.30 (non-blocking item 2). |
| B3 missing worked methods | Resolved | FV formula (29–30); semi-annual worked example (55); bootstrap split (62–65). Only the 2y1y formula is missing (B6.5). |
| B4 unsourced facts | Mostly resolved | 7, 11, 12, 13, 111, 112 (secondary), 116 are now backed. New or remaining: 98, 10, 36, 118, and 7's 2014 Fitch rating (new B3). |
| B5 slide 113 date | Resolved | "From December 2021", matching BoE `16 Dec 21 \| 0.25`. |
| B6 lucidity | Mostly resolved | About 20 gaps are down to 6. Bank Rate (round-2 B6.4) is still undefined despite the response's claim. |
| B7 titles | Resolved | 54 and 67 are points; long titles are shortened, five still border on 3 lines. |
