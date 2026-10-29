NOT READY. Grade estimate B+: the Q2/Q3 analysis is strong, but the plan has one finance inconsistency that drives the Q3/Q4 headline numbers, several factual errors in titles, external facts with no source behind them, and it fails the new lucidity test (H11).

# Jaguar storyline: strict independent review (gate 1)

Deliverable: `review/jaguar/01-storyline.md` (116 slides). Checked against the brief, `case-layout.txt`, CLAUDE.md, DESIGN.md, PROGRESS.md (user feedback and decisions), the `calcs.py` output, `exhibits.csv`, `sources.md` and `sources_research.md`. I did not take the "Response to the grader" section on trust; each claim was checked against the files.

## 1. Verdict
**NOT READY. B+.** Fails H3, H4, H6, H7, H8, H9 and H11. Quality scores below 4 on Q2, Q3, Q4, Q5 and Q6.

## 2. Hard requirements

| # | Result | Evidence |
|---|---|---|
| H1 Structure | PASS | Overview 3–17 → Exhibits 18–42 → Q1 43–55, Q2 56–75, Q3 76–90, Q4 91–103 → Epilogue 104–115 → Team 116. |
| H2 Every exhibit | PASS (minor) | Ex1 19–25, Ex2 26–29, Ex3 30–31 (rebuilt from Treasury CSV; source logged in `sources.md` #1), Ex4 32–35, Ex5 36–38, Ex6 39–41, synthesis 42. Each has a native rebuild, key numbers and an implication. Minor: slide 31 says the "1-year … priced the tender". The tender was priced off the 0.25% May-2016 note at 0.395%, a 14-month bond, not the 1-year point. |
| H3 Every question, all seven elements | **FAIL** | Q3's NPV is not shown step by step. Slides 82–84 list the dated flows with no discount factor or PV column. Slides 85–86 are a "step summary". Slide 87 compresses the whole after-tax calculation (after-tax coupons, the premium's tax shield, discounting at 2.80%) into one slide. The `calcs.py` "slide version" uses a per-100 shortcut (value of the old debt avoided − price paid), but the plan never shows why that shortcut equals the NPV of the 23 flows. Q4 has no stated assumptions beyond "assumptions" on 92, and its alternatives (93) carry no numbers. Q1–Q2 pass. |
| H4 External, sourced, current | **FAIL** | Many `[src]` tags have no entry in either sources file. `sources_research.md` R2-6 says "Industry facts … Not researched". Unsupported slides: **7** (sales by region FY2015, China JV 2014), **8** (industry drivers), **9** (BMW/Mercedes/Audi 2014 volumes), **4** (timeline and "five owners"), **108–109** (2015–2021 sales/profit, China, diesel, Brexit, Project Charge, COVID, chips), **110** (what JLR paid to refinance in 2019–20; no 2019–20 coupons are in the files). **Slide 12** puts B1 in 2011, but the sources say 2011 was "reportedly Ba3 … NOT verified", and B1 was a *later* fall (2019–23). **Slide 14**'s "strong demand for high-yield bonds" is contradicted by its own source: Fortune, 9 Mar 2015, has junk spreads *widening* from 330bp to 460bp. "Today" (Oct 2026) stops at FY2026. The 2026 rating actions are flagged as search-snippet only, and nothing from Q1 FY27 appears. |
| H5 No teaching note | PASS | No slide cites, quotes or refers to it. |
| H6 Titles are points and fit in two lines | **FAIL** | Label titles: **17** "The deal in one picture", **72** "Four answers, one picture", **78** "Assumptions", **82–84** "Incremental cash flows, 2015–2017 / 2018–2019 / 2020–2021", **105** "What we found". Titles that will not fit in two lines at headline size (25+ words): **42**, **27**, **31**, **50**, **52**, **69**, **86**. Factually wrong titles: **23**, **112** (see H8). |
| H7 Finance correct | **FAIL** | **(a) Discount-rate inconsistency (blocking).** Slide 67 argues correctly that for a 14-month claim "the right discount rate is far below 3.5%", and the market's 2.28% yield to call agrees (68). Yet slides 86, 87 and 101 value the "called in May 2016" baseline at 3.5% (109.11). That produces the headline NPV of −US$13.4m (86), −US$10.4m after tax (87), and "bondholders gained 3.24 over being called" (101). At a 14-month JLR rate (≈0.9–2.3%), the value to call is ≈111.3–112.3, so the "vs call" NPV is about −US$0.5m to −4.4m and the holders' gain is ≈0–1 point. The conclusion ("no economic saving") survives, but the numbers and the reasoning contradict each other. **(b)** Slide 48 calls all 304bp "credit spread". That block also contains the call-option premium in the 2011 non-call-5 bond and the slope of the credit curve (10-year vs 5-year spreads). Slide 54 admits the call issue but never takes it out of the waterfall. **(c)** Slide 64 says "certain to call"; a call is near-certain, not certain. **(d)** Slides 80 and 95 present "interest falls by US$16.8m a year" without saying that this saving lasts only until May 2016 on the realistic baseline (JLR would have called anyway). **(e)** The tax rate on slide 87: the premium is paid on 17 Mar 2015, which falls in the UK FY2014 (21% main rate to 31 Mar 2015, per `sources_research.md` R2-7). State why 20% is used. |
| H8 Numbers | **FAIL** | 18 of the 21 numbers checked match (table below). Errors: **slide 23**'s title "each new dollar note has carried a lower coupon" is false. The coupons by issue run 8.125% → 5.625% → 4.125% → **4.25%** → 3.5%, so Oct 2014 is higher than Dec 2013, and the tenors are mixed (10-year 2023 vs 5-year 2018). **Slide 112**: "JLR became investment grade in 2024–25". Moody's Ba1 (Jun 2025) is still sub-investment grade, and under the definition in the notes' own indenture investment grade needs BBB− **and** Baa3. **Slide 101**: 1.07 should be 1.08 (112.3514 − 111.276 = 1.075). **Slide 12**: B1 (see H4). |
| H9 User decisions | **FAIL** | The gate 0 decision was "lead with the call-aware value (≈109–112). Show the … to-maturity value (≈125) as the naive upper bound". The plan *leads* Q2 with Method A, the naive 125.43 (61–62), and only reaches the call on 63–66. Slide 22 uses the Exhibit's Dec-2014 rate (£263m) for a £ saving, against "US$ maths, one conversion at 1.50". Either label it as the Exhibit's own £ figure or redo it at 1.50 (£12.6m). The maturity note (74) and one-slide-per-repeat are honoured. |
| H10 Known traps | PASS | US$410m 8.125% semi-annual and the May 2016 call (60, 63–66); FX (25); clean vs dirty (58–59, 62, 70); the gap to ~125 and to the ~11% actual premium (72–73); the efficient-market lesson tested (48–52, 85–90). |
| **H11 Lucidity** | **FAIL** | The core concepts arrive after the slides that need them, and several are never introduced at all. Slides that would lose a basic reader as planned: **16, 17, 21, 23, 26, 27, 31, 34, 48, 52, 59, 61, 64, 65, 69, 85, 86, 87, 96, 100** (detail in section 5, B1). |

## 3. Quality scores

| | Score | Reason |
|---|---|---|
| Q1 Depth | 4 | Q1 is tested three ways and Q2 reconciles four values. But the 304bp "credit" block and the 3.5% call baseline are asserted rather than tested. |
| Q2 Logic and flow | 3 | Concepts come after their use (spread on 45 after 23 and 31; call on 63 after 21, 27 and 50). Q2 runs naive-first against the user's decision. Repeats: 27/50/64/68, 23/51, 31/49, 22/80. |
| Q3 Evidence | 3 | The case and the tender releases are used very well. But 8+ planned external facts have no source, and slide 14's claim is contradicted by its own source. |
| Q4 Lucidity | 2 | About 20 slides need a definition, a concept slide or a "so what" that the plan doesn't provide. There is no present-value, basis-point, YTM or NPV primer before first use. |
| Q5 Calculations | 3 | Q1, Q2 and the exhibit ratios are fully traceable. Q3's NPV and after-tax steps are not shown. |
| Q6 Overview and epilogue | 3 | The arc is good (tender outcome → 2016 call → 2020 maturity at COVID → cyber attack → TMPV). But 108–110 and 4, 7–9 are unsourced, 112 is factually wrong, and "today" stops at FY2026. |

## 4. Number spot-check

| Number | Slide | Source | Match |
|---|---|---|---|
| £2,448m drawn, £1,517m undrawn | 19 | exhibits.csv Ex1 Total | yes |
| Notes 92% of borrowing (2,255/2,448) | 20 | Ex1 | yes |
| £12.2m + £21.9m = £34.0m | 22 | calcs EXTRA | yes (but at the Exhibit's FX, see H9) |
| 410/263 = 1.559; £273.3m at 1.50 | 25 | calcs | yes |
| YTM 5.94%, YTC 2.28% at 111.276 | 27 | calcs Q1 | yes |
| 1Y 0.18→0.26, 5Y 1.83→1.57, 10Y 3.15→2.10 | 31 | sources.md #1 | yes |
| Revenue +43%, PBT +69% FY12–14 | 32 | calcs | yes |
| EBITDA margin 14.8% → 18.0% | 33 | calcs | yes |
| FCF 1,090 / 580 / 1,066 / 540; after interest and dividends 962 / 251 / 647 / 293 | 37 | calcs | yes |
| Net cash 456 → 1,604; D/E 0.68 → 0.36 | 40–41 | calcs | yes |
| Spreads 497bp / 193bp; fall 462 = 105 + 53 + 304 | 46–48 | calcs Q1 | yes |
| Accrued 122 days → US$27.53; 136 → US$30.69 | 59 | calcs; PR Newswire | yes |
| Naive 128.18 − 2.75 = 125.43 | 61–62 | calcs A | yes |
| To call at 3.5% = 109.11; at 0.50% = 112.85 | 66–67 | calcs | yes |
| 0.395% + 0.50% → 112.35; US$1,123.52 / 1,093.52 | 69–71 | calcs; pricing release | yes |
| Nov-2021 naive value 127.26 | 74 | calcs | yes |
| Cash needed 471.9; surplus 28.1; saving 16.8/yr; premium 50.6 | 79–81 | calcs | yes |
| NPV +53.5 / −13.4 / +44.8 / −10.4 / −4.4 | 85–88 | calcs | numbers yes; method inconsistent (H7a) |
| 1.07 per 100 over market | 101 | calcs: 1.08 | **no** |
| 79.61%, US$326.4m, US$375.7m; US$83.6m in May 2016 | 106–107 | releases; 20-F | yes |
| "Each new US$ coupon lower" | 23 | sources R2-1 (4.125% then 4.25%) | **no** |
| "Investment grade 2024–25" | 112 | Moody's Ba1 Jun 2025 | **no** |
| Moody's B1 in 2011 | 12 | sources E: "reportedly Ba3, NOT verified" | **no** |
| £22.9bn FY2026; TMPV owner | 114 | sources F, R2-5 | yes |

## 5. Blocking items (slide → problem → exact fix)

**B1. Lucidity (H11): add the concepts before their first use, and a plain line on each slide listed.**
- Add a short **"Bond toolkit"** block before the exhibit section (after 17, or at the start of 18–19), one idea per slide:
  - face value and price per 100
  - coupon, semi-annual payments
  - basis point (1bp = 0.01%)
  - present value and discounting (formula in words, then a one-bond example)
  - YTM as "the single rate that makes the PV of the flows equal the price"
  - credit spread = corporate yield − Treasury yield (move slide 45 here)
  - call option, yield to call and yield to worst (move the concept from 63–64 here)
  - clean vs full price (move 58 here)
- **Q3 opening:** a concept slide on incremental cash flows and NPV, saying in words "+ = JLR better off", before slide 82.
- **Q4:** a concept slide on market efficiency and MM in plain words, before slide 100.
- Per slide:
  - 16: define tender offer, consent solicitation, covenant and early premium, one line each.
  - 17: label every arrow with what the money is.
  - 21: what "callable" means.
  - 23, 31: what the bp and spread figures mean.
  - 26: drop or explain the ISIN, 144A/Reg S and "indicative" jargon.
  - 27: YTM vs YTC in words.
  - 34: what capitalising development costs does to profit.
  - 48: what "tenor effect" means.
  - 52: what a high-yield index spread is.
  - 59: the 30/360 day count in words.
  - 61: say in words what discounting does before the table.
  - 64: yield to worst.
  - 65: replace "negative convexity" with a plain picture (price capped near the call price), then name it.
  - 69: coupon 0.25% vs yield 0.395%, and what a fixed spread is.
  - 85–87: what NPV > 0 means for JLR.
  - 86: why refinancing at the market rate has zero NPV.
  - 96: what stripping covenants does to a holder.
- **Storyline rule:** every calculation line ends with its one-line "so what".

**B2. Discount-rate inconsistency (H7a), slides 86, 87, 89, 101, 102.**
- Value the "called in May 2016" baseline at a 14-month JLR rate consistent with slide 67: the market's 2.28% yield to call, and/or the tender's 0.895%. Keep 3.5% only as a labelled sensitivity.
- Recompute: vs call ≈ −US$4.4m at 2.28% (equal to the market comparison) and ≈ 0 at 0.895%. Then update the after-tax version, the holders' gain on 101, and Tata's position on 102.
- Retitle 86 and 101 to the corrected magnitudes.

**B3. Q3 calculation steps (H3/Q5), slides 82–87.**
- Add discount-factor and PV columns to 82–84, with totals.
- Add one slide showing that NPV = PV(old flows avoided) − cash paid, which is why the per-100 version (value avoided − price paid) gives the same answer.
- Split 87 into: after-tax flows table → tax shield on the premium → discount at 3.5% × (1 − t) → result.
- State the 21% vs 20% timing choice.

**B4. Factual title and number errors (H8/H4).**
- 23: retitle, e.g. "Coupons on JLR's dollar notes fell from 8.125% (2011) to 3.5% (2015), but tenors differ". Plot spread over the tenor-matched Treasury and mark the 4.25% exception. Flag the approximate issue dates.
- 112: "S&P made JLR investment grade in Aug 2024; Moody's still rates it one notch below (Ba1)".
- 12: remove B1 for 2011, or source it. Start from sourced points only (Ba3 → Ba2 Sep 2013; positive outlooks late 2014 per the case).
- 101: 1.08, not 1.07.

**B5. Unsourced external facts (H4).**
- Source before gate 2, or cut: 4 (owners timeline), 7 (regional sales, China JV), 8 (industry drivers), 9 (rival volumes), 108–109 (2015–21 performance and events), 110 (2019–20 refinancing coupons; this is the hindsight point, so it must be sourced).
- Rewrite 14: high-yield spreads had *widened* to ~460bp by Mar 2015 (energy sell-off), yet JLR still priced at 193bp over the 5-year Treasury. That makes a stronger point than "strong demand".
- Add a current (2026) data point: latest quarter results, and a verified rating status after the cyber attack.

**B6. Q2 order against the user's decision (H9), slides 61–66.**
- Put the call (63–64) and Method B / tender value (66–70) first. Then show Method A (61–62) as the naive upper bound, followed by 72–73.

**B7. Label titles and overlong titles (H6).**
- Give 17, 72, 78, 82–84 and 105 point titles.
- Cut 27, 31, 42, 50, 52, 69 and 86 to two lines (≈15 words or fewer), moving the detail into the body.

## 6. Non-blocking improvements (most valuable first)
1. Slide 48: label the 304bp as "credit spread, incl. call premium and credit-curve slope". Add one line estimating the call component, e.g. the 2015 value of the issuer's call (≈14 points, slide 65) as a yield equivalent. This makes slide 55's "mostly credit" more defensible.
2. Merge the repeats: put 27's YTC on the toolkit slide and keep 68 as the Q2 check; let 50 point back to 27; 49 restates 31; 22 and 80 overlap.
3. Slides 80/95: say that the US$16.8m a year runs against the hold-to-2021 view. Against the call view, the saving after May 2016 is about zero.
4. Slide 65: say that 125.43 and 111.28 come from different dates and yields, so 14 points is an approximate option value.
5. Q2 answer (75): add the effect of the consent solicitation. Non-tenderers lose their covenants, which pushes holders to accept even near the market price, and that helps explain why 79.6% tendered early.
6. Q4: also cover other existing creditors (the other five note series). JLR adds about US$90m of gross debt and moves this maturity to 2020; is either a small cost to them?
7. Q4 alternatives (93): attach one number to each alternative, e.g. the open-market buyback cost at 111.28, or a call in May 2016 = 104.0625 + coupons.
8. Slide 31: replace "the 1-year priced the tender" with "the 14-month 0.25% May 2016 Treasury (0.395%) priced the tender".
9. Depth: 116 slides against the brief's 150–200 and the 268-slide benchmark. The toolkit block (B1) and the Q3 step slides (B3) close much of this gap with real content.
10. Slide 52: say the two high-yield figures come from different indices and dates (BofA ≈10 May 2011; Fortune, unnamed index, 9 Mar 2015), so ~40bp is indicative only.

## Strongest parts
- Q2 reproduces the actual tender price to the cent (0.395% + 50bp to the May 2016 call at 104.0625 → 112.35). It reconciles 109.11 / 111.28 / 112.35 / 125.43 and explains the gap to the naive 125. This is the analytical centre of the deck and well above a class answer.
- Q1 tests the "better credit, not lower Treasuries" claim three ways: same bond, issue by issue, and against the market.
- The exhibit section goes past description: cash interest cover, capitalised development costs, the effective tax rate, the FX implied by Exhibit 1, and Exhibit 3 rebuilt from official Treasury data.
- The epilogue closes the loop on the decision: tender take-up, the residual called in 2016, and the 2020 maturity at COVID.
