# Main script to execute the project
import logging
import os
from dotenv import find_dotenv, load_dotenv

from utils import setup_logging

# Initial setup find .env file, setup paths for config and logs directory
env_setup = find_dotenv()
load_dotenv()

config_dir = "../config"
log_dir = "../logs"


if __name__ == '__main__':
    pass
    # setup_logging(config_dir, log_dir)
    # Main logger
    # logger = logging.getLogger(__name__)