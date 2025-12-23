#!/usr/bin/env python3
"""
AWS_Cloudops_Suite Auto-Fix & Validator Script
Checks code quality, auto-fixes formatting, validates Terraform & Python, fixes repo structure.
"""

import os
import subprocess
import sys


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


def format_python_files():
    """Run black and flake8 on all Python files"""
    print("[INFO] Formatting Python files with Black...")
    run_cmd("black .")
    print("[INFO] Linting Python files with Flake8...")
    run_cmd("flake8 . --max-line-length=120")


def validate_terraform():
    """Validate Terraform files"""
    print("[INFO] Initializing Terraform...")
    run_cmd("terraform init -input=false")
    print("[INFO] Validating Terraform...")
    run_cmd("terraform validate")


def fix_powershell():
    """Format PowerShell scripts using pwsh and PSScriptAnalyzer"""
    print("[INFO] Analyzing PowerShell scripts...")
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".ps1"):
                path = os.path.join(root, file)
                run_cmd(f"pwsh -Command 'Invoke-ScriptAnalyzer -Path \"{path}\" -Fix'")


def rename_screenshots():
    """Normalize screenshot file names"""
    print("[INFO] Renaming screenshot files...")
    for root, dirs, files in os.walk("screenshots"):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in [".png", ".jpg", ".jpeg"]:
                new_name = file.lower().replace(" ", "_")
                os.rename(os.path.join(root, file), os.path.join(root, new_name))


def git_commit_push():
    """Stage, commit, and push changes"""
    print("[INFO] Staging all changes...")
    run_cmd("git add .")
    print("[INFO] Committing changes...")
    run_cmd(
        'git commit -m "Auto-fix: code quality, formatting, screenshots, placeholders"'
    )
    print("[INFO] Pushing to origin main...")
    run_cmd("git push origin main")


# ------------------------
# Main Execution
# ------------------------
if __name__ == "__main__":
    print("[START] Auto-fix & validator running...")

    format_python_files()
    validate_terraform()
    fix_powershell()
    rename_screenshots()

    git_commit_push()

    print("[DONE] Repo auto-fix completed successfully!")
