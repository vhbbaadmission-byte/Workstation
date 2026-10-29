# Group 10 — HBS Case 1 decks

## Start of every session
1. `git pull --rebase`
2. Read `CLAUDE.md` (this file), `DESIGN.md` and `review/PROGRESS.md`. Before any design work, **open and look at all three reference images** with the Read tool (it shows images):
   - `design/references/ref-1-bettertask-indigo.png`
   - `design/references/ref-2-pilot44-overview.png`
   - `design/references/ref-3-pilot44-detail.png`

   PROGRESS.md says where we are and holds every approval and piece of feedback the user has given. It outranks your memory of earlier conversation.
3. Continue from the "Next step" in PROGRESS.md.

## The job
**Two decks, one design system:**
1. **Jaguar**: JLR's 2015 bond refinancing
2. **UK Gilts**: bond pricing, YTM, the yield curve, and rate risk

Both decks use the same design (one gate 2). The deliverable is `.pptx` only; PDF is not accepted. A hard copy is printed with **one slide per page** and spiral bound, so every slide must also read well on paper. The deadline has been extended; ask the user for the date at gate 0.

## Materials
Everything is in `Group 10 - HBS Case 1 Assignment_MATERIALS-*.zip`. Unzip it into `materials/` (gitignored). The `CFA Reference Materials/*.zip` files are zips too; unzip only the readings you need.

Per case folder (`Jaguar/`, `UK Gilts/`):

| File | What it is | How to use it |
|---|---|---|
| `Case Files/* Case.pdf` (+ `UK Gilts.xlsx`) | The case and its exhibits | Primary source. Every exhibit must appear in the deck. |
| `Case Files/* Questions.docx` | **Teaching note with answers** | For **checking only**. Never copy its wording, never cite it on a slide, never use its numbers without our own working. For "what happened next", cite the public sources it points to (exchange notices, annual reports) after checking them yourself. |
| `Case Presentation Instructions.docx` | The grading brief | Hard rules (below). Re-read it before every gate. |
| `CFA Reference Materials/CFA * Guide.txt` | Which CFA readings matter, in priority order | Read the "Essential" readings first. Theory, terms and formulas follow CFA Level 1. |
| `G1 NESA (Final).pptx` (268 slides), `G2 WACC vs Equity.pptx` | Past case-study decks | **The flow and depth the professor expects.** Guides, not limits: go beyond them where the case calls for it. |
| `Investment-Analysis.pptx` | Lecture deck | Level, and how concepts are explained |
| `Cash Flow Statement.pptx` | Lecture deck | Background knowledge, only when needed |
| `UK Gilts/Spartan Inc (V3).docx`, `3.2 Spartan Solution.xlsx` | **A different case** (Spartan Inc) and its solution | Reference for how worked solutions are laid out. Don't mix its content into UK Gilts. |

Note: `UK Gilts Questions.docx` lists its four questions twice. There are four questions, not eight.

## Level
CFA Level 1 depth, for a BBA/MBA finance class. Concepts are explained where the class would need them, and every number is derived on the slide.

## Hard rules (from the instructions)
- Structure: **Case Overview → Exhibits Analysis → Main Case Analysis → Epilogue → final slide**. Follow the case's chronology where it makes sense.
- Overview and epilogue bring in **external, current information**: the company or market, what happened after the case, where things stand today. Cite every source on the slide.
- **Every exhibit**: rebuild it as a clean native table or chart from its numbers (the PDF has a "Do Not Copy" watermark, so don't screenshot it), label it "Exhibit N" with its source, then say what it shows, the key numbers and trends, what they mean, and what they imply for the decision.
- **Every assigned question**: state it, break it into parts, apply theory, state assumptions, compare alternatives, and **show every calculation step on the slides**. No "see Excel".
- **Final slide**: each member's photo, full name and student ID. The user will provide these; until then use a clearly marked placeholder.
- The deck stands on its own. Body text **at least 18pt**. Charts, tables and maths readable. No overcrowding. Consistent layout, fonts and colours.
- No slide limit. Length follows the content; never pad to reach a count. Depth and flow matter more than count.

## How we work: approve first, then build
The user works like a director with an editor: **no long builds without sign-off.** At each gate: save the deliverable in `review/<case>/` (or `review/shared/` for gate 2), update PROGRESS.md, commit and push, show it in chat, then **stop and wait**.

- **Only the word "Approved" moves to the next step.** Any other reply, including "looks good but fix X", means: make the changes, show it again, and wait.
- Write the user's feedback **word for word** into PROGRESS.md before acting on it. Design feedback also goes into DESIGN.md.
- Never change something already approved without asking.

### Gate 0: Brief (per case)
1. Unzip the materials and turn each file into text (`markitdown`).
2. **Pull every exhibit number into `work/<case>/exhibits.csv`.** Have two `sonnet-worker`s extract the numbers independently, diff their files, and fix any mismatch against the PDF. Check that totals add up (balance sheet balances, cash flow subtotals sum).
3. Read the "Essential" CFA readings, and study how G1 and G2 open, pace exhibits, go deep on calculations and move between sections.
4. **Test the session's tools:** can you search and fetch the web? Can you create a Claude Slides artifact? If either fails, tell the user now.
5. Write `00-brief.md`: the case in plain words; every exhibit and question; the CFA concepts you'll use; your one-line answer to each question; the traps you found; the research plan; your questions for the user (including the deadline). **Stop.**

### Gate 1: Answers + storyline (per case)
1. **Solve every question fully before planning any slides**, in `work/<case>/calcs.py` (runnable; prints every intermediate number) plus `work/<case>/answers.md` (method, assumptions, results).
2. **Independent check:** a `sonnet-worker` solves the same questions from the case alone, without seeing your answers. Compare its numbers with yours and with the teaching note. Explain every difference in `answers.md`; never hide one. Tag each answer: *solid*, *debatable* or *uncertain*.
3. Write `01-storyline.md`: one line per slide, giving its section, **the point it makes** (this becomes its title), and what it shows (which exhibit, calculation, chart or source). Never fix how many bullets, rows or boxes a slide has.
4. Add an **instructions checklist**: every requirement in the instructions → the slide numbers that meet it.
5. Where showing every step would flood the deck (e.g. pricing nine gilts), propose how to show it (e.g. one full worked example, then a results table with the formula stated) and **let the user choose**. **Stop.**

### Gate 2: The look (once, shared by both decks)
1. Design in **Claude Slides** (create a Slides artifact, the `/slides` template; if you can't start one yourself, ask the user to type `/slides` with your brief). Follow DESIGN.md: design from `design/references/`, then the `apple-design` polish pass.
2. Make 6 sample slides with real content from Jaguar: cover, section divider, exhibit + analysis, calculation, chart, conclusion. Make them in **both palette directions** (A indigo, B lime), recommend one, and check every slide against DESIGN.md yourself first.
3. **PowerPoint export test.** Ask the user to export the samples to PPTX, open them in real PowerPoint, and report: is the text editable (not pictures)? Are the fonts right? Are the charts editable? Is everything readable and at least 18pt? Commit the exported file to `review/shared/02-look.pptx` and run `scripts/check_deck.py` on it.
4. **Decide the build tool** with the user and record it in PROGRESS.md:
   - **Export is good →** build both decks in Claude Slides and export.
   - **Export is weak →** Claude Slides stays the design master; build the .pptx with python-pptx (`mck-ppt-design`, `pptx-author` for technique only), matching the approved Slides design slide by slide, and compare renders side by side.
   **Stop.**

### Gate 3: Build, one section at a time (per case)
Sections: Overview → Exhibits → each Question → Epilogue → Final slide.
1. Build the section from the approved storyline and look. `sonnet-worker`s may build slides; you check every slide at full size.
2. All numbers come from `exhibits.csv` / `calcs.py`, never retyped from memory. Charts are generated from the data.
3. After each section, run the checks:
   - `scripts/check_deck.py` (text size, titles, overflow, crowding)
   - full-size render check of every slide (DESIGN.md rules, axis labels, legends, contrast)
   - every number on the slides matches `exhibits.csv` / `calcs.py`
4. Show the section (Slides link, or a contact sheet via `scripts/contact_sheet.py`), commit, and push. **Stop.**

### Gate 4: Final check (per case)
1. `ib-check-deck` over the whole deck: the same number is the same everywhere, numbers match the story.
2. Tick the instructions checklist against the finished deck.
3. Print check: view every slide in greyscale; fix anything that becomes hard to read.
4. `humanizer` pass on the slide text: wording only. **Diff every number before and after; they must not change.**
5. Write `04-qc.md` with the results, and remind the user to embed fonts (DESIGN.md → Fonts) and flip through the deck in real PowerPoint. **Stop.**

## When to stop and ask, even between gates
- Your answer and the teaching note differ by more than rounding.
- Data is missing, or two sources disagree.
- Web research or Claude Slides doesn't work.
- A rule can't be met (e.g. a calculation won't fit at 18pt even when split).
- You'd need to change something already approved.

For everything else, make a sensible choice, log it under "Decisions made" in PROGRESS.md, and list those decisions at the next gate.

## Known traps
**Jaguar**
- The tender is for the **US$410m 8.125% notes due 2021** (Exhibit 1). They pay **semi-annual** coupons and are **callable from May 2016**; consider what the call does to the price bondholders would accept.
- Notes are in US$, while JLR reports in £. State the exchange rate you use and why.
- Clean vs dirty price: the tender paid accrued interest separately.
- Your answer to Q2 may differ from the teaching note's (25–29% premium) and from the actual tender (~11%). Explaining the gap is part of the analysis.
- The case's core lesson: in an efficient market, refinancing at a fair price creates little or no value; JLR's lower rate came from better credit, not lower Treasury yields (they moved only ~26bp). Test this, don't just assert it.

**UK Gilts**
- Exhibit 1 uses **annual coupons** (a simplification; real gilts pay semi-annually). Say so.
- Prices are per £100 of face value.
- The CFA guide puts duration and convexity in "Essential"; use them to explain the +1% yield shift.

## Facts, sources and numbers
- **No source, no fact.** Every external fact goes into `work/<case>/sources.md` with its URL, the date accessed, and the exact quote, and gets a source line on its slide. Spot-check what helpers bring back.
- Number formats, used everywhere: money in £m or US$m to 1 decimal place; bond prices to 2 dp; yields and rates as % to 2 dp; basis points as whole numbers. Say the units on every table and axis.
- Slide titles state the point in plain words, at most 2 lines (see DESIGN.md).
- No speaker notes.

## Skills in `.claude/skills/`
- `markitdown`: read PDFs, Word and Excel files
- `brainstorming`: **use it before every planning step**: gate 0 questions, the gate 1 storyline, the gate 2 look, and any time the user's direction leaves a real choice open. Look at the materials first, lay out the options with trade-offs, and recommend one. Its output goes into the gate files in `review/`, not `docs/superpowers/`. Don't use its visual-companion server. The approval gates above replace its "writing-plans" hand-off, which isn't installed here.
- `apple-design`: polish pass after designing from the references (DESIGN.md says which parts apply)
- `anti-slop-slides`: design principles only (it builds HTML; we don't)
- `mck-ppt-design`, `pptx-author`: python-pptx technique, only if gate 2 picks the code route. Their colours, layouts and output folders are overridden by DESIGN.md and this file.
- `ib-check-deck`: final number and consistency check
- `humanizer`: tidy slide wording; never touch numbers or finance terms
- `dispatching-parallel-agents`: how to split independent work across helpers
- `verification-before-completion`: before saying anything is done or correct, check it (render it, recount it, recompute it) and show the evidence

## Using Sonnet helpers
You (Opus) are the lead. Hand work to the **`sonnet-worker`** agent (`.claude/agents/`) whenever you judge Sonnet can do it well. That means the task is clearly defined, has a checkable result, and needs no judgment calls. This saves time and usage, and independent pieces can run in parallel.

| Usually give to Sonnet | Keep for yourself |
|---|---|
| Turning materials into text; extracting exhibit numbers (twice, independently) | Understanding the case; gate 0 brief |
| Gathering external facts with sources | The storyline (gate 1) |
| Building slides from an **approved** storyline section + DESIGN.md | Design decisions and the gate 2 look |
| Contact sheets; first-pass checks (18pt, axis labels, legends) | Financial reasoning: bond pricing, yields, cash flows, final answers |
| Re-solving the questions independently to cross-check yours | Talking to the user, and anything shown at a gate |

Rules:
- When a helper builds or checks slides, its brief must tell it to open `DESIGN.md` and the three images in `design/references/` first.
- Give each helper a self-contained brief: the exact task, the input files, the slide numbers or storyline lines, where to save, and what "done" looks like. It can't see this conversation.
- **Check everything a helper returns before it reaches the user.** Look at the rendered slides and spot-check numbers against the sources. You're responsible for the result.
- If a helper's work is weak, redo it yourself or re-brief it more tightly. Don't hand it on.

## Tools
- `scripts/cloud-setup.sh` (runs at session start): python-pptx, markitdown, LibreOffice, poppler, fonts. If a tool is missing, rerun it.
- `scripts/contact_sheet.py deck.pptx out.png [--first N --last M]`: slides as one numbered grid image. For checking details, render single slides at full size.
- `scripts/check_deck.py deck.pptx`: rule checks; exit code 1 on failure. Self-test: `python3 scripts/test_check_deck.py`. On a Claude Slides export, if a failure comes from how the export is structured (e.g. sizes inherited from the layout) rather than a real problem, confirm it visually and note it in the QC report.

## Git and files
- Commit and push to `main` after every gate and every built section. Always `git pull --rebase` before pushing. The two cases have separate folders, so parallel sessions shouldn't collide.
- `materials/`: unzipped inputs (gitignored)
- `work/<case>/`: `exhibits.csv`, `calcs.py`, `answers.md`, `sources.md`
- `review/PROGRESS.md`: status, approvals, feedback, decisions
- `review/<case>/`, `review/shared/`: gate deliverables
- `build/`: deck-building scripts (code route only)
- `output/`: final `.pptx` files
