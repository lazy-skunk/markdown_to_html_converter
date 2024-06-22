import os
import pytest
from src.logger import Logger

@pytest.fixture(scope="function")
def setup_and_cleanup_log_file():
    log_file = "test.log"

    yield log_file
    
    if os.path.exists(log_file):
        os.remove(log_file)

def test_singleton_logger(setup_and_cleanup_log_file):
    log_file = setup_and_cleanup_log_file
    logger1 = Logger(log_file=log_file).get_logger()
    logger2 = Logger(log_file=log_file).get_logger()

    assert logger1 is logger2, "Logger instances should be the same"
