from datetime import datetime
from random import randint
from uuid import uuid4
import boto3
import json
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)

'''
Currently, the validator does nothing, but the proposal is to check for all of:
    *   Size of the file < 2GB
    *   File is the accepted types (TBD)
'''
def lambda_handler(event, context):

    # log the event and context
    # logger.info(event)
    # logger.info(context)

    acceptable_file_types = ['mp3', 'ogg', 'flacc']

    # Get the uploaded file name and ARN
    payload = json.load(event)
    file_size = event['Records'][0]['s3']['object']['size']  # in S3, sizes are in bytes, must convert to something human readable (divide by 1024 for kB)
    file_name = event['Records'][0]['s3']['object']['key']
    uuid = str(uuid4())  # Unique ID for the transaction
    timestamp = datetime.now().isoformat()  # Timestamp of the when the transaction was completed

    response = {
        "file_size": file_size,
        "file_name": file_name,
        "uuid": uuid,
        "timestamp": timestamp
    }
    logger.info(response)

    return response
