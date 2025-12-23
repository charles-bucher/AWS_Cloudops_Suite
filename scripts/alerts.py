import boto3


def send_alert(message):
    sns = boto3.client("sns")
    topic_arn = "arn:aws:sns:us-east-1:123456789012:CloudOpsAlerts"
    sns.publish(TopicArn=topic_arn, Message=message)
    print("Alert sent:", message)


if __name__ == "__main__":
    send_alert("Test alert from CloudOps Suite")
