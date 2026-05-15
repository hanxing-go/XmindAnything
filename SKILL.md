---
name: xmind-converter
description: >
  Converts PDF files, Markdown documents, web URLs, GitHub projects, local directories (mixed file types), or plain text into XMind mind maps (.xmind files).
  Use when the user asks to: (1) convert a PDF/paper/article into a mind map or 思维导图/脑图,
  (2) turn a Markdown document or README into a structured diagram,
  (3) visualize a webpage or blog post as a mind map,
  (4) generate architecture diagrams from GitHub repos or local project directories,
  (5) organize study materials (directories with mixed files) into thematic mind maps,
  (6) create an XMind file from any text content, (7) 将文章/论文/文档/网页/项目转为思维导图.
  Requires xmindmark CLI. For scanned PDFs: tesseract-ocr + poppler-utils. For xlsx/pptx: openpyxl + python-pptx (auto-install on first use).
---

# XMind Converter (v2.2)

Convert any content (PDF, Markdown, URL, GitHub projects, directories, plain text, and more) into XMind mind maps using XMindMark format + xmindmark CLI.

## Prerequisites

```bash
# Core tool
xmindmark --version || npm install -g xmindmark

# For scanned/OCR PDFs (install on first use):
apt-get install -y tesseract-ocr tesseract-ocr-chi-sim poppler-utils
```

## Workflow

```
Input → Extract content → Structure into XMindMark → Convert to .xmind → Upload & share link
```

### Step 1: Identify input type

| Input | Detection | Scenario |
|-------|-----------|----------|
| Directory (目录) | `[ -d "$input" ]` 为真 | [project](references/scenario-project.md) |
| GitHub URL | URL 含 `github.com` | [project](references/scenario-project.md) |
| PowerPoint (.pptx) | File extension | [pptx](references/scenario-pptx.md) |
| PowerPoint (.ppt) | File extension (旧格式) | [pptx](references/scenario-pptx.md) → LibreOffice 转 pptx |
| Word (.docx) | File extension | [docx](references/scenario-docx.md) |
| Word (.doc) | File extension (旧格式) | [docx](references/scenario-docx.md) → LibreOffice 转 docx |
| PDF (.pdf) | File extension or "论文/paper" | [paper](references/scenario-paper.md) |
| Scanned PDF | `pdftotext` returns < 100 bytes | [ocr-pdf](references/scenario-ocr-pdf.md) |
| Markdown (.md) | File extension | [markdown](references/scenario-markdown.md) |
| Web URL (http/https) | Starts with http (非GitHub) | [url](references/scenario-url.md) |
| Other file types (.yaml/.json/.py/...) | File extension | [format-registry](references/format-registry.md) |
| Plain text | None of above | Auto-structure |

### Step 2: Extract and structure

**输入判断逻辑（按优先级）：**
1. 先判是否目录 `[ -d "$input" ]` → [project](references/scenario-project.md) 子场景 B
2. 再判是否 GitHub URL → [project](references/scenario-project.md) 子场景 A
3. 再判文件扩展名 → 查 [format-registry](references/format-registry.md)
4. 其余走现有文本逻辑

**Scan-detection for PDFs:** First test if PDF is text-based or scanned:
```bash
pdftotext input.pdf /tmp/test.txt && wc -c /tmp/test.txt
```
If < 100 bytes → scanned, needs OCR. Jump to [ocr-pdf](references/scenario-ocr-pdf.md).

**Text-based PDFs:** Use `pdf` tool → extract title/authors/abstract/method/results/conclusion → each section 2-4 bullet points.

**Scanned PDFs (OCR):** Convert to images → tesseract OCR → read result → structure. Full workflow in [ocr-pdf](references/scenario-ocr-pdf.md). Prerequisite: `apt-get install -y tesseract-ocr tesseract-ocr-chi-sim poppler-utils`.

**Markdown:** Parse `#` = center, `##` = main branch, `###` = sub-branch. 1-2 sentences per node.

**URLs:** Use `web_fetch` (readability mode auto-strips nav/ads). Identify natural chapter boundaries. Read [scenario-url.md](references/scenario-url.md) for real-world example.

**Plain text:** Group related ideas into thematic branches. Center topic from first sentence.

**其他文件格式：** 查 [format-registry](references/format-registry.md)，按对应方法提取。
- 文本类：提取结构信息（key/列名/标题），不提取全文
- 源码类：提取 class/function 签名，不提取实现细节
- 二进制类：首次使用时安装对应 Python 库（openpyxl / python-pptx）
- 跳过图片/视频/音频/压缩包/二进制库，最后标注「已跳过 N 个文件」

### Step 3: Generate XMindMark

Write to `.xmindmark` file. Syntax reference: [SYNTAX.md](references/SYNTAX.md).

**Critical rules (tested against xmindmark 0.3.2):**

- Line 1 = center topic (no prefix)
- Main branches: `- ` prefix, no indent
- Sub-branches: 4 spaces, `* ` or `- `
- Max 4 levels deep, 3-7 children per branch
- No spaces inside `[]` markers
- **DO NOT use `[B]:` or `[S]:` title syntax** — crashes xmindmark 0.3.2 parser
- **DO NOT use cross-branch `[1]`/`[^1]` relationships** — XMind draws ugly crossing lines
- Use `[B]` boundaries and `[S]` summaries without titles only

### Step 4: Convert

```bash
rm -f output.xmind && xmindmark -f xmind output.xmindmark
```

Skip SVG export (requires Chromium download, often fails on servers).

### Step 5: Upload & share

```bash
# Upload
RESULT=$(curl -s -F "file=@output.xmind" https://tmpfiles.org/api/v1/upload)
# API returns: {"status":"success","data":{"url":"https://tmpfiles.org/{id}/file.xmind"}}
# ⚠️ The API url is a LANDING PAGE with ads. Always use /dl/ prefix for direct download:
# Direct URL: https://tmpfiles.org/dl/{id}/file.xmind
```

## XMindMark Quick Syntax

```
Center Topic

- Main Branch 1 [B1]
    * Sub-topic 1.1
        - Detail A
        - Detail B
    * Sub-topic 1.2

- Main Branch 2 [B2]
    * Point A
    * Point B

- Key Takeaways [S1]
    * Conclusion 1
    * Conclusion 2
```

**Remember:** No `[B]:`/`[S]:` titles. No cross-branch `[1]`/`[^1]`. Keep nodes short.
