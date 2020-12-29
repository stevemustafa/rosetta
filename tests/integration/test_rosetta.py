import pytest
import os
import subprocess


''' 
The objective of these tests is to automate the running of the end to end simulation of a file being uploaded to S3 
raising the event which then starts the entire process
The test tests both a success criterion as well as the fail criteria
'''

def test_s3_event_should_pass() :
    """
    Sample subprocess code
    ***********************
    import subprocess
    process = subprocess.Popen(['echo', 'More output'],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    stdout, stderr
    Returns
    -------

    """
    pass