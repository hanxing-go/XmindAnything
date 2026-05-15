# 🧠 XmindAnything (v2.2)

> *An OpenClaw Skill — convert any content into XMind mind maps.*  
> *将任意内容转为 XMind 思维导图的 OpenClaw Skill。*

[![OpenClaw Skill](https://img.shields.io/badge/OpenClaw-Skill-00d4aa)](https://github.com/openclaw/openclaw)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

<details open>
<summary>🌐 Language / 语言</summary>

Click to expand your preferred language below:

<details open>
<summary>🇬🇧 English</summary>
<br>

## What It Does

Send any content to your AI agent → get an `.xmind` mind map back with a download link.

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

</details>

<details>
<summary>🇨🇳 中文</summary>
<br>

## 功能简介

把任意内容发给 AI → 得到一个 `.xmind` 思维导图 + 下载链接。

| 输入 | 输出 |
|-------|--------|
| 📄 PDF（文字版/扫描版） | 结构化脑图 |
| 📝 Markdown 文档 | 按标题层级展开 |
| 🌐 网页（博客/论坛/教程） | 语义脑图 |
| 📎 Word (.docx / .doc) | 标题 + 段落 + 表格 |
| 📊 PowerPoint (.pptx / .ppt) | 语义分组的幻灯片脑图 |
| 🏗️ GitHub 项目 | 架构总览 |
| 📂 目录（混合文件） | 主题归纳 |
| 💻 源码 (.py, .java, .go 等) | 模块/类签名图 |
| 📋 YAML / JSON / CSV / TOML 等 | 结构图 |

## 快速开始

```bash
npm install -g xmindmark
```

然后对 AI 说：

```
"把这个论文转成思维导图"
"把这篇博客可视化"
"把 README 转成 XMind"
"把这个学习资料目录整理成脑图"
"分析一下这个 GitHub 项目的架构"
"帮我把这个 PPT 转成思维导图"
```

AI 会自动完成：识别类型 → 提取内容 → 语义结构化 → 转换 → 上传 → 返回下载链接。

## 环境依赖

| 输入类型 | 依赖 |
|------------|-----------|
| 全部 | `xmindmark` (npm) |
| Markdown / 网页 / 源码 / 配置文件 | 无 |
| 文字 PDF | `poppler-utils` (pdftotext) |
| 扫描版 PDF | `tesseract-ocr` + `poppler-utils` |
| DOCX / DOC | `python-docx` + LibreOffice (.doc 转换用) |
| PPTX / PPT | `python-pptx` + LibreOffice (.ppt 转换用) |
| XLSX | `openpyxl` |

## 工作流程

```
输入 → 识别类型 → 提取内容 → AI 语义结构化 → xmindmark 转换 → 上传 → 下载链接
```

详见 [SKILL.md](SKILL.md) 和 [references/](references/)。

## License

MIT

</details>

</details>
