# AWS_Cloudops_Suite

![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![CloudWatch](https://img.shields.io/badge/CloudWatch-%23FF4F8B.svg?style=for-the-badge&logo=Amazon%20CloudWatch&logoColor=white)
![License](https://img.shields.io/github/license/charles-bucher/AWS_Cloudops_Suite?style=for-the-badge)

Production-ready AWS monitoring infrastructure using GuardDuty, CloudWatch, SNS, Lambda, and Terraform. Built to learn cloud security and observability without spending hundreds on third-party monitoring tools.

---

## What This Does

This is a complete monitoring stack for AWS infrastructure:

- **GuardDuty** continuously scans for security threats
- **CloudWatch** tracks metrics, dashboards, and alarms
- **SNS** sends alerts via email/SMS when things break
- **Lambda** runs automated response functions
- **S3** stores security findings and logs
- **Terraform** deploys everything with one command

**The Problem:** Small teams need 24/7 monitoring but DataDog costs $500-1,200/month and commercial tools add up fast.

**This Solution:** Uses AWS native services to get the same capabilities for ~$20/month in AWS costs. Everything's infrastructure-as-code so it's repeatable and version-controlled.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                  Terraform Infrastructure                    │
│     (GuardDuty, CloudWatch, SNS, Lambda, S3, IAM, DynamoDB) │
└────────────────────┬────────────────────────────────────────┘
                     │
        ┌────────────┴────────────┐
        │                         │
   ┌────▼─────┐            ┌─────▼─────┐
   │ GuardDuty│            │CloudWatch │
   │ Threat   │            │ Metrics & │
   │ Detection│            │  Alarms   │
   └────┬─────┘            └─────┬─────┘
        │                         │
        └────────────┬────────────┘
                     │
              ┌──────▼──────┐
              │ SNS Alerts  │
              │ (Email/SMS) │
              └──────┬──────┘
                     │
         ────────────┴────────────┐
        │                         │
   ┌────▼─────┐            ┌─────▼─────┐
   │ Lambda   │            │  S3 Logs  │
   │ Response │            │ & Evidence│
   │ Functions│            │  Storage  │
   └──────────┘            └───────────┘
```

---

## Deployment Screenshots

### Complete Suite Plan
![Full Suite Plan](screenshots/cloudops_00_suite_plan.png)

### Initial Setup
![AWS Access Key](screenshots/CloudOps_01_cloudopsaccess_key.png)
![Backend Config](screenshots/CloudOps_02_backend_config.png)
![Boto3 Install](screenshots/CloudOps_03_boto3_install.png)
![CLI Config](screenshots/CloudOps_04_cli_conf.png)

### AWS Services Deployed
![CloudWatch](screenshots/CloudOps_05_cloudwatch.png)
![Confirm Setup](screenshots/CloudOps_06_confirm.png)
![DynamoDB Confirm](screenshots/CloudOps_07_dynamo_confirm.png)
![IAM Roles](screenshots/CloudOps_08_iam_roles.png)
![User Permissions](screenshots/CloudOps_09_user_permissions.png)
![Lambda Functions](screenshots/CloudOps_10_lambda_functions.png)

### Monitoring & Metrics
![Metrics 1](screenshots/CloudOps_11_metrics.png)
![Metrics 2](screenshots/CloudOps_12_metrics_2.png)
![Metrics 3](screenshots/CloudOps_13_metrics_3.png)

### Environment Configuration  
![Python Setup](screenshots/CloudOps_14_python.png)
![S3 Buckets](screenshots/CloudOps_15_s3_buckets.png)
![S3 Created](screenshots/CloudOps_16_s3_created.png)

### Terraform Deployment
![Terraform Confirm](screenshots/CloudOps_17_terraform_confirm.png)
![Terraform](screenshots/CloudOps_18_terraform.png)
![Terraform Installed](screenshots/CloudOps_19_terraform_installed.png)
![Terraform Install Process](screenshots/CloudOps_20_terraform_install.png)

---

## What's Actually Deployed

| Service | What It Does | Configuration |
|---------|-------------|---------------|
| **GuardDuty** | Security threat detection | Enabled with continuous monitoring |
| **CloudWatch** | Infrastructure monitoring | Custom dashboards, metrics, alarms |
| **SNS** | Alert notifications | Email/SMS topics configured |
| **Lambda** | Automated responses | Python functions for incident handling |
| **S3** | Evidence storage | Versioned buckets with encryption |
| **IAM** | Access control | Least-privilege roles and policies |
| **DynamoDB** | State locking | Terraform backend state table |

---

## How to Deploy

### Prerequisites
- AWS account with admin access
- Terraform 1.0+
- Python 3.8+
- AWS CLI configured
- Git

### Installation

```bash
# Clone repository
git clone https://github.com/charles-bucher/AWS_Cloudops_Suite.git
cd AWS_Cloudops_Suite

# Configure AWS credentials
aws configure
# Enter: Access Key ID, Secret Access Key, Region (us-east-1), Output (json)

# Set up Python environment
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt

# Initialize Terraform
terraform init

# Review what will be created
terraform plan

# Deploy infrastructure
terraform apply
# Type 'yes' when prompted
```

### Verify Deployment

```bash
# Check GuardDuty is running
aws guardduty list-detectors

# Check CloudWatch alarms
aws cloudwatch describe-alarms

# Check SNS topics
aws sns list-topics

# Test SNS notifications
python scripts/send_test_notification.py
```

### Cleanup

```bash
# Remove all resources (avoids AWS charges)
terraform destroy
```

---

## Monthly Costs

| Service | Cost |
|---------|------|
| GuardDuty | $4.60/month (30-day free trial first) |
| CloudWatch | $3-10/month (depends on metrics) |
| SNS | $0.50/month (email notifications) |
| S3 | $1-2/month (log storage) |
| Lambda | Free tier covers most usage |
| DynamoDB | Free tier (state locking) |
| **Total** | **$15-30/month** |

Compare to: DataDog ($500-1,200/month), New Relic ($600+/month), Splunk ($1,000+/month)

---

## Project Structure

```
AWS_Cloudops_Suite/
├── main.tf                 # Primary infrastructure resources
├── variables.tf            # Configuration inputs
├── outputs.tf              # Exported values
├── backend.tf              # S3 + DynamoDB state management
├── provider.tf             # AWS provider config
├── scripts/                # Automation scripts
│   ├── send_test_notification.py
│   └── verify_deployment.sh
├── screenshots/            # Deployment evidence (21 images)
├── docs/                   # Technical documentation
├── tests/                  # Infrastructure validation
├── .github/workflows/      # CI/CD automation
└── README.md              # This file
```

---

## What I Learned Building This

**Terraform & IaC:**
- Managing remote state with S3 + DynamoDB locking
- Debugging IAM permissions (failed many times before getting roles right)
- Organizing Terraform code for reusability
- Using variables and outputs effectively

**AWS Services:**
- Configuring GuardDuty and interpreting security findings
- Setting up CloudWatch alarms that aren't too noisy
- Integrating SNS for multi-channel notifications
- Lambda function deployment and error handling
- S3 bucket security (versioning, encryption, access policies)

**Python & Automation:**
- Using Boto3 SDK to interact with AWS services
- Error handling in automation scripts
- Testing infrastructure deployments programmatically

**Development Process:**
- Git version control and meaningful commits (35+ iterations)
- Documentation as I build (not after)
- Incremental testing and validation

---

## Why I Built This

I'm teaching myself cloud engineering after working in logistics for 15 years. This project represents 6+ months of learning AWS, Terraform, and Python through documentation, Stack Overflow, and a lot of trial and error.

I built a monitoring platform instead of following tutorials because I wanted to prove I could:
- Design multi-service AWS infrastructure
- Deploy production-grade monitoring
- Document everything clearly
- Troubleshoot and iterate (35+ actual deployments to AWS)

The 21 screenshots show the real deployment process - setup, configuration, deployment, and validation. Every commit in the history represents actual work and problem-solving, not just theory.

---

## What's Next

**Immediate improvements:**
- AWS Config integration for compliance rules
- VPC Flow Logs analysis
- RDS performance insights
- Cost anomaly detection alerts
- Multi-region deployment capability

**Learning goals:**
- AWS Certified Solutions Architect - Associate
- Kubernetes and container monitoring (ECS/EKS)
- Advanced Terraform modules and patterns
- Python testing frameworks (pytest)

---

## Technical Details

**Infrastructure as Code:**
- All resources defined in Terraform
- Remote state backend (S3 + DynamoDB)
- Modular structure for reuse
- CI/CD ready with GitHub Actions

**Security Best Practices:**
- Least-privilege IAM roles
- Encrypted S3 buckets
- Security group configurations
- GuardDuty continuous monitoring

**Automation:**
- Python scripts using Boto3
- Bash scripts for deployment tasks
- Error handling and validation
- Testing and verification workflows

---

## About Me

**Charles Bucher**  
Cloud Support Engineer (in training)  
📍 Pinellas Park, FL  
✉️ quietopscb@gmail.com  
🔗 [GitHub](https://github.com/charles-bucher) | [LinkedIn](https://linkedin.com/in/charles-bucher-cloud)

I'm self-teaching cloud engineering and building production infrastructure projects to demonstrate capabilities for Cloud Support or Junior DevOps roles. Currently working full-time as a delivery driver while learning AWS, Terraform, and Python.

**Looking for:** Remote Cloud Support Engineer, Junior DevOps, or CloudOps positions where I can prove what I can do through hands-on work.

---

## License

MIT License - see [LICENSE](LICENSE) file

**Note:** This infrastructure is for educational and demonstration purposes. Test in non-production environments and understand AWS billing before deploying to your account.

---

**Last Updated:** December 2025
**Project Status:** Active development - 35+ commits showing real iteration and problem-solving

This infrastructure was deployed and tested multiple times. All screenshots represent actual AWS resources I configured and validated.