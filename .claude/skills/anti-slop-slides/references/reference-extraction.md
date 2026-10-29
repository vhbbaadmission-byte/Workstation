# Phase 0 — Reference Extraction (vision intake)

When the user attaches an image — a slide, a screenshot, a poster, a UI, any
design they like — read its design system out of the pixels and hand it to the
rest of the pipeline. This is what lets the deck *adopt a look you point at*
instead of inventing one.

Influenced by the `anydesign` and `analysis-screenshot` skills. The governing
principle is theirs: **values are sampled, roles are reasoned, and every inference
carries a confidence marker.** Never invent a hex.

---

## The one rule of extraction

**Vision hallucinates hex codes. Scripts don't.** So split the work:

- **Sampled (trust the script):** exact colors and their area share come from
  `assets/extract_palette.py`. Run it, use its hexes verbatim.
- **Reasoned (trust your eyes):** which sampled color is the accent vs. background,
  the type personality, the layout skeleton, the mood. Vision assigns roles to the
  sampled values and reads structure the script can't.

Tag every field you write with a confidence marker:
`✅ observed directly · ⚠️ inferred · ❓ guessed, ask the user`.

---

## Steps

1. **Run the sampler.** `python assets/extract_palette.py <image> --json`. It returns
   real swatches (hex + % + luminance + saturation), a dark/light/mid theme read,
   the aspect ratio, and whether it looks like a 16:9 slide. Take the hexes as-is.
2. **Assign roles with vision.** Look at the image and map the sampled swatches to
   `--bg`, `--bg-2`, `--fg`, `--muted`, `--accent` (+`--accent-2`), `--good/--warn`.
   The script's `role_guess` is a starting point — override it when your eyes
   disagree (it can't tell an accent used sparingly from a large colored panel).
3. **Read typography.** Serif or sans? Geometric or humanist? Display weight, body
   weight, letter-spacing on labels, the size jump from body to headline. Name two
   real fonts that match the feel (you cannot read the exact embedded font from a
   raster, so pick close matches and mark them `⚠️`).
4. **Read the composition.** Grid or free? Where does the eye enter? Full-bleed image
   or contained? Alignment (left/centered/split)? Whitespace density? Motifs (rules,
   kickers, oversized numerals, borders, glows)? This becomes the Phase 2 direction.
5. **Read the mood and the ONE thing.** One paragraph: what does this design *feel*
   like, and what is the single strongest move that makes it itself (the accent
   discipline, the type contrast, the bleed image, the flat editorial calm)?
6. **Write the sidecars.** Emit the extraction as `design.md` (schema below) plus the
   Phase-1 files `tokens.md`, `voice.md`, `mood.md` so Soul and the Phase 6 critiques
   consume them directly.

---

## design.md schema (7 sections — from anydesign)

```markdown
---
source: <path to the attached image>
theme: dark | light | mid
confidence: <overall ✅ / ⚠️ / ❓ mix>
---

## 1. TL;DR
One line: what this design is and the look we are adopting from it.

## 2. Visual Identity
Mood (one paragraph). The ONE brand thing. Voice adjectives if text is present.

## 3. Tokens
Palette as a CSS :root block using the SAMPLED hexes, each with its role and a
confidence marker. Type scale (heading font, body font, sizes, weights).

## 4. Components
What building blocks appear: cards, stat strips, tables, dividers, kickers, rules,
image treatment. Map each to a primitive in html-presentation-patterns.md.

## 5. Layout
Grid, alignment, whitespace density, where the eye enters, bleed vs. contained.

## 6. Reconstruction Notes
Concrete instructions to rebuild this look on the 1280x720 canvas: which layout
class, which primitives, how the accent is used, how images are tamed.

## 7. Do's / Don'ts
Guardrails pulled from the reference. Open questions to ask the user (❓ items).
```

---

## Handoff into the pipeline

- **→ Phase 1 (Soul):** the extracted `tokens.md` / `voice.md` / `mood.md` ARE the
  brand tokens. Skip the from-scratch build; confirm the `❓` items with the user.
- **→ Phase 2 (Reality):** the layout read in sections 4–6 IS the named composition
  direction. You usually do not need three previews — you have the target look.
  Still repaint with the sampled tokens, never copy the reference's content.
- **Copyright line:** adopt the *system* (color, type, layout language), not the
  reference's exact artwork, logos, or copy. If the image is a specific brand's
  slide, treat it as inspiration for structure, not a asset to reproduce.
