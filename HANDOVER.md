# Handover: Group 10, HBS Case 1 decks (Jaguar + UK Gilts)

**Paused on 2026-10-30, at gate 1 round 3, on the user's instruction.** This file tells the next Claude session (Claude Code, Cowork or similar) how to pick up exactly where we stopped.

## 1. What this project is
Two finance case decks, each a `.pptx` with **one design system shared by both**:
- **Jaguar Land Rover:** the 2015 refinancing of US$410m 8.125% notes with US$500m 3.5% notes.
- **UK Gilts:** bond pricing, YTM, the yield curve, and interest-rate risk.

The decks are for a BBA/MBA finance class at CFA Level 1 depth. They are presented live and also printed one slide per page, with no speaker notes, so each slide must stand on its own.

## 2. Read these first, in this order
1. `CLAUDE.md`: the job, hard rules, the gate workflow, and **"Standing rules from the user"** (these override everything else).
2. `review/PROGRESS.md`: status, next step, **every piece of user feedback word for word**, and every decision.
3. `DESIGN.md`: the design rules, including the **lucidity rule**. Open the three images in `design/references/`.
4. `review/shared/review-rubric.md`: the strict review criteria that decide approval.

## 3. Where we are
| | Jaguar | UK Gilts |
|---|---|---|
| Gate 0 (brief) | **Approved** | **Approved** |
| Gate 1 (answers + storyline) | Answers done and cross-checked; storyline round 3 written, sources round 3 applied; **strict review round 3 not yet run** | Answers done and cross-checked (exact match); storyline round 3 + fixes from strict review r3 applied ("A− once fixed"); **one more strict review needed** |
| Gate 2 (look) | Not started. Claude Slides artifact created and empty: https://claude.ai/artifact/FDSxNWFitiAfajUBNh6h5X | (shared) |
| Gates 3–4 | Not started | Not started |

**Approval rule for gate 1:** the user delegated approval to the independent strict reviewer: *"If they approve it, it is approved from my side … move on to the next stage."* When both storylines get **READY** under `review/shared/review-rubric.md`, gate 1 is approved, and you go straight to gate 2.

## 4. What to do next
1. Run `pip install scipy` if needed, then `python3 work/gilts/calcs.py` and `python3 work/jaguar/calcs.py`. Both should run cleanly.
2. Strict review: run the `grader` agent with the rubric (see the briefs in the history: verify everything, run `calcs.py`, check at least 20 numbers, check sources). Gilts is round 4; Jaguar is round 3. Fix every blocking item, then re-run until both are READY.
3. Gate 2: design both palette directions in the Claude Slides artifact, following DESIGN.md and the reference images, with 6 sample slides from Jaguar. Then the PPTX export test with the user. See CLAUDE.md gate 2.

## 5. Key results so far (details in `work/*/answers.md`)
**UK Gilts:**
- Missing values (annual basis):

  | | 2y | 5y | 10y | 30y |
  |---|---|---|---|---|
  | Price | 106.84 | 98.86 | 97.65 | 102.32 |

  | | 1y | 3y | 7y | 20y | 50y |
  |---|---|---|---|---|---|
  | YTM | 0.73% | 2.06% | 3.54% | 4.38% | 4.24% |
- At +1% the 1-year falls −0.98% and the 50-year −17.74%; modified duration runs from 0.99 to 20.82.
- An independent solver matched every number.
- Exhibit 1 is a teaching set, about one point above the real 9 May 2014 gilt curve (DMO data).

**Jaguar:**
- **Q1:** the coupon fell 462bp: the credit spread 304bp (66%), Treasury level and tenor 158bp. Like for like, the 5-year Treasury fell only 26bp.
- **Q2:** holders accept about **111–112** clean. JLR's actual offer, priced to the May 2016 call at 0.395% + 0.50%, gives 112.35 and is reproduced to within US$0.01. The naive value to 2021 is 125.43.
- **Q3:** against the realistic baseline (called 2016, at 2.28%) the NPV is −US$7.1m (after tax −US$7.3m). The naive figure (+US$53.6m) is an illusion.
- **Q4:** about no value for JLR or Tata; tendering holders +US$4.4m over the market.

## 6. User rules to keep
- **Only the word "Approved"** moves a gate, except the delegated rule for gate 1 above.
- **Questions to the user:** multiple choice, very simple words, why the question arose, what each option leads to, and a recommendation.
- **Lucidity:** a part-way CFA Level 1 reader with no presenter must follow every slide. Never cut analysis to get there.
- **One slide per repeated calculation.**
- **Decisions:**
  - Jaguar: call-aware Q2 first; US$ maths with one conversion at 1.50; the case's 15 May 2021 maturity plus one note slide (the filing says 15 Nov 2021).
  - Gilts: annual coupons plus one semi-annual comparison; no real gilt names (none matched with certainty).
- **Helpers:** every brief carries tough, explicit criteria and all restrictions.
- **The teaching notes** (`*Questions.docx`) are for checking only; never cite them.

## 7. File map
| Path | What |
|---|---|
| `Group 10 - HBS Case 1 Assignment_MATERIALS-*.zip` | Original materials (unzip into `materials/`, which is gitignored) |
| `materials/text/`, `materials/cfatxt/` | Text versions of the case, instructions, past decks and CFA readings (included in the handover zip) |
| `review/<case>/00-brief.md` | Gate 0 briefs (approved) |
| `review/<case>/01-storyline.md` | **Current slide plans** (Gilts 120 slides, Jaguar 127), each with its review responses |
| `review/<case>/01-grader-report.md`, `01-strict-review*.md` | Independent reviews |
| `work/<case>/calcs.py` | Every calculation; run it to see each step |
| `work/<case>/answers.md` | Methods, results, cross-check comparisons, tags |
| `work/<case>/exhibits.csv` (+ `_A`, `_B`) | Exhibit data (two independent extractions, 100% agreement) |
| `work/<case>/sources.md`, `sources_research.md` | External facts with URL, date and exact quote; secondary sources labelled |
| `work/<case>/check/` | Independent solver's work |
| `scripts/` | `check_deck.py`, `contact_sheet.py`, `cloud-setup.sh` |
| `.claude/agents/`, `.claude/skills/` | Helper definitions (sonnet-worker, grader) and skills |

## 8. Known gaps and cautions
- **Facts still secondary:**
  - the S&P 2016 downgrade, today's Fitch rating, and today's gilt prices/curve (giltsyield.com)
  - the 2014 competitor volumes for BMW and Audi
  - the market-wide high-yield spreads (~502bp in May 2011, ~460bp in Mar 2015; different indices, so indicative only)
  - the Tata Motors demerger, and the cyber-attack rating outlooks
- **Not found:** the early-repayment terms of the 2020 notes (sec.gov blocks automated tools); industry-wide premium SUV growth.
- **To re-check before submission:** Bank Rate (next decision 5 Nov 2026), today's yields, and JLR's latest results and ratings.
- **The user still has to supply:** the cover details (course, names) and the final slide (photos, full names, student IDs).
- **Git:** all work is on branch `claude/eloquent-cray-g3ajd9` (not yet merged to `main`).
