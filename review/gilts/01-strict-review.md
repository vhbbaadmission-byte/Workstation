NOT READY. Grade estimate: B+ as planned. The finance and Q2 are strong, but repeated calculations are compressed against the user's rule, several external facts have no source, and too many slides would lose a basic-level reader.

# UK Gilts: strict review of the gate 1 storyline

Reviewed: `review/gilts/01-storyline.md` (97 slides), checked against the grading brief, the case text, CLAUDE.md, DESIGN.md, PROGRESS.md, the output of `python3 work/gilts/calcs.py`, `work/gilts/sources_research.md` and the earlier grader report. The authors' "Response to the grader" was checked item by item, not taken on trust.

## 1. Verdict
**NOT READY. Grade estimate B+.** Five hard requirements fail: H3, H4, H6, H9 and H11. Two quality scores are below 4: Q4 lucidity (2) and Q5 calculations (3). Q3 evidence also scores 3.

## 2. Hard requirements

| # | Result | Evidence |
|---|---|---|
| H1 Structure | PASS | Opening 1–2, overview 3–15, exhibits 16–23, Q1 24–35, Q2 36–53, Q3 54–63, Q4 64–85, epilogue 86–96, team placeholder 97. |
| H2 Every exhibit | PASS | The case has one exhibit (Exhibit 1, "Source: IMD research"). Slide 17 rebuilds it natively. Slides 18–20 cover what it shows and the key numbers, slide 21 what it means (a teaching set about 1 point above the real 9 May 2014 market, checked against the DMO xls: 2.803 / 3.393 / 3.365), and slide 23 the implication. |
| H3 Every question, all seven elements | **FAIL** | Q1: the reinvestment slide (28) gives only results (247.08, 215.41, 195.00); the future value of reinvested coupons is never shown. Q2: the semi-annual comparison (53) is a results table with no worked semi-annual price or yield, so the method is never shown. Q3: the bootstrap and two forward rates are crammed onto one slide (58). Q4: the +1% repricing is worked for only 3 of 9 gilts (66–68); duration for 2 of 9 (72, 74); convexity for 2 gilts on one slide (79); PVBP, the £ loss (70) and the −1% case (82) are tables only. Slide 81's −17.31% cannot be reproduced from the slides: it needs convexity 701.03, but slide 79 shows 711.82, which gives −17.26%. |
| H4 External sourced facts | **FAIL** | Slide 11 still holds placeholders "[x]% to [y]%", and the sources files have no debt/GDP or deficit data. Slide 12 (US Treasury and Bund yields, May 2014 and today): no source anywhere. Slide 88 ("record lows in 2020"): no source. Slide 89 ("the UK's rating downgrade"): the sources hold only a Moody's outlook change (not a downgrade) and an aggregator row they themselves flag as "ambiguous"; there is no primary S&P June 2016 downgrade. Slide 7 (ratings today): S&P and Moody's are "not directly sourced" (sources line 249). Slide 93 (QT start): only the 2026 APF letter, with no QT start date or first sale. Slide 90's title "From 2022 … Bank Rate rose from 0.1%" is contradicted by its own source: the first rise was 16 Dec 2021. Also, `work/gilts/sources.md` (required by CLAUDE.md) does not exist; only the helper's `sources_research.md` does. |
| H5 No teaching note | PASS (with a warning) | Nothing is quoted or cited. But slide 84's tag "(case teaching point)" refers to the teaching note's concept list, not the case; it must never reach a slide. Remove it from the plan. |
| H6 Titles state the point, ≤ 2 lines | **FAIL** | Slide 52 "Exhibit 1 completed" is still a label. The earlier grader flagged it (item 17), and the response claims "all titles are now points", which is false. Slide 59 "Three theories explain a curve's shape" is a label. Slide 11's title has placeholders. Slides 10, 84 and 92 have titles of about 115–145 characters, which will not fit in 2 lines at title size. |
| H7 Finance correct at CFA L1 | PASS (with corrections needed) | No outright conceptual error. Points to correct: slide 81 calls −17.74% from ApproxModDur/ApproxCon "exact", but it is exact by construction (built from the same P₊ and P₋), so it is not a validation. Slide 92 "our +1% scenario exactly" overclaims: the 2022 move was not a parallel shift. Slide 61 gives one cause (pension demand) for the long-end dip and leaves out convexity value and the coupon effect. Slide 60 reads the exhibit's forwards as market expectations, but slide 21 has just said the exhibit is not the real market. Slide 70 "£1m holding" is £1m face value (the 50-year holding is worth £949,600). |
| H8 Numbers right | PASS (two blemishes) | 31 numbers checked (table below). All match calcs.py or the sources within rounding. Blemishes: slide 56 says "falls 14bp at 50", but calcs gives 20y→50y −13bp (4.375 → 4.244), so the 14 comes only from adding rounded steps. Slide 70 shows money to the pound (£168,478), against the project rule of £m to 1 dp. |
| H9 User decisions honoured | **FAIL** | PROGRESS.md (2026-10-29): "Repeats = One slide each → every repeated calculation gets its own slide (formula → numbers → result)". Q2 complies (41–51). Q4 does not: the +1% repricing for 2, 3, 5, 7, 20 and 30 years, the Macaulay/modified duration for 1, 2, 3, 7, 20, 30 and 50 years, and the convexity for every gilt except the 10- and 50-year exist only as table rows (69, 75, 77). The 10- and 50-year convexity share one slide (79). Bootstrap z2, z3 and the forwards share slide 58. The response lists "8 (decided by user)" under "Not done", which hides this. Other decisions are honoured: annual coupons plus one semi-annual comparison (38, 53), and gilt names only when certain (22). |
| H10 Known traps | PASS | Annual-coupon simplification flagged (23, 38, 53); per £100 (5, 38); duration and convexity explain +1% (71–82). |
| H11 Lucidity | **FAIL** | About 20 slides would lose a basic-level reader with no presenter. List in section 5, item B6. |

## 3. Quality scores

| | Score | Reason |
|---|---|---|
| Q1 Depth | 4 | Goes well beyond the questions: reinvestment risk, three yield measures, bootstrapped forwards, the coupon effect, convexity asymmetry, and the exhibit against the real 2014 curve. Some claims are still asserted rather than tested (61, 60). |
| Q2 Logic and flow | 4 | Clear overview → exhibit → Q1–Q4 → epilogue arc. Concept order breaks in places: spot rates are used on 58 but explained on 62, and YTM, premium and the yield curve are used in the exhibit section (19–20) before Q1 defines them. |
| Q3 Evidence | 3 | Excellent use of DMO 9 May 2014 prices (21, 94) and the BoE LDI blog (92). But five overview/epilogue slides rest on facts that have no source (7, 11, 12, 88, 89), and the 3bp real long-end dip is too thin to support slide 61's causal claim. |
| Q4 Lucidity | 2 | Many slides introduce jargon (QE, IRR, bootstrap, spot/forward, 1y1y, interpolation, bond-equivalent yield, PVBP, ApproxCon, LDI, QT, bp) with no plain-words definition, or before the concept slide. |
| Q5 Calculations | 3 | Q2 is exemplary (cash flows → PV table → annuity form → bracket → interpolate → reprice check). Q4, Q3's bootstrap, the semi-annual comparison and the reinvestment example skip steps, and slide 81 is not traceable. |
| Q6 Overview and epilogue | 4 | Current to October 2026 (Bank Rate 3.75%, the 4% 2060 at about 75, today's curve), with a real tie-back (92, 94). Held back by unsourced or placeholder slides (11, 12, 88, 89) and slide 90's date error. |

## 4. Number spot-check

| Number | Slide | Source | Match |
|---|---|---|---|
| PVs 2.67 / 2.59 / 2.52 / 2.44 / 88.63 | 40 | calcs worked example A | yes |
| 98.86 | 41 | calcs Q2 | yes |
| 2.75 × 4.5797 + 86.26 | 42 | calcs annuity form | yes |
| 106.84 | 43 | calcs | yes |
| 97.65 | 44 | calcs | yes |
| 102.32 | 45 | calcs | yes |
| 0.73% | 46 | calcs example B | yes |
| 107.21 / 104.24 → 2.064% / exact 2.063% | 47–48 | calcs interpolation | yes |
| 112.46 / 106.00 → 3.550% / 3.541% | 49 | calcs | yes |
| 110.19 / 96.88 → 4.395% / 4.375% | 50 | calcs | yes |
| 100.00 / 81.74 → 4.276% / 4.245% | 51 | calcs | yes |
| Max 0.03 price, 1bp yield (semi-annual) | 53 | calcs semi-annual block | yes |
| +331 / +34 / −2 / −12bp | 57 | calcs Q3 | yes |
| "falls 14bp at 50" | 56 | calcs: 20y→50y −13bp | **no** (rounding; make it 13 or say "from 4.38% to 4.24%") |
| z2 1.77%, z3 2.09%, 1y1y 2.81%, 2y1y 2.75% | 58 | calcs bootstrap | yes |
| 247.08 / 215.41 / 195.00; 3.66% / 3.15% | 28 | calcs reinvestment | yes |
| 5.00% / 4.59% / 3.54% (7-year) | 29 | calcs current yield | yes |
| 101.49, −0.98% | 66 | calcs Q4 | yes |
| 90.06, −7.78% | 67 | calcs Q4 | yes |
| 78.11, −17.74% | 68 | calcs Q4 | yes |
| 18 times (17.74 / 0.98) | 69 | calcs | yes |
| −£168,478 / −£10,076 | 70 | calcs money block | yes (format breaks the £m rule) |
| MacD 4.74, ModD 4.60 | 72–73 | calcs | yes |
| MacD 8.50, ModD 8.17 | 74 | calcs | yes |
| −9.12% / −7.78% / −7.00% | 76 | calcs coupon effect | yes |
| ApproxCon 81.65 / 711.82 | 79 | calcs | yes |
| −7.76% | 80 | calcs | yes |
| −17.31% | 81 | calcs (Conv 701.03) vs slide 79 (711.82 → −17.26%) | **no** (not traceable on the slides) |
| +24.86% vs −17.74% | 82 | calcs ±1% | yes |
| 2.80% / 3.39% / 3.36% real yields, 9 May 2014 | 21 | DMO xls 2.803 / 3.393 / 3.365 | yes |
| 114.76 → about 75 (4% 2060) | 94 | DMO xls; giltsyield £75.28 (secondary) | yes |
| £1,365bn / £2,817bn | 9 | DMO GAR 2013-14 Table C1; GAR 2025-26 Table 20 (calc) | yes (check both are on the same uplifted-nominal basis) |
| 29% / 27% / 26% holders | 10 | GAR 2013-14: 29.2 / 26.6 / 26.4 | yes (the 26.4% is dated "end-2014" in the source; footnote it) |
| £375bn QE; 0.50% since 5 Mar 2009 | 13 | GAR 2013-14; BoE database | yes |
| Bank Rate 0.1% → 5.25%, "from 2022" | 90 | BoE: first rise 16 Dec 2021 | **no** (the date is wrong) |
| Bank Rate 3.75% | 95 | BoE database, Sept 2026 MPS | yes |
| −11.89% (20-year) | 92 | calcs | yes |

## 5. Blocking items (exact fixes)

**B1. H9/H3: Q4 repeated calculations (slides 66–81).**
- Give each remaining gilt its own +1% repricing slide: 2, 3, 5, 7, 20 and 30 years (6 slides). Each shows the annuity formula with the new yield plugged in → new price → % change → a one-line so-what.
- Give the 50-year its own Macaulay/modified duration slide: it is the headline 20.82.
- For the other duration gilts, either add one slide each (the user's rule) or bring a compact alternative to the user as a multiple-choice question. Do not decide alone.
- Split slide 79 into a 10-year convexity slide and a 50-year convexity slide.
- Add one worked −1% repricing (the 50-year: 94.96 → 118.57, +24.86%) before the table on 82.
- Add one worked PVBP and money-loss example before the table on 70.

**B2. H3/Q5: traceability (slides 80–81).** Use one convexity measure throughout. Either derive the analytic convexity (701.03) on a slide and use it on 80–81, or plug slide 79's 711.82 into slide 81 (giving −17.26%) and re-word the title. Re-word "give −17.74% exactly" as "match by construction, because they are built from the same two prices".

**B3. H3: missing worked methods (slides 28, 53, 58).**
- Slide 28: show the future value of the reinvested coupons, FV = C × [(1+r)^N − 1]/r + 100 (4.75 × 24.30 + 100 at 2%, and so on), then the realised return formula with numbers.
- Slide 53: add one worked semi-annual example, e.g. the 2-year at 1.74%: the semi-annual cash flows of 2.625 discounted at 0.87% per half-year = 106.87, against 106.84 annual. State that the yield is quoted as an annual rate compounded twice a year.
- Slide 58: split into three slides (z2; z3; the two forwards), each formula → numbers → result.

**B4. H4: unsourced facts (slides 7, 11, 12, 88, 89, 93).** Fetch and log, with URL, date and exact quote, in `work/gilts/sources.md` (create it, as CLAUDE.md requires):
- slide 11: ONS/OBR public sector net debt and deficit, 2007, 2014 and latest, and replace "[x]%/[y]%" with the numbers
- slide 12: 10-year UST and Bund yields on or near 9 May 2014 and today
- slide 88: the 2020 record-low gilt yield (BoE or DMO)
- slide 89: the S&P downgrade of 27 June 2016 from S&P or a primary report
- slide 7: S&P and Moody's current ratings from their own releases
- slide 93: the BoE notice of the first QT gilt sale (1 Nov 2022)

Any fact still unsourced comes off the slide.

**B5. H4/H8: slide 90.** Re-title it: "From December 2021, inflation returned and Bank Rate rose from 0.10% to 5.25% by August 2023" (BoE database: 16 Dec 21 0.25 … 03 Aug 23 5.25).

**B6. H11: lucidity. Slides that would lose a basic-level reader, and what to add.**
1. **Slide 7:** define "risk-free rate" (the return with no chance of default) and what AAA/AA ratings mean, in one line each.
2. **Slide 10:** the Bank of England "owning" gilts appears before QE is explained (13). Add a one-line plain gloss of QE here, or swap 10 and 13.
3. **Slide 12:** define "Bunds", "Treasuries" and "sovereign spread" (the extra yield one government pays over another).
4. **Slide 13:** define Bank Rate (the BoE's policy rate) and QE (the central bank creating money to buy gilts and push yields down).
5. **Slides 17–20:** the exhibit section uses price per £100, coupon, YTM, premium/discount and "yields rise with maturity" before Q1 defines them. Add a one-slide "five words you need" primer before slide 17 (face value, coupon, price per £100, YTM in one line, par/premium/discount), or a plain gloss on 17.
6. **Slide 27:** define IRR in plain words (the single discount rate at which the PV of the cash flows equals the price).
7. **Slide 28:** define "realised return", and end with the so-what: if rates fall, a holder earns less than the YTM promised.
8. **Slide 29:** define current yield (the annual coupon ÷ price; it ignores the gain or loss at maturity).
9. **Slide 42:** define "annuity" (equal payments every year) before the formula.
10. **Slides 47–48:** explain "bracket" and "interpolate" in words: try two yields whose prices sit either side of the target, then estimate in proportion.
11. **Slide 53:** semi-annual compounding and the quoted-yield convention need a plain sentence.
12. **Slide 57:** "bp" is used from slide 53 on, but never defined. Define it at first use: 1bp = 0.01 percentage point.
13. **Slide 58:** spot rate, forward rate, "z1/z2", "1y1y", "2y1y" and "bootstrap" are all undefined, and the spot-vs-YTM slide (62) comes after. Move the concept from 62 before 58 and define each term in words.
14. **Slides 59–60:** define "term premium" and "preferred habitat" in plain words. Turn 59's title into a point.
15. **Slide 65:** define "parallel shift".
16. **Slide 70:** define PVBP in words (£ change in value for a 0.01% change in yield). Label the units: per £1m (or £100m) face.
17. **Slide 79:** replace "ApproxCon, P₋, P₊" with words first (price if yield falls 1%, price if it rises 1%), then the symbols.
18. **Slide 81:** "higher-order effects" means nothing to the target reader. Say: "the curve bends more than a two-term estimate can capture when the move is as big as 1%".
19. **Slide 91:** define LDI funds and margin (collateral) calls in plain words; nothing in the plan does.
20. **Slide 93:** define QT (the BoE selling or not replacing its gilts, the reverse of QE).

Also: every calculation slide in 66–82 needs an explicit closing so-what line. The plan states one only for some.

**B7. H6: titles.**
- Slide 52 → "Completed, Exhibit 1 shows six premium gilts and three discount gilts; yields run from 0.73% to 4.38%". Count from calcs: premium are the 1, 2, 3, 7, 20 and 30-year; discount are the 5, 10 and 50-year.
- Slide 59 → a point, e.g. "Three theories explain why this curve rises, and each predicts a different shape".
- Shorten 10, 84 and 92 to 2 lines and move the detail into the body.

## 6. Non-blocking improvements (most valuable first)
1. **Slide 94: close the loop with your own tools.** The 4% 2060 yield went from 3.365% (May 2014) to 5.737% (today), +237bp. Duration alone (ModD 22.24) predicts about −53%; the actual move, 114.76 → 75.28, is −34%. That is convexity, plus 12 fewer years to maturity, on a real bond. This is the strongest possible epilogue slide.
2. **Slide 70:** use £100m face so money follows the £m-to-1-dp rule (50-year −£16.8m, 1-year −£1.0m) and makes the contrast obvious.
3. **Slide 61:** add the competing explanations for a falling long end (the value of convexity, the coupon effect) and present pension demand as the most likely one, not the only one. Say plainly that the real dip on 9 May 2014 was only 3bp (3.39% → 3.37%) on a 46-year bond, so the evidence is suggestive, not proof.
4. **Slide 21:** "the shape matches" is overstated. The real curve rose from 20 to 30 years (3.32% → 3.39%), while the exhibit's falls (4.38% → 4.36%). Say "similar shape at the short end; the long end is flatter in reality".
5. **Slide 60:** add one line saying the 2.81% forward is what the exhibit's curve implies, not what the 2014 market priced (slide 21). Then add the hindsight test: Bank Rate was actually cut in August 2016, so the implied rise never came. This tests the theory, not just asserts it.
6. **Slide 92:** replace "exactly" with "about the same size, but not parallel: the long end moved most".
7. **Slide 9:** confirm that the 2014 £1,365bn includes inflation uplift on index-linked gilts, as the 2026 figure does; otherwise "doubled" compares different bases.
8. **Slide 10:** footnote that the DMO dates the BoE's 26.4% as "end-2014" in a 2013-14 review.
9. **Slide 2:** "rate risk" in the opening line; gloss it ("how much a bond's price falls when rates rise").
10. **Slide 75:** label the range as modified duration (the 1-year's Macaulay duration is 1.00), so it reads consistently with slides 72–74.

## Earlier grader report: resolution check
Resolved: items 1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 14, 15 (structure only, sources missing), 16, 18, 20, 21.
Not resolved: item 7 in part (convexity is derived, but the convexity used on 81 differs from the one derived on 79); item 8 (Q4 still compressed, see B1); item 17 (slide 52 is still a label); item 19 (deferred).
