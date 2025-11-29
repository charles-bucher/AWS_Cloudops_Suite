terraform {
  required_version = ">= 1.0"

  backend "s3" {
    bucket         = "charlesb-terraform-state"  # Replace with your S3 bucket for remote state
    key            = "cloudOps-guardDuty-automation/terraform.tfstate"
    region         = "us-east-1"                 # Region of the S3 bucket
    dynamodb_table = "terraform-locks"           # Optional: DynamoDB table for state locking
    encrypt        = true                        # Encrypt state at rest
  }
}

# Optional: lock table creation example (if it doesn't exist)
# resource "aws_dynamodb_table" "terraform_lock" {
#   name         = "terraform-locks"
#   billing_mode = "PAY_PER_REQUEST"
#   hash_key     = "LockID"
#   attribute {
#     name = "LockID"
#     type = "S"
#   }
# }
