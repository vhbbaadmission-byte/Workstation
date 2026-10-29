# Phase 6 — Anti-Slop Adversarial Checklist

Run this as a bug hunt. Assume each item is broken until you have looked and
confirmed it is not. Fix, then run the whole list again. Loop until fully clean.

## Identity (Soul held the line)
- [ ] Palette matches the Phase 1 tokens exactly — no stray default indigo/violet,
      no color that was never declared in `:root`.
- [ ] Heading + body fonts are the declared pair, applied consistently.
- [ ] Accent color used with restraint, not on every element.
- [ ] Voice matches the brand adjectives; no banned phrase survived.

## Composition (Reality held the line)
- [ ] Layout is the named system from Phase 2, not a generic centered stack.
- [ ] No "accent rule bar under every single title" tic.
- [ ] Each slide says ONE thing; no slide is a wall of bullets.
- [ ] Numbers/comparisons are structured blocks (strips, tables, arcs), not prose.
- [ ] Whitespace is generous; type is large; primitives are reused, not reinvented.

## Icons (Power's no-reuse rule)
- [ ] ONE icon family across the whole deck.
- [ ] No icon appears twice. Keep the running used-icons list and diff it.
- [ ] Icon weight/color follows brand tokens. No default icon-in-a-circle motif
      unless it is a deliberate brand choice.

## Voice (Mind humanized)
- [ ] No AI vocabulary (delve, leverage, robust, seamless, elevate, unlock…).
- [ ] No rule-of-three padding, no negative parallelism ("not X, but Y"), no
      vague attributions ("studies show", "experts say").
- [ ] No em dashes in prose. No filler ("in today's fast-paced world").
- [ ] Headlines have a point of view, not a neutral summary.

## Substrate mechanics (Space)
- [ ] Nothing overflows the 1280×720 canvas (overflow past 720px is a bug).
- [ ] Page counters are derived in JS; `.count` spans are empty in HTML.
- [ ] No hardcoded slide numbers anywhere.
- [ ] Keyboard nav works (←/→/space/PageUp/PageDown, P prints).

## Print / PDF path
- [ ] `@page size` matches the slide dimensions (no scaling/crop).
- [ ] `print-color-adjust:exact` present — dark backgrounds print dark.
- [ ] `page-break-inside:avoid` per slide; no trailing blank page.
- [ ] On-screen chrome (nav help) hidden in print.

## Leftovers
- [ ] No placeholder text ("Lorem", "TODO", "[client]", initials boxes meant to
      be photos).
- [ ] No broken image/asset paths.
- [ ] Contrast is readable everywhere, including text over images.

When every box is checked on a fresh pass with no fixes needed, Time returns clean.
