#!/usr/bin/env python3
"""
scripts/guardduty-enable.py

Enables AWS GuardDuty for the account in a specified region or all regions.
"""

import boto3
import os
import logging
from botocore.exceptions import ClientError

# ===== Configuration =====
REGIONS = os.environ.get("AWS_REGIONS", "us-east-1").split(",")  # comma-separated list of regions
ADMIN_ACCOUNT_ID = os.environ.get("ADMIN_ACCOUNT_ID")  # optional, for multi-account setup

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def enable_guardduty(region):
    client = boto3.client("guardduty", region_name=region)
    try:
        # Check if GuardDuty is already enabled
        detectors = client.list_detectors()["DetectorIds"]
        if detectors:
            logging.info(f"GuardDuty already enabled in {region} (DetectorId: {detectors[0]})")
            return detectors[0]
        # Create detector
        response = client.create_detector(Enable=True)
        detector_id = response["DetectorId"]
        logging.info(f"GuardDuty enabled in {region} (DetectorId: {detector_id})")
        return detector_id
    except ClientError as e:
        logging.error(f"Failed to enable GuardDuty in {region}: {e}")
        return None

def main():
    for region in REGIONS:
        enable_guardduty(region.strip())

if __name__ == "__main__":
    main()
