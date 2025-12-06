# AWS CloudOps Suite | Entry-Level CloudOps Project

[![AWS](https://img.shields.io/badge/AWS-CloudOps-orange)](https://aws.amazon.com/)
[![Terraform](https://img.shields.io/badge/Terraform-IaC-blue)](https://www.terraform.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

**Hands-on AWS project to demonstrate practical CloudOps skills for learning and entry-level roles.**  

---

## 📋 About
This project demonstrates a **hands-on AWS CloudOps environment**, designed for entry-level Cloud Support or Junior DevOps roles.  

**Key features:**

- AWS GuardDuty for security monitoring  
- AWS CloudWatch for metrics, monitoring, and alerts  
- AWS SNS for automated notifications  
- AWS S3 for storing monitoring findings  
- Terraform for Infrastructure as Code  
- Python scripts for automation using Boto3  

**Purpose:** Learn, implement, and troubleshoot cloud infrastructure, and showcase practical skills in a real project.

---

## 🏗️ CloudOps Workflow

1. **Terraform Deployment** – Provision AWS resources (GuardDuty, CloudWatch, SNS, S3)  
2. **Security Monitoring** – GuardDuty detects threats and findings  
3. **Alerts & Automation** – CloudWatch alarms trigger SNS notifications  
4. **Evidence Storage** – Findings stored in S3  

---

## 🚀 Quick Start

### Prerequisites
- AWS Free Tier account  
- Terraform 1.0+  
- Python 3.8+  
- AWS CLI configured  

### Installation
```bash
git clone https://github.com/charles-bucher/AWS_Cloudops_Suite.git
cd AWS_Cloudops_Suite

python -m venv venv

# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

pip install -r requirements.txt

aws configure
Deploy Infrastructure
bash
Copy code
terraform init
terraform plan
terraform apply
📸 Screenshots & Evidence
User Interface
User Login:

Main Dashboard:

Error Logs View:

API Response Example:

Admin Screens
Admin Login:

Admin Dashboard & Error Logs:


Admin API Response:

Secondary & Tertiary Users
Secondary User Login & Dashboard:


Secondary User Error Logs & API Response:


Tertiary User Login & Dashboard:


Tertiary User Error Logs & API Response:


Test Login Screen:

Python Automation Example
python
Copy code
import boto3

sns = boto3.client('sns')
sns.publish(
    TopicArn='arn:aws:sns:region:account-id:topic',
    Message='Test Alert from CloudOps Suite'
)
📚 Skills Learned & Demonstrated
AWS CloudWatch monitoring and alarms

AWS SNS notifications and alerts

AWS GuardDuty security monitoring

Python automation with Boto3

Terraform Infrastructure as Code

S3, Lambda, DynamoDB, IAM

Observability, alerting, and incident response

🎯 Next Steps
Add RDS monitoring scenarios

Analyze VPC flow logs

Build CI/CD pipeline using GitHub Actions

Implement cost monitoring and unit tests

💼 Entry-Level Career Relevance
Demonstrates skills for:

Cloud Support Engineer / Technician

Junior CloudOps / DevOps roles

AWS Infrastructure Automation & Troubleshooting

Security Monitoring & Incident Response

📝 License
MIT License – see LICENSE

📧 Contact
Charles Bucher | Pinellas Park, FL
✉️ quietopscb@gmail.com
🔗 GitHub • LinkedIn

🔑 Keywords for ATS
AWS, CloudOps, Cloud Support, Junior DevOps, Terraform, Python, CloudWatch, GuardDuty, Lambda, S3, DynamoDB, IAM, Boto3, Monitoring, Alerting, Automation, Infrastructure as Code, Observability

