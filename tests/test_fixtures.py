import pytest
import subprocess

@pytest.fixture(autouse=True, scope="session")
def setup():
    generate_event_process = subprocess.run(['sam', 'local', 'start-lambda'])