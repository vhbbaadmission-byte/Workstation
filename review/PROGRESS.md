# Progress

Read this at the start of every session. Update it at every gate and after every piece of user feedback.

## Status
| | Jaguar | UK Gilts |
|---|---|---|
| Current gate | 1 — round 3 plan done; strict review not yet READY | 1 — round 3 fixes applied; strict review r3 said A− once fixed |
| Last approved | Gate 0 (2026-10-29) | Gate 0 (2026-10-29) |

Shared gate 2 (look): not started · Build tool: not decided · Claude Slides link: https://claude.ai/artifact/FDSxNWFitiAfajUBNh6h5X (created empty at gate 0 as the tool test; used at gate 2)

## Next step
Session paused for handover (user, 2026-10-30). The next session:
1. Read `HANDOVER.md`, then this file, CLAUDE.md and DESIGN.md.
2. Run the strict review (`grader` with `review/shared/review-rubric.md`) on `review/gilts/01-storyline.md` (round 4) and `review/jaguar/01-storyline.md` (round 3). Fix and repeat until both are READY.
3. When both are READY, gate 1 counts as approved (user's delegated approval) → start gate 2 (the look) in the Claude Slides artifact.

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
- 2026-10-30: "These agents have completely completed their work. Stop and repackage this entire thing into a zip file that I can later hand over to Claude, CoWork, and similar structures, and they can continue from there. Do not continue after the agents have output. Once agents have given their comments, update the plans accordingly and create a handover zip with all of the information, all of the progress, and all the details, and that's it. Hand it over to CoWork, and let me know on Zabbix and give me the link to it." → After the running helpers (Gilts strict review r3, Jaguar sources round 3) report: apply their comments to the plans, build a handover zip, stop. No further review rounds in this session.
- 2026-10-29: "Basic finance, as in they have a basic understanding of, let's say, CFA Level 1 or close to it, but not really complete. Someone is studying for it, not really basic finance. If that is what basic finance means, they should understand what's going on. Again it does not mean making the analysis too simple, making it element-free, or removing any key analysis that should be done. It does not mean that. You have to complete all the analysis for the professional role that you're asked to do but present them with lucidity so that it's easier to understand." → Lucidity reader = a CFA Level 1 candidate part-way through their studies. Full professional analysis stays; presentation must let that reader follow every step.
- 2026-10-29: "use lucidity is a very important factor. Can someone go into it and understand what the strength is and what is being said? Is it being understood? Even if the presenter was removed, would it still be understood? The slide, in the context of that, is lucid if someone with a very basic understanding would understand what's being said. I think, in your current context, there is a bit of lucidity. Lucidity does not mean removing stuff or removing complex analysis. It just means ensuring that they are shown or explained clearly. For any helpers, this and feature content are very major criteria." → Lucidity is a hard pass/fail criterion for every reviewer and every slide: a reader with only basic finance, and no presenter, must understand each slide's point. Keep the full complexity; explain it clearly.
- 2026-10-29 (gate 1, conditional approval): "It is approved from my end, given that the helpers agree that this is a good form. When you assign the helpers, make sure that you give them tough criteria and you explain to them what they need to do. The helpers are issued on that level, on a very sophisticated level, keeping all the restrictions and everything in mind. If they approve it, it is approved from my side. If they approve it, as soon as it's approved, move on to the next stage." → Gate 1 is approved once the independent reviewers (strict brief) pass both storylines; then go straight to gate 2. Standing rule: every helper brief carries tough, explicit pass/fail criteria and all project restrictions.
- 2026-10-29: "did uRun like a secondary helper, an independent agent, to check your plan and approve it."
- 2026-10-29: "what do i approve" / "do you have the city group and nesa slides?"
- 2026-10-29 (gate 1 questions, chosen): Bond date = "Case date + one note (Recommended)" → use 15 May 2021, one slide notes the filing's 15 Nov 2021 (naive value 125.43 → 127.26; answer unchanged). Repeats = "One slide each (Recommended)" → every repeated calculation gets its own slide (formula → numbers → result).
- 2026-10-29: "anything to approve?"
- 2026-10-29: "approved" → gate 0 approved for both cases.
- 2026-10-29: "I'm happy with all of that for now. Let's move on to the next"
- 2026-10-29: "I have connected with GitHub. Next time, when you ask me questions like "Your language was too complex for me," for now, even make a guess. I'm guessing what you said was right and accurate. Whenever you have questions for me next, keep the language as simple as possible, and make your explanations bigger and more simple so that I can understand what the implications are and what could have" → Rule: every question to the user uses very simple words, explains longer and more plainly what each choice means and what happens if they pick it, and avoids finance jargon (or explains it).
- 2026-10-29 (gate 0 questions, answered by choice): Jaguar Q2 = "Call-aware first (Recommended)"; Currency = "US$, convert once (Recommended)"; Gilts basis = "Annual + 1 comparison (Recommended)"; Gilt names = "Name only if certain (Recommended)". Also: "Ask them a question with choices. Remember to see the repercussions: why this question arose, what my options are, and what the repercussions are for the options. As for GitHub, it is connected." → From now on, put questions to the user as multiple-choice, each saying why it arose and what each option leads to.
- 2026-10-29 (gate 0, after network test): "you have full network access now , as for the designs ensure you use the claude design style workflow to achieve that levle of quality and accuracy"
- 2026-10-29 (start of gate 0): "session branch is fine, both" — push to `claude/eloquent-cray-g3ajd9` instead of `main`; run gate 0 for both cases in this session.

## Decisions made without asking (show these at the next gate)
- Gate 1: no Gilts bond matches a real gilt with certainty → case labels kept (user rule).
- Gate 1: Exhibit 1 (Gilts) described as a teaching set; yields ~1 point above the real 9 May 2014 market (DMO data).
- Gate 1: JLR call price taken as 104.0625 (reproduces the published tender price); the OM's "104.663%" treated as a misprint.
- Gate 1: Jaguar Q3 adds an after-tax version at the UK 20% rate; Q1's level/tenor split shown as one 158bp block (the order changes the split).
- Gate 1: grader suggestions accepted except Gilts "non-parallel shift" (one line only); reasons in each storyline.
- Work on branch `claude/eloquent-cray-g3ajd9` (user: "session branch is fine").
- `exhibits.csv` = extractor B's file for both cases. Extractor A agreed on every value; A's raw file is kept as `exhibits_A.csv`.
- Jaguar Exhibit 3 (a chart with no numbers) is rebuilt from US Treasury's official daily par yield CSV, appended to `exhibits.csv` and logged in `work/jaguar/sources.md`. Its 5-year values match the two labels printed on the chart.
- CFA readings unzipped only for the Essential/recommended modules, into `materials/cfa/` (gitignored).
- Web test: search worked from the start; fetch was blocked until the user opened the network, then worked.
