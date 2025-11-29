# DEPLOYMENT GUIDE

## Quick Start (5 Minutes)

### 1. Set Your Email Address

Edit `variables.tf` and change the default email:

```hcl
variable "alert_email" {
  description = "Email address for CloudWatch alert notifications"
  type        = string
  default     = "YOUR-EMAIL@example.com"  # ← CHANGE THIS!
```

### 2. Deploy

```bash
terraform init
terraform plan
terraform apply
```

### 3. Confirm Email

Check your email and click the AWS SNS confirmation link.

---

## Detailed Steps

### A. Verify Prerequisites

```bash
# Check Terraform version
terraform --version
# Should be v1.0 or higher

# Check AWS credentials
aws sts get-caller-identity
# Should show your AWS account details
```

### B. Deploy Infrastructure

```bash
# Initialize (first time only)
terraform init

# Preview changes
terraform plan

# Deploy
terraform apply
```

**Expected output:**
```
Apply complete! Resources: 5 added, 0 changed, 0 destroyed.

Outputs:

cpu_alarm_arn = "arn:aws:cloudwatch:us-east-1:..."
ec2_instance_id = "i-0abc123def456..."
ec2_public_ip = "54.123.45.67"
health_alarm_arn = "arn:aws:cloudwatch:us-east-1:..."
next_steps = <<EOT

✅ Deployment Complete!

Next Steps:
1. Check your email...
```

### C. Confirm SNS Subscription

1. **Check Email** - Look for "AWS Notification - Subscription Confirmation"
2. **Click Link** - "Confirm subscription"
3. **See Confirmation** - "Subscription confirmed!"

**Until you confirm, NO alerts will be sent.**

### D. Verify Deployment

**Check EC2 Instance:**
```bash
aws ec2 describe-instances \
  --instance-ids $(terraform output -raw ec2_instance_id)
```

**Check CloudWatch Alarms:**
```bash
aws cloudwatch describe-alarms \
  --alarm-names ec2-high-cpu-alarm ec2-status-check-failed
```

---

## Testing

### Test 1: Trigger CPU Alarm Manually

**Via AWS Console:**
1. Go to CloudWatch → Alarms
2. Select "ec2-high-cpu-alarm"
3. Actions → "Set alarm state to 'In alarm'"
4. Check your email in 1-2 minutes

### Test 2: Generate Real CPU Load

**SSH into EC2 (requires key pair - not included in this project):**
```bash
# Install stress tool
sudo yum install -y stress

# Generate 80% CPU for 5 minutes
stress --cpu 2 --timeout 300
```

**Watch CloudWatch:**
```bash
aws cloudwatch get-metric-statistics \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --dimensions Name=InstanceId,Value=$(terraform output -raw ec2_instance_id) \
  --start-time $(date -u -d '10 minutes ago' +%Y-%m-%dT%H:%M:%S) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
  --period 60 \
  --statistics Average
```

---

## Customization

### Change CPU Threshold

**Option 1: Edit variables.tf**
```hcl
variable "cpu_threshold" {
  default     = 80  # Changed from 70 to 80
}
```

**Option 2: Use terraform.tfvars**
```bash
# Create terraform.tfvars
cat > terraform.tfvars <<EOF
alert_email   = "your-email@example.com"
cpu_threshold = 80
EOF

# Apply changes
terraform apply
```

### Change AWS Region

**Edit variables.tf:**
```hcl
variable "aws_region" {
  default     = "us-west-2"  # Changed from us-east-1
}
```

**Also update AMI** (AMIs are region-specific):
```hcl
variable "ec2_ami" {
  # Find AMI: aws ec2 describe-images --owners amazon \
  #   --filters "Name=name,Values=amzn2-ami-hvm-*-x86_64-gp2" \
  #   --query 'Images[0].ImageId' --output text
  default     = "ami-0abcdef1234567890"
}
```

---

## Troubleshooting

### Issue: "No such file or directory"

**Problem:** Running commands from wrong directory

**Solution:**
```bash
cd aws_monitoring_observability
pwd  # Should end with /aws_monitoring_observability
```

### Issue: "Error: Duplicate resource"

**Problem:** Old broken main.tf still present

**Solution:**
```bash
# This script fixed it! Just re-apply:
terraform init -upgrade
terraform apply
```

### Issue: "Not receiving email alerts"

**Checklist:**
- [ ] Confirmed SNS subscription via email link?
- [ ] Checked spam folder?
- [ ] Alarm actually in "ALARM" state?
- [ ] Correct email in variables.tf?

**Verify subscription:**
```bash
aws sns list-subscriptions-by-topic \
  --topic-arn $(terraform output -raw sns_topic_arn)
```

Should show `"SubscriptionArn": "arn:aws:sns:..."` (not "PendingConfirmation")

### Issue: "AccessDenied" errors

**Problem:** AWS credentials not configured or insufficient permissions

**Solution:**
```bash
# Configure AWS CLI
aws configure

# Test credentials
aws sts get-caller-identity
```

**Required IAM permissions:**
- EC2:RunInstances, DescribeInstances
- CloudWatch:PutMetricAlarm, DescribeAlarms
- SNS:CreateTopic, Subscribe

---

## Cleanup

### Remove All Resources

```bash
terraform destroy
```

Type `yes` when prompted.

**This will delete:**
- EC2 instance
- CloudWatch alarms (2)
- SNS topic
- SNS subscription

**This will NOT delete:**
- Terraform state files (manual deletion required)
- SNS subscription confirmation emails

### Complete Cleanup

```bash
# Remove Terraform state
rm -rf .terraform/
rm terraform.tfstate*
rm .terraform.lock.hcl

# Remove custom config
rm terraform.tfvars
```

---

## What Gets Deployed

| Resource Type | Name | Purpose |
|--------------|------|---------|
| EC2 Instance | monitoring-demo | Test instance for CPU monitoring |
| SNS Topic | cloudwatch-cpu-alerts | Alert delivery mechanism |
| SNS Subscription | Email | Sends alerts to your inbox |
| CloudWatch Alarm | ec2-high-cpu-alarm | Monitors CPU > 70% |
| CloudWatch Alarm | ec2-status-check-failed | Monitors instance health |

**Total Resources:** 5

---

## Cost Monitoring

### Check Current Costs

```bash
# Get month-to-date EC2 costs
aws ce get-cost-and-usage \
  --time-period Start=2025-11-01,End=2025-11-30 \
  --granularity MONTHLY \
  --metrics BlendedCost \
  --filter file://filter.json

# filter.json:
{
  "Dimensions": {
    "Key": "SERVICE",
    "Values": ["Amazon Elastic Compute Cloud - Compute"]
  }
}
```

### Set Cost Alert (Future Enhancement)

Will be added in next iteration to alert when AWS costs exceed $10/month.

---

## Next Steps

After successfully deploying this project:

1. **Add CloudWatch Dashboard** - Visualize metrics in real-time
2. **Build Similar Project** - RDS monitoring or Lambda observability
3. **Study for AWS Cert** - Solutions Architect Associate
4. **Update LinkedIn** - Add project to portfolio

---

**Questions?** Open an issue on GitHub: https://github.com/charles-bucher/aws_monitoring_observability/issues
