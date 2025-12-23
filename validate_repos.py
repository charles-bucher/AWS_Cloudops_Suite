import os
import subprocess
import sys

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))


def run(cmd, cwd=REPO_ROOT, check=True):
    print(f"[RUN] {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)
    if check and result.returncode != 0:
        print(f"[ERROR] Command failed: {' '.join(cmd)}")
    return result


def python_auto_fix():
    print("[INFO] Removing unused imports with autoflake...")
    run(
        [
            sys.executable,
            "-m",
            "autoflake",
            "--remove-all-unused-imports",
            "--in-place",
            "--recursive",
            ".",
        ]
    )

    print("[INFO] Formatting Python files with Black...")
    run([sys.executable, "-m", "black", "."])

    print("[INFO] Linting Python files with Flake8...")
    run([sys.executable, "-m", "flake8", ".", "--max-line-length=120"])


def terraform_validate():
    backend_file = os.path.join(REPO_ROOT, "Backend.tf")
    if os.path.exists(backend_file):
        with open(backend_file, "r") as f:
            content = f.read()
            if "does this need backend" in content:
                print(
                    "[WARNING] Placeholder text found in Backend.tf, skipping init/validate."
                )
                return
    print("[INFO] Initializing Terraform...")
    run(["terraform", "init", "-input=false"], check=False)
    print("[INFO] Validating Terraform...")
    run(["terraform", "validate"], check=False)


def powershell_fix():
    scripts_dir = os.path.join(REPO_ROOT, "scripts")
    if os.path.exists(scripts_dir):
        for file in os.listdir(scripts_dir):
            if file.endswith(".ps1"):
                full_path = os.path.join(scripts_dir, file)
                print(f"[INFO] Auto-fixing PowerShell script: {file}")
                # Use PowerShell instead of pwsh for Windows compatibility
                run(
                    [
                        "powershell.exe",
                        "-Command",
                        f"Invoke-ScriptAnalyzer -Path '{full_path}' -Fix",
                    ],
                    check=False,
                )


def normalize_screenshots():
    screenshots_dir = os.path.join(REPO_ROOT, "screenshots")
    if os.path.exists(screenshots_dir):
        print("[INFO] Normalizing screenshot file names...")
        for file in os.listdir(screenshots_dir):
            old_path = os.path.join(screenshots_dir, file)
            new_name = file.lower().replace(" ", "_")
            new_path = os.path.join(screenshots_dir, new_name)
            if old_path != new_path:
                os.rename(old_path, new_path)


def git_commit_push():
    print("[INFO] Staging all changes...")
    run(["git", "add", "."])
    # Only commit if there are changes
    result = run(["git", "diff", "--cached", "--quiet"], check=False)
    if result.returncode != 0:
        print("[INFO] Committing changes...")
        run(
            [
                "git",
                "commit",
                "-m",
                "Auto-fix: Python, Terraform, PowerShell, screenshots",
            ]
        )
        print("[INFO] Pushing to origin main...")
        run(["git", "push"])
    else:
        print("[INFO] No changes to commit.")


if __name__ == "__main__":
    print("[START] Repo Auto-Fix & Validator running...")
    python_auto_fix()
    terraform_validate()
    powershell_fix()
    normalize_screenshots()
    git_commit_push()
    print("[DONE] Repo auto-fix completed successfully!")
