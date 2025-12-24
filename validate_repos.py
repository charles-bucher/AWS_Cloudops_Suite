import os
import re

class RepoValidator:
    def __init__(self, repo_root="."):
        self.repo_root = repo_root
        self.warnings = []
        self.passed_checks = 0

    def validate_readme(self, readme_path):
        if not os.path.isfile(readme_path):
            self.warnings.append(f"[WARN] README.md not found: {readme_path}")
            return

        with open(readme_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Check for required sections
        required_sections = ["TL;DR", "Incident Scenarios", "Installation", "Skills"]
        for section in required_sections:
            if not any(re.search(rf"^\s*#+\s*{section}", line) for line in lines):
                self.warnings.append(f"[WARN] Missing section: '{section}' in {readme_path}")

        # Check for trailing whitespace
        for i, line in enumerate(lines):
            if line.rstrip() != line:
                self.warnings.append(f"[WARN] Trailing whitespace on line {i+1} in {readme_path}")

        # Simple table header validation
        table_headers = ["ID", "Incident", "Services", "Difficulty", "Status"]
        table_found = any(all(header in line for header in table_headers) for line in lines)
        if not table_found:
            self.warnings.append(f"[WARN] Missing columns in table: {table_headers} in {readme_path}")
        else:
            self.passed_checks += 1

    def validate_screenshots(self, scenario_path):
        screenshots_path = os.path.join(scenario_path, "screenshots")
        if not os.path.isdir(screenshots_path):
            self.warnings.append(f"[WARN] No screenshot directory in {scenario_path}")
        else:
            images = [f for f in os.listdir(screenshots_path) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
            if not images:
                self.warnings.append(f"[WARN] No screenshots found in {screenshots_path}")
            else:
                self.passed_checks += 1

    def run(self):
        scenario_folders = [f for f in os.listdir(self.repo_root) if f.startswith("0") and os.path.isdir(os.path.join(self.repo_root, f))]
        for scenario in scenario_folders:
            scenario_path = os.path.join(self.repo_root, scenario)
            readme_path = os.path.join(scenario_path, "README.md")
            self.validate_readme(readme_path)
            self.validate_screenshots(scenario_path)

        # Summary
        print("="*60)
        if self.warnings:
            print(f"⚠️  WARNINGS ({len(self.warnings)}):")
            for w in self.warnings:
                print(f"  • {w}")
        else:
            print("✅ No warnings found.")
        print("="*60)
        print(f"Passed checks: {self.passed_checks}")

if __name__ == "__main__":
    validator = RepoValidator(repo_root=".")
    validator.run()
