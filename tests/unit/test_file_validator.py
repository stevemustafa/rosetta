import pytest
from .. import functions as functions
import os
import json


def test_file_validator():
    context =''
    sample_payload = 'functions/file_validator/sampleJSON'
    payload_path = os.path.abspath( os.path.join(os.path.curdir,sample_payload))
    # print("path == {}".format(payload_path))
    with open(payload_path, 'r') as f:
        payload = json.load(f)
    result = functions.file_validator.lambda_handler(context, payload)
    print(result)
