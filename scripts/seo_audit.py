#!/usr/bin/env python3
"""Lightweight SEO checks for PromptSeen AI static HTML pages."""
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
HTML = sorted(ROOT.rglob("*.html"))
ERRORS = []
WARNINGS = []

for path in HTML:
    if any(part.startswith(".") for part in path.relative_to(ROOT).parts):
        continue
    raw = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    title = re.search(r"<title>(.*?)</title>", raw, re.I | re.S)
    desc = re.search(r'<meta name="description" content="([^"]*)"', raw, re.I)
    canonical = re.search(r'<link rel="canonical" href="([^"]+)"', raw, re.I)
    h1 = re.findall(r"<h1\b[^>]*>(.*?)</h1>", raw, re.I | re.S)
    if not title or not title.group(1).strip():
        ERRORS.append(f"{rel}: missing title")
    elif len(title.group(1)) > 70:
        WARNINGS.append(f"{rel}: title may be long ({len(title.group(1))} chars)")
    if not desc or not desc.group(1).strip():
        ERRORS.append(f"{rel}: missing meta description")
    elif len(desc.group(1)) > 170:
        WARNINGS.append(f"{rel}: description may be long ({len(desc.group(1))} chars)")
    if not canonical:
        ERRORS.append(f"{rel}: missing canonical URL")
    if len(h1) != 1:
        WARNINGS.append(f"{rel}: expected one H1; found {len(h1)}")
    if 'name="robots"' not in raw:
        WARNINGS.append(f"{rel}: missing robots meta directive")

sitemap = ROOT / "sitemap.xml"
try:
    tree = ET.parse(sitemap)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    for loc in tree.findall(".//sm:loc", ns):
        if not loc.text or not loc.text.startswith("https://promptseen-ai.github.io/"):
            ERRORS.append(f"sitemap: invalid URL entry {loc.text!r}")
except Exception as exc:
    ERRORS.append(f"sitemap.xml parse error: {exc}")

for name in ("robots.txt", "llms.txt"):
    if not (ROOT / name).exists():
        ERRORS.append(f"missing required file: {name}")

for warning in WARNINGS:
    print("WARN:", warning)
for error in ERRORS:
    print("ERROR:", error)
print(f"SEO audit scanned {len(HTML)} HTML file(s), {len(ERRORS)} error(s), {len(WARNINGS)} warning(s).")
sys.exit(1 if ERRORS else 0)
