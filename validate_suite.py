import os
import sys
import ast

# Config: required folders and files
REQUIRED_FOLDERS = ["src", "scripts", "screenshots"]
REQUIRED_FILES = ["README.md", "LICENSE", "SECURITY.md"]
README_IMAGE_DIR = "screenshots"

def check_folders():
    print("Checking folders...")
    missing = []
    for folder in REQUIRED_FOLDERS:
        if not os.path.isdir(folder):
            missing.append(folder)
    if missing:
        print(f"❌ Missing folders: {missing}")
    else:
        print("✅ All required folders exist.")

def check_files():
    print("\nChecking required files...")
    missing = []
    for file in REQUIRED_FILES:
        if not os.path.isfile(file):
            missing.append(file)
        else:
            if os.path.getsize(file) == 0:
                print(f"⚠️ {file} exists but is empty.")
    if missing:
        print(f"❌ Missing files: {missing}")
    else:
        print("✅ All required files exist and are non-empty.")

def check_python_scripts():
    print("\nChecking Python scripts in src/ and scripts/...")
    folders_to_check = ["src", "scripts"]
    errors = []
    for folder in folders_to_check:
        if not os.path.isdir(folder):
            continue
        for root, _, files in os.walk(folder):
            for f in files:
                if f.endswith(".py"):
                    path = os.path.join(root, f)
                    if os.path.getsize(path) == 0:
                        errors.append(f"{path} is empty")
                        continue
                    try:
                        with open(path, "r", encoding="utf-8") as file:
                            ast.parse(file.read())
                    except Exception as e:
                        errors.append(f"{path} parse error: {e}")
    if errors:
        print("❌ Python script issues:")
        for e in errors:
            print("   -", e)
    else:
        print("✅ All Python scripts parse correctly.")

def check_readme_images():
    print("\nChecking README images...")
    if not os.path.isfile("README.md"):
        print("⚠️ README.md missing, skipping image check")
        return
    missing_images = []
    with open("README.md", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("![") and "](" in line:
                img_path = line.split("](")[1].split(")")[0]
                # Normalize relative paths
                img_path = os.path.join(os.getcwd(), img_path)
                if not os.path.isfile(img_path):
                    missing_images.append(img_path)
    if missing_images:
        print("❌ Missing images referenced in README:")
        for img in missing_images:
            print("   -", img)
    else:
        print("✅ All README images exist.")

def check_repo_structure():
    check_folders()
    check_files()
    check_python_scripts()
    check_readme_images()

if __name__ == "__main__":
    print("Starting repository validation...\n")
    check_repo_structure()
    print("\nValidation complete.")
