import boto3

def monitor_ec2():
    cloudwatch = boto3.client('cloudwatch')
    metrics = cloudwatch.list_metrics(Namespace='AWS/EC2')
    print("Collected EC2 metrics:", metrics)

if __name__ == "__main__":
    monitor_ec2()
