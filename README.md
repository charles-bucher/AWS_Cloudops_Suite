# AWS CloudOps Suite

[![AWS](https://img.shields.io/badge/AWS-CloudWatch_Lambda_GuardDuty-FF9900?style=flat-square&logo=amazon-aws)](https://aws.amazon.com/)
[![Terraform](https://img.shields.io/badge/Terraform-Infrastructure-7B42BC?style=flat-square&logo=terraform)](https://www.terraform.io/)
[![Python](https://img.shields.io/badge/Python-Automation-3776AB?style=flat-square&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)

> Hands-on AWS monitoring, alerting, and automation project built while learning CloudOps practices.

---

## 📋 What This Is

A personal learning project where I built an AWS monitoring and automation pipeline from scratch. This demonstrates practical skills in CloudWatch monitoring, Terraform infrastructure deployment, Python automation, and security monitoring with GuardDuty.

**Built for:** Demonstrating CloudOps and Cloud Support engineering skills for entry-level to junior positions.

---

## 🎯 Skills Demonstrated

| Skill Area | Technologies Used |
|------------|------------------|
| **Cloud Monitoring** | AWS CloudWatch metrics, alarms, dashboards |
| **Security Monitoring** | AWS GuardDuty, automated findings alerts |
| **Infrastructure as Code** | Terraform (HCL), backend state management |
| **Automation** | Python, Boto3 SDK, AWS CLI |
| **Serverless** | AWS Lambda functions |
| **Storage & Databases** | S3 buckets, DynamoDB tables |
| **Identity & Access** | IAM roles, policies, user permissions |

---

## 🏗️ System Architecture

### Overall CloudOps Pipeline

```mermaid
graph TB
    subgraph "AWS CloudOps Monitoring & Automation Pipeline"
        A[CloudWatch Metrics] --> B[Custom Alarms]
        B --> C{Threshold Exceeded?}
        
        C -->|Yes| D[SNS Topic]
        C -->|No| A
        
        D --> E[Email Alert]
        
        F[GuardDuty] --> G[Security Findings]
        G --> H[Python Monitor Script]
        H --> I[findings-monitor.py]
        I --> J[S3 Findings Bucket]
        J --> K[Alert Email]
        
        L[Terraform] --> M[Infrastructure Deployment]
        M --> N[Lambda Functions]
        M --> O[DynamoDB Tables]
        M --> P[IAM Roles]
        
        N --> Q[CloudWatch Logs]
        Q --> A
        
        R[Python Scripts] --> S[Automated Tasks]
        S --> T[Boto3 API Calls]
    end
    
    style D fill:#ffd43b
    style E fill:#51cf66
    style K fill:#ff6b6b
    style M fill:#4dabf7
```

---

### Terraform Infrastructure Workflow

```mermaid
flowchart LR
    subgraph "Infrastructure as Code Deployment"
        A[Local Development] --> B[terraform init]
        B --> C[terraform plan]
        C --> D{Review Changes}
        
        D -->|Approve| E[terraform apply]
        D -->|Reject| C
        
        E --> F[AWS Provider]
        
        F --> G[Create IAM Roles]
        F --> H[Deploy Lambda]
        F --> I[Create S3 Buckets]
        F --> J[Setup DynamoDB]
        F --> K[Configure CloudWatch]
        
        G --> L[State File]
        H --> L
        I --> L
        J --> L
        K --> L
        
        L --> M[S3 Backend]
        M --> N[DynamoDB Lock Table]
    end
    
    style E fill:#7B42BC
    style M fill:#FF9900
    style N fill:#FF9900
```

---

### GuardDuty Security Monitoring Flow

```mermaid
sequenceDiagram
    participant GD as GuardDuty
    participant PY as Python Script
    participant S3 as S3 Bucket
    participant SNS as SNS Topic
    participant Email as Email Alert
    
    Note over GD: Continuous threat detection
    GD->>GD: Analyze VPC Flow Logs
    GD->>GD: Analyze CloudTrail Events
    GD->>GD: Analyze DNS Logs
    
    alt Finding Detected
        GD->>PY: Security Finding Event
        PY->>PY: Parse finding details
        PY->>S3: Store finding JSON
        PY->>SNS: Publish alert
        SNS->>Email: Send notification
        
        Note over Email: Admin reviews finding
    else No Findings
        GD->>PY: Status: Clean
        Note over PY: Script continues monitoring
    end
    
    PY->>PY: Sleep 5 minutes
    PY->>GD: Check for new findings
```

---

### CloudWatch Monitoring & Alerting

```mermaid
graph TD
    subgraph "Monitoring System"
        A[EC2 Instances] --> B[CloudWatch Agent]
        C[Lambda Functions] --> D[CloudWatch Logs]
        E[S3 Buckets] --> F[Access Logs]
        
        B --> G[CloudWatch Metrics]
        D --> G
        F --> G
        
        G --> H{Metric Threshold}
        
        H -->|CPU > 80%| I[High CPU Alarm]
        H -->|Errors > 10| J[Error Rate Alarm]
        H -->|Normal| K[OK State]
        
        I --> L[SNS Topic: Critical]
        J --> L
        
        L --> M[Email Alert]
        L --> N[Lambda: Auto-Remediation]
        
        N --> O[Scale Resources]
        N --> P[Restart Service]
        N --> Q[Log Incident]
        
        Q --> R[DynamoDB Incident Table]
    end
    
    style I fill:#ff6b6b
    style J fill:#ff6b6b
    style K fill:#51cf66
    style M fill:#ffd43b
    style R fill:#4dabf7
```

---

### Project Learning Phases

```mermaid
graph LR
    subgraph "Phase 1: Setup"
        A1[AWS CLI Config]
        A2[Boto3 Install]
        A3[Terraform v1.13.2]
    end
    
    subgraph "Phase 2: State Management"
        B1[S3 Backend]
        B2[DynamoDB Lock]
        B3[Secure Credentials]
    end
    
    subgraph "Phase 3: IAM & Security"
        C1[IAM Roles]
        C2[Policies]
        C3[User Permissions]
    end
    
    subgraph "Phase 4: Monitoring"
        D1[CloudWatch Metrics]
        D2[Custom Alarms]
        D3[Dashboards]
    end
    
    subgraph "Phase 5: Automation"
        E1[Lambda Functions]
        E2[Python Scripts]
        E3[S3 Storage]
    end
    
    subgraph "Phase 6: Infrastructure"
        F1[Terraform Deploy]
        F2[Outputs]
        F3[State Management]
    end
    
    A1 --> A2 --> A3
    A3 --> B1 --> B2 --> B3
    B3 --> C1 --> C2 --> C3
    C3 --> D1 --> D2 --> D3
    D3 --> E1 --> E2 --> E3
    E3 --> F1 --> F2 --> F3
    
    style A1 fill:#4dabf7
    style B1 fill:#4dabf7
    style C1 fill:#ff6b6b
    style D1 fill:#ffd43b
    style E1 fill:#51cf66
    style F1 fill:#7B42BC
```

---

### Data Flow Diagram

```mermaid
flowchart TD
    subgraph "CloudOps Data Pipeline"
        A[AWS Resources] -->|Metrics| B[CloudWatch]
        A -->|Logs| C[CloudWatch Logs]
        A -->|Events| D[EventBridge]
        
        B --> E[Metric Filters]
        C --> F[Log Groups]
        D --> G[Event Rules]
        
        E --> H{Alarm State}
        F --> I[Log Insights]
        G --> J[Event Targets]
        
        H -->|ALARM| K[SNS Topic]
        H -->|OK| L[Dashboard]
        
        I --> M[Query Results]
        J --> N[Lambda Trigger]
        
        K --> O[Email/SMS]
        K --> N
        
        N --> P[Python Handler]
        P --> Q{Action Type}
        
        Q -->|Store| R[S3 Bucket]
        Q -->|Record| S[DynamoDB]
        Q -->|Alert| T[SNS]
        
        R --> U[Long-term Storage]
        S --> V[Incident Database]
        T --> W[Notification System]
    end
    
    style H fill:#ffd43b
    style K fill:#ff6b6b
    style L fill:#51cf66
    style P fill:#4dabf7
```

---

## 📸 Implementation Evidence

### Phase 1: Environment Setup

<details>
<summary>📋 AWS Configuration & Authentication</summary>

**AWS Access Key Configuration:**
![CloudOps Access Key](https://raw.githubusercontent.com/charles-bucher/AWS_Cloudops_Suite/main/screenshots/CloudOps_01_cloudopsaccess_key.png)
*Configured AWS CLI with access keys for programmatic access*

**Backend State Configuration:**
![Backend Config](https://raw.githubusercontent.com/charles-bucher/AWS_Cloudops_Suite/main/screenshots/CloudOps_02_backend_config.png)
*Set up Terraform backend for remote state management in S3*

**Boto3 SDK Installation:**
![Boto3 Install](https://raw.githubusercontent.com/charles-bucher/AWS_Cloudops_Suite/main/screenshots/CloudOps_03_boto3_install.png)
*Installed AWS SDK for Python (Boto3) for automation scripts*

**CLI Configuration Verification:**
![CLI Config](https://raw.githubusercontent.com/charles-bucher/AWS_Cloudops_Suite/main/screenshots/CloudOps_04_cli_conf.png)
*Verified AWS CLI configuration and credentials*

**CloudWatch Initial Setup:**
![CloudWatch Setup](https://raw.githubusercontent.com/charles-bucher/AWS_Cloudops_Suite/main/screenshots/CloudOps_05_cloudwatch.png)
*Configured CloudWatch for metrics collection and monitoring*

</details>

---

### Phase 2: State Management & Database

<details>
<summary>📋 Terraform State & DynamoDB</summary>

**State Lock Confirmation:**
![Confirmation](https://raw.githubusercontent.com/charles-bucher/AWS_Cloudops_Suite/main/screenshots/CloudOps_06_confirm.png)
*Verified Terraform state locking mechanism*

**DynamoDB State Lock Table:**
![DynamoDB Confirm](https://raw.githubusercontent.com/charles-bucher/AWS_Cloudops_Suite/main/screenshots/CloudOps_07_dynamo_confirm.png)
*Created DynamoDB table for Terraform state locking to prevent concurrent modifications*

</details>

---

### Phase 3: Identity & Access Management

<details>
<summary>📋 IAM Roles & Permissions</summary>

**IAM Roles Created:**
![IAM Roles](https://raw.githubusercontent.com/charles-bucher/AWS_Cloudops_Suite/main/screenshots/CloudOps_08_iam_roles.png)
*Configured IAM roles for Lambda functions and EC2 instances*

**User Permission Policies:**
![User Permissions](https://raw.githubusercontent.com/charles-bucher/AWS_Cloudops_Suite/main/screenshots/CloudOps_09_user_permissions.png)
*Applied least-privilege IAM policies for secure access control*

</details>

---

### Phase 4: Serverless Functions

<details>
<summary>📋 Lambda Deployment</summary>

**Lambda Functions Deployed:**
![Lambda Functions](https://raw.githubusercontent.com/charles-bucher/AWS_Cloudops_Suite/main/screenshots/CloudOps_10_lambda_functions.png)
*Created Lambda functions for automated monitoring and alerting tasks*

</details>

---

### Phase 5: Monitoring & Metrics

<details>
<summary>📋 CloudWatch Metrics Dashboard</summary>

**Metrics Overview:**
![Metrics Overview](https://raw.githubusercontent.com/charles-bucher/AWS_Cloudops_Suite/main/screenshots/CloudOps_11_metrics.png)
*CloudWatch dashboard showing key infrastructure metrics*

**CPU Utilization Metrics:**
![Metrics Detail 2](https://raw.githubusercontent.com/charles-bucher/AWS_Cloudops_Suite/main/screenshots/CloudOps_12_metrics_2.png)
*Detailed CPU utilization tracking for EC2 instances*

**Custom Metric Configuration:**
![Metrics Detail 3](https://raw.githubusercontent.com/charles-bucher/AWS_Cloudops_Suite/main/screenshots/CloudOps_13_metrics_3.png)
*Custom CloudWatch metrics for application-specific monitoring*

</details>

---

### Phase 6: Automation & Storage

<details>
<summary>📋 Python Scripts & S3 Management</summary>

**Python Automation Script:**
![Python Execution](https://raw.githubusercontent.com/charles-bucher/AWS_Cloudops_Suite/main/screenshots/CloudOps_14_python.png)
*Python script execution for GuardDuty findings monitoring*

**S3 Buckets Overview:**
![S3 Buckets](https://raw.githubusercontent.com/charles-bucher/AWS_Cloudops_Suite/main/screenshots/CloudOps_15_s3_buckets.png)
*S3 buckets created for Terraform state and GuardDuty findings storage*

**S3 Bucket Creation Confirmation:**
![S3 Created](https://raw.githubusercontent.com/charles-bucher/AWS_Cloudops_Suite/main/screenshots/CloudOps_16_s3_created.png)
*Successful creation of findings storage bucket*

</details>

---

### Phase 7: Infrastructure as Code

<details>
<summary>📋 Terraform Deployment Process</summary>

**Terraform Deployment Confirmation:**
![Terraform Confirm](https://raw.githubusercontent.com/charles-bucher/AWS_Cloudops_Suite/main/screenshots/CloudOps_17_terraform_confirm.png)
*Terraform plan confirmation before applying infrastructure changes*

**Terraform Execution:**
![Terraform Setup](https://raw.githubusercontent.com/charles-bucher/AWS_Cloudops_Suite/main/screenshots/CloudOps_18_terraform.png)
*Running Terraform apply to provision AWS resources*

**Terraform Installation Verified:**
![Terraform Installed](https://raw.githubusercontent.com/charles-bucher/AWS_Cloudops_Suite/main/screenshots/CloudOps_19_terraform_installed.png)
*Terraform v1.13.2 successfully installed and configured*

**Terraform Installation Process:**
![Terraform Install](https://raw.githubusercontent.com/charles-bucher/AWS_Cloudops_Suite/main/screenshots/CloudOps_20_terraform_install.png)
*Step-by-step Terraform installation on Windows*

</details>

---

## 📁 Project Structure

```
AWS_Cloudops_Suite/
├── .github/workflows/       # CI/CD automation (future)
├── diagrams/architecture/   # Architecture diagrams
├── docs/                    # Documentation
├── screenshots/             # Implementation evidence (20 images)
├── scripts/                 # Python automation scripts
│   ├── findings-monitor.py  # GuardDuty monitoring
│   └── health-check.py      # Infrastructure health checks
├── tests/                   # Test suites
├── main.tf                  # Primary Terraform configuration
├── variables.tf             # Terraform variables
├── outputs.tf               # Terraform outputs
├── backend.tf               # Remote state configuration
├── provider.tf              # AWS provider configuration
├── backend.conf             # Backend credentials (gitignored)
└── README.md                # This file
```

---

## 🚀 Quick Start

### Prerequisites

- AWS Free Tier account
- Terraform 1.0+
- Python 3.8+
- AWS CLI configured

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
# source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Configure AWS credentials
aws configure
```

### Deploy Infrastructure

```bash
# Initialize Terraform
terraform init

# Review planned changes
terraform plan

# Apply infrastructure
terraform apply
```

### Run Monitoring Scripts

```bash
# Activate virtual environment
.\venv\Scripts\activate

# Run GuardDuty findings monitor
python scripts/findings-monitor.py

# Run infrastructure health check
python scripts/health-check.py
```

---

## 📚 What I Learned

### AWS Services
- **CloudWatch**: Creating custom metrics, alarms, and dashboards
- **GuardDuty**: Security threat detection and automated findings alerts
- **Lambda**: Serverless function deployment and event-driven architecture
- **S3**: Bucket management, lifecycle policies, and secure storage
- **DynamoDB**: NoSQL database for Terraform state locking
- **IAM**: Role-based access control and least-privilege policies

### Infrastructure as Code
- Writing modular Terraform configurations
- Managing remote state with S3 and DynamoDB
- Using variables and outputs for reusable infrastructure
- Terraform workspace management

### Automation & Scripting
- Boto3 SDK for AWS API interactions
- Python scripts for continuous monitoring
- Automated alerting workflows
- Environment variable management for credentials

### DevOps Practices
- Git version control for infrastructure code
- Documentation with screenshots for proof of work
- Modular code organization
- Security best practices (credential management, least privilege)

---

## 🎯 Next Steps

**Planned Improvements:**
- [ ] Add RDS database monitoring scenarios
- [ ] Implement VPC flow log analysis
- [ ] Create Route53 health check automation
- [ ] Build CI/CD pipeline with GitHub Actions
- [ ] Add comprehensive unit tests
- [ ] Create cost optimization monitoring

---

## 💼 Skills for Job Applications

This project demonstrates skills relevant to:

**Cloud Support Engineer Roles:**
- CloudWatch monitoring and troubleshooting
- Security incident detection with GuardDuty
- IAM policy management
- AWS CLI proficiency

**DevOps Engineer Roles:**
- Infrastructure as Code (Terraform)
- Python automation scripting
- CI/CD pipeline concepts
- Version control with Git

**Cloud Operations Roles:**
- Proactive monitoring and alerting
- Serverless architecture (Lambda)
- Resource provisioning and management
- Documentation and runbook creation

---

## 📧 Contact

**Charles Bucher**  
📍 Pinellas Park, Florida  
✉️ quietopscb@gmail.com  
🔗 [GitHub](https://github.com/charles-bucher) • [LinkedIn](https://linkedin.com/in/charles-bucher-cloud)

Currently building cloud infrastructure skills and seeking Cloud Support Engineer or Junior DevOps opportunities.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

Built while learning from:
- AWS Official Documentation
- Terraform Registry and Best Practices
- Python Boto3 SDK Documentation
- CloudOps community resources

---

**Keywords for ATS:** AWS, CloudOps, Terraform, Python, CloudWatch, GuardDuty, Lambda, S3, DynamoDB, IAM, Infrastructure as Code, Boto3, Monitoring, Alerting, Security Automation, DevOps, Cloud Support, Incident Response, Observability