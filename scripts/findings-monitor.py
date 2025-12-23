#!/usr/bin/env python3
"""
scripts/findings-monitor.py

Monitors an S3 bucket for new GuardDuty findings and sends email alerts via AWS SES.
"""

import boto3
import json
import os
import logging
from datetime import datetime, timezone
from botocore.exceptions import ClientError

# ===== Configuration =====
BUCKET_NAME = os.environ.get("FINDINGS_BUCKET", "your-findings-bucket")
ALERT_EMAIL = os.environ.get("ALERT_EMAIL", "alert@example.com")
REGION = os.environ.get("AWS_REGION", "us-east-1")
PREFIX = os.environ.get("FINDINGS_PREFIX", "guardduty-findings/")

# Track last processed timestamp (local file)
LAST_RUN_FILE = ".last_run"

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# AWS clients
s3 = boto3.client("s3", region_name=REGION)
ses = boto3.client("ses", region_name=REGION)


# ===== Functions =====
def get_last_run_time():
    if os.path.exists(LAST_RUN_FILE):
        with open(LAST_RUN_FILE, "r") as f:
            return float(f.read().strip())
    return 0


def save_last_run_time(timestamp):
    with open(LAST_RUN_FILE, "w") as f:
        f.write(str(timestamp))


def list_new_findings():
    last_run = get_last_run_time()
    paginator = s3.get_paginator("list_objects_v2")
    page_iterator = paginator.paginate(Bucket=BUCKET_NAME, Prefix=PREFIX)

    new_files = []
    for page in page_iterator:
        for obj in page.get("Contents", []):
            if obj["LastModified"].timestamp() > last_run:
                new_files.append(obj["Key"])

    return new_files


def read_s3_object(key):
    response = s3.get_object(Bucket=BUCKET_NAME, Key=key)
    return response["Body"].read().decode("utf-8")


def send_alert(subject, body):
    try:
        ses.send_email(
            Source=ALERT_EMAIL,
            Destination={"ToAddresses": [ALERT_EMAIL]},
            Message={"Subject": {"Data": subject}, "Body": {"Text": {"Data": body}}},
        )
        logging.info(f"Alert sent: {subject}")
    except ClientError as e:
        logging.warning(f"SES failed, printing to console: {e}")
        print("----- GUARD DUTY ALERT -----")
        print(subject)
        print(body)
        print("----------------------------")


def process_findings():
    logging.info("Starting GuardDuty findings monitor...")
    new_files = list_new_findings()

    if not new_files:
        logging.info("No new findings detected.")
        return

    for key in new_files:
        logging.info(f"Processing finding: {key}")
        try:
            content = read_s3_object(key)
            data = json.loads(content)
            subject = f"GuardDuty Alert: Severity {data.get('severity', 'Unknown')}"
            body = json.dumps(data, indent=4)
            send_alert(subject, body)
        except Exception as e:
            logging.error(f"Error processing {key}: {e}")


# ===== Main =====
if __name__ == "__main__":
    try:
        process_findings()
    finally:
        # Save last run timestamp
        save_last_run_time(datetime.now(timezone.utc).timestamp())
        logging.info("Finished GuardDuty findings monitor.")
