# Setup Guide — CloudOps GuardDuty Automation

This guide explains how to set up, deploy and manage the CloudOps GuardDuty Automation project. Use it to quickly bootstrap your AWS security & monitoring infrastructure with Terraform, backed by S3 & DynamoDB, and integrated with CI/CD pipelines.

---

## Table of Contents

1. [Prerequisites](#prerequisites)  
2. [Clone the Repository](#clone-the-repository)  
3. [AWS Credentials & Configuration](#aws-credentials--configuration)  
4. [Create Remote State Backend (S3 + DynamoDB lock)](#create-remote-state-backend-s3--dynamodb-lock)  
5. [Configure Backend.tf](#configure-backendtf)  
6. [Initialize & Deploy Infrastructure](#initialize--deploy-infrastructure)  
7. [Post‑Deployment: Alert Email & S3 Findings Bucket Setup](#post-deployment-alert-email--s3-findings-bucket-setup)  
8. [Destroy / Teardown Infrastructure](#destroy--teardown-infrastructure)  
9. [CI/CD Integration (GitHub Actions)](#cicd-integration-github-actions)  
10. [Troubleshooting](#troubleshooting)  
11. [Next Steps / Future Enhancements](#next-steps--future-enhancements)  

---

## Prerequisites

- An AWS account with sufficient permissions (GuardDuty, S3, IAM, optionally DynamoDB). :contentReference[oaicite:1]{index=1}  
- [AWS CLI](https://aws.amazon.com/cli/) installed and configured. :contentReference[oaicite:2]{index=2}  
- [Terraform](https://www.terraform.io/) installed (version 1.0+ recommended). :contentReference[oaicite:3]{index=3}  
- Git CLI to clone the repo. :contentReference[oaicite:4]{index=4}  
- (Optional but strongly recommended) An S3 bucket for remote Terraform state + a DynamoDB table for state locking. :contentReference[oaicite:5]{index=5}  

---

## Clone the Repository

```bash
git clone https://github.com/charles‑bucher/cloudOps-guardDuty-automation.git
cd cloudOps-guardDuty-automation
AWS Credentials & Configuration
Run:

bash
Copy code
aws configure
Provide your AWS Access Key ID, Secret Access Key, and default region (e.g., us-east-1) when prompted. 
GitHub

Create Remote State Backend (S3 + DynamoDB lock)
If you don’t already have a remote state bucket + lock table:

bash
Copy code
# Create S3 bucket (adjust bucket name & region accordingly)
aws s3api create-bucket \
  --bucket YOUR-UNIQUE-BUCKET-NAME \
  --region us-east-1

# (Optional) Create DynamoDB table for state locking
aws dynamodb create-table \
  --table-name terraform-lock \
  --attribute-definitions AttributeName=LockID,AttributeType=S \
  --key-schema AttributeName=LockID,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST \
  --region us-east-1
GitHub

Configure Backend.tf
Open Backend.tf and replace placeholder values with your actual bucket and table names. Example:

hcl
Copy code
terraform {
  backend "s3" {
    bucket         = "YOUR-UNIQUE-BUCKET-NAME"
    key            = "guardduty/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-lock"      # optional
    encrypt        = true
  }
}
GitHub

Initialize & Deploy Infrastructure
bash
Copy code
terraform init
terraform plan
terraform apply
During apply you'll be prompted for necessary variables, such as:

alert_email — email to receive GuardDuty alerts

bucket_name — name of S3 bucket where GuardDuty findings will be stored

region — AWS region for deployment (e.g., us-east-1) 
GitHub

⚠️ Always review the plan before applying in production accounts. 
GitHub

Post‑Deployment: Alert Email & S3 Findings Bucket Setup
After deployment:

Ensure the S3 bucket for GuardDuty findings exists and that the configured email (or SNS hook, if implemented later) receives alerts.

Confirm the AWS IAM permissions used have correct access to S3, GuardDuty, and any necessary policies (per README). 
GitHub
+1

Destroy / Teardown Infrastructure
To remove all resources created by the setup:

bash
Copy code
terraform destroy
# If using DynamoDB locking and want to skip lock issues:
terraform destroy -lock=false
Then optionally clean up local Terraform files:

bash
Copy code
rm -rf .terraform/
rm -f .terraform.lock.hcl
rm -f terraform.tfstate*
GitHub

CI/CD Integration (GitHub Actions)
This project includes a GitHub Actions workflow that:

Validates Terraform formatting

Checks configuration syntax

Ensures code quality before deployment

This helps maintain a clean, testable IaC repo. 
GitHub

Troubleshooting
Problem	Possible Solution
Backend initialization error	Run terraform init -reconfigure 
GitHub
State lock acquisition error	Ensure DynamoDB lock table exists — or run destroy with -lock=false. 
GitHub
S3 Access Denied	Verify Backend.tf bucket name is correct, and AWS credentials have proper S3 permissions. 
GitHub
GuardDuty / IAM permission errors	Confirm that AWS user/role has rights to create GuardDuty detectors, S3 buckets, IAM roles/policies. 
GitHub
+1

Next Steps / Future Enhancements
Add notifications (e.g. SNS or email) for GuardDuty findings (if not yet configured) 
GitHub

Implement automated remediation (e.g. Lambda-based responses) after detection 
GitHub
+1

Expand to multi-region or multi-account support (if applicable) — this may require IAM + AWS Organizations configuration or adaptation. 
GitHub
+1

Add dashboards (e.g. CloudWatch) for monitoring security metrics across deployments. 
GitHub

Last updated: 2025-11-26

yaml
