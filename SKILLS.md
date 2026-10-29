# Skills for this project

Cloud sessions (claude.ai/code) only see skills committed to `.claude/skills/`, plus skills turned on in your claude.ai account. Plugins and skills that only live on your PC are not loaded.

## In this repo (`.claude/skills/`)

| Skill | What it does here | Source | License |
|---|---|---|---|
| `mck-ppt-design` | Builds consulting-style .pptx with python-pptx: layouts, charts, tables | [likaku/Mck-ppt-design-skill](https://github.com/likaku/Mck-ppt-design-skill) | Apache-2.0 |
| `pptx-author` | Writes a .pptx file headless (no PowerPoint app) | [anthropics/financial-services](https://github.com/anthropics/financial-services) (40k★) | Apache-2.0 |
| `ib-check-deck` | QC pass: same number on every slide, numbers match the story, wording, formatting | [anthropics/financial-services](https://github.com/anthropics/financial-services) | Apache-2.0 |
| `anti-slop-slides` | Design rules so slides don't look AI-made; can copy a look from a reference image | Your own skill | — |
| `humanizer` | Strips AI-sounding phrasing from slide text and notes | [blader/humanizer](https://github.com/blader/humanizer) (62k★) | MIT |
| `markitdown` | Turns the case PDFs, Word, Excel and PPT files into readable text | [microsoft/markitdown](https://github.com/microsoft/markitdown) (192k★) | MIT |

## Turn on in claude.ai (can't be copied here)

Anthropic's own **pptx**, **xlsx**, **docx** and **pdf** skills are licensed so they can't be copied into a repo. Turn them on in claude.ai → Settings → Capabilities → Skills, and cloud sessions load them automatically.

## Looked at and left out

- `frontend-slides`, `impeccable`, `ui-ux-pro-max`: they produce HTML/web UI, but the deliverable must be .pptx.
- LSEG bond skills (in anthropics/financial-services): they need a paid LSEG data connection.
- Superpowers (brainstorming/plans): its approval steps will be written into this project's own workflow instead.

## Tools the setup script installs

`scripts/cloud-setup.sh` runs at the start of each cloud session. It installs python-pptx, markitdown, matplotlib, openpyxl, Pillow, and LibreOffice + poppler, which render slides to PNG so they can be reviewed as contact sheets. To make sessions start faster, paste the same script into your cloud environment's **Setup script** box; that result is cached.
