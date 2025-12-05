AWS CloudOps Suite








📋 Project Overview

Hands-on AWS monitoring, alerting, and automation project built while learning CloudOps practices.

Includes:

GuardDuty security monitoring & automated findings alerts

CloudWatch metrics, alarms, dashboards

S3 buckets for storing findings

SNS topic for alert notifications

Python scripts for automation

Terraform workflows for Infrastructure as Code

🚀 Quick Start: Reproduce the Stack
1. Prerequisites

AWS Free Tier account

Terraform 1.0+

Python 3.8+

AWS CLI configured

2. Clone the Repository
git clone https://github.com/charles-bucher/AWS_Cloudops_Suite.git
cd AWS_Cloudops_Suite

3. Configure Python Environment
python -m venv venv
# Activate
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt


Screenshot:

4. Configure AWS Credentials
aws configure


Screenshots:




5. Terraform Initialization & Plan
terraform init -reconfigure
terraform plan


Screenshot:

6. Apply the Terraform Stack
terraform apply


Screenshots:




7. Run Monitoring Scripts
python scripts/findings-monitor.py
python scripts/health-check.py


Screenshots:




8. Verify in AWS Console

Screenshots:












9. Cleanup (Optional)
terraform destroy

✅ Skills Demonstrated

Cloud monitoring & security automation

Terraform Infrastructure as Code

Python scripting for CloudOps

AWS IAM & resource management

Proactive alerting workflows

📁 Project Structure
AWS_Cloudops_Suite/
├── screenshots/
├── scripts/
├── tests/
├── main.tf
├── variables.tf
├── outputs.tf
├── backend.tf
├── provider.tf
├── README.md
└── requirements.txt
