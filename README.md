# ⚡ AWS Monitoring & Observability Project

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/charles-bucher/aws_monitoring_observability/terraform-apply.yml?branch=main)
![Terraform](https://img.shields.io/badge/Terraform-v1.5+-blue)
![Python](https://img.shields.io/badge/Python-3.8+-yellow)
![License](https://img.shields.io/badge/License-MIT-green)
![AWS Free Tier](https://img.shields.io/badge/AWS-Free%20Tier-lightgrey)

---

## 👋 About This Project
**Proactively monitor AWS workloads with Terraform, CloudWatch, and GuardDuty.**  

This hands-on lab demonstrates observability and monitoring pipelines for EC2, security, and operational metrics. It uses **Terraform**, **CloudWatch**, **SNS**, and **GuardDuty**, with CI/CD workflows to practice CloudOps skills in a learning environment.

---

## 🚀 Features
- **EC2 Monitoring:** Track CPU, memory, and disk metrics with CloudWatch alarms  
- **Centralized Logging:** Aggregate application logs and run queries with CloudWatch Logs Insights  
- **Security Alerts:** GuardDuty findings sent to SNS notifications  
- **Infrastructure as Code:** Deploy infrastructure reliably using Terraform  
- **Automation:** CI/CD workflows using GitHub Actions  

---

## 🏗️ Architecture & Workflow
![Architecture Diagram](screenshots/architecture-overview.png)  

**Workflow Overview:**  
1. Terraform deploys EC2, CloudWatch metrics, SNS topics, and GuardDuty.  
2. EC2 metrics and application logs are aggregated and monitored.  
3. GuardDuty detects anomalies and triggers SNS notifications.  
4. GitHub Actions validates Terraform and automates deployments.  

---

## 🛠️ Quick Start
```bash
# Clone repository
git clone https://github.com/charles-bucher/aws_monitoring_observability.git
cd aws_monitoring_observability

# Deploy infrastructure
terraform init
terraform plan
terraform apply
