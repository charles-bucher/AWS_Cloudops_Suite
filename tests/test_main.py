#!/usr/bin/env python3
"""
scripts/test-main.py

Quick test script to validate CloudOps GuardDuty Automation setup.
Checks:
- S3 bucket accessibility
- GuardDuty detector existence
"""

import boto3
import os
import logging
from botocore.exceptions import ClientError

# ===== Configuration =====
BUCKET_NAME = os.environ.get("FINDINGS_BUCKET", "guardduty-findings-charlesb")
REGION = os.environ.get("AWS_REGION", "us-east-1")

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# AWS clients
s3 = boto3.client("s3", region_name=REGION)
guardduty = boto3.client("guardduty", region_name=REGION)

def test_s3_bucket():
    try:
        response = s3.list_objects_v2(Bucket=BUCKET_NAME, MaxKeys=1)
        logging.info(f"S3 bucket '{BUCKET_NAME}' is accessible. Contents (max 1): {response.get('Contents', [])}")
    except ClientError as e:
        logging.error(f"Failed to access S3 bucket '{BUCKET_NAME}': {e}")

def test_guardduty_detector():
    try:
        detectors = guardduty.list_detectors()["DetectorIds"]
        if detectors:
            logging.info(f"GuardDuty detector exists in {REGION}: {detectors[0]}")
        else:
            logging.warning(f"No GuardDuty detector found in {REGION}. Consider running guardduty-enable.py")
    except ClientError as e:
        logging.error(f"Failed to list GuardDuty detectors in {REGION}: {e}")

def main():
    logging.info("Starting CloudOps GuardDuty Automation test...")
    test_s3_bucket()
    test_guardduty_detector()
    logging.info("Test complete.")

if __name__ == "__main__":
    main()
