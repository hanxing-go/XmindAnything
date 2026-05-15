# 🧠 XmindAnything (v2.2)

> *Convert any content into XMind mind maps — an OpenClaw Skill.*  
> *将任意内容转为 XMind 思维导图 — 一个 OpenClaw Skill。*

[![OpenClaw Skill](https://img.shields.io/badge/OpenClaw-Skill-00d4aa)](https://github.com/openclaw/openclaw)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

📖 **Read this in:** [English](README.md) | [中文](README_zh.md)

---

## What It Does

**Send any content to your AI agent → get an `.xmind` mind map back with a download link.**

| Input | Output |
|-------|--------|
| 📄 PDF (text or scanned) | Structured brain map |
| 📝 Markdown document | Heading-based hierarchy |
| 🌐 Web URL (blog, tutorial, forum) | Semantic mind map |
| 📎 Word (.docx / .doc) | Headings + paragraphs + tables |
| 📊 PowerPoint (.pptx / .ppt) | Semantically grouped slides |
| 🏗️ GitHub project | Architecture overview |
| 📂 Directory of mixed files | Thematic organization |
| 💻 Source code (.py, .java, .go, etc.) | Module/class signature map |
| 📋 YAML / JSON / CSV / TOML | Structure diagram |

## Quick Start

```bash
npm install -g xmindmark
```

Then tell your AI agent:

```
"Turn this paper into a mind map"
"Visualize this blog post"
"Convert this README to XMind"
"Organize this study material folder"
"Analyze this GitHub repo's architecture"
"Turn this PowerPoint into a mind map"
```

The agent handles detection, extraction, structuring, conversion, and uploading.

## Requirements

| Input Type | Dependency |
|------------|-----------|
| All | `xmindmark` (npm) |
| Markdown / Web URL / Source code / Configs | None |
| Text PDF | `poppler-utils` (pdftotext) |
| Scanned PDF | `tesseract-ocr` + `poppler-utils` |
| DOCX / DOC | `python-docx` + LibreOffice (for .doc) |
| PPTX / PPT | `python-pptx` + LibreOffice (for .ppt) |
| XLSX | `openpyxl` |

## How It Works

```
Input → Detect type → Extract content → AI semantic structuring → xmindmark conversion → Upload → Download link
```

See [SKILL.md](SKILL.md) for the full agent workflow and [references/](references/) for per-format extraction guides.

## License

MIT
