import pytest
from .. import functions as functions
import os
from pathlib import Path
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def test_file_validator_should_pass(json_path='/Users/stemusta/Desktop/Conclaves/POC/rosetta/functions/file_validator/pass_sampleJSON.json'):
    context =''
    # sample_payload = 'functions/file_validator/sampleJSON.json'
    #json_path = '/Users/stemusta/Desktop/Conclaves/POC/rosetta/functions/file_validator/pass_sampleJSON.json'


    # payload_path = os.path.abspath( os.path.join(os.path.curdir,sample_payload))
    # print("path == {}".format(payload_path))
    with open(json_path) as json_file:
        payload = json.load(json_file)
    result = functions.file_validator.lambda_handler(payload, context)
    print(result)

def test_file_validator_should_fail_filetype(json_path='/Users/stemusta/Desktop/Conclaves/POC/rosetta/functions/file_validator/fail_incorrectfiletype_sampleJSON.json'):
    context =''
    # sample_payload = 'functions/file_validator/sampleJSON.json'
    #json_path = '/Users/stemusta/Desktop/Conclaves/POC/rosetta/functions/file_validator/pass_sampleJSON.json'

    # payload_path = os.path.abspath( os.path.join(os.path.curdir,sample_payload))
    # print("path == {}".format(payload_path))
    with open(json_path) as json_file:
        payload = json.load(json_file)
    try:
        result = functions.file_validator.lambda_handler(payload, context)
    except functions.file_validator.FileTypeIncorrect as fti:
        # logger.exception('caught excepton: Check the submitted filetype or size')
        logger.exception(fti.message)

def test_file_validator_should_fail_filesize(json_path='/Users/stemusta/Desktop/Conclaves/POC/rosetta/functions/file_validator/fail_filetoobig_sampleJSON.json'):
    context =''
    # sample_payload = 'functions/file_validator/sampleJSON.json'
    #json_path = '/Users/stemusta/Desktop/Conclaves/POC/rosetta/functions/file_validator/pass_sampleJSON.json'

    # payload_path = os.path.abspath( os.path.join(os.path.curdir,sample_payload))
    # print("path == {}".format(payload_path))
    with open(json_path) as json_file:
        payload = json.load(json_file)
    try:
        result = functions.file_validator.lambda_handler(payload, context)
    except functions.file_validator.FileTooLarge as ftl:
        # logger.exception('caught excepton: Check the submitted filetype or size')
        logger.exception(ftl.message)

