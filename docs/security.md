# Security — AWS_Cloudops_Suite

This document outlines the **security measures, policies, and best practices** used in the AWS_Cloudops_Suite environment. It focuses on AWS service configuration, automated monitoring, and access control.

---

## 🔐 IAM & Access Management

- **Least-Privilege Access**: All IAM roles and policies follow the principle of least privilege.
- **Role-Based Access Control**: Lambda, Terraform, and monitoring scripts use dedicated roles.
- **Policies**: Modular, reusable policies applied to specific services or functions.
- **Validation**: `validate_repos.py` ensures roles and permissions exist and are correct.

**Example: Lambda Execution Role**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "guardduty:GetFindings",
        "cloudwatch:PutMetricData"
      ],
      "Resource": "*"
    }
  ]
}
