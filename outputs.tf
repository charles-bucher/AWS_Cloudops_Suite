# ===== GuardDuty Outputs =====
output "guardduty_detector_id" {
  value       = aws_guardduty_detector.main.id
  description = "ID of the GuardDuty detector"
}

output "guardduty_detector_arn" {
  value       = aws_guardduty_detector.main.arn
  description = "ARN of the GuardDuty detector"
}

output "guardduty_account_id" {
  value       = aws_guardduty_detector.main.account_id
  description = "AWS account ID where GuardDuty is enabled"
}

# ===== S3 Bucket Outputs =====
output "findings_bucket_id" {
  value       = aws_s3_bucket.findings.id
  description = "Name of the S3 bucket storing GuardDuty findings"
}

output "findings_bucket_arn" {
  value       = aws_s3_bucket.findings.arn
  description = "ARN of the S3 bucket storing GuardDuty findings"
}

output "findings_bucket_region" {
  value       = aws_s3_bucket.findings.region
  description = "AWS region where the findings bucket is located"
}

# ===== General Outputs =====
output "deployment_region" {
  value       = var.region
  description = "AWS region where resources are deployed"
}

output "environment" {
  value       = "dev"
  description = "Environment designation for this deployment"
}