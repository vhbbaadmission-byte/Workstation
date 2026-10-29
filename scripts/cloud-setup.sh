#!/bin/bash
# Installs what the skills need. Runs only in cloud sessions; safe to re-run.
[ "$CLAUDE_CODE_REMOTE" = "true" ] || exit 0

python3 -c "import pptx, markitdown, matplotlib, openpyxl, PIL" 2>/dev/null ||
  pip install -q python-pptx lxml 'markitdown[all]' matplotlib openpyxl Pillow

# LibreOffice + poppler turn .pptx into PNGs so slides can be looked at (contact sheets).
command -v soffice >/dev/null && command -v pdftoppm >/dev/null ||
  { apt-get update -qq && apt-get install -y -qq libreoffice-impress poppler-utils fonts-liberation; }
exit 0
