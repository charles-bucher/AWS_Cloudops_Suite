import os
import argparse
from pathlib import Path

# =======================
# REPO CONFIG (EDIT PER REPO)
# =======================

REPO_PROFILE = {
    "name": "AWS Cloud Repo",
    "required_sections": [
        "Overview",
        "Architecture",
        "Failure",
        "Investigation",
        "Root Cause",
        "Remediation",
        "Prevention"
    ],
    "required_extensions": [".py", ".tf"],
    "min_python_loc": 300,
    "min_readme_words": 400,
    "require_screenshots": True,
    "require_logs": True
}

PLACEHOLDER_PATTERNS = [
    "todo",
    "lorem ipsum",
    "coming soon",
    "placeholder",
    "tbd"
]

IMAGE_EXTENSIONS = [".png", ".jpg", ".jpeg", ".gif", ".webp"]

# =======================
# SCAN FUNCTIONS
# =======================

def count_python_loc(base):
    loc = 0
    for root, _, files in os.walk(base):
        for f in files:
            if f.endswith(".py"):
                with open(os.path.join(root, f), encoding="utf-8", errors="ignore") as fh:
                    for line in fh:
                        if line.strip() and not line.strip().startswith("#"):
                            loc += 1
    return loc


def scan_placeholders(base):
    hits = []
    for root, _, files in os.walk(base):
        for f in files:
            path = os.path.join(root, f)
            try:
                with open(path, encoding="utf-8", errors="ignore") as fh:
                    content = fh.read().lower()
                    for p in PLACEHOLDER_PATTERNS:
                        if p in content:
                            hits.append(path)
                            break
            except:
                pass
    return hits


def analyze_readme(base):
    readme = Path(base) / "README.md"
    if not readme.exists():
        return 0, REPO_PROFILE["required_sections"]

    text = readme.read_text(encoding="utf-8", errors="ignore")
    words = len(text.split())

    missing_sections = [
        s for s in REPO_PROFILE["required_sections"]
        if s.lower() not in text.lower()
    ]

    return words, missing_sections


def find_files_by_extension(base, ext):
    matches = []
    for root, _, files in os.walk(base):
        for f in files:
            if f.endswith(ext):
                matches.append(os.path.join(root, f))
    return matches


def find_screenshots(base):
    screenshots = []
    for root, _, files in os.walk(base):
        for f in files:
            if any(f.lower().endswith(ext) for ext in IMAGE_EXTENSIONS):
                full_path = os.path.join(root, f)
                try:
                    # Ignore tiny junk / empty images
                    if os.path.getsize(full_path) > 10_000:
                        screenshots.append(full_path)
                except:
                    pass
    return screenshots


def find_logs(base):
    logs = []
    for root, _, files in os.walk(base):
        for f in files:
            if "log" in f.lower() or f.lower().endswith(".log"):
                logs.append(os.path.join(root, f))
    return logs

# =======================
# MAIN VALIDATION
# =======================

def main(repo_path):
    score = 100
    issues = []

    # Python LOC
    py_loc = count_python_loc(repo_path)
    if py_loc < REPO_PROFILE["min_python_loc"]:
        score -= 20
        issues.append(f"Low Python LOC ({py_loc})")

    # README
    readme_words, missing_sections = analyze_readme(repo_path)
    if readme_words < REPO_PROFILE["min_readme_words"]:
        score -= 15
        issues.append(f"Thin README ({readme_words} words)")

    if missing_sections:
        score -= 15
        issues.append(f"Missing README sections: {missing_sections}")

    # Placeholders
    placeholders = scan_placeholders(repo_path)
    if placeholders:
        score -= 20
        issues.append(f"Placeholder content found in {len(placeholders)} files")

    # Required file types
    for ext in REPO_PROFILE["required_extensions"]:
        if not find_files_by_extension(repo_path, ext):
            score -= 10
            issues.append(f"Missing required file type: {ext}")

    # Screenshots / diagrams (recursive)
    screenshots = find_screenshots(repo_path)
    if REPO_PROFILE["require_screenshots"] and not screenshots:
        score -= 15
        issues.append("No screenshots or diagrams found anywhere in repo")

    # Architecture-specific screenshot signal
    diagram_hits = [
        s for s in screenshots
        if "diagram" in s.lower() or "arch" in s.lower()
    ]
    if REPO_PROFILE["require_screenshots"] and screenshots and not diagram_hits:
        score -= 10
        issues.append("Screenshots found, but no architecture/diagram evidence")

    # Logs / investigation artifacts
    logs = find_logs(repo_path)
    if REPO_PROFILE["require_logs"] and not logs:
        score -= 10
        issues.append("No logs or investigation artifacts found")

    # =======================
    # REPORT
    # =======================

    print("\n=== REPO VALIDATION REPORT ===")
    print(f"Repo: {REPO_PROFILE['name']}")
    print(f"Final Score: {max(score, 0)}/100")

    if issues:
        print("\nIssues:")
        for i in issues:
            print(f"- {i}")
    else:
        print("\nNo issues detected. Strong hire signal.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deep repository validator")
    parser.add_argument("repo_path", help="Path to repository")
    args = parser.parse_args()
    main(args.repo_path)
