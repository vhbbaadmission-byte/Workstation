# Design rules

These are the user's rules. They override skill defaults **and the reference images**. Check every slide against them before showing it.

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
- Every slide: title, a slide number, and a source line when it uses data. The cover has the case name, Group 10, and the course; ask the user for names and course details at gate 0.

## Don't
- **No small text above titles.** Don't put an eyebrow, kicker or small caps label above every slide title. The title stands on its own.
- **No rounded capsules or pills.** Where a label, tag or box is needed, use a plain **rectangle** (square corners). Use one only when it's needed.
- **Go light on bento boxes.** Don't default to grids of cards or tiles. Use them only when the content really is a set of equal, separate items. Prefer open layouts: charts, big numbers, step-by-step working, and text with whitespace.

## Charts
- **Check every chart's axis labels and legend.** Every axis has a title and units, the tick labels are readable, and the legend is present. Nothing is cut off, overlapping, covered by the chart, or too small to read (18pt minimum; this applies to chart text too). Check this on the rendered contact sheet, not just in the code.
- Style charts like the references: no chart border, faint or no gridlines, the accent colour on the series that matters and neutrals on the rest, and direct labels where they fit.

## Calculation slides
These make up a large part of the deck. Lay each one out as **formula → numbers plugged in → result**, with the result in large type and the accent colour. One step per slide if needed; never shrink text to fit.

## Still to come from the user
Anything else: logo, extra examples, more do's and don'ts. Gate feedback gets added here.
