#!/usr/bin/env python3
"""Extract structure from .ipynb Jupyter notebooks — cells, outputs, metadata."""
import json, sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_ipynb.py <file.ipynb>")
        sys.exit(1)

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        nb = json.load(f)

    print(f"CELL_COUNT:{len(nb.get('cells', []))}")
    print(f"NB_FORMAT:{nb.get('nbformat')}.{nb.get('nbformat_minor')}")
    meta = nb.get('metadata', {})
    kernel = meta.get('kernelspec', {}).get('display_name', 'unknown')
    lang = meta.get('language_info', {}).get('name', 'unknown')
    print(f"KERNEL:{kernel}")
    print(f"LANGUAGE:{lang}")

    for i, cell in enumerate(nb.get('cells', [])):
        ctype = cell.get('cell_type', 'unknown')
        source = ''.join(cell.get('source', []))[:300]
        if not source.strip():
            continue

        # Determine if heading
        if ctype == 'markdown' and source.startswith('#'):
            level = len(source) - len(source.lstrip('#'))
            print(f"\n===CELL{i}:MD_H{level}===")
        elif ctype == 'markdown':
            print(f"\n===CELL{i}:MD===")
        else:
            print(f"\n===CELL{i}:CODE===")

        print(source.strip()[:500])

if __name__ == '__main__':
    main()
