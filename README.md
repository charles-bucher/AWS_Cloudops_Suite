# AWS CloudOps Suite | Production-Ready Monitoring & Security

![AWS](https://img.shields.io/badge/AWS-CloudOps-orange) ![Terraform](https://img.shields.io/badge/IaC-Terraform-blue) ![Python](https://img.shields.io/badge/Automation-Python-green) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

**Hands-on AWS CloudOps environment demonstrating infrastructure monitoring, security automation, and incident response for entry-level Cloud Support and DevOps roles.**

---

## 📋 Project Overview

This repository showcases a complete AWS CloudOps infrastructure built with **Terraform** and automated with **Python (Boto3)**. The project demonstrates practical skills for Cloud Support Engineer, Junior DevOps, and CloudOps roles.

### **What This Project Does:**
- 🔐 **Security Monitoring:** AWS GuardDuty detects threats and anomalies
- 📊 **Infrastructure Monitoring:** CloudWatch metrics, dashboards, and alarms
- 🔔 **Automated Alerting:** SNS notifications for critical events
- 💾 **Evidence Storage:** S3 buckets store findings and logs
- ⚙️ **Automation:** Python scripts using Boto3 for operational tasks
- 🏗️ **Infrastructure as Code:** Complete Terraform deployment

### **Business Value:**
- Reduces MTTR (Mean Time To Resolution) through automated monitoring
- Proactive security threat detection with GuardDuty
- Cost-effective monitoring using AWS native services
- Reproducible infrastructure through IaC

---

## 🏗️ Architecture & Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    Terraform Deployment                      │
│  (GuardDuty, CloudWatch, SNS, S3, Lambda, IAM, DynamoDB)    │
└────────────────────┬────────────────────────────────────────┘
                     │
        ┌────────────┴────────────┐
        │                         │
   ┌────▼─────┐            ┌─────▼─────┐
   │ GuardDuty│            │CloudWatch │
   │ Security │            │ Monitoring│
   │ Findings │            │  & Alarms │
   └────┬─────┘            └─────┬─────┘
        │                         │
        └────────────┬────────────┘
                     │
              ┌──────▼──────┐
              │  SNS Alerts │
              │ (Email/SMS) │
              └──────┬──────┘
                     │
              ┌──────▼──────┐
              │  S3 Storage │
              │  (Findings) │
              └─────────────┘
```

**Workflow:**
1. **Deploy:** Terraform provisions all AWS resources
2. **Monitor:** GuardDuty scans for security threats, CloudWatch tracks metrics
3. **Alert:** SNS sends notifications when alarms trigger
4. **Store:** S3 retains findings for compliance and analysis
5. **Automate:** Python scripts perform operational tasks

---

## 📸 Infrastructure Screenshots

### Project Planning & Setup

<details>
<summary>🖼️ Initial Setup & Configuration (5 screenshots)</summary>

#### Infrastructure Plan
![CloudOps Suite Plan](screenshots/cloudops_00_suite_plan.png)
*Complete infrastructure design showing all AWS services to be deployed*

#### AWS Access Configuration
![IAM Access Key](screenshots/CloudOps_01_cloudopsaccess_key.png)
*IAM user with programmatic access configured for Terraform and Python automation*

#### Terraform Backend Setup
![Terraform Backend](screenshots/CloudOps_02_backend_config.png)
*S3 backend configured for remote state storage with DynamoDB locking*

#### Python Environment
![Boto3 Installation](screenshots/CloudOps_03_boto3_install.png)
*Python Boto3 SDK installed for AWS automation scripts*

#### AWS CLI Configuration
![CLI Config](screenshots/CloudOps_04_cli_conf.png)
*AWS CLI configured with credentials and default region*

</details>

---

### Core Infrastructure Deployed

<details>
<summary>🖼️ AWS Services Running (8 screenshots)</summary>

#### CloudWatch Monitoring
![CloudWatch Dashboard](screenshots/CloudOps_05_cloudwatch.png)
*CloudWatch dashboard with custom metrics, alarms, and log groups configured*

#### Terraform Deployment Confirmation
![Terraform Success](screenshots/CloudOps_06_confirm.png)
*Terraform apply complete - all resources successfully created*

#### DynamoDB State Table
![DynamoDB](screenshots/CloudOps_07_dynamo_confirm.png)
*DynamoDB table created for Terraform state locking*

#### IAM Roles & Policies
![IAM Roles](screenshots/CloudOps_08_iam_roles.png)
*IAM roles with least-privilege policies for Lambda and service access*

#### User Permissions
![User Permissions](screenshots/CloudOps_09_user_permissions.png)
*IAM user permissions configured for CloudOps automation*

#### Lambda Functions
![Lambda Functions](screenshots/CloudOps_10_lambda_functions.png)
*Lambda functions deployed for automated incident response and alerting*

#### S3 Buckets
![S3 Buckets - List](screenshots/CloudOps_15_s3_buckets.png)
*S3 buckets created for GuardDuty findings, CloudWatch logs, and Terraform state*

#### S3 Bucket Details
![S3 Created](screenshots/CloudOps_16_s3_created.png)
*S3 bucket with versioning and encryption enabled for compliance*

</details>

---

### Monitoring & Metrics

<details>
<summary>🖼️ CloudWatch Metrics & Alarms (3 screenshots)</summary>

#### CloudWatch Metrics - View 1
![Metrics 1](screenshots/CloudOps_11_metrics.png)
*EC2 instance metrics showing CPU utilization, network traffic, and disk I/O*

#### CloudWatch Metrics - View 2
![Metrics 2](screenshots/CloudOps_12_metrics_2.png)
*Custom application metrics and performance indicators*

#### CloudWatch Metrics - View 3
![Metrics 3](screenshots/CloudOps_13_metrics_3.png)
*Lambda function metrics showing invocations, duration, and errors*

</details>

---

### Automation & Tooling

<details>
<summary>🖼️ Python & Terraform (5 screenshots)</summary>

#### Python Boto3 Script
![Python Script](screenshots/CloudOps_14_python.png)
*Python automation script using Boto3 to interact with AWS services*

#### Terraform Configuration
![Terraform Config](screenshots/CloudOps_17_terraform_confirm.png)
*Terraform configuration files defining infrastructure as code*

#### Terraform Apply
![Terraform Apply](screenshots/CloudOps_18_terraform.png)
*Terraform apply showing resources being created with progress output*

#### Terraform Installed
![Terraform Version](screenshots/CloudOps_19_terraform_installed.png)
*Terraform v1.0+ installed and verified*

#### Terraform Installation
![Terraform Install Process](screenshots/CloudOps_20_terraform_install.png)
*Terraform installation and configuration process*

</details>

---

## 🚀 Quick Start

### **Prerequisites**
- AWS Free Tier account
- Terraform 1.0+
- Python 3.8+
- AWS CLI configured

### **Installation**

```bash
# Clone repository
git clone https://github.com/charles-bucher/AWS_Cloudops_Suite.git
cd AWS_Cloudops_Suite

# Set up Python virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure AWS credentials
aws configure
```

### **Deploy Infrastructure**

```bash
# Initialize Terraform
terraform init

# Review planned changes
terraform plan

# Deploy infrastructure
terraform apply

# Verify resources
aws guardduty list-detectors
aws cloudwatch describe-alarms
aws s3 ls
```

### **Test Automation**

```bash
# Run Python automation script
python scripts/send_test_notification.py

# Check SNS notifications
# (You should receive email/SMS alert)
```

### **Cleanup**

```bash
# Destroy all resources
terraform destroy
```

---

## 💻 Technical Skills Demonstrated

### **AWS Services**
- ✅ **GuardDuty:** Security threat detection and monitoring
- ✅ **CloudWatch:** Metrics, alarms, dashboards, log groups
- ✅ **SNS:** Notification system for alerts and events
- ✅ **S3:** Object storage for findings and logs
- ✅ **Lambda:** Serverless functions for automation
- ✅ **IAM:** Identity and access management with least privilege
- ✅ **DynamoDB:** State locking for Terraform

### **Infrastructure as Code**
- ✅ **Terraform:** Complete infrastructure provisioning
- ✅ **Modular Design:** Reusable, maintainable code
- ✅ **Remote State:** S3 backend with DynamoDB locking
- ✅ **Variables:** Parameterized configurations

### **Automation & Scripting**
- ✅ **Python:** Boto3 SDK for AWS automation
- ✅ **Bash:** Deployment and maintenance scripts
- ✅ **Error Handling:** Robust exception management
- ✅ **Logging:** Comprehensive operational logging

### **CloudOps Practices**
- ✅ **Monitoring:** Proactive infrastructure observability
- ✅ **Alerting:** Automated notification workflows
- ✅ **Security:** Threat detection and compliance
- ✅ **Incident Response:** Automated remediation
- ✅ **Documentation:** Clear, comprehensive guides

---

## 📚 What I Learned

### **Technical Growth**
- Deployed production-grade monitoring infrastructure
- Automated security monitoring with GuardDuty
- Configured multi-service alerting workflows
- Managed infrastructure state with Terraform
- Integrated Python automation with AWS services

### **Operational Skills**
- Troubleshooting CloudWatch alarm configurations
- Debugging Terraform state issues
- Managing IAM permissions and policies
- Designing cost-effective monitoring solutions
- Documenting infrastructure for team collaboration

### **Best Practices**
- Infrastructure as Code for reproducibility
- Least-privilege IAM policies for security
- Remote state management with locking
- Modular Terraform code organization
- Comprehensive error handling in automation

---

## 🎯 Next Steps & Improvements

### **Planned Enhancements**
- [ ] Add RDS database monitoring scenarios
- [ ] Implement VPC Flow Logs analysis
- [ ] Build CI/CD pipeline with GitHub Actions
- [ ] Add cost monitoring and budget alerts
- [ ] Create automated testing suite
- [ ] Develop incident response playbooks
- [ ] Integrate with PagerDuty or Slack

### **Learning Goals**
- [ ] AWS SysOps Administrator certification
- [ ] Advanced Terraform patterns
- [ ] Kubernetes monitoring (EKS)
- [ ] GitOps workflows
- [ ] Advanced Python testing (pytest)

---

## 💼 Career Relevance

**This project demonstrates skills for:**

✅ **Cloud Support Engineer / Technician**
- Troubleshooting AWS service issues
- Monitoring infrastructure health
- Responding to alerts and incidents
- Customer-facing technical support

✅ **Junior CloudOps / DevOps Engineer**
- Infrastructure automation with Terraform
- Python scripting for operational tasks
- CI/CD pipeline understanding
- Monitoring and observability

✅ **AWS Infrastructure Automation**
- IaC deployment and management
- Service integration and orchestration
- Security and compliance monitoring
- Cost optimization awareness

✅ **Security Monitoring & Incident Response**
- Threat detection with GuardDuty
- Alert triage and investigation
- Automated remediation workflows
- Security event logging

---

## 📝 Project Structure

```
AWS_Cloudops_Suite/
├── main.tf                 # Main Terraform configuration
├── variables.tf            # Input variables
├── outputs.tf              # Output values
├── backend.tf              # Remote state configuration
├── provider.tf             # AWS provider config
├── scripts/                # Python automation scripts
├── screenshots/            # Infrastructure evidence
├── docs/                   # Documentation
├── tests/                  # Testing scripts
└── README.md              # This file
```

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

---

## 📧 Contact

**Charles Bucher** | Pinellas Park, FL  
✉️ quietopscb@gmail.com  
🔗 [GitHub](https://github.com/charles-bucher) • [LinkedIn](https://linkedin.com/in/charles-bucher-cloud)

---

## 🏷️ Keywords for ATS

AWS • CloudOps • Cloud Support • Junior DevOps • Terraform • Python • CloudWatch • GuardDuty • Lambda • S3 • DynamoDB • IAM • Boto3 • Monitoring • Alerting • Automation • Infrastructure as Code • Observability • Security Monitoring • Incident Response • SNS • EC2 • VPC • Cost Optimization • Remote Work • Entry Level

---

*This project was built to demonstrate hands-on AWS CloudOps skills for entry-level cloud engineering roles. All infrastructure shown in screenshots was deployed, tested, and documented as part of the learning process.*

*Last Updated: December 2025*