#!/usr/bin/env python3
import os, re
from urllib.parse import unquote

root = os.getcwd()
exts_try = ['.md', '.markdown', '.html', '.htm']
patterns = [
    re.compile(r'!\[.*?\]\((.*?)\)'),
    re.compile(r'\[.*?\]\((.*?)\)'),
    re.compile(r'src=["\'](.*?)["\']', re.I),
    re.compile(r'href=["\'](.*?)["\']', re.I),
]
skip_schemes = ('http:', 'https:', 'mailto:', 'tel:', 'javascript:')
missing = {}

def norm(p):
    return unquote(p.split('?')[0].split('#')[0])


def looks_like_local_path(t):
    # ignore template tags, code fragments, and HTML-like tokens
    if any(ch in t for ch in ('{', '}', '<', '>', '$')):
        return False
    if t.startswith(('/', './', '../')):
        return True
    if '/' in t:
        return True
    lower = t.lower()
    for e in ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.html', '.htm', '.md', '.markdown', '.pdf', '.zip', '.tar', '.gz', '.js', '.css'):
        if lower.endswith(e):
            return True
    return False

for dirpath, dirs, files in os.walk(root):
    if any(part in ('_site', '.git', 'venv-utility', 'node_modules') for part in dirpath.split(os.sep)):
        continue
    for fname in files:
        if not fname.lower().endswith(('.md', '.markdown', '.html', '.htm')):
            continue
        fp = os.path.join(dirpath, fname)
        try:
            with open(fp, encoding='utf-8', errors='ignore') as fh:
                s = fh.read()
        except Exception:
            continue
        for pat in patterns:
            for m in pat.findall(s):
                target = m.strip()
                if not target or target.startswith('#'):
                    continue
                if target.startswith(skip_schemes):
                    continue
                if not looks_like_local_path(target):
                    continue
                t = norm(target)
                if t.startswith('/'):
                    cand = os.path.join(root, t.lstrip('/'))
                    cands = [cand]
                else:
                    cand = os.path.normpath(os.path.join(dirpath, t))
                    cands = [cand]
                    base, ext = os.path.splitext(cand)
                    if ext == '':
                        for e in exts_try:
                            cands.append(base + e)
                        cands.append(os.path.join(cand, 'index.html'))
                exists = any(os.path.exists(c) for c in cands)
                if not exists:
                    missing.setdefault(fp, []).append((target, cands))

if not missing:
    print("No local missing files found.")
else:
    print("Missing local targets:")
    for src, items in sorted(missing.items()):
        print(f"\nIn {src}:")
        for target, cands in items:
            print(f"  -> {target}")
            for c in cands:
                print(f"     checked: {c} {'(exists)' if os.path.exists(c) else '(missing)'}")
