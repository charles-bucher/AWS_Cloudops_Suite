import os
import re

# Get AWS account ID and bucket name from environment variables
AWS_ACCOUNT_ID = os.getenv("AWS_ACCOUNT_ID", "722631436033")
BUCKET_NAME = "charles-dr-simulation-tfstate"

# Regex patterns for placeholders
PLACEHOLDER_PATTERNS = [
    r"<YOUR_.*?>",
    r"ACCOUNT_ID",
    r"BUCKET_NAME",
    r"123456789012",
    rf"arn:aws:.*?:{AWS_ACCOUNT_ID}:.*",
    r"INSERT_.*",
    r"CHANGE_.*",
    r"UPDATE_.*"
]

def scan_placeholders(repo_path="."):
    print("\n🔍 Detecting Placeholders...")
    found = False
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith((".py", ".tf")):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                for pattern in PLACEHOLDER_PATTERNS:
                    if re.search(pattern, content):
                        print(f"  📍 {file_path} - {pattern}")
                        found = True
    if not found:
        print("🎉 No placeholders found! Everything is replaced.")

if __name__ == "__main__":
    repo_path = input("Enter repository path (or press Enter for current directory): ").strip()
    if not repo_path:
        repo_path = "."
    scan_placeholders(repo_path)
