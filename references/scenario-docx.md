# Scenario: Word 文档 (.docx / .doc)

从 Microsoft Word 文档中提取完整内容（标题、段落、表格），转为结构化 XMindMark。

## Prerequisites

```bash
# 安装 python-docx（.docx 提取）
pip install --break-system-packages -i https://pypi.org/simple/ python-docx

# 如果是 .doc（旧格式），先用 LibreOffice 转换
apt-get install -y libreoffice-impress-nogui        # 通常已安装 PPT → PPTX 时附带
soffice --headless --convert-to docx --outdir /tmp input.doc
```

## Step 1: Identify .doc vs .docx

```python
# 扩展名判断
if file.lower().endswith('.docx'):
    # 直接用 python-docx 解析
elif file.lower().endswith('.doc') and not file.lower().endswith('.docx'):
    # 先 soffice --headless --convert-to docx，再解析
else:
    ERROR("Not a Word document")
```

## Step 2: Extract content

使用本 Skill 内置脚本 `scripts/extract_docx.py`（自动处理 .doc → .docx 转换）：

```bash
python3 scripts/extract_docx.py document.docx > /tmp/docx_content.txt
```

然后 `read /tmp/docx_content.txt` 获取结构化文本。

**提取内容：**
- 所有段落文本，按 Word 内置样式识别标题层级
- 所有表格数据（最多 20 行），转为 Markdown 表格
- 页码统计

## Step 3: Semantic structuring

**结构化原则（同 PPTX 场景）：**
1. **主题分组 > 页面顺序** — 不按"第1节→第2节"展开，按语义归类
2. **识别自然章节** — 标题样式为 Heading 1/2 处作为主分支节点
3. **合并相关内容** — 同一主题下分散的段落合并到一个子节点
4. **表格归类** — 每个表格归入其最近的章节标题下
5. **目标 3-7 个主分支**

## Step 4: Generate XMindMark

**示例输出格式：**

```
文档标题

- 章节1: 背景介绍
    * 要点1
    * 要点2
    * 要点3

- 章节2: 核心概念 [B1]
    * 概念A
        - 子点1
        - 子点2
    * 概念B
    * 📊 表格: 数据对比
        - | A | B | C |

- 章节3: 应用与实践
    * 案例1
    * 案例2

- 章节4: 总结 [S1]
    * 结论1
    * 结论2
```

## Edge Cases

- **纯表格文档**：表格为主分支，每张表一个主分支
- **无标题样式**：AI 自行识别语义断点分组
- **超大文档（>50页）**：只提取标题结构 + 前3级内容，每个主分支控制在 3-5 个子节点
- **加密/损坏**：报告无法打开，建议用户重新导出
