import os
import pytest

TEST_BUCKET = os.getenv("TEST_BUCKET", "charles-dr-simulation-tfstate")

def test_bucket_name():
    assert TEST_BUCKET is not None
