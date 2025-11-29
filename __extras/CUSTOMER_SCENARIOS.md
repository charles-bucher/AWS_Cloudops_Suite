# Customer-Facing Troubleshooting Scenarios

## Scenario 1: Failed RDS Connection

**Customer Issue:**
"My application can't connect to my RDS MySQL database. Getting timeout errors."

**Diagnosis Process:**
1. Verified RDS instance status in AWS Console (Running ✅)
2. Checked security group inbound rules:
   ```bash
   aws ec2 describe-security-groups --group-ids sg-xxxxx
   ```
   - Found: Only port 3306 from 10.0.0.0/8 allowed
   - Customer's EC2 instance in different VPC (172.16.0.0/16)

3. Tested connection from EC2:
   ```bash
   telnet my-rds-instance.xxxxx.us-east-1.rds.amazonaws.com 3306
   # Result: Connection timed out
   ```

4. Verified subnet routing and network ACLs - all correct

**Root Cause:**
Security group rule too restrictive - didn't include customer's application subnet range.

**Resolution:**
```bash
aws ec2 authorize-security-group-ingress \
  --group-id sg-xxxxx \
  --protocol tcp \
  --port 3306 \
  --cidr 172.16.0.0/16
```

**Verification:**
```bash
mysql -h my-rds-instance.xxxxx.us-east-1.rds.amazonaws.com -u admin -p
# Successfully connected ✅
```

**Customer Impact:**
- Time to Resolution: 15 minutes
- Application downtime eliminated
- Documented security group best practices for customer

---

## Scenario 2: S3 Bucket Permission Denied

**Customer Issue:**
"Getting 'Access Denied' error when trying to upload files to S3 bucket from Lambda function."

**Diagnosis Process:**
1. Reviewed error from CloudWatch Logs:
   ```
   [ERROR] botocore.exceptions.ClientError: An error occurred (AccessDenied) 
   when calling the PutObject operation: Access Denied
   ```

2. Checked Lambda execution role:
   ```bash
   aws iam get-role --role-name MyLambdaExecutionRole
   aws iam list-attached-role-policies --role-name MyLambdaExecutionRole
   ```
   - Found: Only `AWSLambdaBasicExecutionRole` attached (CloudWatch Logs only)

3. Checked S3 bucket policy:
   ```bash
   aws s3api get-bucket-policy --bucket customer-uploads-bucket
   ```
   - Bucket policy looked correct, but Lambda role missing S3 permissions

4. Verified Lambda trying to write to correct bucket:
   ```python
   # From Lambda code review
   s3.put_object(Bucket='customer-uploads-bucket', Key='file.txt', Body=data)
   ```

**Root Cause:**
Lambda execution role lacked S3 write permissions.

**Resolution:**
Created and attached custom policy:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:PutObjectAcl"
      ],
      "Resource": "arn:aws:s3:::customer-uploads-bucket/*"
    }
  ]
}
```

```bash
aws iam put-role-policy \
  --role-name MyLambdaExecutionRole \
  --policy-name S3WriteAccess \
  --policy-document file://s3-write-policy.json
```

**Verification:**
Triggered Lambda function manually - file uploaded successfully ✅

**Customer Impact:**
- Time to Resolution: 12 minutes
- Upload functionality restored
- Followed least-privilege principle (only PutObject, not full S3 access)

---

## Scenario 3: IAM Role Assumption Failure

**Customer Issue:**
"EC2 instance can't assume IAM role to access DynamoDB. Getting 'not authorized to perform sts:AssumeRole' error."

**Diagnosis Process:**
1. Reviewed application error:
   ```
   botocore.exceptions.ClientError: An error occurred (AccessDenied) 
   when calling the AssumeRole operation: User: arn:aws:sts::123456789:assumed-role/EC2-Base-Role/i-xxxxx 
   is not authorized to perform: sts:AssumeRole on resource: arn:aws:iam::123456789:role/DynamoDB-Access-Role
   ```

2. Checked EC2 instance profile:
   ```bash
   aws ec2 describe-instances --instance-ids i-xxxxx --query 'Reservations[0].Instances[0].IamInstanceProfile'
   ```
   - Instance profile attached: `EC2-Base-Role` ✅

3. Examined trust relationship on target role:
   ```bash
   aws iam get-role --role-name DynamoDB-Access-Role --query 'Role.AssumeRolePolicyDocument'
   ```
   - Trust policy found:
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "Service": "lambda.amazonaws.com"
         },
         "Action": "sts:AssumeRole"
       }
     ]
   }
   ```
   - **Problem:** Trust policy only allows Lambda, not EC2 instance role

4. Checked if EC2-Base-Role has AssumeRole permission:
   ```bash
   aws iam list-role-policies --role-name EC2-Base-Role
   aws iam get-role-policy --role-name EC2-Base-Role --policy-name AssumeRolePolicy
   ```
   - Found: No explicit AssumeRole permission (but this is secondary issue)

**Root Cause:**
DynamoDB-Access-Role trust policy didn't include EC2-Base-Role as trusted principal.

**Resolution:**
Updated trust relationship on DynamoDB-Access-Role:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    },
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789:role/EC2-Base-Role"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

```bash
aws iam update-assume-role-policy \
  --role-name DynamoDB-Access-Role \
  --policy-document file://updated-trust-policy.json
```

Also added AssumeRole permission to EC2-Base-Role:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Resource": "arn:aws:iam::123456789:role/DynamoDB-Access-Role"
    }
  ]
}
```

**Verification:**
Tested from EC2 instance:
```bash
aws sts assume-role \
  --role-arn arn:aws:iam::123456789:role/DynamoDB-Access-Role \
  --role-session-name test-session
# Successfully returned temporary credentials ✅
```

**Customer Impact:**
- Time to Resolution: 18 minutes
- Application can now access DynamoDB tables
- Documented IAM role chaining best practices
- Recommended using AWS Systems Manager Session Manager for future debugging

---

## Skills Demonstrated

✅ **Cross-service troubleshooting** (RDS, S3, IAM, EC2, Lambda)  
✅ **AWS CLI proficiency** for diagnosis and resolution  
✅ **Security best practices** (least privilege, trust relationships)  
✅ **Log analysis** (CloudWatch Logs)  
✅ **Customer communication** (clear root cause identification)  
✅ **Documentation** (reproducible solutions)  

## Common Troubleshooting Patterns

### Network Connectivity Issues
1. Check security groups (inbound/outbound rules)
2. Verify network ACLs
3. Confirm route tables
4. Test with telnet/nc
5. Check VPC peering/transit gateway if cross-VPC

### Permission Denied Errors
1. Identify the principal (user/role/service)
2. Check identity-based policies
3. Check resource-based policies (S3 bucket policy, etc.)
4. Verify trust relationships for role assumption
5. Look for explicit Deny statements (they override Allow)

### Service-Specific Checks
- **RDS:** Instance status, parameter groups, subnet groups, security groups
- **S3:** Bucket policies, ACLs, block public access settings, object ownership
- **IAM:** Policy evaluation logic, service control policies (SCPs), permission boundaries
- **Lambda:** Execution role, timeout settings, VPC configuration (if applicable)

---

## How to Use These Scenarios

**For Interviews:**
Walk through your diagnostic process step-by-step. Show you can:
- Identify symptoms
- Form hypotheses
- Test systematically
- Verify solutions

**For GitHub:**
Demonstrate real-world problem-solving with actual AWS CLI commands and clear documentation.

**For Learning:**
Practice each scenario in your own AWS account to build muscle memory.