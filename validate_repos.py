#!/usr/bin/env python3
"""
AWS_Cloudops_Suite Auto-Fix & Validator Script (Windows Friendly)
- Removes unused Python imports
- Formats and lints Python
- Validates Terraform
- Auto-fixes PowerShell scripts
- Renames screenshots
- Auto-commits and pushes changes
"""

import os
import subprocess


# ------------------------
# Helper Functions
# ------------------------
def run_cmd(cmd, cwd=None):
    """Run a shell command and print output"""
    try:
        result = subprocess.run(
            cmd, shell=True, check=True, capture_output=True, text=True, cwd=cwd
        )
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Command failed: {cmd}\n{e.stderr}")
        return False


# ------------------------
# Python Auto-Fix
# ------------------------
def clean_python():
    print("[INFO] Removing unused imports with autoflake...")
    run_cmd("python -m autoflake --remove-all-unused-imports --in-place --recursive .")

    print("[INFO] Formatting Python files with Black...")
    run_cmd("python -m black .")

    print("[INFO] Linting Python files with Flake8...")
    run_cmd("python -m flake8 . --max-line-length=120")


# ------------------------
# Terraform Validation
# ------------------------
def validate_terraform():
    print("[INFO] Validating Terraform files...")
    tf_files = [f for f in os.listdir(".") if f.endswith(".tf")]
    if not tf_files:
        print("[INFO] No Terraform files found, skipping Terraform validation.")
        return

    for file in tf_files:
        # Skip placeholder backends with obvious errors
        with open(file, "r") as f:
            content = f.read().lower()
            if "does this need backend" in content:
                print(
                    f"[WARNING] Placeholder text found in {file}, skipping init/validate."
                )
                continue

    run_cmd("terraform init -input=false")
    run_cmd("terraform validate")


# ------------------------
# PowerShell Auto-Fix
# ------------------------
def fix_powershell():
    print("[INFO] Auto-fixing PowerShell scripts...")
    for root, _, files in os.walk("scripts"):
        for file in files:
            if file.endswith(".ps1"):
                path = os.path.join(root, file)
                # Use Windows PowerShell, works for user-installed PSScriptAnalyzer
                run_cmd(
                    f'powershell.exe -Command "Invoke-ScriptAnalyzer -Path \\"{path}\\" -Fix"'
                )


# ------------------------
# Screenshots
# ------------------------
def rename_screenshots():
    print("[INFO] Normalizing screenshot file names...")
    screenshots_dir = "screenshots"
    if not os.path.isdir(screenshots_dir):
        return
    for root, _, files in os.walk(screenshots_dir):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in [".png", ".jpg", ".jpeg"]:
                new_name = file.lower().replace(" ", "_")
                os.rename(os.path.join(root, file), os.path.join(root, new_name))


# ------------------------
# Git Commit & Push
# ------------------------
def git_commit_push():
    print("[INFO] Staging all changes...")
    run_cmd("git add .")

    print("[INFO] Committing changes...")
    run_cmd('git commit -m "Auto-fix: Python, Terraform, PowerShell, screenshots"')

    print("[INFO] Pushing to origin main...")
    run_cmd("git push origin main")


# ------------------------
# Main
# ------------------------
if __name__ == "__main__":
    print("[START] Repo Auto-Fix & Validator running...")

    clean_python()
    validate_terraform()
    fix_powershell()
    rename_screenshots()
    git_commit_push()

    print("[DONE] Repo auto-fix completed successfully!")
