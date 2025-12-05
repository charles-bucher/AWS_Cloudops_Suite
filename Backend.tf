terraform {
  backend "s3" {
    bucket = "charlesb-terraform-state"
    key    = "AWS_Cloudops_Suite/terraform.tfstate"
    region = "us-east-1"
  }
}
