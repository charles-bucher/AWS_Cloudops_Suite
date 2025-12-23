import json


def handler(event, context):
    """
    Basic Lambda handler function
    """
    print(f"Received event: {json.dumps(event)}")

    return {
        "statusCode": 200,
        "body": json.dumps(
            {"message": "Lambda function executed successfully", "event": event}
        ),
    }
