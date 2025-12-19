#!/usr/bin/env python3
"""
AWS CloudOps Suite - Complete Repository Validator
Author: Charles Bucher
Purpose: Verify AWS_CloudOps_Suite has all critical files for CloudOps/DevOps roles

This validator checks EVERYTHING needed for CloudOps Engineer positions:
- Infrastructure as Code (Terraform)
- Automation scripts (Python)
- Lambda functions
- Monitoring & remediation
- Professional documentation
- CI/CD pipelines
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple
from datetime import datetime


class CloudOpsSuiteValidator:
    """Validates AWS CloudOps Suite repository"""
    
    def __init__(self, repo_path: str = "."):
        self.repo_path = Path(repo_path)
        self.critical_issues = []
        self.warnings = []
        self.successes = []
        self.score = 0
        self.max_score = 0
        
    def add_points(self, points: int, message: str):
        """Add points for completeness"""
        self.score += points
        self.max_score += points
        self.successes.append(f"✅ [{points:2d}pts] {message}")
    
    def lose_points(self, points: int, message: str, is_critical: bool = True):
        """Lose points for missing items"""
        self.max_score += points
        if is_critical:
            self.critical_issues.append(f"❌ CRITICAL [-{points}pts] {message}")
        else:
            self.warnings.append(f"⚠️  WARNING  [-{points}pts] {message}")
    
    # ==================== ROOT LEVEL FILES ====================
    
    def check_root_files(self):
        """Check critical root-level files"""
        print("\n" + "="*80)
        print("1️⃣  ROOT LEVEL FILES (Infrastructure Foundation)")
        print("="*80)
        
        root_files = {
            "README.md": (10, "Main documentation"),
            "LICENSE": (3, "Open source license"),
            ".gitignore": (2, "Git hygiene"),
            "Backend.tf": (5, "Terraform backend config"),
            "backend.conf": (3, "Backend configuration"),
            "main.tf": (8, "Main Terraform entry point"),
            "outputs.tf": (4, "Terraform outputs"),
            "provider.tf": (5, "AWS provider config"),
            "variables.tf": (5, "Terraform variables")
        }
        
        for filename, (points, purpose) in root_files.items():
            filepath = self.repo_path / filename
            if filepath.exists():
                self.add_points(points, f"{filename:20s} - {purpose}")
            else:
                is_critical = points >= 5
                self.lose_points(points, f"Missing {filename} - {purpose}", is_critical)
    
    # ==================== TERRAFORM DIRECTORY ====================
    
    def check_terraform_directory(self):
        """Check terraform/ directory structure"""
        print("\n" + "="*80)
        print("2️⃣  TERRAFORM DIRECTORY (IaC Organization)")
        print("="*80)
        
        terraform_dir = self.repo_path / "terraform"
        
        if not terraform_dir.exists():
            self.lose_points(20, "terraform/ directory missing - Core IaC structure!", True)
            return
        
        self.add_points(5, "terraform/ directory exists")
        
        # Check for organized Terraform structure
        tf_files = {
            "main.tf": (5, "Main infrastructure code"),
            "variables.tf": (4, "Variable definitions"),
            "outputs.tf": (3, "Output definitions"),
            "provider.tf": (3, "Provider configuration"),
            "versions.tf": (2, "Version constraints")
        }
        
        for filename, (points, purpose) in tf_files.items():
            filepath = terraform_dir / filename
            if filepath.exists():
                self.add_points(points, f"terraform/{filename:15s} - {purpose}")
            else:
                self.warnings.append(f"⚠️  [-{points}pts] terraform/{filename} missing - {purpose}")
                self.max_score += points
        
        # Check for module organization
        modules_dir = terraform_dir / "modules"
        if modules_dir.exists():
            self.add_points(5, "terraform/modules/ - Modular architecture")
            
            # Check for common modules
            common_modules = ["vpc", "ec2", "s3", "lambda", "iam", "monitoring"]
            found_modules = [d.name for d in modules_dir.iterdir() if d.is_dir()]
            
            for module in found_modules:
                if module in common_modules:
                    self.add_points(2, f"  └─ Module: {module}")
        
        # Check for environments
        environments = ["dev", "staging", "prod", "test"]
        for env in environments:
            env_dir = terraform_dir / env
            if env_dir.exists():
                self.add_points(3, f"terraform/{env}/ - Environment separation")
    
    # ==================== SCRIPTS DIRECTORY ====================
    
    def check_scripts_directory(self):
        """Check scripts/ directory"""
        print("\n" + "="*80)
        print("3️⃣  SCRIPTS DIRECTORY (Automation & Operations)")
        print("="*80)
        
        scripts_dir = self.repo_path / "scripts"
        
        if not scripts_dir.exists():
            self.lose_points(25, "scripts/ directory missing - No automation!", True)
            return
        
        self.add_points(5, "scripts/ directory exists")
        
        # Critical CloudOps scripts
        critical_scripts = {
            "monitoring.py": (8, "Monitoring automation"),
            "remediation.py": (8, "Auto-remediation"),
            "alerts.py": (6, "Alert management"),
            "backup.py": (5, "Backup automation"),
            "cost_optimization.py": (5, "Cost management"),
            "security_audit.py": (5, "Security auditing"),
            "health_check.py": (4, "Health checking"),
            "deployment.py": (4, "Deployment automation")
        }
        
        found_scripts = []
        try:
            all_files = list(scripts_dir.iterdir())
            py_files = [f for f in all_files if f.suffix == '.py' and f.is_file()]
            found_scripts = [f.name for f in py_files]
            
            for script_name, (points, purpose) in critical_scripts.items():
                if script_name in found_scripts:
                    self.add_points(points, f"scripts/{script_name:25s} - {purpose}")
                else:
                    is_critical = points >= 6
                    self.lose_points(points, f"Missing scripts/{script_name} - {purpose}", is_critical)
            
            # Bonus for additional scripts
            extra_scripts = set(found_scripts) - set(critical_scripts.keys())
            if extra_scripts:
                self.add_points(len(extra_scripts), f"Bonus: {len(extra_scripts)} additional scripts")
                
        except Exception as e:
            self.lose_points(10, f"Cannot check scripts/: {str(e)}", True)
    
    # ==================== LAMBDAS DIRECTORY ====================
    
    def check_lambdas_directory(self):
        """Check lambdas/ directory"""
        print("\n" + "="*80)
        print("4️⃣  LAMBDAS DIRECTORY (Serverless Functions)")
        print("="*80)
        
        lambdas_dir = self.repo_path / "lambdas"
        
        if not lambdas_dir.exists():
            self.lose_points(20, "lambdas/ directory missing - No serverless!", True)
            return
        
        self.add_points(5, "lambdas/ directory exists")
        
        # Check for Lambda functions
        try:
            subdirs = [d for d in lambdas_dir.iterdir() if d.is_dir()]
            
            if subdirs:
                self.add_points(5, f"Found {len(subdirs)} Lambda function(s)")
                
                for lambda_dir in subdirs:
                    lambda_name = lambda_dir.name
                    
                    # Check for required Lambda files
                    index_file = lambda_dir / "index.py"
                    requirements = lambda_dir / "requirements.txt"
                    
                    if index_file.exists():
                        self.add_points(3, f"  └─ {lambda_name}/index.py")
                    else:
                        self.warnings.append(f"⚠️  [-3pts] {lambda_name}/index.py missing")
                        self.max_score += 3
                    
                    if requirements.exists():
                        self.add_points(2, f"  └─ {lambda_name}/requirements.txt")
            else:
                # Check for flat structure
                index_file = lambdas_dir / "index.py"
                requirements = lambdas_dir / "requirements.txt"
                
                if index_file.exists():
                    self.add_points(5, "lambdas/index.py - Lambda handler")
                else:
                    self.lose_points(5, "lambdas/index.py missing", True)
                
                if requirements.exists():
                    self.add_points(3, "lambdas/requirements.txt - Dependencies")
                else:
                    self.warnings.append("⚠️  [-3pts] lambdas/requirements.txt missing")
                    self.max_score += 3
                    
        except Exception as e:
            self.lose_points(10, f"Cannot check lambdas/: {str(e)}", True)
    
    # ==================== DOCUMENTATION ====================
    
    def check_documentation(self):
        """Check documentation directory"""
        print("\n" + "="*80)
        print("5️⃣  DOCUMENTATION (Professional Communication)")
        print("="*80)
        
        docs_dir = self.repo_path / "docs"
        
        if not docs_dir.exists():
            self.warnings.append("⚠️  [-10pts] docs/ directory missing")
            self.max_score += 10
            return
        
        self.add_points(5, "docs/ directory exists")
        
        # Check for documentation files
        doc_files = {
            "architecture.md": (4, "Architecture documentation"),
            "deployment.md": (3, "Deployment guide"),
            "operations.md": (3, "Operations runbook"),
            "troubleshooting.md": (3, "Troubleshooting guide"),
            "setup.md": (2, "Setup instructions"),
            "monitoring.md": (2, "Monitoring guide"),
            "security.md": (2, "Security practices")
        }
        
        try:
            for doc_name, (points, purpose) in doc_files.items():
                doc_path = docs_dir / doc_name
                if doc_path.exists():
                    self.add_points(points, f"docs/{doc_name:20s} - {purpose}")
                else:
                    self.warnings.append(f"⚠️  [-{points}pts] docs/{doc_name} missing - {purpose}")
                    self.max_score += points
        except Exception as e:
            pass
    
    # ==================== DIAGRAMS ====================
    
    def check_diagrams(self):
        """Check diagrams directory"""
        print("\n" + "="*80)
        print("6️⃣  DIAGRAMS (Visual Architecture)")
        print("="*80)
        
        diagrams_dir = self.repo_path / "diagrams"
        
        if not diagrams_dir.exists():
            self.warnings.append("⚠️  [-8pts] diagrams/ directory missing")
            self.max_score += 8
            return
        
        self.add_points(4, "diagrams/ directory exists")
        
        try:
            diagram_files = [
                f for f in diagrams_dir.iterdir()
                if f.suffix.lower() in ['.png', '.jpg', '.jpeg', '.svg', '.pdf']
            ]
            
            if diagram_files:
                self.add_points(8, f"Found {len(diagram_files)} architecture diagram(s)")
                
                # Check for specific diagrams
                diagram_types = ['architecture', 'network', 'deployment', 'monitoring']
                for dtype in diagram_types:
                    if any(dtype in f.name.lower() for f in diagram_files):
                        self.add_points(2, f"  └─ Has {dtype} diagram")
            else:
                self.warnings.append("⚠️  [-8pts] No diagram files found")
                self.max_score += 8
        except Exception as e:
            pass
    
    # ==================== SCREENSHOTS ====================
    
    def check_screenshots(self):
        """Check screenshots directory"""
        print("\n" + "="*80)
        print("7️⃣  SCREENSHOTS (Implementation Proof)")
        print("="*80)
        
        screenshots_dir = self.repo_path / "screenshots"
        
        if not screenshots_dir.exists():
            self.warnings.append("⚠️  [-10pts] screenshots/ directory missing")
            self.max_score += 10
            return
        
        self.add_points(3, "screenshots/ directory exists")
        
        try:
            screenshot_files = [
                f for f in screenshots_dir.iterdir()
                if f.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif']
            ]
            
            count = len(screenshot_files)
            if count >= 5:
                self.add_points(10, f"Excellent: {count} screenshots")
            elif count >= 3:
                self.add_points(6, f"Good: {count} screenshots")
                self.max_score += 4
            elif count >= 1:
                self.add_points(3, f"Minimal: {count} screenshot(s)")
                self.max_score += 7
            else:
                self.warnings.append("⚠️  [-10pts] No screenshots found")
                self.max_score += 10
        except Exception as e:
            pass
    
    # ==================== TESTS ====================
    
    def check_tests(self):
        """Check tests directory"""
        print("\n" + "="*80)
        print("8️⃣  TESTS (Code Quality)")
        print("="*80)
        
        tests_dir = self.repo_path / "tests"
        
        if not tests_dir.exists():
            self.warnings.append("⚠️  [-8pts] tests/ directory missing")
            self.max_score += 8
            return
        
        self.add_points(3, "tests/ directory exists")
        
        try:
            test_files = [f for f in tests_dir.iterdir() if f.suffix == '.py']
            
            if test_files:
                self.add_points(8, f"Found {len(test_files)} test file(s)")
                
                # Check for test types
                test_types = ['unit', 'integration', 'terraform']
                for ttype in test_types:
                    if any(ttype in f.name.lower() for f in test_files):
                        self.add_points(2, f"  └─ Has {ttype} tests")
            else:
                self.warnings.append("⚠️  [-8pts] No test files found")
                self.max_score += 8
        except Exception as e:
            pass
    
    # ==================== CI/CD ====================
    
    def check_cicd(self):
        """Check CI/CD configuration"""
        print("\n" + "="*80)
        print("9️⃣  CI/CD PIPELINES (Automation)")
        print("="*80)
        
        github_dir = self.repo_path / ".github"
        
        if not github_dir.exists():
            self.warnings.append("⚠️  [-10pts] .github/ directory missing - No CI/CD")
            self.max_score += 10
            return
        
        self.add_points(3, ".github/ directory exists")
        
        # Check for workflows
        workflows_dir = github_dir / "workflows"
        if workflows_dir.exists():
            self.add_points(5, ".github/workflows/ - CI/CD pipelines")
            
            try:
                workflow_files = [f for f in workflows_dir.iterdir() if f.suffix in ['.yml', '.yaml']]
                
                if workflow_files:
                    self.add_points(10, f"Found {len(workflow_files)} workflow(s)")
                    
                    # Check for specific workflows
                    workflow_types = ['terraform', 'test', 'deploy', 'lint', 'security']
                    for wtype in workflow_types:
                        if any(wtype in f.name.lower() for f in workflow_files):
                            self.add_points(2, f"  └─ {wtype.capitalize()} workflow")
                else:
                    self.warnings.append("⚠️  [-10pts] No workflow files found")
                    self.max_score += 10
            except Exception as e:
                pass
        else:
            self.warnings.append("⚠️  [-15pts] .github/workflows/ missing")
            self.max_score += 15
    
    # ==================== README CONTENT ====================
    
    def check_readme_content(self):
        """Check README quality"""
        print("\n" + "="*80)
        print("🔟 README CONTENT (First Impression)")
        print("="*80)
        
        readme_path = self.repo_path / "README.md"
        
        if not readme_path.exists():
            self.lose_points(15, "README.md missing - Critical!", True)
            return
        
        try:
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read().lower()
            
            # Check for important sections
            sections = {
                'cloudops': 'CloudOps focus',
                'terraform': 'IaC mentioned',
                'aws': 'AWS platform',
                'monitoring': 'Monitoring capability',
                'automation': 'Automation focus',
                'lambda': 'Serverless functions',
                'architecture': 'Architecture documentation',
                'diagram': 'Diagrams referenced',
                'screenshot': 'Screenshots included'
            }
            
            for keyword, description in sections.items():
                if keyword in content:
                    self.add_points(2, f"README mentions: {description}")
                else:
                    self.warnings.append(f"⚠️  [-2pts] README missing: {description}")
                    self.max_score += 2
            
            # Check for professional elements
            if 'charles' in content or 'bucher' in content:
                self.add_points(3, "Author identified")
            
            if 'linkedin' in content or 'github' in content:
                self.add_points(3, "Contact/profile links")
            
            if 'install' in content or 'setup' in content:
                self.add_points(3, "Setup instructions")
            
        except Exception as e:
            self.warnings.append(f"⚠️  Cannot read README: {str(e)}")
    
    # ==================== FINAL REPORT ====================
    
    def generate_report(self):
        """Generate final validation report"""
        print("\n" + "="*80)
        print("="*80)
        print("📊 AWS CLOUDOPS SUITE - VALIDATION REPORT")
        print("="*80)
        print("="*80)
        
        percentage = (self.score / self.max_score * 100) if self.max_score > 0 else 0
        
        print(f"\n{'SCORE':^40s}")
        print(f"{'-'*80}")
        print(f"  Your Score:        {self.score:3d} / {self.max_score:3d} points")
        print(f"  Percentage:        {percentage:.1f}%")
        print(f"  Critical Issues:   {len(self.critical_issues)}")
        print(f"  Warnings:          {len(self.warnings)}")
        
        # Determine level
        print(f"\n{'REPOSITORY QUALITY':^80s}")
        print(f"{'-'*80}")
        
        if percentage >= 90 and len(self.critical_issues) == 0:
            level = "🌟 EXCELLENT - PRODUCTION READY"
            message = "Repository is professional and complete!"
        elif percentage >= 75 and len(self.critical_issues) <= 2:
            level = "✅ GOOD - MINOR IMPROVEMENTS"
            message = "Strong foundation, address critical items"
        elif percentage >= 60:
            level = "⚠️  FAIR - NEEDS WORK"
            message = "Good start, complete critical sections"
        else:
            level = "❌ INCOMPLETE"
            message = "Focus on core infrastructure first"
        
        print(f"  {level}")
        print(f"  {message}")
        
        # Critical issues
        if self.critical_issues:
            print(f"\n{'CRITICAL ISSUES':^80s}")
            print(f"{'-'*80}")
            for issue in self.critical_issues:
                print(f"  {issue}")
        
        # Warnings
        if self.warnings:
            print(f"\n{'WARNINGS':^80s}")
            print(f"{'-'*80}")
            for warning in self.warnings[:10]:  # Show top 10
                print(f"  {warning}")
            if len(self.warnings) > 10:
                print(f"  ... and {len(self.warnings) - 10} more warnings")
        
        # Next steps
        print(f"\n{'NEXT STEPS':^80s}")
        print(f"{'-'*80}")
        
        if len(self.critical_issues) > 0:
            print("\n  1. ❌ Fix all critical issues above")
            print("  2. ⚠️  Address warnings")
            print("  3. 🔄 Run validator again")
        else:
            print("\n  ✅ Repository structure is solid!")
            print("  📝 Continue adding content and documentation")
            print("  🚀 Ready for CloudOps/DevOps job applications")
        
        print("\n" + "="*80)
        print(f"✅ Validation complete: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"🎯 Target: CloudOps Engineer / DevOps Engineer / SRE roles\n")
        
        return {
            "score": self.score,
            "max_score": self.max_score,
            "percentage": percentage,
            "critical_issues": len(self.critical_issues),
            "level": level,
            "ready": percentage >= 75 and len(self.critical_issues) <= 2
        }
    
    def run_validation(self):
        """Run full validation"""
        print("\n" + "="*80)
        print("🔍 AWS CLOUDOPS SUITE VALIDATOR")
        print("="*80)
        print(f"Repository: {self.repo_path.absolute()}")
        print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*80)
        
        self.check_root_files()
        self.check_terraform_directory()
        self.check_scripts_directory()
        self.check_lambdas_directory()
        self.check_documentation()
        self.check_diagrams()
        self.check_screenshots()
        self.check_tests()
        self.check_cicd()
        self.check_readme_content()
        
        return self.generate_report()


def main():
    """Main execution"""
    repo_path = sys.argv[1] if len(sys.argv) > 1 else "."
    
    validator = CloudOpsSuiteValidator(repo_path)
    result = validator.run_validation()
    
    exit_code = 0 if result["ready"] else 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
