# Format Registry

文件扩展名 → 提取方法映射表。用于处理 PDF/MD/URL/DOCX 之外的文件类型。

---

## Registry Table

### 文本类

| 扩展名 | 提取方法 | 工具 |
|--------|----------|------|
| .yaml / .yml | 读文本 → 提取顶层 key + 嵌套结构 | 无 |
| .json | 读文本 → 提取顶层 key + 嵌套结构 | 无 |
| .toml | 读文本 → 提取 section 和 key | 无 |
| .xml | 读文本 → 提取主要标签名（第一层） | 无 |
| .csv / .tsv | 读文本 → 列名 + 行数统计 | 无 |
| .rst | 读文本 → 提取标题 (===, ---, ~~~) | 无 |
| .tex | 读文本 → 提取 \section, \subsection | 无 |
| .html | web_fetch/读文件 → 提取 h1-h4 | 无 |

### 源码类

| 扩展名 | 提取方法 | 工具 |
|--------|----------|------|
| .py | 读文本 → re: class/def 签名 | 无 |
| .java | 读文本 → re: class/interface/public method | 无 |
| .go | 读文本 → re: type/func 签名 | 无 |
| .js / .ts | 读文本 → re: class/function/export | 无 |
| .c / .cpp / .h | 读文本 → re: struct/function 签名 | 无 |
| .rs | 读文本 → re: struct/enum/fn 签名 | 无 |

### 文档类（需额外工具）

| 扩展名 | 提取方法 | 工具 |
|--------|----------|------|
| .docx | `python3 /tmp/extract_docx.py` → 标题/段落/表格 | python-docx |
| .doc  | `soffice --headless --convert-to docx` → 同上 | python-docx + LibreOffice |
| .pptx | `python3 /tmp/extract_pptx.py` → 每页标题 + 文本框 + 表格 | python-pptx |
| .ppt  | `soffice --headless --convert-to pptx` → 同上 | python-pptx + LibreOffice |

### 二进制/混合类（需额外 Python 库）

| 扩展名 | 提取方法 | 工具 |
|--------|----------|------|
| .ipynb | `python3 -c "import json;..."` → cell 提取 | python3 |
| .xlsx | `python3 -c "import openpyxl;..."` → Sheet 名 + 表头 | openpyxl |
| .epub | `unzip -p toc.ncx` → 提取目录结构 | unzip |

---

## 提取原则

### 文本类
提取**结构信息**（key/列名/标题），不是全文。输出为脑图中的「配置结构」节点。

### 源码类
提取 **class/function/type 签名**，不提取实现细节。输出为「模块结构」节点。

正则参考：
- **Python**: `r'(class|def)\s+(\w+)'`
- **Java**: `r'(public|private|protected)\s+(class|interface)\s+(\w+)'`
- **Go**: `r'(type|func)\s+(\w+)'`
- **JS/TS**: `r'(class|function|export)\s+(\w+)'`
- **C/C++**: `r'(struct|class)\s+(\w+)|(\w+\s+\w+\s*\([^)]*\)\s*\{)'`
- **Rust**: `r'(struct|enum|fn|trait)\s+(\w+)'`

### 二进制类
需额外 Python 库。首次使用时安装并在输出中提醒用户：
```bash
pip install --break-system-packages python-pptx openpyxl python-docx
```

### 跳过
以下类型直接跳过，在输出末尾标注「已跳过 N 个文件」：
- 图片: .png/.jpg/.jpeg/.gif/.webp/.svg/.bmp
- 视频: .mp4/.avi/.mov/.mkv/.webm
- 音频: .mp3/.wav/.ogg/.flac
- 压缩包: .zip/.tar/.gz/.rar/.7z
- 二进制库: .so/.o/.a/.dll/.exe/.class/.pyc
- 特殊目录: .git/ node_modules/ __pycache__/ venv/ .venv/

---

## 使用流程

1. 遇到非 PDF/MD/URL/DOCX 的文件时，查本表
2. 找到对应扩展名的提取方法
3. 按提取原则执行，保持输出简洁（只提取结构/签名）
4. 对项目场景，源码文件汇总为一个「源码结构」节点，不在根节点散开
