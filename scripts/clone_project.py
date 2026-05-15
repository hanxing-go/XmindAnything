#!/usr/bin/env python3
"""Clone a GitHub repo and extract project metadata.

Usage: python clone_project.py <github_url> [--branch main]
Output: structured metadata to stdout, repo cloned to ./repos/<owner>-<repo>
"""
import sys, os, json, subprocess, re, glob

def run(cmd, **kwargs):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True, **kwargs)

def main():
    if len(sys.argv) < 2:
        print("Usage: python clone_project.py <github_url>")
        sys.exit(1)

    url = sys.argv[1]
    # Parse owner/repo from URL
    match = re.search(r'github\.com/([^/]+)/([^/\s.]+)', url)
    if not match:
        print(f"ERROR: Not a GitHub URL: {url}")
        sys.exit(1)

    owner, repo = match.groups()
    dest = f"/tmp/proj-{repo}"

    # Clean previous clone
    run(f"rm -rf {dest}")

    # Clone
    result = run(f"git clone --depth 1 --single-branch {url} {dest}", timeout=60)
    if result.returncode != 0:
        print(f"ERROR: Clone failed:\n{result.stderr}")
        sys.exit(1)

    print(f"REPO:{owner}/{repo}")
    print(f"DEST:{dest}")

    # Detect project type
    tech_stack = []
    if os.path.exists(f"{dest}/package.json"):
        tech_stack.append("Node.js")
    if os.path.exists(f"{dest}/requirements.txt") or glob.glob(f"{dest}/*.py"):
        tech_stack.append("Python")
    if os.path.exists(f"{dest}/Cargo.toml"):
        tech_stack.append("Rust")
    if os.path.exists(f"{dest}/go.mod"):
        tech_stack.append("Go")
    if os.path.exists(f"{dest}/pom.xml") or glob.glob(f"{dest}/*.java"):
        tech_stack.append("Java")
    if os.path.exists(f"{dest}/Makefile"):
        tech_stack.append("C/Make")
    if os.path.exists(f"{dest}/CMakeLists.txt"):
        tech_stack.append("CMake")
    if os.path.exists(f"{dest}/Dockerfile"):
        tech_stack.append("Docker")
    print(f"TECH:{','.join(tech_stack) if tech_stack else 'unknown'}")

    # Count files (exclude .git, node_modules, etc.)
    result = run(f"find {dest} -type f ! -path '*/.git/*' ! -path '*/node_modules/*' ! -path '*/__pycache__/*' ! -path '*/target/*' ! -path '*/vendor/*' | wc -l")
    print(f"FILES:{result.stdout.strip()}")

    # Lines of code by language
    for ext, lang in [('*.py', 'Python'), ('*.java', 'Java'), ('*.go', 'Go'),
                       ('*.rs', 'Rust'), ('*.js', 'JS'), ('*.ts', 'TS'),
                       ('*.c', 'C'), ('*.cpp', 'CPP'), ('*.h', 'Header')]:
        result = run(f"find {dest} -name '{ext}' ! -path '*/.git/*' | xargs wc -l 2>/dev/null | tail -1")
        lines = result.stdout.strip().split()[-1] if result.stdout.strip() else '0'
        if lines != '0':
            print(f"LOC:{lang}:{lines}")

    # Find README
    for f in ["README.md", "README.rst", "README", "readme.md", "Readme.md"]:
        path = os.path.join(dest, f)
        if os.path.isfile(path):
            print(f"README:{path}")
            break

    # Directory tree (top 2 levels)
    result = run(f"tree -L 2 --dirsfirst -I 'node_modules|__pycache__|target|build|dist|.git|vendor|*.pyc' {dest}")
    print(f"TREE:{result.stdout}")
    if result.stderr:
        print(f"TREE_ERR:{result.stderr}")

if __name__ == '__main__':
    main()
