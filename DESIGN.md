# Design rules

These are the user's rules. They override skill defaults **and the reference images**. Check every slide against them before showing it.

## The standard
**Claude Design level, not "a PowerPoint".** Think like a designer making a premium editorial deck, not like someone filling slide templates. Design happens in **Claude Slides** (see CLAUDE.md, gate 2). Every slide should look like it came out of Claude Design at its best: considered composition, generous space, a clear focal point, refined type. Then make it hold up as a `.pptx` on paper.

## Process
1. **Design from the references** in `design/references/` (open and study all three before gate 2).
2. **Then apply the `apple-design` skill as a polish pass** over that design. It's written for web UI, so use only the parts that apply to static slides: §12 materials and depth, §15 typography (optical size, tracking, leading), and §16 the design foundations (restraint, hierarchy, consistency). Skip its motion and gesture sections and its "Initial Response" greeting.
3. Then check the result against the rules below.

## References: what to take from them
| File | What it is | Take from it |
|---|---|---|
| `ref-1-bettertask-indigo.png` | Indigo/violet pitch deck | One-colour palette in tints (deep indigo → lavender) on white or off-white, with dark navy for impact slides. Huge numbers as heroes. Metric lists with thin rules and → arrows. Clean bar charts with faint gridlines. Green for up, red for down. |
| `ref-2-pilot44-overview.png`, `ref-3-pilot44-detail.png` | Editorial "Swiss" deck | Lime accent + black + sage grey + dark green on white. Lots of whitespace. Title top-left with content placed right or below. Tables with thin rules and a solid black header row. Stacked bar charts. Process flows with **square** boxes and arrows. Section numbers ("01"). Thin rule at the top, page number top-right. |

**What both share, and what to keep:**
- Big headlines in a **regular or light** weight (not bold), tight letter spacing, left-aligned, often over 2–3 lines
- One accent colour family plus neutrals; colour is used to point at the key thing
- Key numbers shown very large
- Thin hairline rules and simple → arrows instead of boxes
- A lot of empty space; few elements per slide

**Where the references break our rules (the rules win):**
- Ref 1's rounded cards, three-card bento row, rounded bars and rounded slide corners → use **square corners** and open layouts.
- Refs 2–3's small monospace running header above every title ("Innovate Smarter Grow Faster") → **leave it out.** A thin top rule and page number are fine.
- Both use small body text (captions around 10pt) → **18pt minimum** still applies. Get the airy look from whitespace and a few large elements, not from tiny text.
- Photos (ref 2) → only if they're real and relevant (JLR, the Bank of England, gilts). No stock people.

**Palette:** the references show two directions, **A: indigo** (ref 1) and **B: lime/black editorial** (refs 2–3). At gate 2, show the same sample slides in both, recommend one, and let the user choose. Don't mix them.

## Fonts
- Headlines and body: **Inter** (closest open font to the references). Numbers in tables and calculations: Inter with tabular figures. Section numbers can use **IBM Plex Mono**.
- The setup script installs both in the cloud, so contact sheets match the final deck.
- **At submission, the fonts must be embedded** or the professor's PC will swap them for Calibri. The user installs Inter and IBM Plex Mono and saves the final deck from PowerPoint with *File → Options → Save → Embed fonts*. Remind the user of this at gate 4.

## Slide basics
- 16:9 widescreen (13.333 × 7.5 in).
- **Titles state the point** in plain words, at most 2 lines: "JLR's cheaper debt came from better credit, not lower rates", not "Yield Analysis". Section dividers and the cover can use short titles.
- Every slide: title, slide number, and a source line when it uses data.
- **Footers** (source line, slide number) may be **12pt**. Everything else is at least 18pt. Footer shapes are named `footer…` so `check_deck.py` applies the 12pt floor to them.
- The cover has the case name, Group 10 and the course; the user will supply names and course details. The final slide holds each member's photo, full name and student ID (from the user; placeholder until then).

## Colour, contrast and print
The hard copy is printed one slide per page, possibly in greyscale. So:
- Text colour against its background must reach a **contrast ratio of at least 4.5:1** (3:1 for text 24pt and up).
- **Lime (direction B) is never a text colour** and never thin lines on white. Use it only as a fill behind black text or as a large shape.
- Pale tints (lavender on indigo, grey on sage) are for shapes, not text.
- Full dark backgrounds only for the cover and section dividers.
- Never carry meaning with colour alone: up/down also gets a sign (+/−) or an arrow, and chart series also differ by position or a direct label.
- Check every slide in greyscale before showing it.

## Don't
- **No small text above titles.** Don't put an eyebrow, kicker or small caps label above every slide title. The title stands on its own.
- **No rounded capsules or pills.** Where a label, tag or box is needed, use a plain **rectangle** (square corners). Use one only when it's needed.
- **Go light on bento boxes.** Don't default to grids of cards or tiles. Use them only when the content really is a set of equal, separate items. Prefer open layouts: charts, big numbers, step-by-step working, and text with whitespace.

## Charts
- **Check every chart's axis labels and legend.** Every axis has a title and units, the tick labels are readable, and the legend is present. Nothing is cut off, overlapping, covered by the chart, or too small to read (18pt minimum; this applies to chart text too). Check this on the rendered contact sheet, not just in the code.
- Style charts like the references: no chart border, faint or no gridlines, the accent colour on the series that matters and neutrals on the rest, and direct labels where they fit.

## Calculation slides
These make up a large part of the deck. Lay each one out as **formula → numbers plugged in → result**, with the result in large type and the accent colour. One step per slide if needed; never shrink text to fit.

## User design feedback, word for word
- 2026-10-29: "use lucidity is a very important factor. Can someone go into it and understand what the strength is and what is being said? Is it being understood? Even if the presenter was removed, would it still be understood? The slide, in the context of that, is lucid if someone with a very basic understanding would understand what's being said. I think, in your current context, there is a bit of lucidity. Lucidity does not mean removing stuff or removing complex analysis. It just means ensuring that they are shown or explained clearly. For any helpers, this and feature content are very major criteria."
  → **Lucidity rule:** every slide must be understood by a reader with basic finance and no presenter. Never cut analysis to achieve it. Instead: define each term the first time it appears (one plain line), say in words what each formula means before the numbers, label every number with what it is and its unit, end each calculation with a one-line "so what", and put the slide's point in its title.
- 2026-10-29: "as for the designs ensure you use the claude design style workflow to achieve that levle of quality and accuracy" → gate 2 is designed in the Claude Slides artifact following its own design workflow (direction → palette/type scale → layouts → slides), not hand-built in code.

## Still to come from the user
Anything else: logo, extra examples, more do's and don'ts. Gate feedback gets added here.
