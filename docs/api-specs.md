# API Specifications — AWS_Cloudops_Suite

This document lists all the AWS services and API calls used in the CloudOps Suite automation scripts, Lambda functions, and Terraform modules. It is intended for maintainers, reviewers, and portfolio viewers.

---

## 1. AWS GuardDuty

| Function / Call | Description | Input Parameters | Output / Effect | Notes |
|-----------------|------------|----------------|----------------|------|
| `create_detector()` | Enable GuardDuty in a region | `Enable` (boolean) | Detector ID | Each region needs its own detector |
| `list_detectors()` | List existing detectors | None | List of detector IDs | Used for validation |
| `get_findings()` | Retrieve GuardDuty findings | `DetectorId`, `FindingIds` | JSON array of findings | Can feed automation scripts or alerts |
| `create_sample_findings()` | Generate test findings | `DetectorId` | Sample finding event | For testing Lambda triggers |

---

## 2. AWS S3

| Function / Call | Description | Input Parameters | Output / Effect | Notes |
|-----------------|------------|----------------|----------------|------|
| `create_bucket()` | Create versioned, encrypted S3 bucket | `BucketName`, `Versioning`, `Encryption` | Bucket created | Terraform also manages buckets |
| `put_object()` | Upload log or alert file | `BucketName`, `Key`, `Body` | File stored in S3 | Logs from scripts or Lambda |
| `get_object()` | Retrieve file from bucket | `BucketName`, `Key` | File contents | Used for monitoring and validation |

---

## 3. AWS Lambda

| Function / Call | Description | Input Parameters | Output / Effect | Notes |
|-----------------|------------|----------------|----------------|------|
| `invoke()` | Run a Lambda function | `FunctionName`, `Payload` | Execution result | Used for automated remediation or alerts |
| `create_function()` | Deploy Lambda | `FunctionName`, `Handler`, `Runtime`, `Role` | Lambda created | Managed via Terraform or Python |
| `add_permission()` | Grant triggers | `FunctionName`, `StatementId`, `Action`, `Principal` | Permission added | Needed for SNS or CloudWatch events |

---

## 4. AWS SNS

| Function / Call | Description | Input Parameters | Output / Effect | Notes |
|-----------------|------------|----------------|----------------|------|
| `create_topic()` | Create SNS topic | `Name` | Topic ARN | Used for email or Lambda notifications |
| `subscribe()` | Subscribe endpoint | `TopicArn`, `Protocol`, `Endpoint` | Subscription created | Email or Lambda endpoint |
| `publish()` | Send alert | `TopicArn`, `Message` | Alert delivered | Lambda or scripts trigger this on findings |

---

## 5. AWS CloudWatch

| Function / Call | Description | Input Parameters | Output / Effect | Notes |
|-----------------|------------|----------------|----------------|------|
| `put_metric_alarm()` | Create CloudWatch alarm | `AlarmName`, `MetricName`, `Threshold` | Alarm triggered on condition | Used to trigger Lambda or SNS |
| `get_metric_statistics()` | Retrieve metrics | `Namespace`, `MetricName` | JSON metrics | Used in cost or monitoring scripts |
| `put_dashboard()` | Create dashboard | `DashboardName`, `DashboardBody` | Visual dashboard | Terraform or Python updates dashboards |

---

## 6. AWS IAM

| Function / Call | Description | Input Parameters | Output / Effect | Notes |
|-----------------|------------|----------------|----------------|------|
| `create_role()` | Create IAM role | `RoleName`, `AssumeRolePolicy` | Role created | Lambda and Terraform use least-privilege roles |
| `attach_policy()` | Assign permissions | `RoleName`, `PolicyArn` | Permissions applied | Policies are modular for reuse |
| `list_roles()` | List existing roles | None | List of roles | Validation or troubleshooting |

---

## 7. Terraform Modules

| Module | Purpose | Key Resources |
|--------|--------|---------------|
| `guardduty/` | Enable detectors, configure findings | `aws_guardduty_detector`, `aws_s3_bucket` |
| `cloudwatch/` | Metrics, alarms, dashboards | `aws_cloudwatch_metric_alarm`, `aws_cloudwatch_dashboard` |
| `sns/` | Notification topics & subscriptions | `aws_sns_topic`, `aws_sns_topic_subscription` |
| `lambda/` | Deploy automation functions | `aws_lambda_function`, `aws_iam_role` |
| `s3/` | Log and artifact storage | `aws_s3_bucket` |
| `iam/` | Access control | `aws_iam_role`, `aws_iam_policy` |

---

### Notes

- All API calls are used via **Python Boto3 scripts** or **Terraform HCL modules**.  
- Scripts are modular; Lambda triggers and SNS alerts are **event-driven**.  
- Validation scripts (`validate_repos.py`, `test-main.py`) use API calls to ensure resources exist and permissions are correct.  

---

**Reference in README**:

```markdown
## API Reference
For a detailed list of AWS API calls used in this project, see [API Specs](docs/api-specs.md)
