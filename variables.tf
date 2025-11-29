variable "region" {
  type        = string
  description = "AWS region for GuardDuty and S3 bucket"
  default     = "us-east-2"
}

variable "findings_bucket" {
  type        = string
  description = "S3 bucket to store GuardDuty findings"
  default     = "guardduty-findings-charlesb"
}
