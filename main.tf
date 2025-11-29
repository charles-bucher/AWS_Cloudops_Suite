terraform {
  required_version = ">= 1.0"

  backend "s3" {
    # Use backend.conf for environment-specific settings
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

# ===== S3 Bucket for GuardDuty Findings =====
resource "aws_s3_bucket" "findings" {
  bucket = var.findings_bucket
  acl    = "private"

  versioning {
    enabled = true
  }

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }

  tags = {
    Name        = "GuardDuty Findings Bucket"
    Environment = "Dev"
  }
}

# ===== GuardDuty Detector =====
resource "aws_guardduty_detector" "main" {
  enable = true
  finding_publishing_frequency = "FIFTEEN_MINUTES"
}

# ===== Outputs =====
output "guardduty_detector_id" {
  value       = aws_guardduty_detector.main.id
  description = "GuardDuty detector ID"
}

output "s3_bucket_name" {
  value       = aws_s3_bucket.findings.id
  description = "S3 bucket storing GuardDuty findings"
}
