terraform {
  required_version = ">= 1.7.5"
}

provider "aws" {
  region = "us-east-1"
}

# Example resource: S3 bucket
resource "aws_s3_bucket" "example" {
  bucket = "aws-cloudops-suite-example-${random_id.bucket_id.hex}"
  acl    = "private"
}

# Random ID for unique bucket name
resource "random_id" "bucket_id" {
  byte_length = 4
}
