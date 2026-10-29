# Group 10 — HBS Case 1 decks

## The job
Build **two PowerPoint decks**, one per case:
1. **Jaguar**: JLR's 2015 bond refinancing (Jaguar Bond Case)
2. **UK Gilts**: bond pricing, YTM, the yield curve, and rate risk

Deliverable is `.pptx` only. The deadline has been extended; ask the user for the new date if it matters.

## Materials
Everything is in `Group 10 - HBS Case 1 Assignment_MATERIALS-*.zip`. Unzip it into `materials/` at the start of the first session (`materials/` is gitignored). Inside, the `CFA Reference Materials/*.zip` files are zips too; unzip only the readings you need.

Per case folder (`Jaguar/`, `UK Gilts/`):

| File | What it is | How to use it |
|---|---|---|
| `Case Files/* Case.pdf` (+ `UK Gilts.xlsx`) | The case and its exhibits | Primary source. Every exhibit must appear in the deck. |
| `Case Files/* Questions.docx` | **Teaching note with answers** | Use it to check your answers. Never copy its wording, and never present its numbers as ours without showing the working. |
| `Case Presentation Instructions.docx` | The grading brief | Hard rules (below). Re-read it before every review gate. |
| `CFA Reference Materials/CFA * Guide.txt` | Which CFA readings matter, in priority order | Read the "Essential" readings first. Theory and formulas should match CFA Level 1. |
| `G1 NESA (Final).pptx` (268 slides), `G2 WACC vs Equity.pptx` | Past case-study decks | **Show the flow and depth the professor expects.** Use them as guides, not limits: go beyond them wherever the case calls for it. |
| `Investment-Analysis.pptx` | Lecture deck | Reference for level and how concepts are explained |
| `Cash Flow Statement.pptx` | Lecture deck | Background knowledge, only when needed |
| `UK Gilts/Spartan Inc (V3).docx`, `3.2 Spartan Solution.xlsx` | Another case and its solution | Reference for how worked solutions are laid out |

## Level
CFA Level 1 depth, written for a BBA/MBA finance class. Every concept is explained before it's used, and every number is derived on the slide.

## Hard rules (from the instructions)
- Structure: **Case Overview → Exhibits Analysis → Main Case Analysis → Epilogue**.
- Overview and epilogue must bring in **external, current information** (the real company or market, what happened after the case, where things stand today). Cite every source on the slide.
- **Every exhibit**: insert it (the case PDF has a "Do Not Copy" watermark on every page, so rebuild each exhibit as a clean native table or chart from its numbers, labelled "Exhibit N" with its source), say what it shows, give the key numbers and trends, say what they mean, and say what they imply for the decision.
- **Every assigned question**: state it, break it into parts, apply theory, give assumptions, compare alternatives, and **show every calculation step on the slides**. No "see Excel".
- The deck must stand on its own. Body text is **at least 18pt**. Charts, tables and maths must be readable. Slides must not be overcrowded. Layout, fonts and colours stay consistent throughout.
- There's no slide limit; 150–200+ is fine. Depth and flow matter more than count.

## How we work: approve first, then build
The user works like a director with an editor: **no long builds without sign-off.** At each gate below, put the deliverable in `review/<case>/`, commit and push it, show it in chat, and **stop and wait** for the user's reply. Only an explicit approval moves you forward. When the user gives feedback, revise and show the gate again.

| Gate | What you show | Format |
|---|---|---|
| **0. Brief** | Your understanding of the case in one page; the questions and exhibits found; your questions for the user | `00-brief.md` |
| **1. Storyline** | Every slide as one line: section, what the slide is for (its message), and the source or exhibit it uses | `01-storyline.md` |
| **2. Look** | 5–6 sample slides (cover, section divider, exhibit + analysis, calculation, chart, conclusion) | `02-look.pptx` + contact sheet PNG |
| **3. Build, one section at a time** | The finished section | Deck + contact sheet PNG of that section |
| **4. Final QC** | Full deck plus a QC report (`ib-check-deck`, 18pt check, every exhibit and question covered) | Final `.pptx` + `04-qc.md` |

Do both cases in parallel or one after the other. Ask the user which at gate 0.

### Content vs design: don't box slides in
- The storyline sets **what each slide says**, not how many bullets, rows or boxes it has. Never fix item counts in advance.
- When content doesn't fit beautifully, **split it into more slides**. Never shrink the font or cram.
- Pick the layout per slide to fit the message (chart, diagram, big number, step-by-step working, comparison). Avoid wall-of-bullets slides.

### Contact sheets
`python3 scripts/contact_sheet.py deck.pptx review/<case>/sheet.png [--first N --last M]` renders slides into one numbered grid image. Before showing one to the user, look at it yourself and fix anything broken, cramped, misaligned or off-style.

## Design
The user will supply design rules (`DESIGN.md`) later. Until then, follow the `anti-slop-slides` principles and take cues from G1 and G2, but keep the gate 2 look easy to change.

## Skills in `.claude/skills/`
- `markitdown`: read PDFs, Word and Excel files
- `mck-ppt-design` / `pptx-author`: build the .pptx with python-pptx
- `anti-slop-slides`: design discipline
- `humanizer`: clean up slide text and speaker notes
- `ib-check-deck`: final number and consistency QC

The setup hook (`scripts/cloud-setup.sh`) installs python-pptx, markitdown, LibreOffice and poppler. If a tool is missing, rerun it.

## Files
- `materials/`: unzipped inputs (gitignored)
- `review/<case>/`: gate deliverables (committed)
- `build/`: the scripts that generate each deck (committed, so decks can be rebuilt after feedback)
- `output/`: final `.pptx` files
