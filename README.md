
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
## Implementation Evidence

### Terraform Plan Output
![Terraform Plan](screenshots/cloudops_00_suite_plan.png)

### AWS Configuration & Access
![CloudOps Access Key](screenshots/CloudOps_01_cloudopsaccess_key.png)
![Backend Config](screenshots/CloudOps_02_backend_config.png)
![Boto3 Install](screenshots/CloudOps_03_boto3_install.png)
![CLI Config](screenshots/CloudOps_04_cli_conf.png)

### CloudWatch & Monitoring
![CloudWatch](screenshots/CloudOps_05_cloudwatch.png)
![Confirm Setup](screenshots/CloudOps_06_confirm.png)

### DynamoDB & IAM
![Dynamo Confirm](screenshots/CloudOps_07_dynamo_confirm.png)
![IAM Roles](screenshots/CloudOps_08_iam_roles.png)
![User Permissions](screenshots/CloudOps_09_user_permissions.png)

### Lambda & Metrics
![Lambda Functions](screenshots/CloudOps_10_lambda_functions.png)
![Metrics 1](screenshots/CloudOps_11_metrics.png)
![Metrics 2](screenshots/CloudOps_12_metrics_2.png)
![Metrics 3](screenshots/CloudOps_13_metrics_3.png)

### Python Scripts & S3
![Python Scripts](screenshots/CloudOps_14_python.png)
![S3 Buckets](screenshots/CloudOps_15_s3_buckets.png)
![S3 Created](screenshots/CloudOps_16_s3_created.png)

### Terraform Deployment
![Terraform Confirm](screenshots/CloudOps_17_terraform_confirm.png)
![Terraform](screenshots/CloudOps_18_terraform.png)
![Terraform Installed](screenshots/CloudOps_19_terraform_installed.png)
![Terraform Install](screenshots/CloudOps_20_terraform_install.png)

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
