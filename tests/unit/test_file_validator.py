import pytest
from .. import functions as functions
import os
from pathlib import Path
import json
import logging
import subprocess
import boto3
import botocore
import botostubs

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def test_file_validator_should_pass(
        json_path='/Users/stemusta/Desktop/Conclaves/POC/rosetta/functions/file_validator/pass_sampleJSON.json'):
    with open(json_path) as json_file:
        payload = json.load(json_file)
    result = functions.file_validator.lambda_handler(payload, None)
    print(result)
    assert result['valid'] == True
    assert result['file_size'] < (2 * 1024 * 1024 * 1024)
    file_name = result['file_name']
    assert str(file_name).split('.')[-1] in ['mp3', 'mp4', 'ogg', 'flac', 'webm', 'amr', 'wav']

    """ result json should be 
    response = {
        "file_size": file_size,
        "file_name": file_name,
        "uuid": uuid,
        "timestamp": timestamp,
        "valid": True
    }
    """


"""acceptable_file_types = ['mp3', 'mp4', 'ogg', 'flac', 'webm', 'amr', 'wav']"""
testdata = [
    ('my-most-awesome-file.mp3', 'mena-conclaves-src'),
    ('my-test-mp4.mp4', 'mena-conclaves-src'),
    ('my-test-ogg.ogg', 'mena-conclaves-src'),
    ('my-test-flac.flac', 'mena-conclaves-src'),
    ('my-test-webm.webm', 'mena-conclaves-src'),
    ('my-test-amr.amr', 'mena-conclaves-src'),
    ('my-test-wav.wav', 'mena-conclaves-src'),
    ('my-test-xyz.xyz', 'mena-conclaves-src'),
]


@pytest.mark.parametrize("key, bucket", testdata)
def test_file_validator_generated_event_should_pass(key, bucket):
    generate_event_process = subprocess.run(
        ['sam', 'local', 'generate-event', 's3', 'put', '--bucket','{}'.format(bucket), '--key', '{}'.format(key)],
        capture_output=True)

    # generated_payload = json.loads(generate_event_process.stdout)
    generated_payload = generate_event_process.stdout

    # Create Lambda SDK client to connect to appropriate Lambda endpoint
    client = boto3.client('lambda', endpoint_url="http://127.0.0.1:3001",
                          use_ssl=False,
                          verify=False,
                          region_name="eu-west-1",
                          config=botocore.client.Config(
                              signature_version=botocore.UNSIGNED,
                              read_timeout=1,
                              retries={'max_attempts': 0},
                          ))  # type: botostubs.Lambda

    response = client.invoke(FunctionName="FileValidator", Payload=generated_payload)

    val=json.load(response['Payload'])
    # assert that the response is both valid, the size is less than 2GB, the file extension is acceptable
    assert val['valid'] == True
    assert val['file_size'] < (2 * 1024**3)
    assert str(val['file_name']).split('.')[-1] in ['mp3', 'mp4', 'ogg', 'flac', 'webm', 'amr', 'wav']

# TODO: assert for "Unhandled exceptions" in respons - .xyz file example
# TODO: parametrize with expected values so that specific parameters can fail automatically
# TODO: Jupyter notebook for the blog post on how to unit test - for subprocess, reference:  https://linuxhint.com/execute_shell_python_subprocess_run_method/

# result = functions.file_validator.lambda_handler(payload, None)
# assert result['valid'] == True
# assert result['file_size'] < (2 * 1024 * 1024 * 1024)
# file_name = result['file_name']
# assert str(file_name).split('.')[-1] in ['mp3', 'mp4', 'ogg', 'flac', 'webm', 'amr', 'wav']


def test_file_validator_should_fail_filetype(
        json_path='/Users/stemusta/Desktop/Conclaves/POC/rosetta/functions/file_validator/fail_incorrectfiletype_sampleJSON.json'):
    with open(json_path) as json_file:
        payload = json.load(json_file)
    try:
        result = functions.file_validator.lambda_handler(payload, None)
    except functions.file_validator.FileTypeIncorrect as fti:
        logger.exception(fti.message)


def test_file_validator_should_fail_filesize(
        json_path='/Users/stemusta/Desktop/Conclaves/POC/rosetta/functions/file_validator/fail_filetoobig_sampleJSON.json'):
    with open(json_path) as json_file:
        payload = json.load(json_file)
    try:
        result = functions.file_validator.lambda_handler(payload, None)
    except functions.file_validator.FileTooLarge as ftl:
        logger.exception(ftl.message)
