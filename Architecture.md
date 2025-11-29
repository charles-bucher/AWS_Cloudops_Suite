# CloudOps GuardDuty Automation — Architecture Overview

This document explains the architecture of the CloudOps GuardDuty Automation project and how its components work together.

---

## Overview

CloudOps GuardDuty Automation automates the deployment, monitoring, and alerting of AWS GuardDuty across single or multiple regions.  
It uses Terraform for infrastructure as code, stores findings in S3, and optionally sends alerts via email.

---

## Architecture Components

| Component | Description |
|-----------|-------------|
| **AWS GuardDuty** | Threat detection service that monitors your AWS accounts for malicious activity and unauthorized behavior. |
| **S3 Bucket** | Stores GuardDuty findings in JSON format. Each finding is timestamped and organized under a defined prefix. |
| **Terraform** | Automates the creation of GuardDuty detectors, S3 bucket, and optionally IAM roles or policies. |
| **Python Monitoring Scripts** | - `findings-monitor.py`: polls the S3 bucket for new findings and sends alerts.<br>- `guardduty-enable.py`: enables GuardDuty detectors across regions.<br>- `test-main.py`: validates setup and connectivity. |
| **CI/CD (Optional)** | GitHub Actions or other pipelines validate Terraform code and automate deployment to AWS accounts. |

---

## Workflow

1. **Terraform Deployment**
   - Provision GuardDuty detectors in selected AWS regions.
   - Create S3 bucket to store findings.
   - Optionally configure IAM policies and remote state.

2. **GuardDuty Detection**
   - GuardDuty monitors AWS accounts and generates findings for suspicious activity.

3. **Findings Storage**
   - Findings are automatically stored in the S3 bucket under a timestamped prefix.

4. **Monitoring & Alerts**
   - `findings-monitor.py` polls the S3 bucket for new findings.
   - Sends alerts via AWS SES or prints to console as fallback.

5. **Optional CI/CD**
   - Terraform code is validated via GitHub Actions before deployment.
   - Ensures reproducible and secure infrastructure changes.

---

## Diagram (ASCII Example)

       +-----------------+
       |  AWS GuardDuty  |
       +--------+--------+
                |
                v
       +-----------------+
       |     S3 Bucket   | <-- findings-monitor.py reads new objects
       +--------+--------+
                |
    +-----------+-----------+
    |                       |
