from pathlib import Path

docs = {
    "setup.md": """# Setup Guide

- Prerequisites: AWS account with IAM access
- Required tools: AWS CLI, Terraform, Python 3.10+
- Clone repository from GitHub
- Configure AWS credentials using least-privilege IAM user
- Set AWS region and environment variables
- Initialize Terraform backend
- Validate Terraform configuration
- Run local validation scripts
""",

    "operations.md": """# Operations Runbook

- Monitor infrastructure health via CloudWatch
- Review logs for Lambda and automation scripts
- Apply Terraform changes using plan before apply
- Perform routine cost reviews and cleanups
- Validate IAM permissions after changes
- Rotate credentials and secrets regularly
- Handle failed deployments using rollback strategy
- Maintain uptime and service availability
""",

    "troubleshooting.md": """# Troubleshooting Guide

- Terraform apply failures due to permission errors
- AWS CLI credential or region misconfiguration
- Lambda execution failures and timeout issues
- Missing environment variables
- State file locking or corruption issues
- Network or IAM policy misconfigurations
- Debug using CloudWatch logs and error output
""",

    "monitoring.md": """# Monitoring & Alerting

- Use AWS CloudWatch for metrics and logs
- Monitor Lambda execution duration and errors
- Track Terraform drift and failed applies
- Set alarms for cost thresholds
- Review logs regularly for anomalies
- Ensure alerts route to appropriate channels
- Maintain visibility into system health
""",

    "security.md": """# Security Practices

- Enforce least-privilege IAM policies
- Avoid hardcoding credentials or secrets
- Use environment variables or AWS Secrets Manager
- Enable logging for audit and traceability
- Review permissions regularly
- Apply security updates to dependencies
- Follow AWS shared responsibility model
"""
}

docs_dir = Path("docs")
docs_dir.mkdir(exist_ok=True)

for filename, content in docs.items():
    file_path = docs_dir / filename
    file_path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"Created {file_path}")

print("\n✅ Documentation skeletons created successfully.")
