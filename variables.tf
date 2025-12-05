variable "region" {
  type        = string
  description = "AWS region for resources"
  default     = "us-east-2"
}

variable "findings_bucket" {
  type        = string
  description = "S3 bucket for GuardDuty findings"
  default     = "guardduty-findings-charlesb"
}

variable "environment" {
  type        = string
  description = "Deployment environment"
  default     = "dev"
}
