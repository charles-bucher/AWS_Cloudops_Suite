#!/bin/bash
# fix-structure.sh
# Sets up proper folder structure for CloudOps GuardDuty Automation repo

# Exit on any error
set -e

echo "Setting up CloudOps GuardDuty Automation repo structure..."

# Create main folders
mkdir -p docs
mkdir -p scripts
mkdir -p terraform

# Create placeholder files if they don't exist
touch docs/README.md
touch docs/setup_guide.md
touch docs/architecture.md
touch docs/troubleshooting.md
touch docs/best_practices.md

touch scripts/findings-monitor.py
touch scripts/guardduty-enable.py
touch scripts/test-main.py

touch terraform/main.tf
touch terraform/variables.tf
touch terraform/outputs.tf
touch terraform/backend.tf
touch terraform/backend.conf

# Optional: set executable permissions for scripts
chmod +x scripts/*.py

echo "Folder structure setup complete."
echo " - docs/      : documentation"
echo " - scripts/   : Python automation scripts"
echo " - terraform/ : Terraform infrastructure code"

echo "You can now edit files in docs/, scripts/, and terraform/ as needed."
