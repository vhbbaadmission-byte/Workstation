---
name: anti-slop-slides
version: 1.2.0
description: |
  Build premium, on-brand HTML slide decks (and PPTX-ready pages) that do NOT
  look like default-AI slop. Runs a fixed six-phase "Infinity Gauntlet" pipeline
  — Soul (brand identity), Reality (composition), Space (substrate/build),
  Power (icon discipline), Mind (humanized voice), Time (adversarial QA) — over
  a self-contained 1280x720 fixed-canvas, print-to-PDF HTML deck.

  If the user attaches a photo, slide, design, UI screenshot, or any image they
  like, a Phase 0 (Vision) fires first: it pixel-samples the real colors
  (assets/extract_palette.py), assigns roles with vision, reads typography and
  composition, and hands the extracted design system to Soul and Reality so the
  deck adopts the referenced look instead of inventing one.

  Use whenever the user wants slides, a pitch deck, a presentation, an HTML deck,
  or to convert content into premium slides — with or without a reference image.
  Trigger: /anti-slop-slides or requests for "slides", "deck", "presentation" that
  should look designed; or when any image is attached alongside slide/deck content.
license: MIT
compatibility: claude-code opencode
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - AskUserQuestion
  - Skill
---

# Anti-Slop Slides — the Infinity Gauntlet pipeline

## What this is

A single skill that produces slide decks which do not read as default-AI slop.
Everyone has the commodity `pptx` / `frontend-design` skills, so everyone ships
the same look: same palette, icon-in-a-circle, rule-of-three cards, serif-over-
sans. This skill treats the commodity substrate as dumb geometry and wraps it in
five discipline stations that inject **identity, composition, icon rigor, voice,
and adversarial QA**.

The default output is a **single self-contained `.html` file**: fixed 1280×720
slides, embedded `<style>`/`<script>`, no build step, prints to a pixel-clean PDF.
See `references/html-presentation-patterns.md` for the full medium model — read it
before building. Start from `assets/deck-template.html`.

## The one rule

**System-first.** Establish identity before generating anything. When no system
is supplied, every model run collapses to the same safe default — that collapse
*is* the slop. So the phases are ordered and you do not skip or reorder them.

## Announce each phase as you enter it. Do not skip. Do not reorder.

**Phase gate:** before starting any phase, confirm the previous phase's output
actually exists (tokens block written, composition chosen, deck file present, etc.).
If it does not, go back and finish it. This is the fix the plan calls for when Claude
skips steps — be prescriptive, do not assume a phase happened.

---

## Phase 0 — Vision (reference intake)  ·  fires only when an image is attached

**Trigger:** the user attaches any image — a slide they like, a UI screenshot, a
poster, a brand swatch, any design they point at. If no image is attached, skip
Phase 0 and start at Phase 1.

Full methodology is in `references/reference-extraction.md`. Summary:

1. **Run the pixel sampler.** Execute:
   ```
   python "~/.claude/skills/anti-slop-slides/assets/extract_palette.py" <image_path> --json
   ```
   Use the hex values verbatim — they are sampled pixels, not guesses. Never invent
   a hex. If Pillow is not installed, ask the user to `pip install Pillow` once.

2. **Assign roles with vision.** Look at the image and map each sampled swatch to
   a CSS token role: `--bg`, `--bg-2`, `--fg`, `--muted`, `--accent` (+ `--accent-2`),
   `--good`/`--warn`. The script's `role_guess` is a starting point — override when
   your eyes disagree (it cannot tell a sparse accent from a large panel).

3. **Read typography.** Serif or sans? Geometric or humanist? Display weight,
   body weight, letter-spacing on labels. Pick two real font names that match the
   feel; mark them `⚠️` (you cannot read exact embedded fonts from a raster).

4. **Read composition.** Grid or free? Full-bleed or contained? Alignment? Whitespace
   density? Motifs (rules, kickers, oversized numerals, borders, glows)? Name the
   layout pattern. This becomes Phase 2's named composition direction.

5. **Read mood + ONE thing.** One paragraph on what the design feels like and the
   single strongest move that makes it itself.

6. **Write the outputs.** Produce:
   - `design.md` — the full 7-section extraction (schema in `references/reference-extraction.md`)
   - `tokens.md` — palette as a CSS `:root` block using sampled hexes + type scale
   - `voice.md` — voice adjectives + banned phrases inferred from the reference's tone
   - `mood.md` — the mood paragraph from step 5

   Tag every field: `✅ observed · ⚠️ inferred · ❓ guessed, ask user`.
   Ask the user to resolve `❓` items before moving on.

**Copyright line:** adopt the *system* (color, type, layout language), not the
reference's exact artwork, logos, or copy. If the image is a specific brand's
asset, treat it as inspiration for structure, never reproduce it.

**Handoff:**
- → Phase 1: tokens are already in `tokens.md`/`voice.md`/`mood.md`. Skip the
  from-scratch build; confirm `❓` items only.
- → Phase 2: the layout read in step 4 IS the named composition direction. Skip
  the three-preview pick — commit to the direction and say which and why.

---

## Phase 1 — Soul (identity)  ·  kills the "everyone's deck" look

Establish brand tokens BEFORE anything renders. Produce a tokens block that all
later phases obey.

**If Phase 0 ran:** `tokens.md`, `voice.md`, and `mood.md` already exist from the
reference extraction. Do NOT rebuild from scratch. Instead: read those three files,
confirm any `❓` items with the user (one AskUserQuestion with only the open items),
then proceed. The Phase 0 sidecars are the Soul output.

**If Phase 0 did not run:**

1. If the user named a client/brand with existing tokens, load them. If the
   `brand-guidelines` skill or a `brand-<client>` skill is installed and relevant,
   invoke it via the Skill tool to pull real tokens.
2. If no tokens exist, build them now — ask only what you cannot infer:
   - **Palette**: background(s), foreground, muted, ONE accent (+ optional accent-2),
     good/warn. Avoid the default indigo/violet SaaS gradient unless the brand is
     actually that.
   - **Type**: one heading font, one body font. Weight carries hierarchy, not a
     dozen sizes.
   - **Voice**: 2–3 adjectives, and a **banned-phrases list** (AI vocabulary,
     rule-of-three padding, "in today's fast-paced world", em dashes in prose).
3. Emit the tokens as a CSS `:root` block (matches the template's token contract).
4. Also persist the identity as small sidecar files next to the deck so Phase 6's
   critique skills can read them: `tokens.md` (palette + type scale), `voice.md`
   (voice adjectives + banned phrases), and `mood.md` (one paragraph on the intended
   feel). `critique-brand-consistency` expects exactly these three files.

**Arbitration:** on color / type / voice, Soul always wins. Non-negotiable.

Ask the user for missing identity inputs using AskUserQuestion when it materially
changes the output (e.g. brand vs. no brand, dark vs. light, accent color).

---

## Phase 2 — Reality (composition)  ·  kills same-layout sameness

Choose ONE named composition system compatible with the brand — never a default.

**If Phase 0 ran:** the composition direction was named in step 4 of the reference
extraction (sections 4–6 of `design.md`). Commit to it directly — state which
direction it is and why. Do NOT generate three previews; the reference image already
made the choice. Still repaint with the sampled Phase 1 tokens; never copy the
reference's actual content or artwork.

**If Phase 0 did not run:**

1. Pick a direction with intent (e.g. dark editorial, brutalist grid, warm
   print-magazine, technical/monospace, high-contrast Swiss). Name it out loud.
2. **Generate three title-slide previews in distinct directions** (per the plan),
   each painted with the Phase 1 tokens — build them as three real `.slide` blocks
   in a scratch HTML file, then present them and wait for the user to pick one.
   Use AskUserQuestion with a short preview of each. If the user already gave a
   strong steer, commit to one and say which and why instead of generating three.

**Both paths:**

3. **Composition only.** If you borrow a template's skeleton (e.g. from
   `frontend-slides`), strip its palette and repaint with Phase 1 tokens. A slide
   says ONE thing; numbers become structured blocks (strips, tables, arcs), not prose.

**Arbitration:** on layout / motif / whitespace, Reality wins. If a template
fights the brand palette, keep the layout skeleton, throw away its colors.

---

## Phase 3 — Space (substrate)  ·  geometry and file mechanics only

Generate the artifact. The substrate makes no surface decisions — those come from
Phases 1 and 2.

- **Default path (recommended):** copy `assets/deck-template.html`, wire in the
  Phase 1 `:root` tokens and Phase 2 composition, then author slides from the
  component vocabulary in `references/html-presentation-patterns.md`
  (`.section-divider`, `.thesis`, `.stat-strip`, tables, `.card` + modifiers,
  `.timeline-3`, `.footer-strip`). Reuse primitives; do not invent bespoke boxes.
- **If the user wants HTML with more scaffolding:** the installed `frontend-slides`
  skill is available via the Skill tool — use it for the substrate, but still feed
  it Phase 1 tokens and repaint any template palette.
- **If the user explicitly wants PPTX:** produce the HTML deck first (it prints to
  a clean 16:9 PDF), or invoke the `anthropic-pptx` substrate (official python-pptx
  skill) via the Skill tool — use `Mck-ppt-design-skill` instead when a
  McKinsey/consultant chart-heavy look is wanted. Still governed by Phases 1–2.

Non-negotiable substrate rules (from the field notes): fixed 1280×720 with
`overflow:hidden`; `@page size` matches slide size; `print-color-adjust:exact`;
`page-break-inside:avoid`; derive page counters in JS (never hand-number);
keyboard nav (←/→/space, P to print).

---

## Phase 4 — Power (icons)  ·  kills lucide-everywhere reuse

Commit to ONE icon family for the whole deck. **No icon may appear twice.** Map
each icon semantically to its slide. Family weight and color follow Phase 1 tokens.

The strongest anti-slop move here is a **bespoke family, not a library lookup**:
invoke the `icon-set-generator` skill via the Skill tool to produce project-specific
SVG icons built from one shared style spec (same stroke weight, corner treatment,
density) — this defeats the "Lucide everywhere" tell outright. Feed it the Phase 1
tokens so weight and color match the brand.

If you cannot guarantee no-reuse, prefer no icons over reused icons — restraint
reads as premium. Track used icons in a list as you place them.

**Arbitration:** Power defers to Soul for family weight and color, but owns the
no-reuse rule absolutely — no phase overrides it.

---

## Phase 5 — Mind (voice)  ·  kills machine phrasing

Humanize every headline and body line. If the `humanizer` skill is installed,
invoke it via the Skill tool on the deck's copy. Otherwise apply its rules
directly: remove AI vocabulary, rule-of-three padding, negative parallelisms,
vague attributions, filler, and **em dashes in prose**. Match the Phase 1 voice
notes and honor the banned-phrases list. A headline should sound like a person
with a point of view, not a summary.

---

## Phase 6 — Time (verification)  ·  the catch loop

Run an ADVERSARIAL critique with fresh eyes. Assume there ARE problems and hunt
them — this is a bug hunt, not a confirmation pass. Work through
`references/anti-slop-checklist.md`. Common kills: reused icons, off-brand color,
generic layout, low contrast, accent line under every title, leftover placeholder
text, content overflowing 720px, rule-of-three prose, hardcoded page numbers.

For a real visual pass (not just reading the source), screenshot each slide, then
invoke the installed critique skills via the Skill tool against those images. Run
the ones that matter for a deck, in this order:

1. `critique-visual-hierarchy` — entry point, eye flow, emphasis
2. `critique-composition` — balance, whitespace, rhythm
3. `critique-typography` — scale, readability, token compliance
4. `critique-color` — contrast ratios, palette coherence, accessibility
5. `critique-information-density` — cognitive load, one-idea-per-slide
6. `critique-brand-consistency` — checks the deck against the `tokens.md`,
   `voice.md`, and `mood.md` you wrote in Phase 1
7. `critique-affordance` — only if the deck has interactive/nav elements

Capture the screenshots with the `webapp-testing` (Playwright) skill. On Windows,
LibreOffice-based PPTX QA is unavailable — serve and critique the rendered HTML
instead (per the plan's Windows note).

For true fresh eyes (the plan's open question on Time), you may instead hand the
screenshots and checklist to a fresh-context subagent so the critique is not
anchored on the choices you just made. Either path is fine; the subagent is simpler
to wire, the in-line critique loop retries more cleanly.

Fix everything found, then re-run the checklist and the critiques. **Loop until it
returns clean.** Verify the print/PDF path (dark backgrounds print dark, no trailing
blank page).

---

## Cost tiers — match effort to stakes

- **Full gauntlet** (all six phases): client-facing, high-stakes decks.
- **Lite gauntlet** (Soul → Space → Mind): internal docs where identity and clean
  prose matter but composition experimentation does not.
- **Substrate only** (Space): throwaway drafts where slop is acceptable.

Default to the full gauntlet unless the user signals it's low-stakes.

## Files in this skill

- `assets/deck-template.html` — ready starter implementing every substrate rule.
- `assets/extract_palette.py` — pixel sampler for Phase 0. Run `python extract_palette.py <image> --json`. Returns real hex swatches, area share, luminance, saturation, theme, and role guesses. Requires Pillow (`pip install Pillow`).
- `references/html-presentation-patterns.md` — the medium model. Read before building.
- `references/anti-slop-checklist.md` — the Phase 6 adversarial checklist.
- `references/reference-extraction.md` — Phase 0 methodology: 6-step extraction process, 7-section `design.md` schema, and handoff rules into Phases 1 and 2.

## Companion skills (the six stones)

This skill is the orchestrator; it invokes these installed skills per phase via the
Skill tool. It still works standalone if any are missing — it falls back to its own
bundled template, rules, and checklist.

| Phase | Stone | Companion skill(s) — all installed | Fallback if absent |
|-------|-------|--------------------|--------------------|
| 0 Vision | reference intake | `assets/extract_palette.py` (pixel sampler, built-in) | skip Phase 0 if no image attached |
| 1 Soul | identity | `brand-guidelines` (or a `brand-<client>` fork) | build tokens inline (or use Phase 0 sidecars) |
| 2 Reality | composition | `frontend-slides`, `frontend-design` | choose a named system by hand (or use Phase 0 layout read) |
| 3 Space | substrate | `frontend-slides` (HTML) · `anthropic-pptx` / `Mck-ppt-design-skill` (PPTX) | `assets/deck-template.html` |
| 4 Power | icons | `icon-set-generator` (bespoke SVG family) | one library family, no reuse |
| 5 Mind | voice | `humanizer` | apply its rules inline |
| 6 Time | verification | `critique-visual-hierarchy`, `critique-composition`, `critique-typography`, `critique-color`, `critique-information-density`, `critique-brand-consistency`, `critique-affordance` + `webapp-testing` (screenshots) | `references/anti-slop-checklist.md` |

Every companion above is installed in `~/.claude/skills/`. The pipeline names each
one explicitly so Claude follows the order rather than guessing — that naming is
what keeps selection accurate even past the ~15-skill ceiling the plan warns about.
