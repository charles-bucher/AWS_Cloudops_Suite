import boto3

def lambda_handler(event, context):
    print("Lambda triggered with event:", event)
    return {"statusCode": 200, "body": "CloudOps Lambda executed successfully"}
