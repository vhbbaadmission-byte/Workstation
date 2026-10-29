# Progress

Read this at the start of every session. Update it at every gate and after every piece of user feedback.

## Status
| | Jaguar | UK Gilts |
|---|---|---|
| Current gate | 0 — brief done, waiting for approval | 0 — brief done, waiting for approval |
| Last approved | — | — |

Shared gate 2 (look): not started · Build tool: not decided · Claude Slides link: https://claude.ai/artifact/FDSxNWFitiAfajUBNh6h5X (created empty at gate 0 as the tool test; used at gate 2)

## Next step
User reviews `review/jaguar/00-brief.md` and `review/gilts/00-brief.md` and answers their questions. On "Approved": gate 1 for both cases.

## Already settled with the user (before gate 0)
- Two decks, one design system shared by both.
- Mostly run in cloud sessions.
- Slide titles state the point.
- Footers (source line, slide number) may be 12pt; everything else at least 18pt.
- No speaker notes.
- Cover details and the final slide (photos, names, student IDs): the user will provide these later.
- G1 and G2 show the expected flow and depth; they're guides, not limits.
- Don't ask for the deadline; work as fast as quality allows.
- The deck is presented live, but with no speaker notes, so slides can't be too sparse.
- The repo stays public.

## User feedback, word for word (newest first)
- 2026-10-29: "I have connected with GitHub. Next time, when you ask me questions like "Your language was too complex for me," for now, even make a guess. I'm guessing what you said was right and accurate. Whenever you have questions for me next, keep the language as simple as possible, and make your explanations bigger and more simple so that I can understand what the implications are and what could have" → Rule: every question to the user uses very simple words, explains longer and more plainly what each choice means and what happens if they pick it, and avoids finance jargon (or explains it).
- 2026-10-29 (gate 0 questions, answered by choice): Jaguar Q2 = "Call-aware first (Recommended)"; Currency = "US$, convert once (Recommended)"; Gilts basis = "Annual + 1 comparison (Recommended)"; Gilt names = "Name only if certain (Recommended)". Also: "Ask them a question with choices. Remember to see the repercussions: why this question arose, what my options are, and what the repercussions are for the options. As for GitHub, it is connected." → From now on, put questions to the user as multiple-choice, each saying why it arose and what each option leads to.
- 2026-10-29 (gate 0, after network test): "you have full network access now , as for the designs ensure you use the claude design style workflow to achieve that levle of quality and accuracy"
- 2026-10-29 (start of gate 0): "session branch is fine, both" — push to `claude/eloquent-cray-g3ajd9` instead of `main`; run gate 0 for both cases in this session.

## Decisions made without asking (show these at the next gate)
- Work on branch `claude/eloquent-cray-g3ajd9` (user: "session branch is fine").
- `exhibits.csv` = extractor B's file for both cases. Extractor A agreed on every value; A's raw file is kept as `exhibits_A.csv`.
- Jaguar Exhibit 3 (a chart with no numbers) is rebuilt from US Treasury's official daily par yield CSV, appended to `exhibits.csv` and logged in `work/jaguar/sources.md`. Its 5-year values match the two labels printed on the chart.
- CFA readings unzipped only for the Essential/recommended modules, into `materials/cfa/` (gitignored).
- Web test: search worked from the start; fetch was blocked until the user opened the network, then worked.
