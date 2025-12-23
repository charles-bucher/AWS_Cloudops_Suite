# AWS_Cloudops_Suite Architecture

This document describes the overall architecture of the CloudOps Suite, showing how AWS services integrate to provide monitoring, security, and automation.

## Architecture Diagram

![CloudOps Architecture](../diagrams/architecture.png)

## Service Flow

1. **GuardDuty**  
   - Detects threats in AWS accounts per region.
   - Findings are sent to S3 and optionally trigger Lambda.

2. **Lambda Functions**  
   - Automatically respond to GuardDuty findings.  
   - Can remediate IAM, EC2, or S3 issues.

3. **SNS Notifications**  
   - Alerts administrators via email or triggers additional Lambdas.  

4. **S3**  
   - Centralized storage for GuardDuty findings and logs.

5. **CloudWatch**  
   - Metrics and alarms monitor the environment.  
   - Triggers automated actions via Lambda.

6. **DynamoDB**  
   - Used for Terraform state locking to ensure safe multi-user deployments.

---

## Terraform Modules

- `guardduty/` – Enable detectors and configure S3 logging  
- `cloudwatch/` – Create dashboards and alarms  
- `sns/` – Topic and subscription setup  
- `lambda/` – Deploy Lambda functions  
- `s3/` – Bucket creation and configuration  
- `iam/` – Roles and policies for least-privilege access
