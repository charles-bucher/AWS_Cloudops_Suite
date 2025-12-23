import subprocess
from pathlib import Path


# -----------------------------
# Helper Functions
# -----------------------------
def calculate_percentage(total, passed):
    return round((passed / total) * 100, 2) if total else 100.0


def run_command(command):
    """Run a shell command and return (returncode, stdout, stderr)"""
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.returncode, result.stdout, result.stderr


def normalize_filename(filename):
    return filename.lower().replace(" ", "_")


def find_placeholders(file_path, placeholders=None):
    placeholders = placeholders or [
        "TODO",
        "does this need backend",
        "FIXME",
        "PLACEHOLDER",
    ]
    content = file_path.read_text(errors="ignore")
    hits = []
    for p in placeholders:
        if p.lower() in content.lower():
            hits.append(p)
    return hits


# -----------------------------
# Python Auto-Fix & Lint
# -----------------------------
print("[INFO] Removing unused imports with autoflake...")
run_command("python -m autoflake --remove-all-unused-imports --in-place --recursive .")

print("[INFO] Formatting Python files with Black...")
run_command("python -m black .")

print("[INFO] Linting Python files with Flake8...")
py_files = list(Path(".").rglob("*.py"))
py_clean = 0
py_placeholders = {}
for f in py_files:
    # Placeholder scan
    ph_hits = find_placeholders(f)
    if ph_hits:
        py_placeholders[f] = ph_hits

    ret, out, err = run_command(f"python -m flake8 {f} --max-line-length=120")
    if not out.strip():
        py_clean += 1
py_percent = calculate_percentage(len(py_files), py_clean)

# -----------------------------
# Terraform Validation
# -----------------------------
print("[INFO] Validating Terraform files...")
tf_files = list(Path(".").rglob("*.tf"))
tf_valid = 0
tf_placeholders = {}
for f in tf_files:
    # Placeholder scan
    ph_hits = find_placeholders(f)
    if ph_hits:
        tf_placeholders[f] = ph_hits
        print(f"[WARNING] Placeholder found in {f}, skipping validate.")
        continue
    ret, out, err = run_command(f"terraform validate {f.parent}")
    if ret == 0:
        tf_valid += 1
tf_percent = calculate_percentage(len(tf_files), tf_valid)

# -----------------------------
# PowerShell Validation
# -----------------------------
print("[INFO] Auto-fixing PowerShell scripts...")
ps_files = list(Path("./scripts").rglob("*.ps1"))
ps_clean = 0
ps_placeholders = {}
for f in ps_files:
    run_command(f"powershell.exe -Command Invoke-ScriptAnalyzer -Path '{f}' -Fix")
    # Placeholder scan
    ph_hits = find_placeholders(f)
    if ph_hits:
        ps_placeholders[f] = ph_hits
    ret, out, err = run_command(
        f"powershell.exe -Command Invoke-ScriptAnalyzer -Path '{f}'"
    )
    if "Warning" not in out:
        ps_clean += 1
ps_percent = calculate_percentage(len(ps_files), ps_clean)

# -----------------------------
# Screenshot Normalization
# -----------------------------
print("[INFO] Normalizing screenshot file names...")
screenshots = list(Path("./screenshots").rglob("*"))
img_files = [f for f in screenshots if f.suffix.lower() in (".png", ".jpg", ".jpeg")]
normalized_count = 0
for f in img_files:
    new_name = normalize_filename(f.name)
    new_path = f.parent / new_name
    if f.name != new_name:
        f.rename(new_path)
    normalized_count += 1
img_percent = calculate_percentage(len(img_files), normalized_count)

# -----------------------------
# Git: Stage, Commit, Push
# -----------------------------
print("[INFO] Staging all changes...")
run_command("git add .")

print("[INFO] Committing changes...")
commit_msg = "Auto-fix: Python, Terraform, PowerShell, screenshots"
ret, out, err = run_command(f'git commit -m "{commit_msg}"')
if ret != 0:
    print(f"[WARNING] Git commit failed (maybe nothing to commit): {err}")

print("[INFO] Pushing to origin main...")
run_command("git push")

# -----------------------------
# Final Report
# -----------------------------
print("\n[DONE] Repo Auto-Fix & Validation Report:")
print(f"Python: {py_percent}% clean ({py_clean}/{len(py_files)})")
print(f"Terraform: {tf_percent}% valid ({tf_valid}/{len(tf_files)})")
print(f"PowerShell: {ps_percent}% warning-free ({ps_clean}/{len(ps_files)})")
print(f"Screenshots: {img_percent}% normalized ({normalized_count}/{len(img_files)})")

# -----------------------------
# Placeholders Report
# -----------------------------
all_placeholders = {
    "Python": py_placeholders,
    "Terraform": tf_placeholders,
    "PowerShell": ps_placeholders,
}
print("\n[INFO] Placeholder Scan Report:")
for category, files in all_placeholders.items():
    if files:
        print(f"\n{category} files needing attention:")
        for f, ph in files.items():
            print(f" - {f}: {', '.join(ph)}")
    else:
        print(f"\n{category}: No placeholders found ✅")
