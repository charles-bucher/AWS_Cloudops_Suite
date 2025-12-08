# AWS CloudOps Monitoring Platform

![AWS](https://img.shields.io/badge/AWS-CloudOps-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-1.0+-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CloudWatch](https://img.shields.io/badge/CloudWatch-Monitoring-FF4F8B?style=for-the-badge&logo=amazon-cloudwatch&logoColor=white)
![GuardDuty](https://img.shields.io/badge/GuardDuty-Security-DD344C?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Lambda](https://img.shields.io/badge/Lambda-Serverless-FF9900?style=for-the-badge&logo=aws-lambda&logoColor=white)
![SNS](https://img.shields.io/badge/SNS-Alerting-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)
![S3](https://img.shields.io/badge/S3-Storage-569A31?style=for-the-badge&logo=amazon-s3&logoColor=white)
![IAM](https://img.shields.io/badge/IAM-Security-DD344C?style=for-the-badge&logo=amazon-aws&logoColor=white)
![DynamoDB](https://img.shields.io/badge/DynamoDB-State-4053D6?style=for-the-badge&logo=amazon-dynamodb&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Commits](https://img.shields.io/badge/Commits-35+-brightgreen?style=for-the-badge&logo=git&logoColor=white)
![Status](https://img.shields.io/badge/Status-Production_Ready-success?style=for-the-badge)

**Production-ready AWS monitoring infrastructure demonstrating security detection, automated incident response, and cost-effective observability for cloud environments.**

---

## What This Platform Does

This infrastructure provides comprehensive AWS monitoring capabilities:

- **Security Monitoring:** AWS GuardDuty continuously scans for security threats and suspicious activity
- **Infrastructure Monitoring:** CloudWatch tracks metrics, alarms, and dashboards across AWS services
- **Automated Alerting:** SNS delivers notifications via email/SMS when alarms trigger
- **Evidence Storage:** S3 buckets store security findings and logs for analysis
- **Automated Deployment:** Terraform provisions entire infrastructure in a single command
- **Incident Response:** Lambda functions execute automated responses to common scenarios

### The Problem This Solves

**Scenario:** Small team running AWS infrastructure needs 24/7 monitoring but lacks budget for commercial tools like DataDog ($500-1,200/month) or dedicated operations staff.

**This Solution:** Uses AWS native services to provide enterprise-grade monitoring at AWS service costs only (~$15-30/month depending on usage):
- GuardDuty for security threat detection
- CloudWatch for infrastructure monitoring
- SNS for alerting
- Lambda for automation
- All provisioned via Terraform IaC

**Why It Matters:** Demonstrates ability to design, deploy, and document production monitoring infrastructure using infrastructure-as-code and cloud-native services.

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
              │ (Multi-     │
              │  Channel)   │
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

### How It Works

1. **Continuous Monitoring:** GuardDuty scans for security threats; CloudWatch tracks infrastructure metrics
2. **Intelligent Alerting:** When thresholds breach, SNS sends notifications via configured channels
3. **Evidence Collection:** S3 stores security findings and logs for analysis and compliance
4. **Automated Response:** Lambda functions can execute remediation workflows for common incidents
5. **State Management:** DynamoDB provides Terraform state locking for team collaboration

---

## Technical Implementation

### AWS Services Configured

| Service | Purpose | What's Deployed |
|---------|---------|-----------------|
| **GuardDuty** | Security threat detection | Enabled with continuous monitoring |
| **CloudWatch** | Infrastructure monitoring | Custom dashboards, metrics, and configurable alarms |
| **SNS** | Alert distribution | Topics configured for email/SMS notifications |
| **Lambda** | Automated responses | Python-based functions for incident handling |
| **S3** | Evidence storage | Versioned buckets with encryption enabled |
| **IAM** | Access control | Least-privilege roles and policies |
| **DynamoDB** | State locking | Table for Terraform backend state management |

### Infrastructure as Code

- **Terraform:** All resources defined in code (main.tf, variables.tf, outputs.tf)
- **Modular Design:** Organized structure enabling reuse and modification
- **Remote State:** S3 backend with DynamoDB locking configured
- **Version Control:** Git tracked with 35+ commits showing development iteration
- **CI/CD Ready:** GitHub Actions workflow included

### Automation Scripts

- **Python/Boto3:** Scripts for interacting with AWS services programmatically
- **Error Handling:** Comprehensive exception management in automation code
- **Testing:** Verification scripts to validate deployment
- **Documentation:** Inline comments explaining logic and decisions

---

## Deployment Guide

### Prerequisites

- AWS account with administrative access
- Terraform 1.0+ installed
- Python 3.8+ with pip
- AWS CLI configured
- Git

### Installation Steps

```bash
# Clone repository
git clone https://github.com/charles-bucher/AWS_Cloudops_Suite.git
cd AWS_Cloudops_Suite

# Configure AWS credentials
aws configure
# Enter: Access Key ID, Secret Access Key, Region, Output format

# Set up Python environment
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt

# Initialize Terraform
terraform init

# Review planned infrastructure changes
terraform plan

# Deploy infrastructure
terraform apply

# Verify deployment
aws guardduty list-detectors
aws cloudwatch describe-alarms
aws sns list-topics
```

### Testing the Deployment

```bash
# Test SNS notification system
python scripts/send_test_notification.py

# Check CloudWatch metrics
aws cloudwatch describe-alarms

# View GuardDuty status
aws guardduty get-detector --detector-id $(aws guardduty list-detectors --query 'DetectorIds[0]' --output text)
```

### Cleanup

```bash
# Remove all deployed resources
terraform destroy
```

---

## Deployment Evidence

This infrastructure has been deployed and tested through 35+ iterations. Screenshots document the complete deployment process:

### Infrastructure Components

- **Architecture Planning:** Initial design and service selection
- **IAM Configuration:** Programmatic access and permission setup
- **Terraform Backend:** S3 + DynamoDB state management configuration
- **Python Environment:** Boto3 SDK installation and testing
- **AWS CLI Setup:** Credential and region configuration

### Deployed Services

- **CloudWatch:** Dashboards, metrics, and alarm configurations
- **DynamoDB:** State locking table for Terraform
- **IAM:** Roles and policies following least-privilege principle
- **Lambda:** Functions deployed and tested
- **S3:** Buckets created with versioning and encryption
- **GuardDuty:** Enabled and actively monitoring

### Monitoring & Metrics

- **EC2 Metrics:** CPU, network, disk I/O tracking
- **Application Metrics:** Custom performance indicators
- **Lambda Metrics:** Invocation counts, duration, errors

*Complete screenshot documentation available in `/screenshots` directory (21 images)*

---

## Skills Demonstrated

### Cloud Platform Knowledge
✅ AWS service selection and integration  
✅ GuardDuty security monitoring setup  
✅ CloudWatch metrics, alarms, and dashboards  
✅ SNS notification configuration  
✅ Lambda function deployment  
✅ S3 bucket management and security  
✅ IAM role and policy creation  

### Infrastructure as Code
✅ Terraform resource provisioning  
✅ Remote state management with S3/DynamoDB  
✅ Modular code organization  
✅ Variable and output management  
✅ Version control with Git  

### Automation & Scripting
✅ Python/Boto3 AWS SDK usage  
✅ Bash scripting for deployment tasks  
✅ Error handling in automation code  
✅ GitHub Actions workflow creation  

### Operational Practices
✅ Infrastructure documentation  
✅ Deployment verification testing  
✅ Security best practices implementation  
✅ Cost-conscious architecture design  
✅ Iterative development and testing  

---

## Project Structure

```
AWS_Cloudops_Suite/
├── main.tf                 # Primary infrastructure resources
├── variables.tf            # Configuration inputs and parameters
├── outputs.tf              # Exported values for integration
├── backend.tf              # S3 + DynamoDB state management
├── provider.tf             # AWS provider configuration
├── scripts/                # Automation and testing scripts
│   ├── send_test_notification.py
│   └── verify_deployment.sh
├── screenshots/            # Deployment evidence (21 images)
├── docs/                   # Technical documentation
├── tests/                  # Infrastructure validation
├── .github/workflows/      # CI/CD automation
└── README.md              # This file
```

---

## Development Process

**Iterative Development:** 35+ commits showing real development progression
- Initial infrastructure design and planning
- Terraform configuration and testing
- Python automation script development
- Documentation and screenshot capture
- Refinement based on testing and feedback

**What I Learned:**
- Deploying multi-service AWS infrastructure with Terraform
- Configuring GuardDuty for security monitoring
- Setting up CloudWatch alarms and dashboards
- Automating AWS tasks with Python/Boto3
- Managing Terraform state with S3/DynamoDB backend
- Troubleshooting IAM permissions and service integrations
- Documenting infrastructure for others to deploy

---

## Next Steps & Improvements

**Planned Enhancements:**
- [ ] AWS Config integration for compliance rules
- [ ] VPC Flow Logs analysis for network monitoring
- [ ] RDS performance insights integration
- [ ] Cost anomaly detection alerts
- [ ] Multi-region deployment capability
- [ ] Terraform modules for reusability

**Learning Goals:**
- AWS Certified Cloud Practitioner (in progress)
- AWS Certified SysOps Administrator - Associate
- Advanced Terraform patterns and modules
- Container monitoring (ECS/EKS)
- Python testing frameworks (pytest)

---

## Use Cases

**This infrastructure demonstrates capabilities for:**

- **Cloud Support Engineer:** Deploying monitoring, troubleshooting alerts, responding to incidents
- **Junior DevOps Engineer:** Infrastructure automation, CI/CD integration, operational tooling
- **CloudOps Technician:** AWS service configuration, monitoring setup, security scanning
- **Site Reliability:** Observability implementation, incident detection, automated response

---

## Why This Project Exists

### The Story

After 15+ years as a delivery driver, I decided my family deserved better. I started teaching myself cloud engineering at night after my kids went to bed. This project represents 6+ months of learning AWS, Terraform, and Python - not from a bootcamp or course, but by reading documentation, breaking things, fixing them, and documenting everything.

I built this monitoring platform because I wanted to prove I could deploy production-grade infrastructure, not just follow tutorials. Every service integration, every Terraform configuration, every Python script - I figured it out, deployed it, broke it, fixed it, and documented it.

### What This Proves

**For Employers:**
- I can learn complex technical skills independently (taught myself AWS, Terraform, Python)
- I deploy working infrastructure, not just theory (35+ actual AWS deployments)
- I document my work clearly (21 screenshots, comprehensive README)
- I understand the why, not just the how (problem/solution framing, business context)
- I'm reliable and committed (15 years steady employment, married 10+ years, 3 kids)

**For My Career:**
- Demonstrates Cloud Support/DevOps capabilities without traditional CS degree
- Proves I can handle production infrastructure and monitoring
- Shows I take initiative and finish what I start
- Foundation for AWS certifications and continued growth

### What I Bring to a Team

**Customer Service Mindset:** 15 years handling deliveries under pressure taught me how to stay calm when things break, communicate clearly with frustrated users, and solve problems methodically.

**Self-Taught Determination:** I don't wait for someone to teach me - I figure it out. Your team uses a new tool? I'll learn it. Documentation is unclear? I'll improve it.

**Reliability:** I've shown up every day for 15 years. Married 10+ years. Three kids. I'm not job-hopping for the next shiny opportunity - I'm looking for a company that invests in people who prove their value.

### What I'm Looking For

A Cloud Support Engineer, Junior DevOps, or CloudOps role at a company that:
- Values self-taught engineers who prove skills through work
- Judges people on who they are today and their current capabilities
- Offers remote work (I'm reliable, but I need flexibility for my family)
- Invests in people who show initiative and continuous learning

I don't need ping pong tables or free lunches. I need a team that values documentation, reliability, and treating infrastructure - and users - with care.

---

## Contributing

This is a portfolio project demonstrating infrastructure deployment skills. Feedback and suggestions are welcome via GitHub issues.

---

## License

MIT License - see [LICENSE](LICENSE) file for details.

This infrastructure is provided for educational and demonstration purposes. Test in non-production environments and understand AWS billing before deploying.

---

## A Note on This README

I'm an engineer, not a marketing writer. I got help polishing this README because I wanted to present my technical work professionally.

**What's 100% mine:**
- Every line of Terraform code in this repo
- All 35 commits showing real iteration and problem-solving
- The 21 screenshots documenting actual AWS deployments
- 6+ months of learning AWS, Terraform, and Python after work
- The decision to document obsessively because that's how I learn best

**What I got help with:**
- Writing this README in a way that doesn't undersell the work
- Structuring the story so it's clear why this matters
- Professional presentation that matches the quality of the infrastructure

The infrastructure is mine. The learning is mine. The late nights debugging IAM permissions are definitely mine. The polish on how I'm presenting it? I got help with that part.

If you want to talk to the engineer who actually built this - who can walk you through every Terraform resource, explain why I chose GuardDuty over Config, or show you the 12 failed deployments before I got state locking right - email me. I'll talk your ear off about CloudWatch alarm thresholds and SNS notification strategies.

---

## Contact

**Charles Bucher**  
Cloud Support Engineer | AWS CloudOps  
📍 Pinellas Park, FL  
✉️ quietopscb@gmail.com  
🔗 [GitHub: @charles-bucher](https://github.com/charles-bucher) | [LinkedIn](https://linkedin.com/in/charles-bucher-cloud)

---

**Currently:** Self-teaching cloud engineering while working full-time. Building production infrastructure projects to demonstrate capabilities for Cloud Support/DevOps roles.

**Open to:** Remote Cloud Support Engineer, Junior DevOps, or CloudOps positions where reliability, technical documentation, and problem-solving skills matter. Especially interested in companies that value self-taught engineers and focus on current capabilities and continuous growth.

---

## Technical Keywords

AWS • CloudOps • Terraform • Infrastructure as Code • CloudWatch • GuardDuty • Lambda • Python • Boto3 • SNS • S3 • IAM • DynamoDB • Infrastructure Monitoring • Security Monitoring • Alert Management • Incident Response • DevOps • SRE • Site Reliability • Observability • Automation • CI/CD • GitOps • Cloud Security • Remote Work • Entry Level • Self-Taught • Cloud Support Engineer

---

*This infrastructure was deployed, tested, and documented through 35+ iterations. All screenshots represent actual AWS resources I configured and validated. Built as a practical learning project to demonstrate production CloudOps capabilities.*

**Last Updated:** December 2025