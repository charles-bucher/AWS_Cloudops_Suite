
import re
import os
import subprocess
from pathlib import Path
import requests

README_PATH = Path("README.md")
PLACEHOLDERS = ["TODO", "FIXME", "PLACEHOLDER", "Placeholder content"]

# --------------------
# Helper Functions
# --------------------
def check_markdown_headers(lines):
    """Ensure proper header order (#, ##, ###)"""
    issues = []
    header_level = 0
    for idx, line in enumerate(lines):
        if line.startswith("#"):
            current_level = len(line.split()[0])
            if current_level - header_level > 1:
                issues.append((idx+1, line.strip()))
            header_level = current_level
    return issues

def check_placeholders(lines):
    flagged = []
    for idx, line in enumerate(lines):
        for kw in PLACEHOLDERS:
            if kw.lower() in line.lower():
                flagged.append((idx+1, line.strip()))
    return flagged

def check_image_links(lines):
    broken = []
    img_regex = re.compile(r"!\[.*?\]\((.*?)\)")
    for idx, line in enumerate(lines):
        match = img_regex.search(line)
        if match:
            img_path = match.group(1)
            if not Path(img_path).exists():
                broken.append((idx+1, img_path))
    return broken

def check_links(lines):
    broken = []
    link_regex = re.compile(r"\[.*?\]\((.*?)\)")
    for idx, line in enumerate(lines):
        match = link_regex.search(line)
        if match:
            url = match.group(1)
            if url.startswith("http"):
                try:
                    r = requests.head(url, timeout=3)
                    if r.status_code >= 400:
                        broken.append((idx+1, url))
                except:
                    broken.append((idx+1, url))
    return broken

def auto_fix_headers(lines):
    """Simple auto-fix: remove extra spaces in headers"""
    fixed = []
    for line in lines:
        if line.startswith("#"):
            fixed.append(re.sub(r"#\s+", lambda m: "#"*len(m.group(0)) + " ", line))
        else:
            fixed.append(line)
    return fixed

# --------------------
# Main
# --------------------
if not README_PATH.exists():
    print("[ERROR] README.md not found")
    exit(1)

with open(README_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Check headers
header_issues = check_markdown_headers(lines)
# Check placeholders
placeholders = check_placeholders(lines)
# Check image links
broken_images = check_image_links(lines)
# Check hyperlinks
broken_links = check_links(lines)

# Attempt simple fixes
lines_fixed = auto_fix_headers(lines)

# Write back auto-fixed README
with open(README_PATH, "w", encoding="utf-8") as f:
    f.writelines(lines_fixed)

# --------------------
# Summary / Percentages
# --------------------
total_checks = 4  # headers, placeholders, images, links
passed_checks = total_checks
if header_issues:
    passed_checks -=1
if placeholders:
    passed_checks -=1
if broken_images:
    passed_checks -=1
if broken_links:
    passed_checks -=1

print("\n[README Deep Validation & Auto-Fix Report]\n")
print(f"Headers issues: {len(header_issues)} lines")
for idx, line in header_issues:
    print(f" - Line {idx}: {line}")
print(f"Placeholders found: {len(placeholders)} lines")
for idx, line in placeholders:
    print(f" - Line {idx}: {line}")
print(f"Broken images: {len(broken_images)}")
for idx, img in broken_images:
    print(f" - Line {idx}: {img}")
print(f"Broken links: {len(broken_links)}")
for idx, url in broken_links:
    print(f" - Line {idx}: {url}")

print(f"\nREADME Health: {round(passed_checks/total_checks*100,1)}%")

print("\n[INFO] Auto-fixed header formatting. Review placeholders, broken links/images manually.")
