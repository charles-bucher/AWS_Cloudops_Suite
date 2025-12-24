#!/usr/bin/env python3
"""
README Validator for AWS_Cloud_Support_Sim
Validates README.md files and ensures screenshots and sections exist.
"""

import os
import sys
import re

# ----------------------
# Configuration
# ----------------------
REQUIRED_SECTIONS = [
    "TL;DR",
    "Quick Start",
    "Incident Scenarios",
    "Installation",
    "Skills",
    "License",
    "Contact"
]

REQUIRED_TABLE_COLUMNS = ["ID", "Incident", "Services", "Difficulty", "Status"]

# ----------------------
# Helper functions
# ----------------------
def check_sections(content):
    warnings = []
    for section in REQUIRED_SECTIONS:
        if section not in content:
            warnings.append(f"Missing section: '{section}'")
    return warnings

def check_tables(content):
    warnings = []
    tables = re.findall(r'\|.*\|', content)
    for table in tables:
        headers = [h.strip() for h in table.split('|') if h.strip()]
        missing_cols = [col for col in REQUIRED_TABLE_COLUMNS if col not in headers]
        for col in missing_cols:
            warnings.append(f"Missing column in table: '{col}'")
    return warnings

def check_images(content, repo_root):
    warnings = []
    images = re.findall(r'!\[.*?\]\((.*?)\)', content)
    for img in images:
        img_path = os.path.join(repo_root, img)
        if not os.path.exists(img_path):
            warnings.append(f"Image does not exist: {img}")
    return warnings

def check_trailing_whitespace(content):
    warnings = []
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.rstrip() != line:
            warnings.append(f"Trailing whitespace on line {i+1}")
    return warnings

# ----------------------
# Main validation
# ----------------------
def validate_readme(readme_path, repo_root=None):
    if repo_root is None:
        repo_root = os.path.dirname(readme_path)
    if not os.path.exists(readme_path):
        print(f"ERROR: README.md not found at {readme_path}")
        return

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    warnings = []
    warnings += check_sections(content)
    warnings += check_tables(content)
    warnings += check_images(content, repo_root)
    warnings += check_trailing_whitespace(content)

    print("\n" + "="*60)
    if warnings:
        print(f"⚠️  WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  • {w}")
    else:
        print("✅ No warnings found.")

    print("="*60 + "\n")

# ----------------------
# Entry point
# ----------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python README_VALIDATOR.py <path_to_README.md> [repo_root]")
        sys.exit(1)

    readme_path = sys.argv[1]
    repo_root = sys.argv[2] if len(sys.argv) > 2 else None

    validate_readme(readme_path, repo_root)
