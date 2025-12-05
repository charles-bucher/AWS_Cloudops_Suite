
[![Terraform](https://img.shields.io/badge/Terraform-v1.0+-623CE4?logo=terraform&logoColor=white)](https://www.terraform.io/) 
[![AWS](https://img.shields.io/badge/AWS-v5.100.0-FF9900?logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen)]()

# AWS CloudOps Suite

![GitHub Repo Size](https://img.shields.io/github/repo-size/charles-bucher/AWS_Cloudops_Suite)
![GitHub Last Commit](https://img.shields.io/github/last-commit/charles-bucher/AWS_Cloudops_Suite)
![GitHub Language](https://img.shields.io/github/languages/top/charles-bucher/AWS_Cloudops_Suite)
![MIT License](https://img.shields.io/badge/license-MIT-blue)

Hands-on AWS monitoring, alerting, and automation project built for learning CloudOps practices and demonstrating practical skills in **CloudWatch monitoring, Terraform infrastructure, Python automation, and GuardDuty security**.

---

## 📋 About

This project sets up a **full-stack AWS CloudOps environment**, including:

- **GuardDuty** for security monitoring
- **CloudWatch** for metrics and alerts
- **S3 Buckets** for findings storage
- **SNS** for notifications
- **Terraform** for infrastructure as code

It’s designed for **entry-level Cloud Support / CloudOps roles** to show practical skills.

---

## 🏗️ System Architecture

**CloudOps Pipeline Overview:**

1. **Terraform Deployment** – Sets up infrastructure including GuardDuty, CloudWatch alarms, SNS topics, and S3 buckets.
2. **Security Monitoring** – GuardDuty monitors threats and findings.
3. **Alerts & Automation** – CloudWatch alarms trigger notifications via SNS.
4. **Evidence Storage** – Findings stored in S3 buckets for auditing.

![CloudOps Architecture](screenshots/cloudops_00_suite_plan.png)

---

## 🚀 Quick Start

### Prerequisites

- AWS Free Tier account
- Terraform 1.0+
- Python 3.8+
- AWS CLI configured

---

### Installation

```bash
# Clone repository
git clone https://github.com/charles-bucher/AWS_Cloudops_Suite.git
cd AWS_Cloudops_Suite

# Create Python virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Configure AWS credentials
aws configure
Deploy Infrastructure
bash
Copy code
# Initialize Terraform
terraform init

# Review planned changes
terraform plan

# Apply infrastructure
terraform apply
Terraform Plan Screenshot:


Run Monitoring Scripts
bash
Copy code
# Activate virtual environment
.\venv\Scripts\activate

# Run GuardDuty findings monitor
python scripts/findings-monitor.py

# Run infrastructure health check
python scripts/health-check.py
📸 Implementation Evidence
## 📸 Implementation Evidence

**Screenshots of CloudOps Suite Deployment and Testing:**

| Step | Screenshot |
|------|------------|
| 01. AWS Access & CLI Config | ![CloudOps_01](screenshots/CloudOps_01_cloudopsaccess_key.png) |
| 02. Backend Config | ![CloudOps_02](screenshots/CloudOps_02_backend_config.png) |
| 03. Python & Boto3 Installation | ![CloudOps_03](screenshots/CloudOps_03_boto3_install.png) |
| 04. AWS CLI Configuration | ![CloudOps_04](screenshots/CloudOps_04_cli_conf.png) |
| 05. CloudWatch Dashboard | ![CloudOps_05](screenshots/CloudOps_05_cloudwatch.png) |
| 06. Terraform Apply Confirmation | ![CloudOps_06](screenshots/CloudOps_06_confirm.png) |
| 07. DynamoDB State Check | ![CloudOps_07](screenshots/CloudOps_07_dynamo_confirm.png) |
| 08. IAM Roles Created | ![CloudOps_08](screenshots/CloudOps_08_iam_roles.png) |
| 09. IAM User Permissions | ![CloudOps_09](screenshots/CloudOps_09_user_permissions.png) |
| 10. Lambda Functions Deployed | ![CloudOps_10](screenshots/CloudOps_10_lambda_functions.png) |
| 11. CloudWatch Metrics | ![CloudOps_11](screenshots/CloudOps_11_metrics.png) |
| 12. CloudWatch Metrics - 2 | ![CloudOps_12](screenshots/CloudOps_12_metrics_2.png) |
| 13. CloudWatch Metrics - 3 | ![CloudOps_13](screenshots/CloudOps_13_metrics_3.png) |
| 14. Python Monitoring Script | ![CloudOps_14](screenshots/CloudOps_14_python.png) |
| 15. S3 Buckets Setup | ![CloudOps_15](screenshots/CloudOps_15_s3_buckets.png) |
| 16. S3 Bucket Creation Confirmed | ![CloudOps_16](screenshots/CloudOps_16_s3_created.png) |
| 17. Terraform Confirmation | ![CloudOps_17](screenshots/CloudOps_17_terraform_confirm.png) |
| 18. Terraform Plan & Output | ![CloudOps_18](screenshots/CloudOps_18_terraform.png) |
| 19. Terraform Installed | ![CloudOps_19](screenshots/CloudOps_19_terraform_installed.png) |
| 20. Terraform Installation | ![CloudOps_20](screenshots/CloudOps_20_terraform_install.png) |
| 21. Full Suite Terraform Plan | ![CloudOps_00](screenshots/cloudops_00_suite_plan.png) |

AWS Access & CLI Config	
Backend Config	
Python & Boto3 Setup	
Terraform Apply	
CloudWatch Metrics	
S3 Buckets	

You can expand this table to include all 20 screenshots in order.

📚 Skills Demonstrated
Area	Technologies / Tools
Cloud Monitoring	CloudWatch metrics, alarms, dashboards
Security Monitoring	GuardDuty findings, automated alerts
Infrastructure as Code	Terraform (HCL), backend S3/DynamoDB
Automation	Python, Boto3 SDK, AWS CLI
Serverless	AWS Lambda functions
Storage & Databases	S3 buckets, DynamoDB tables
IAM & Security	Roles, policies, user permissions

🎯 Next Steps
Add RDS monitoring scenarios

Implement VPC flow log analysis

Build CI/CD pipeline with GitHub Actions

Add unit tests and cost monitoring

💼 Career Relevance
Skills highlighted in this project are applicable to:

Cloud Support Engineer

Junior DevOps / CloudOps Roles

Infrastructure as Code / AWS Automation

📝 License
This project is licensed under the MIT License. See the LICENSE file for details.

📧 Contact
Charles Bucher
📍 Pinellas Park, Florida
✉️ quietopscb@gmail.com
🔗 GitHub • LinkedIn

Keywords for ATS: AWS, CloudOps, Terraform, Python, CloudWatch, GuardDuty, Lambda, S3, DynamoDB, IAM, Infrastructure as Code, Boto3, Monitoring, Alerting, Security Automation, DevOps, Cloud Support, Incident Response, Observability
