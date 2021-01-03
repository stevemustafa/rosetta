from datetime import datetime
from random import randint
from uuid import uuid4
import boto3
import json
import logging
from exc


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

    # FLAC, MP3, MP4, Ogg, WebM, AMR, or WAV
    acceptable_file_types = ['mp3', 'mp4', 'ogg', 'flac', 'webm', 'amr', 'wav']

    # Get the uploaded file name and ARN
    s3 = event['Records'][0]['s3']
    file_size = s3['object']['size']  # in S3, sizes are in bytes, must convert to something human readable (divide by 1024 for kB)
    if file_size > (2 * 1024 * 1024 * 1024): # calculated binary 2GB
        raise FileTooLarge(file_size=file_size)
    file_name = s3['object']['key']

    # check file type is one of the accepted variety
    if not file_name.split('.')[-1] in acceptable_file_types:
        custom_error = '\nException : not acceptable file type\n'
        custom_error += 'FileTypeError : ' + file_name.split('.')[-1] + '\n'
        raise FileTypeIncorrect(file_extension=(file_name.split('.')[-1]))

    uuid = str(uuid4())  # Unique ID for the transaction
    timestamp = datetime.now().isoformat()  # Timestamp of the when the transaction was completed

    response = {
        "file_size": file_size,
        "file_name": file_name,
        "uuid": uuid,
        "timestamp": timestamp,
        "valid": True
    }
    # logger.info(response)


    return response
