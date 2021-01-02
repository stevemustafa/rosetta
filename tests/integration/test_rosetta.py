import pytest
import os
import subprocess


''' 
The objective of these tests is to automate the running of the end to end simulation of a file being uploaded to S3 
raising the event which then starts the entire process
The test tests both a success criterion as well as the fail criteria
'''
@pytest.mark.skip
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
    #pass
    """ 
    The expected command should be:  
    
    sam local generate-event s3 put --bucket mena-conclaves-src --key my-most-awesome-file.mp3 | sam local invoke "FileValidator" --event -
    
    in future iterations, this should trigger the stepfunctions workflow
     
    """
    # sam local generate-event s3 put --bucket mena-conclaves-src --key my-most-awesome-file.mp3
    generate_event_process = subprocess.Popen(['sam','local', 'generate-event', 's3', 'put', '--bucket', 'mena-conclaves-src', '--key', 'my-most-awesome-file.mp3'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    # stdout, stderr = process.communicate()

    file_validator_process = subprocess.Popen(['sam','local', 'invoke', '"FileValidator"','--event ' ])
    generate_event_process.stdout.close()

    output = file_validator_process.communicate()

    for o in output:
        print(o)