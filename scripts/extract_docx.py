#!/usr/bin/env python3
"""Extract text from .docx or .doc (via LibreOffice) into structured Markdown."""
import sys, os, subprocess, glob

def convert_doc_to_docx(path):
    """Convert .doc (old binary) to .docx using LibreOffice headless."""
    outdir = os.path.dirname(path) or "/tmp"
    result = subprocess.run(
        ["soffice", "--headless", "--convert-to", "docx", "--outdir", outdir, path],
        capture_output=True, text=True, timeout=120
    )
    if result.returncode != 0:
        print(f"ERROR: LibreOffice conversion failed:\n{result.stderr}", file=sys.stderr)
        sys.exit(1)
    # find the output file
    basename = os.path.splitext(os.path.basename(path))[0]
    outpath = os.path.join(outdir, basename + ".docx")
    if not os.path.exists(outpath):
        # maybe it has a different name pattern
        for f in glob.glob(os.path.join(outdir, "*.docx")):
            print(f"DEBUG: found {f}", file=sys.stderr)
        sys.exit(1)
    return outpath

def extract_docx(path):
    """Extract all text from a .docx file, preserving structure."""
    from docx import Document
    doc = Document(path)

    output = []
    output.append(f"# {os.path.basename(path)}")

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue
        style = para.style.name.lower() if para.style else ""
        # Determine heading level
        if "heading 1" in style or "title" in style:
            output.append(f"\n## {text}")
        elif "heading 2" in style:
            output.append(f"\n### {text}")
        elif "heading 3" in style:
            output.append(f"\n#### {text}")
        elif "heading" in style:
            output.append(f"\n### {text}")
        elif "list" in style or para.paragraph_format.first_line_indent:
            output.append(f"- {text}")
        else:
            output.append(f"\n{text}")

    # Tables
    for i, table in enumerate(doc.tables):
        output.append(f"\n---\n### 📊 表格 {i+1}:")
        for row in table.rows[:20]:  # max 20 rows
            cells = [cell.text.strip().replace('\n', ' ') for cell in row.cells]
            output.append(f"| {' | '.join(cells)} |")

    return '\n'.join(output)

def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_docx.py <file.docx|file.doc>")
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.exists(path):
        print(f"ERROR: File not found: {path}")
        sys.exit(1)

    # If .doc, convert first
    if path.lower().endswith('.doc') and not path.lower().endswith('.docx'):
        print(f"Converting .doc to .docx: {path}", file=sys.stderr)
        path = convert_doc_to_docx(path)

    if not path.lower().endswith('.docx'):
        print(f"ERROR: Not a .docx file: {path}")
        sys.exit(1)

    md = extract_docx(path)
    print(md)

if __name__ == '__main__':
    main()
