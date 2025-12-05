AWS CloudOps Suite
GitHub Repo Size
GitHub Last Commit
GitHub Language
License: MIT
Hands‑on AWS monitoring, alerting, and automation project built for learning CloudOps practices and demonstrating practical skills in CloudWatch monitoring, Terraform infrastructure, Python automation, and GuardDuty security.

📋 About
This project sets up a full‑stack AWS CloudOps environment, including:
- GuardDuty for security monitoring
- CloudWatch for metrics and alerts
- S3 Buckets for findings storage
- SNS for notifications
- Terraform for infrastructure as code
Designed for entry‑level Cloud Support / CloudOps roles to showcase practical skills.

🏗️ System Architecture
CloudOps Pipeline Overview:
- Terraform Deployment – Infrastructure setup (GuardDuty, CloudWatch alarms, SNS topics, S3 buckets)
- Security Monitoring – GuardDuty detects threats and findings
- Alerts & Automation – CloudWatch alarms trigger SNS notifications
- Evidence Storage – Findings stored in S3 for auditing

🚀 Quick Start
Prerequisites
- AWS Free Tier account
- Terraform 1.0+
- Python 3.8+
- AWS CLI configured
Installation
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
# Initialize Terraform
terraform init

# Review planned changes
terraform plan

# Apply infrastructure
terraform apply



📸 Implementation Evidence
Terraform Plan Output
|  | 
|  | 



AWS Configuration & Access
|  |  |  |  | 
|  |  |  |  | 



CloudWatch & Monitoring
|  |  | 
|  |  | 



DynamoDB & IAM
|  |  |  | 
|  |  |  | 



Lambda & Metrics
|  |  |  |  | 
|  |  |  |  | 



Python Scripts & S3
|  |  |  | 
|  |  |  | 



Terraform Deployment
|  |  |  |  | 
|  |  |  |  | 



📚 Skills Demonstrated
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 



🎯 Next Steps
- Add RDS monitoring scenarios
- Implement VPC flow log analysis
- Build CI/CD pipeline with GitHub Actions
- Add unit tests and cost monitoring

💼 Career Relevance
Skills highlighted in this project are applicable to:
- Cloud Support Engineer
- Junior DevOps / CloudOps Roles
- Infrastructure as Code / AWS Automation

📝 License
This project is licensed under the MIT License. See the LICENSE file for details.

📧 Contact
Charles Bucher
📍 Pinellas Park, Florida
✉️ quietopscb@gmail.com
🔗 GitHub • LinkedIn

🔑 Keywords for ATS
AWS, CloudOps, Terraform, Python, CloudWatch, GuardDuty, Lambda, S3, DynamoDB, IAM, Infrastructure as Code, Boto3, Monitoring, Alerting, Security Automation, DevOps, Cloud Support, Incident Response, Observability


