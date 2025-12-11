# AWS_Cloudops_Suite – Cloud Support & AWS Monitoring Lab

## TL;DR

**AWS_Cloudops_Suite** is a full-stack AWS monitoring and automation lab built with Terraform, CloudWatch, GuardDuty, SNS, Lambda, S3, and IAM.  

**Purpose:** Hands-on learning of cloud troubleshooting, incident response, and infrastructure-as-code.  

**Key Features:**
- GuardDuty detects security threats.
- CloudWatch monitors metrics, dashboards, and alarms.
- SNS sends notifications via email/SMS.
- Lambda automates responses to incidents.
- S3 stores logs and findings.
- Terraform deploys and manages everything reproducibly.

**Deploy in ~30 min:** `terraform init` → `terraform plan` → `terraform apply`  

**Cost:** ~$15–30/month vs. $500–1,200/month for commercial monitoring tools.  

**Skills Practiced:** AWS services integration, IaC, Python automation, troubleshooting, monitoring, security, and CI/CD workflows.

**Who I am:** Self-taught AWS CloudOps engineer building hands-on labs while working full-time; learning by doing, documenting, and iterating on real deployments.


[![GitHub stars](https://img.shields.io/github/stars/Charles-bucher/AWS_Cloudops_Suite?style=social)](https://github.com/Charles-bucher/AWS_Cloudops_Suite/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Charles-bucher/AWS_Cloudops_Suite?style=social)](https://github.com/Charles-bucher/AWS_Cloudops_Suite/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/charles-bucher-cloud)

---

## 📍 Location
Pinellas Park, FL

---

## 👤 About This Repo
**AWS_Cloudops_Suite** is a **hands-on, production-grade monitoring and security lab** built to learn Cloud Support and AWS service integration.  
It’s fully **Terraform-managed**, with **GuardDuty, CloudWatch, SNS, Lambda, S3, IAM, and DynamoDB**.  
All screenshots and commits represent **real deployments and problem-solving**.  

> “This project represents 6+ months of late-night learning, trial-and-error deployments, and iterative improvement in cloud troubleshooting.”

---

## 🚀 Core Skills Practiced
- AWS Services: EC2, S3, VPC, RDS, Lambda, CloudFormation, CloudWatch, GuardDuty, SNS, IAM, DynamoDB  
- Automation & IaC: Terraform, Python/Boto3, Bash, PowerShell  
- Monitoring: CloudWatch dashboards, alarms, SNS notifications, log analysis  
- Troubleshooting: IAM policies, security groups, network connectivity, incident response  
- DevOps Tools: Git, GitHub, GitHub Actions, AWS CLI  

---

## 🛠️ Project Overview
**Goal:** Provide small teams with **24/7 AWS monitoring** using native services (~$20/month) instead of expensive SaaS tools ($500+/month).  

| Service      | What It Does                          | Rough Lab Impact / Notes |
|-------------|--------------------------------------|-------------------------|
| GuardDuty   | Security threat detection             | ~5–10 simulated findings/week |
| CloudWatch  | Metrics, dashboards, alarms          | Monitored ~15 key metrics; ~50–70% alert optimization |
| SNS         | Email/SMS alerts                      | Multi-channel notifications tested |
| Lambda      | Automated responses                   | Handled ~3–5 auto-remediation tasks/week |
| S3          | Log/evidence storage                  | Versioned & encrypted buckets |
| IAM         | Access control                        | Least-privilege roles successfully deployed |
| DynamoDB    | Terraform remote state locking        | ~5–10 lab deployments |

---

## 📸 Deployment Screenshots
<details>
<summary>View All Screenshots</summary>

![ACS_01](screenshots/ACS_01_aws_access_key.png)  
![ACS_02](screenshots/ACS_02_backend_config.png)  
![ACS_03](screenshots/ACS_03_boto3_install.png)  
![ACS_04](screenshots/ACS_04_cli_config.png)  
![ACS_05](screenshots/ACS_05_cloudwatch_setup.png)  
![ACS_06](screenshots/ACS_06_cloudwatch_confirm.png)  
![ACS_07](screenshots/ACS_07_dynamodb_confirm.png)  
![ACS_08](screenshots/ACS_08_iam_roles.png)  
![ACS_09](screenshots/ACS_09_user_permissions.png)  
![ACS_10](screenshots/ACS_10_lambda_functions.png)  
![ACS_11](screenshots/ACS_11_metrics_1.png)  
![ACS_12](screenshots/ACS_12_metrics_2.png)  
![ACS_13](screenshots/ACS_13_metrics_3.png)  
![ACS_14](screenshots/ACS_14_python_setup.png)  
![ACS_15](screenshots/ACS_15_s3_buckets.png)  
![ACS_16](screenshots/ACS_16_s3_created.png)  
![ACS_17](screenshots/ACS_17_terraform_init.png)  
![ACS_18](screenshots/ACS_18_terraform_plan.png)  
![ACS_19](screenshots/ACS_19_terraform_apply.png)  
![ACS_20](screenshots/ACS_20_terraform_installed.png)  
![ACS_21](screenshots/ACS_21_terraform_destroy.png)  
![ACS_22](screenshots/ACS_22_terraform_apply_after_destroy.png)  
![ACS_23](screenshots/ACS_23_github_actions_pr.png)  
![ACS_24](screenshots/ACS_24_github_actions_main.PNG)  
![ACS_25](screenshots/ACS_25_suite_plan.png)  

</details>

<details>
<summary>Architecture Diagrams</summary>

![AWS CloudOps Architecture](screenshots/AWS CloudOps Architecture 2.png)  
![AWS_Cloudops_suite_Diagram](screenshots/AWS_Cloudops_suite_Diagram.png)  

</details>

---

## ⚙️ How to Deploy

### Prerequisites
- AWS account with admin access  
- Terraform 1.0+  
- Python 3.8+  
- AWS CLI configured  
- Git  

### Installation
```bash
git clone https://github.com/charles-bucher/AWS_Cloudops_Suite.git
cd AWS_Cloudops_Suite

aws configure  # Access Key, Secret, Region, Output

python -m venv venv
# Windows: .\venv\Scripts\activate
# Linux/macOS: source venv/bin/activate
pip install -r requirements.txt

terraform init
terraform plan
terraform apply  # type 'yes'
