# HTML Presentation Patterns — Field Notes

Working reference distilled from building and editing self-contained HTML decks
(e.g. the RNP × Pushkang dealership deck). These are the patterns that make an
HTML file behave like a real, print-ready slide presentation rather than a web
page. A skill can lean on this as its mental model for the medium.

---

## 1. Core model: fixed-canvas slides, one file

The whole deck is **one self-contained `.html` file** — embedded `<style>` and
`<script>`, no build step, no framework. It opens in any browser and prints to
PDF directly. This is the single most important property: portability. Treat it
as the default unless told otherwise.

Each slide is a **fixed-size box**, not a fluid layout:

```css
.slide{ position:relative; width:1280px; height:720px; overflow:hidden; }
```

- **1280×720** is the 16:9 working canvas. Everything is authored to fit inside
  it exactly. Nothing reflows — if content overflows 720px, it's a bug, not a
  scroll.
- Slides stack vertically down the page with a gap, so the whole deck scrolls as
  one column of "cards" on screen.
- `overflow:hidden` on the slide is what lets bleed backgrounds and off-canvas
  glows sit safely without spilling.

**Implication for editing:** every change is a fit problem. Adding a row means
something else has to give (padding, font-size, a `justify-content` change).
Never assume vertical space is free.

---

## 2. Print-to-PDF is a first-class output, not an afterthought

The deck is designed so `window.print()` produces a pixel-clean PDF, one slide
per page. This is usually the *actual deliverable*. The rules that make it work:

```css
@page { size: 1280px 720px; margin: 0; }
@media print {
  *{ -webkit-print-color-adjust:exact !important; print-color-adjust:exact !important; }
  html,body{ background:#000; padding:0; margin:0; }
  body{ display:block; }
  .slide{ box-shadow:none; page-break-after:always; page-break-inside:avoid; margin:0; }
  .slide:last-of-type{ page-break-after:auto; }
  .nav-help{ display:none; }
}
```

Non-negotiables learned here:
- **`print-color-adjust:exact`** or dark backgrounds print white. Every time.
- **`@page size` must match the slide dimensions** or you get scaling/cropping.
- **`page-break-inside:avoid`** per slide, `page-break-after:always`, and clear
  it on `:last-of-type` to avoid a trailing blank page.
- Hide on-screen chrome (nav help, hints) in print.

If a design looks right on screen but wrong in the PDF, the cause is almost
always one of these four.

---

## 3. Design tokens up top; three type sizes do the work

Everything theming-related is a CSS custom property in `:root`. Editing the deck
means touching tokens, not hunting hardcoded values.

```css
:root{
  --bg:#0a0a0a; --bg-2:#111; --bg-3:#161616;
  --line:rgba(255,255,255,.08); --line-2:rgba(255,255,255,.14);
  --fg:#fff; --muted:#a5a5a5; --dim:#6f6f6f;
  --accent:#d3381c; --accent-2:#ff6a3d;
  --good:#3ecf8e; --warn:#e0b341;
}
```

Type scale is intentionally **small — a few sizes, and font-weight carries the
hierarchy** rather than a dozen sizes:

- `.kicker` / `.eyebrow` — 11px, uppercase, wide letter-spacing (`.22em`),
  accent or muted. The label above a headline.
- `.title` 40px / `.title-lg` 56px / `.mega` 72px — the three headline tiers.
- `.sub` 18px muted, `.body` / `.t-body` 15–16px, `.caveat` 12px italic.
- A **`.rule`** (56px × 2px accent bar) and the accent color are the two main
  "this matters" signals. Used sparingly.

Lesson: restraint reads as premium. New content should reuse an existing type
class, not introduce a new size.

---

## 4. Layering discipline (z-index is a fixed contract)

Every slide has the same stacking contract, which keeps backgrounds, decorative
overlays, and content from fighting:

- `z-index:0` — backgrounds (`.bg-dark`, `.bg-flat`, bleed images, gradients)
- `z-index:1` — the global faint grid overlay (`.slide::before`)
- `z-index:2+` — content (`.pad`, `.footer-strip`)

The `.pad` is the content frame: `position:absolute; inset:0;
padding:56px 72px 72px; display:flex; flex-direction:column`. Almost all slide
content lives inside one `.pad`, and vertical rhythm is controlled with
`justify-content` (`space-between`, `space-evenly`, `center`) rather than manual
margins. This is the main lever for making a slide "sit" correctly.

---

## 5. A component vocabulary, reused across slides

The deck is really a small library of block primitives. New slides are
assembled from these, not designed from scratch. The recurring ones:

| Primitive | Purpose |
|---|---|
| `.section-divider` | Chapter break: giant numeral + label + title + lede |
| `.thesis` | One big statement slide; oversized headline + support line |
| `.stat-strip` | 4-cell horizontal band of big-number stats |
| `.cmp-table` / `.data-table` / `.risk-table` | Structured comparison tables |
| `.matrix` | Claim ↔ evidence two-column rows |
| `.two-col` / `.grid-3` / `.grid-4` | Column and card grids |
| `.card` (`.is-key`, `.is-flush`) | The one generic box primitive |
| `.timeline-3` / `.gate-list` | Sequenced steps / numbered stages |
| `.callout` / `.open-q` | Highlighted single statements |
| `.footer-strip` | Per-slide footer: progress motif + page counter |

**One-card principle:** there's a single `.card` primitive with modifier
classes (`.is-key` = accent border, `.is-flush` = borderless) rather than many
bespoke boxes. Prefer extending a primitive with a modifier over inventing new
CSS.

Layout variants are also just classes on `.slide`:
`.layout-right`, `.layout-split`, `.layout-quiet` — each rewrites `.pad`
padding/alignment. Reach for these before writing inline layout overrides.

---

## 6. Never hand-number slides — derive counters in JS

Page counters and progress indicators are computed at load, so inserting or
deleting a slide never desyncs numbering:

```js
const all = document.querySelectorAll('.slide');
const total = all.length;
all.forEach((s, i) => {
  const cnt = s.querySelector('.footer-strip .count');
  if (cnt) cnt.textContent = `${String(i+1).padStart(2,'0')} / ${String(total).padStart(2,'0')}`;
});
```

Corollary: leave the `.count` span **empty** in the HTML. Any hardcoded number
is a lie waiting to happen. (The stage-motif dots in the footer *are* manual per
slide — those mark which chapter you're in, not the page number.)

---

## 7. Keyboard navigation for presenting

Minimal, expected controls make on-screen presenting usable:

```js
// ← / → / space / PageUp / PageDown move between slides (scrollIntoView, centered)
// P triggers window.print()
```

The "current slide" is found by whichever slide center is nearest the viewport
center — robust to the scroll-column layout. A small fixed `.nav-help` chip
documents the keys and is hidden in print.

---

## 8. Imagery: bleed, tint, and grayscale for cohesion

Photos are used as **atmospheric backgrounds**, not inline figures, and always
tamed so they don't fight the type:

- Absolutely-positioned full-bleed layer at `z-index:0`, `background-size:cover`.
- Knocked back with `opacity:.3–.55` **plus** `filter:grayscale() contrast()`.
- A **gradient scrim** on top (`linear-gradient(90deg, #0a0a0a 94% → transparent)`)
  so headline text stays readable over any image.
- Accent color re-introduced via a `radial-gradient` glow, not via the photo.

Real product/portrait images that need to read true (e.g. device shots, team
photos) go in bordered containers (`.pk-device .photo`, `.person .photo`) with
`object-fit:contain`/`cover` — grayscale is dialed *down* for faces.

Assets live in a sibling `slides-assets/` folder referenced by absolute path
(`/slides-assets/...`), which matters when the file is served from a `public/`
root rather than opened via `file://`.

---

## 9. Editing lessons (things that bit, so they don't again)

- **Serving vs. `file://`.** Absolute asset paths (`/slides-assets/...`) only
  resolve when served from that web root. If a Vite/dev server won't boot (Node
  version mismatch, ESM config errors), a plain static server on the `public/`
  folder (`python -m http.server`) is the fastest reliable way to preview.
- **Placeholders → real images.** Swapping an initials-box placeholder for a
  photo is just moving from a flex-centered text div to
  `background-image:url(...)` on the same `.photo` box — the sizing is already
  defined by the class, so don't re-specify height inline.
- **Reordering people/items** is pure DOM order; the `.is-key` accent modifier
  is what marks "first / most important," so move the modifier, not just the
  block.
- **Every insert is a subtraction somewhere.** On a fixed 720px canvas, adding a
  table row or a team member means reducing padding, dropping a font size, or
  switching the container's `justify-content`. Check the whole slide fits after
  any addition.
- **Match the surrounding idiom.** The file mixes a token/utility system with
  targeted inline `style=""` overrides for one-off spacing. Follow whichever the
  neighboring slide uses rather than imposing a new convention.

---

## 10. What "good" looks like here

The deck's aesthetic is deliberate and worth preserving when extending it:

- Dark, flat, editorial. One accent color used with restraint.
- Faint 80px grid as texture; no drop shadows or skeuomorphism on content.
- Generous whitespace; a slide says **one** thing.
- Numbers and comparisons rendered as structured blocks (strips, tables,
  waterfalls, arcs), not prose.
- Consistent footer, consistent chapter-divider rhythm, consistent type scale —
  the repetition is what makes 35 slides feel like one document.

When in doubt: fewer elements, larger type, more space, reuse an existing
primitive.
