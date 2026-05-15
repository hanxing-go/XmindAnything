# 🧠 XmindAnything (v2.2)

> *One Skill, infinite inputs. Any content → XMind mind map in seconds.*  
> *一个 Skill，无限输入。任意内容 → XMind 思维导图，秒级生成。*

**🌐 [English](#english) | [中文](#中文)**

---

<a id="english"></a>
## 🇬🇧 English

**Convert any content into XMind mind maps — PDF, Markdown, URLs, PPT/PPTX, DOC/DOCX, GitHub repos, directories, and 30+ file types.**

<div align="center">

| 📄 PDF | 📝 Markdown | 🌐 Web URL | 📎 Word(.docx/.doc) | 🔍 Scanned PDF | 🏗️ Project | 📂 Directory | 📊 PPT(.pptx/.ppt) |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Text & OCR | Heading parser | Blog/Forum/Tutorial | Headings+Paragraphs+Tables | tesseract OCR | GitHub/Local | Mixed file sets | Slides & Tables |

</div>

### ✨ What Makes It Unique

```
Before: "I have a 26-page paper, a blog post, and a README..."
        "I need to spend 2 hours making mind maps for each..."

After:  Drag & drop → 30 seconds → .xmind file ready.
        8+ input types, 1 unified output.
```

| Capability | XmindAnything | Other Tools |
|------------|:--:|:--:|
| Markdown → XMind | ✅ | ⭐ Few (0-53 stars) |
| Web URL → XMind | ✅ | ❌ None exist |
| Text PDF → XMind | ✅ | ❌ None exist |
| Scanned PDF (OCR) → XMind | ✅ | ❌ None exist |
| DOCX/DOC → XMind | ✅ | ❌ None exist |
| PPTX/PPT → XMind (with tables) | ✅ | ❌ None exist |
| GitHub Project → Architecture Map | ✅ | ❌ None exist |
| Directory/Mixed Files → Thematic Map | ✅ | ❌ None exist |
| Source code (.py/.java/.go) → Signature Map | ✅ | ❌ None exist |
| YAML/JSON/CSV → Structure Map | ✅ | ❌ None exist |
| AI understands & structures content | ✅ | ❌ Prompt only |
| Auto-upload shareable download link | ✅ | ❌ |

### 🚀 Quick Start

#### Install

```bash
# 1. Install the converter CLI
npm install -g xmindmark

# 2. (Optional) For scanned PDF support
apt-get install -y tesseract-ocr tesseract-ocr-chi-sim poppler-utils

# 3. (Optional) For Office document support
pip install --break-system-packages python-docx python-pptx openpyxl
apt-get install -y libreoffice-impress-nogui  # for legacy .ppt/.doc
```

#### Use It

Just send ANY of these to the AI:

```
"Turn this paper into a mind map"              ← PDF
"Visualize this blog post"                     ← URL
"Convert this README to XMind"                ← Markdown
"Turn this scanned PDF into a brain map"       ← Scanned PDF (OCR)
"Convert this Word doc to a mind map"          ← DOCX / DOC
"Turn this PowerPoint into a mind map"         ← PPTX / PPT
"Analyze the architecture of this GitHub repo"  ← GitHub Project
"Organize this study material folder"          ← Directory
"Visualize this YAML config"                  ← Config file
"Map out this Python module structure"         ← Source code
```

The AI will automatically:
1. 🔍 Detect the input type
2. 📖 Extract the content
3. 🧠 Structure it into a hierarchical mind map
4. 🔧 Convert to `.xmind` via xmindmark
5. 📤 Upload and give you a download link

### 📦 Requirements

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
| Source code | None |
| YAML/JSON/CSV/TOML/XML | None |

### 🎯 Comparison with xmindify

| | xmindify | XmindAnything v2.2 |
|------|:--:|:--:|
| Input sources | AI conversation only | 8+ types + format registry |
| Architecture | TypeScript MCP Server | AI-native Markdown Skill |
| Platform | MCP-compatible clients | OpenClaw |
| Output | XMind + SVG | XMind + share link |
| Test coverage | Unknown | 10 real-world tests ✅ |

### 🧪 Tested On

| # | Input | Type | Result |
|:--:|------|------|:--:|
| 1 | HeteroMesh README | Markdown | ✅ |
| 2 | 看雪 Android 加固 | Web URL | ✅ |
| 3 | 看雪 OLLVM 教程 | Web URL | ✅ |
| 4 | 看雪 ELF Linker | Web URL | ✅ |
| 5 | TRELLIS 论文 | Scanned PDF (26pg) | ✅ |
| 6 | 通訳資料 | DOCX | ✅ |
| 7 | 英语作文模板 | Text PDF | ✅ |
| 8 | 第２編 音声・音韻 (40pg) | PPT (.ppt legacy) | ✅ |
| 9 | 年終述职 (8pg) | PPTX | ✅ |
| 10 | Qwen3-TTS 论文 | Text PDF | ✅ |

---

<a id="中文"></a>
## 🇨🇳 中文

**将任意内容一键转为 XMind 思维导图 — PDF、Markdown、网页、PPT/PPTX、DOC/DOCX、GitHub 项目、学习资料目录，以及 30+ 种文件格式。**

### ✨ 独特之处

| 能力 | XmindAnything | 其他工具 |
|------------|:--:|:--:|
| Markdown → 思维导图 | ✅ | ⭐ 极少 (0-53 stars) |
| 网页 → 思维导图 | ✅ | ❌ 不存在 |
| 文字 PDF → 思维导图 | ✅ | ❌ 不存在 |
| 扫描版 PDF (OCR) → 思维导图 | ✅ | ❌ 不存在 |
| DOCX/DOC → 思维导图 | ✅ | ❌ 不存在 |
| PPTX/PPT → 思维导图（含表格） | ✅ | ❌ 不存在 |
| GitHub 项目 → 架构脑图 | ✅ | ❌ 不存在 |
| 目录/混合文件 → 主题脑图 | ✅ | ❌ 不存在 |
| 源码 (.py/.java/.go) → 签名图 | ✅ | ❌ 不存在 |
| YAML/JSON/CSV → 结构图 | ✅ | ❌ 不存在 |
| AI 理解并结构化内容 | ✅ | ❌ 仅提示词 |
| 自动上传可分享下载链接 | ✅ | ❌ |

### 🚀 快速开始

```bash
# 安装转换 CLI
npm install -g xmindmark

# (可选) 扫描版 PDF 支持
apt-get install -y tesseract-ocr tesseract-ocr-chi-sim poppler-utils

# (可选) Office 文档支持
pip install --break-system-packages python-docx python-pptx openpyxl
apt-get install -y libreoffice-impress-nogui  # 旧格式 .ppt/.doc 需要
```

发任意内容给 AI，自动识别、提取、结构化、转换、上传：

```
"把这个论文转成思维导图"              ← PDF
"把这篇博客可视化"                    ← URL
"把 README 转成 XMind"                ← Markdown
"把这个扫描版论文做成脑图"             ← 扫描版 PDF (OCR)
"帮我把这个 Word 文档转成脑图"        ← DOCX / DOC
"帮我把这个 PPT 转成思维导图"         ← PPTX / PPT
"分析一下这个 GitHub 项目的架构"       ← GitHub 项目
"把这个学习资料目录整理成脑图"         ← 目录
"把这个 YAML 配置文件可视化"           ← 配置文件
"把这个 Python 模块结构画成脑图"       ← 源码
```

### 🏗️ 工作流程

```
输入(8+类型) → 识别类型 → 提取内容 → AI 语义结构化 → xmindmark 转换 → 上传 → 下载链接
```

---

## 📄 License

MIT

---

<div align="center">

**Made with 💚 by [@hanxing-go](https://github.com/hanxing-go)**

*"The only skill that turns anything into a mind map."*  
*"万物皆可脑图。"*

</div>
