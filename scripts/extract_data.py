#!/usr/bin/env python3
"""Extract structure from YAML, JSON, CSV, TOML, XML files.

Outputs a tree-like structure suitable for AI semantic reorganization.
"""
import sys, os, json, csv, io

def extract_json(path):
    with open(path, 'r') as f:
        data = json.load(f)
    return json.dumps(data, indent=2, ensure_ascii=False, default=str)

def extract_yaml(path):
    import yaml
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
    return yaml.dump(data, indent=2, allow_unicode=True, default_flow_style=False)

def extract_csv(path):
    with open(path, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    out = io.StringIO()
    out.write(f"ROWS:{len(rows)}\nCOLS:{len(rows[0]) if rows else 0}\n---\n")
    for i, row in enumerate(rows[:30]):
        out.write(" | ".join(row) + "\n")
    if len(rows) > 30:
        out.write(f"... (剩余 {len(rows)-30} 行)\n")
    return out.getvalue()

def extract_toml(path):
    try:
        import tomllib
    except ImportError:
        import toml
        with open(path, 'r') as f:
            data = toml.load(f)
        return toml.dumps(data)
    with open(path, 'rb') as f:
        data = tomllib.load(f)
    return json.dumps(data, indent=2, ensure_ascii=False, default=str)

def extract_xml(path):
    import xml.etree.ElementTree as ET
    tree = ET.parse(path)
    root = tree.getroot()
    out = io.StringIO()

    def walk(node, depth=0):
        tag = node.tag.split('}')[-1] if '}' in node.tag else node.tag
        text = (node.text or '').strip()
        line = "  " * depth + f"<{tag}>"
        if text:
            line += f" {text[:100]}"
        out.write(line + "\n")
        for child in node:
            walk(child, depth + 1)

    walk(root)
    return out.getvalue()

MAPPING = {
    '.json': extract_json,
    '.yaml': extract_yaml,
    '.yml': extract_yaml,
    '.csv': extract_csv,
    '.tsv': extract_csv,
    '.toml': extract_toml,
    '.xml': extract_xml,
}

def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_data.py <file>")
        sys.exit(1)

    path = sys.argv[1]
    ext = os.path.splitext(path)[1].lower()

    if ext not in MAPPING:
        print(f"ERROR: Unsupported format: {ext}")
        sys.exit(1)

    try:
        result = MAPPING[ext](path)
        print(f"FORMAT:{ext}")
        print(result)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
