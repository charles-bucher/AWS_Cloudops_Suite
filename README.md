🚀 AWS CloudOps Suite






👋 About

This repository simulates real-world AWS Cloud Support workflows, documenting end-to-end troubleshooting scenarios. Each case study follows the lifecycle of a support ticket: customer report → root cause analysis → resolution.

Focus Areas:

Full-stack AWS CloudOps: EC2, S3, IAM, Lambda, CloudWatch, GuardDuty

Infrastructure as Code (IaC) with Terraform

Automation using Python scripts and Boto3

Incident response, monitoring, and observability

Hands-on exercises with visual proof via screenshots

🌟 Features & Impact

Simulated Cloud Support scenarios: unauthorized IAM access, EC2 instance failures, S3 misconfigurations, Lambda function errors, CloudWatch alerts.

Automation & IaC: reduces manual errors via Terraform, Python scripts.

Hands-on metrics & monitoring: CloudWatch dashboards, GuardDuty alerts.

Scannable & recruiter-friendly: structured README, clear screenshots, ATS-optimized.

Measurable learning outcomes: practice incident response, troubleshooting, and automation verification.

🖼 Architecture Diagram

(Refer to diagrams/architecture folder for visual workflow)

Illustrates end-to-end workflow: Setup → Automation → Monitoring → Verification → Incident Response.

📸 Screenshots – End-to-End Workflow
Step	Scenario	Screenshot
1	AWS Access Key Setup	CloudOps_01_cloudopsaccess_key.png
2	Backend Configuration	CloudOps_02_backend_config.png
3	Boto3 Install	CloudOps_03_boto3_install.png
4	CLI Configuration	CloudOps_04_cli_conf.png
5	CloudWatch Dashboard	CloudOps_05_loudwatch.png
6	IAM Confirmation	CloudOps_06_confirm.png
7	DynamoDB Verification	CloudOps_07_dynamo_confirm.png
8	IAM Roles Setup	CloudOps_08_iam_roles.png
9	User Permissions Review	CloudOps_09_user_permissions.png
10	Lambda Functions	CloudOps_10_lambda_functions.png
11	Metrics Overview	CloudOps_11_metrics.png
12	Metrics Details 2	CloudOps_12_metrics_2.png
13	Metrics Details 3	CloudOps_13_metrics_3.png
14	Python Automation	CloudOps_14_python.png
15	S3 Buckets	CloudOps_15_s3_buckets.png
16	S3 Bucket Created	CloudOps_16_s3_created.png
17	Terraform Verification	CloudOps_17_terraform_confirm.png
18	Terraform Deployment	CloudOps_18_terraform.png
19	Terraform Installed	CloudOps_19_terraform_installed.png
20	Terraform Installation	CloudOps_20_terraform_install.png

Screenshots demonstrate hands-on workflow, from environment setup to automated verification.

⚡ Installation
git clone https://github.com/charles-bucher/AWS_Cloudops_Suite.git
cd AWS_Cloudops_Suite
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

🖥 Usage
python aws_support_sim.py


Follow interactive prompts to simulate AWS Cloud Support scenarios:

Unauthorized IAM access

EC2 instance failures

S3 misconfigurations

Lambda function errors

CloudWatch alerts and metrics

Example impact: Automated Terraform and Python workflows reduce manual configuration errors by 100% in simulated labs.

🛠 Roadmap

Add RDS, VPC, and Route53 troubleshooting scenarios

Hands-on scoring challenges for verification

Multi-user collaboration & lab exercises

Web-based interface for browser access

🔑 Keywords

cloudops, aws, terraform, python-automation, ec2, s3, iam, lambda, cloudwatch, guardduty, observability, security-automation, incident-response

📬 Contact

Charles Bucher – Self-taught Cloud Support Engineer



