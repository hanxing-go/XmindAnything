#!/usr/bin/env python3
"""
XmindAnything Content Cleaning Pipeline
输入: 从 PDF/OCR 等来源提取的原始文本
输出: 清洗后的结构化文本，去掉垃圾信息，保留知识点

Usage:
    python3 scripts/clean_content.py < input.txt > output.txt
    python3 scripts/clean_content.py input.txt [output.txt]
"""

import re
import sys
from typing import List


# ─────────────── 规则集 ───────────────

# 1. 引用标记: [1], [2,3], [42,45,67], [1, 2, 3]
RE_CITATION = re.compile(r'\[\d+(?:\s*[,;\s]\s*\d+)*\]')

# 2. 行末纯页码（独立数字行，1-4位）
RE_PAGE_NUMBER = re.compile(r'^\d{1,4}$')

# 3. 图表/表格编号标记: "Figure 1.", "Fig. 1:", "Table XIV.", "TABLE 14."
RE_FIGURE_TABLE = re.compile(
    r'^(Figure|Fig\.?|TABLE|Table)\s+[IVXLCDM\d]+[.:]\s*',
    re.IGNORECASE
)

# 4. 页眉元数据: ISBN, DOI, URL, 会议名, 页码行
RE_METADATA = re.compile(
    r'^(ISBN\s+[\d\-]+|https?://\S+|www\.\S+|'
    r'\d{4}\.\s+\d+[,\s]+\d+$|'     # "2024. 2, 3" 纯引用索引行
    r'Computer Vision Foundation|IEEE Computer Society|'
    r'This ICCV paper is the Open Access|'
    r'Except for this watermark|'
    r'the final published version)',
    re.IGNORECASE
)

# 5. 连续数字列表行（参考文献索引残留）: "2013. 6, 7"
RE_REF_INDEX = re.compile(r'^\d{4}\.\s+[\d,\s]+$')

# 6. 纯标点/空白折行垃圾
RE_GARBAGE_LINE = re.compile(r'^[\s\.,;:\-–—•·\(\)\[\]{}⟨⟩]+$')

# 7. References 段检测（学术论文尾部）
RE_REFERENCES_HEADER = re.compile(
    r'^(References|REFERENCES|Bibliography)\s*$'
)

# 8. 参考文献条目残留: "[42] Author..." / "N. Author..." 开头
RE_REF_ENTRY = re.compile(r'^\[\d+\]\s+\w')

# 9. LaTeX 公式渲染残留 (pdftotext 产物)
RE_LATEX_ARTIFACT = re.compile(r'<latexit[ >]')


def remove_citations(text: str) -> str:
    """移除行内引用标记 [1] [2,3] [42,45]"""
    return RE_CITATION.sub('', text)


def is_clean_line(line: str) -> bool:
    """判断一行是否值得保留"""
    stripped = line.strip()

    if not stripped:
        return False  # 空行保留（段落分隔）

    if len(stripped) <= 3 and stripped.isdigit():
        return False  # 纯页码

    if RE_PAGE_NUMBER.match(stripped):
        return False

    if RE_REF_INDEX.match(stripped):
        return False

    if RE_GARBAGE_LINE.match(stripped):
        return False

    if RE_FIGURE_TABLE.match(stripped):
        # 保留带描述的图表标题, 过滤纯编号
        rest = RE_FIGURE_TABLE.sub('', stripped).strip()
        return len(rest) > 10

    if RE_METADATA.match(stripped):
        return False

    # 参考文献条目（含年份+页码标记，但无实质内容）
    if RE_REF_ENTRY.match(stripped):
        return False

    # 纯年份+尾随数字行 "2023. 6, 7"
    if re.match(r'^\d{4}\.\s*\d[\d,\s]*$', stripped):
        return False

    # LaTeX 公式渲染残留
    if RE_LATEX_ARTIFACT.match(stripped):
        return False

    return True


def merge_broken_lines(lines: List[str]) -> List[str]:
    """
    合并被折断的句子:
    - 不以大写字母/数字开头的行 → 可能是上行续接
    - 前一行不以 .:!? 结尾 → 可能未结束
    """
    merged = []
    buffer = ""

    for line in lines:
        stripped = line.strip()
        if not stripped:
            if buffer:
                merged.append(buffer)
                buffer = ""
            merged.append("")
            continue

        if buffer:
            # 判断是否应该合并
            prev = buffer.rstrip()
            should_merge = False

            # 前一行不以句末标点结束
            if not prev.endswith(('.', ':', '!', '?', ')', ']', '"', "'", ';')):
                should_merge = True
            # 当前行以小写字母开头（续接）
            elif stripped and stripped[0].islower():
                should_merge = True

            if should_merge:
                buffer += " " + stripped
            else:
                merged.append(buffer)
                buffer = stripped
        else:
            buffer = stripped

    if buffer:
        merged.append(buffer)

    return merged


def normalize_whitespace(lines: List[str]) -> List[str]:
    """规范化空白：合并连续空行，去首尾空白"""
    result = []
    prev_empty = False

    for line in lines:
        stripped = line.strip()
        if not stripped:
            if not prev_empty:
                result.append("")
            prev_empty = True
        else:
            result.append(stripped)
            prev_empty = False

    # 去掉首尾空行
    while result and not result[0]:
        result.pop(0)
    while result and not result[-1]:
        result.pop()

    return result


def truncate_at_references(lines: List[str]) -> List[str]:
    """在 References 标题处截断，后面全是参考文献条目"""
    for i, line in enumerate(lines):
        stripped = line.strip()
        if RE_REFERENCES_HEADER.match(stripped):
            # 往回找最近的空行，确保 References 标题也被移除
            return lines[:i]
    return lines


def clean_content(text: str) -> str:
    """主清洗流程"""
    # Step 1: 移除引用标记
    text = remove_citations(text)

    # Step 2: 按行处理
    lines = text.split('\n')

    # Step 3: 截断 References 段
    lines = truncate_at_references(lines)

    # Step 4: 垃圾行过滤
    cleaned_lines = [l for l in lines if is_clean_line(l)]

    # Step 5: 合并折断行
    merged = merge_broken_lines(cleaned_lines)

    # Step 6: 规范化空白
    result = normalize_whitespace(merged)

    return '\n'.join(result)


def main():
    if len(sys.argv) >= 3:
        with open(sys.argv[1], 'r') as f:
            text = f.read()
        output = clean_content(text)
        with open(sys.argv[2], 'w') as f:
            f.write(output)
    elif len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as f:
            text = f.read()
        output = clean_content(text)
        print(output)
    else:
        text = sys.stdin.read()
        output = clean_content(text)
        print(output)


if __name__ == '__main__':
    main()
