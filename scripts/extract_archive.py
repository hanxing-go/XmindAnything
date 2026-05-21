#!/usr/bin/env python3
"""Extract archive files (.zip, .tar.gz, .tar.bz2, .tar.xz, .7z, .rar) to a temp directory.

Usage: python extract_archive.py <archive_file>
Output: extraction path, file count, directory tree
"""
import sys, os, subprocess, tempfile, zipfile, tarfile, shutil

def extract_zip(path, dest):
    with zipfile.ZipFile(path, 'r') as zf:
        zf.extractall(dest)

def extract_tar(path, dest):
    with tarfile.open(path, 'r:*') as tf:
        tf.extractall(dest)

def extract_7z(path, dest):
    subprocess.run(['7z', 'x', f'-o{dest}', '-y', path],
                   capture_output=True, check=True)

def extract_rar(path, dest):
    subprocess.run(['unrar', 'x', '-y', path, f'{dest}/'],
                   capture_output=True)

MAPPING = {
    '.zip': extract_zip,
    '.tar': extract_tar,
    '.gz': extract_tar,
    '.tgz': extract_tar,
    '.bz2': extract_tar,
    '.tbz2': extract_tar,
    '.xz': extract_tar,
    '.txz': extract_tar,
    '.tar.gz': extract_tar,
    '.tar.bz2': extract_tar,
    '.tar.xz': extract_tar,
    '.7z': extract_7z,
    '.rar': extract_rar,
}

def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_archive.py <archive>")
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.exists(path):
        print(f"ERROR: File not found: {path}")
        sys.exit(1)

    fname = os.path.basename(path).lower()

    # Match extension (handle double extensions like .tar.gz)
    ext = None
    for candidate in sorted(MAPPING.keys(), key=len, reverse=True):
        if fname.endswith(candidate):
            ext = candidate
            break

    if not ext:
        print(f"ERROR: Unsupported archive format: {fname}")
        sys.exit(1)

    dest = tempfile.mkdtemp(prefix='arc_')

    try:
        MAPPING[ext](path, dest)
    except Exception as e:
        print(f"ERROR: Extraction failed: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"DEST:{dest}")
    result = subprocess.run(f"find {dest} -type f | wc -l",
                            shell=True, capture_output=True, text=True)
    print(f"FILES:{result.stdout.strip()}")

    # Tree
    result = subprocess.run(
        f"tree -L 3 --dirsfirst {dest}",
        shell=True, capture_output=True, text=True, timeout=30
    )
    print(f"TREE:{result.stdout}")

if __name__ == '__main__':
    main()
