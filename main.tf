# =====================
# S3 bucket for findings
# =====================
resource "aws_s3_bucket" "findings" {
  bucket = var.findings_bucket
  acl    = "private"

  tags = {
    Name        = "GuardDuty Findings Bucket"
    Environment = var.environment
    Region      = var.region
  }
}

resource "aws_s3_bucket_versioning" "findings" {
  bucket = aws_s3_bucket.findings.id
  versioning_configuration {
    status = "Enabled"
  }
}

# =====================
# Enable GuardDuty
# =====================
resource "aws_guardduty_detector" "main" {
  enable = true
}

# =====================
# CloudWatch Alarm Example
# =====================
resource "aws_cloudwatch_metric_alarm" "guardduty_finding" {
  alarm_name          = "GuardDutyFindingAlarm"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 1
  metric_name         = "FindingsCount"
  namespace           = "AWS/GuardDuty"
  period              = 300
  statistic           = "Sum"
  threshold           = 0

  alarm_description = "Alert if GuardDuty finds any findings."
}

# =====================
# SNS Topic for Alerts
# =====================
resource "aws_sns_topic" "alerts" {
  name = "cloudops-alerts"
}

resource "aws_cloudwatch_metric_alarm" "finding_alarm_sns" {
  alarm_name          = "GuardDutyFindingAlarmSNS"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 1
  metric_name         = "FindingsCount"
  namespace           = "AWS/GuardDuty"
  period              = 300
  statistic           = "Sum"
  threshold           = 0
  alarm_actions       = [aws_sns_topic.alerts.arn]
}
