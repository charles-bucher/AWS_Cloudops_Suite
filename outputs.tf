output "deployment_region" {
  value       = var.region
  description = "AWS region of deployment"
}

output "environment" {
  value       = var.environment
  description = "Deployment environment"
}

output "findings_bucket_id" {
  value       = aws_s3_bucket.findings.id
  description = "Name of the S3 bucket storing GuardDuty findings"
}

output "findings_bucket_arn" {
  value       = aws_s3_bucket.findings.arn
  description = "ARN of the S3 bucket storing GuardDuty findings"
}

output "guardduty_detector_id" {
  value       = aws_guardduty_detector.main.id
  description = "GuardDuty detector ID"
}

output "alert_sns_topic_arn" {
  value       = aws_sns_topic.alerts.arn
  description = "SNS topic ARN for GuardDuty alerts"
}
