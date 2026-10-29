# Independent review rubric (strict)

The user approves a gate **only if an independent reviewer passes it under this rubric**. Be the toughest fair examiner: a finance professor marking a high-stakes case presentation (CFA Level 1 depth, BBA/MBA), and a technical editor. Do not trust the authors' own claims (for example, their "response to the grader" section): verify every claim against the files.

## What you are reviewing
- **Gate 1 (storyline):** a one-line-per-slide plan. Judge whether a deck built exactly from this plan would earn an A.
- **Gate 4 (finished deck):** the deck itself.

## Sources of truth (read them; do not rely on memory)
1. The grading brief: `materials/text/<case>/Case Presentation Instructions.docx.md`
2. The case: `materials/text/<case>/case-layout.txt`
3. Project rules: `CLAUDE.md` (sections "The job", "Level", "Hard rules", "Known traps", "Facts, sources and numbers") and `DESIGN.md` (titles, 18pt minimum, calculation-slide layout)
4. User decisions: `review/PROGRESS.md` (sections "User feedback" and "Decisions made"). A plan that contradicts a user decision fails.
5. The numbers: `work/<case>/calcs.py` (run it: `python3 work/<case>/calcs.py`), `work/<case>/exhibits.csv`, `work/<case>/answers.md`
6. Sources: `work/<case>/sources.md`, `work/<case>/sources_research.md`
7. Benchmark depth: the professor's past decks run to 268 slides with one calculation step per slide (`materials/text/Jaguar/G1 NESA (Final) 11.09.2026.pptx.md`).

## Hard requirements (any failure = NOT READY)
H1. **Structure:** Case Overview → Exhibits Analysis → Main Case Analysis (each question) → Epilogue → final team slide (photo, full name, student ID; a placeholder is allowed).
H2. **Every exhibit:** rebuilt natively (never a screenshot), labelled "Exhibit N" with its source, and followed by what it shows, the key numbers/trends, what they mean, and the implication for the decision. Check each exhibit in the case one by one.
H3. **Every question:** stated; broken into parts; theory applied; evidence (case + external); assumptions stated; alternatives compared; **every calculation step shown on slides** (formula → numbers plugged in → result; no "see Excel"). Check each question one by one against all seven.
H4. **Overview and epilogue:** external, current, sourced information (what happened after the case, where things stand today, as of October 2026). Every external fact is marked as sourced, and the sources file actually supports it.
H5. **No teaching note** is cited, quoted or referred to anywhere.
H6. **Titles** state the point in plain words (a finding, not a label) and fit in two lines.
H7. **Finance is correct at CFA Level 1:** definitions, formulas, conventions (clean/full price, accrued interest 30/360, YTM as IRR and its assumptions, yield-to-call/worst, callable = straight − call, duration, convexity, spreads, NPV logic, MM and market efficiency, after-tax cost of debt). Any conceptual error is blocking.
H8. **Numbers are right:** spot-check at least 15 numbers in the plan against `calcs.py` output, `exhibits.csv` or the sources files. Any mismatch beyond rounding is blocking. Number formats: money to 1 dp, prices to 2 dp, yields to 2 dp, bp whole.
H9. **User decisions are honoured** (from PROGRESS.md). For example, Jaguar: call-aware Q2 first, US$ maths with one conversion at 1.50, the case's May 2021 maturity plus one note slide, one slide per repeated calculation. Gilts: annual coupons plus one semi-annual comparison, gilt names only when certain, one slide per repeated calculation.
H10. **Known traps** in CLAUDE.md are handled (each one explicitly).
H11. **Lucidity (user's top criterion).** The reader is a student part-way through CFA Level 1: they know the basics (time value of money, what a bond is) but have not mastered every topic (e.g. callable bonds, convexity, spot/forward rates, refinancing NPV). They read on paper with no presenter. Lucidity must NEVER come from simplifying or dropping analysis: the full professional analysis must be there, presented so this reader can follow it. For EVERY slide, ask: would they understand what is being said and why it matters? Lucidity does NOT mean removing complex analysis. It means the complexity is shown and explained clearly:
   - each technical term (YTM, spread, accrued interest, call option, duration, convexity, NPV, bp…) is defined in plain words before or where it is first used
   - each formula is explained in words before the numbers are plugged in
   - each number says what it is and its unit
   - each calculation ends with a plain "so what"
   - concept slides come before the slides that use the concept
   - titles say the point in everyday language
   List every slide that would leave such a reader lost, and say what to add. More than a handful of such slides = FAIL.

## Quality scores (1–5 each; READY needs every score ≥ 4)
Q1 Depth of analysis (beyond the obvious; tests claims rather than asserting them)
Q2 Logic and flow (chronology where sensible, each slide earns its place, no repetition)
Q3 Use of evidence (case, exhibits, external sources, used as evidence and not decoration)
Q4 Lucidity: a part-way CFA Level 1 reader with no presenter follows every slide, with no analysis dropped (see H11); score 5 only if no slide would lose them
Q5 Calculations (complete, traceable, readable, nothing skipped)
Q6 Overview and epilogue (informative, current, tied back to the case decision)

## Verdict
- **READY:** zero hard-requirement failures, all quality scores ≥ 4, and your grade estimate is A− or better.
- **NOT READY:** anything else. List the blocking items, each with slide numbers and the exact fix.

## Report format
1. Verdict (READY / NOT READY) and grade estimate, on one line.
2. Hard requirements: H1–H10, each PASS/FAIL with evidence (slide numbers, file lines).
3. Quality scores Q1–Q6 with one-line reasons.
4. Number spot-check table: number, slide, source, match yes/no.
5. Blocking items (if any): slide, problem, exact fix.
6. Non-blocking improvements, at most 10, most valuable first.
