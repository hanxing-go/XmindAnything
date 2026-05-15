# 🧠 xmind-converter (v2.0)

> *One Skill, many inputs. Any content → XMind mind map in seconds.*

**将任意内容一键转为 XMind 思维导图 — PDF、Markdown、网页、DOCX、GitHub 项目、学习资料目录，甚至扫描版论文。**

---

<div align="center">

| 📄 PDF | 📝 Markdown | 🌐 Web URL | 📎 Word(.docx/.doc) | 🔍 Scanned PDF | 🏗️ Project | 📂 Directory | 📊 PPT(.pptx/.ppt) |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 文字型 & OCR | 标题层级解析 | 博客/论坛/教程 | 标题+段落+表格 | tesseract 识别 | GitHub/本地项目 | 混合文件资料集 | 幻灯片+表格 |

</div>

---

## ✨ What Makes It Unique

```
Before: "I have a 26-page paper, a blog post, and a README..."
        "I need to spend 2 hours making mind maps for each..."

After:  Drag & drop → 30 seconds → .xmind file ready.
        5 input types, 1 unified output.
```

| Capability | This Skill | Other Tools |
|------------|:--:|:--:|
| Markdown → XMind | ✅ | ⭐ Few (0-53 stars) |
| Web URL → XMind | ✅ | ❌ None exist |
| Text PDF → XMind | ✅ | ❌ None exist |
| Scanned PDF (OCR) → XMind | ✅ | ❌ None exist |
| DOCX/DOC → XMind | ✅ | ❌ None exist |
| PPTX/PPT → XMind (含表格) | ✅ | ❌ None exist |
| GitHub Project → Architecture Map | ✅ | ❌ None exist |
| Directory/Mixed Files → Thematic Map | ✅ | ❌ None exist |
| Source code (.py/.java/.go) → Signature Map | ✅ | ❌ None exist |
| YAML/JSON/CSV → Structure Map | ✅ | ❌ None exist |
| AI understands & structures content | ✅ | ❌ Prompt only |
| Auto-upload shareable download link | ✅ | ❌ |

---

## 🚀 Quick Start

### Install

```bash
# 1. Install the converter CLI
npm install -g xmindmark

# 2. (Optional) For scanned PDF support
apt-get install -y tesseract-ocr tesseract-ocr-chi-sim poppler-utils

# 3. (Optional) For DOCX support
pip install --break-system-packages python-docx
```

### Use It

Just send ANY of these to the AI:

```
"把这个论文转成思维导图"              ← PDF
"把这篇博客可视化"                    ← URL
"把 README 转成 XMind"                ← Markdown
"把这个扫描版论文做成脑图"             ← Scanned PDF (OCR)
"帮我把这个 Word 文档转成脑图"            ← DOCX / DOC
"帮我把这个 PPT 转成思维导图"         ← PPTX / PPT
"分析一下这个 GitHub 项目的架构"       ← GitHub Project
"把这个学习资料目录整理成脑图"         ← Directory / study materials
"把这个 YAML 配置文件可视化"           ← Config file
"把这个 Python 模块结构画成脑图"       ← Source code
```

The AI will automatically:
1. 🔍 Detect the input type
2. 📖 Extract the content (pdftotext / OCR / web_fetch / python-docx)
3. 🧠 Structure it into a hierarchical mind map
4. 🔧 Convert to `.xmind` via xmindmark
5. 📤 Upload and give you a download link

---

## 📸 Examples

### 🏗️ GitHub Project → Architecture Map

```
https://github.com/hanxing-go/HeteroMesh (RPC framework)
  ↓ git clone --depth 1 → README + tree + go.mod
  ↓
  项目简介 | 核心架构 | 技术栈 | 快速开始 | 项目规模
```

### 📂 Study Materials → Thematic Map

```
/data/ml-course/ (20 files: PDF + XLSX + CSV + MD)
  ↓ semantic grouping by subdirectory
  ↓
  第一章: Intro | 第二章: Regression | 第三章: Classification | ...
  主文档内容 + 📎 附属文件 (表头/结构)
```

### 📄 Academic Paper → XMind

```
TRELLIS: Structured 3D Latents (26 pages, scanned PDF)
  ↓ OCR → 111KB text → 7 branches
  ↓
  基本信息 | 方法 SLAT | 两阶段生成 | 3D编辑 | 实验 | 结论
```

### 🌐 Tech Blog → XMind

```
https://bbs.kanxue.com/thread-286929.htm (Android hardening)
  ↓ web_fetch → 6 branches
  ↓
  概述 | 前置知识 | Java反射 | ClassLoader | 四代加固 | 项目代码
```

### 📝 README → XMind

```
HeteroMesh project README.md
  ↓ parse headings → 7 branches
  ↓
  项目定位 | 系统架构 | 核心模块 | 技术栈 | 开发进度 | 设计亮点 | 性能数据
```

### 📊 PPTX → XMind

```
季度汇报.pptx (25 页, 含 6 个表格)
  ↓ python-pptx 提取 → 25 个主分支
  ↓
  每页标题 + 文本框要点 + 表格数据完整保留
```

---

## 🏗️ How It Works

```
┌──────────────┐
│    Input     │  PDF / MD / URL / DOCX / Scanned PDF / GitHub Project / Directory
└──────┬───────┘
       ▼
┌──────────────┐
│   Detect     │  dir? github URL? pdftotext? extension? → match scenario
└──────┬───────┘
       ▼
┌──────────────┐
│   Extract    │  pdf tool / tesseract OCR / web_fetch / python-docx / read file / git clone
└──────┬───────┘
       ▼
┌──────────────┐
│  Structure   │  AI reads content → semantic grouping → XMindMark format
└──────┬───────┘
       ▼
┌──────────────┐
│   Convert    │  xmindmark -f xmind → .xmind file
└──────┬───────┘
       ▼
┌──────────────┐
│    Share     │  Upload to tmpfiles.org → shareable download link
└──────────────┘
```

---

## 📦 Requirements

| Input Type | Dependency |
|------------|-----------|
| All | `xmindmark` (npm) |
| Markdown | None |
| Web URL | None |
| Text PDF | `poppler-utils` (pdftotext) |
| Scanned PDF | `tesseract-ocr` + `tesseract-ocr-chi-sim` + `poppler-utils` |
| DOCX / DOC | `python-docx` (pip) + LibreOffice (.doc→.docx) |
| XLSX | `openpyxl` (pip) |
| PPTX / PPT | `python-pptx` (pip) + LibreOffice (.ppt→.pptx) |
| EPUB | `unzip` (built-in) |
| Source code (.py/.java/.go/...) | None (text reading) |
| YAML/JSON/CSV/TOML/XML | None (text reading) |

---

## 🎯 Comparison with xmindify

| | xmindify | xmind-converter v2.0 |
|------|:--:|:--:|
| Input sources | AI conversation only | 7 types + format registry |
| Architecture | TypeScript MCP Server | AI-native Markdown Skill |
| Platform | MCP-compatible clients | OpenClaw |
| Output | XMind + SVG | XMind + share link |
| Test coverage | Unknown | 8 real-world tests ✅ |

---

## 🧪 Tested On

| # | Input | Type | Result |
|:--:|------|------|:--:|
| 1 | HeteroMesh README | Markdown | ✅ |
| 2 | 看雪 Android 加固 | Web URL | ✅ |
| 3 | 看雪 OLLVM 教程 | Web URL | ✅ |
| 4 | 看雪 ELF Linker | Web URL | ✅ |
| 5 | TRELLIS 论文 | Scanned PDF (26pg) | ✅ |
| 6 | 通訳資料 | DOCX | ✅ |
| 7 | 英语作文模板 | Text PDF | ✅ |
| 8 | 第２編 音声・音韻 (40页) | PPT (.ppt 旧格式) | ✅ |
| 9 | PPTX test (年終述职 8页) | PPTX | ✅ |
| 10 | Qwen3-TTS 论文 | Text PDF | ✅ |

---

## 📄 License

MIT

---

<div align="center">

**Made with 💚 by 小 Miku & Master**

*"The only skill that turns anything into a mind map."*

</div>
