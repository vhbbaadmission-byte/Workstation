---
name: markitdown
version: 1.1.0
description: Convert files/URLs to Markdown via Microsoft MarkItDown. Supports PDF, Word, PPT, Excel, images, audio, HTML, YouTube, CSV, JSON, XML, ZIP, EPub.
license: MIT
compatibility: claude-code opencore
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, AskUserQuestion]
---

# MarkItDown Skill

Convert any file or URL to Markdown using `markitdown`.

## Install
```bash
pip install 'markitdown[all]'   # Python 3.10+
```

## CLI
```bash
markitdown file.pdf             # stdout
markitdown file.pdf -o out.md   # save
cat file.pdf | markitdown       # pipe
markitdown url --use-plugins    # plugins
```

## Python API
```python
from markitdown import MarkItDown
md = MarkItDown()
print(md.convert("file.pdf").text_content)

# LLM image descriptions
from openai import OpenAI
md = MarkItDown(llm_client=OpenAI(), llm_model="gpt-4o")

# Scanned PDFs via Azure
md = MarkItDown(docintel_endpoint="https://<resource>.cognitiveservices.azure.com/")

# Plugins
md = MarkItDown(enable_plugins=True)
```

## Formats
PDF, DOCX, PPTX, XLSX, HTML, YouTube URLs, CSV, JSON, XML, ZIP, EPub, images (EXIF/OCR), audio (transcription)

## Flow
1. Ask: file path or URL? Output inline or to file?
2. Check install: `python -m markitdown --help`; install if missing
3. Convert: `markitdown "<input>" -o out.md`
4. Short output → show inline. Long → save + report path.
5. On error: missing dep → `pip install 'markitdown[pdf]'` etc.; scanned PDF → use `docintel_endpoint`; image no text → use `llm_client`

## Security
Use `convert_local()` for local-only; `convert_stream()` for untrusted input.
