import logging.config
import os
from datetime import datetime

def setup_logging(config_dir, log_dir):
    """Load logging config"""
    log_config = {'dev': "logging.dev.ini"}
    config = log_config.get(os.environ['ENV'], "logging.dev.ini")
    config_path = "/".join([config_dir, config])

    timestamp = datetime.now().strftime("%Y%m%d-%H:%M:%S")

    logging.config.fileConfig(
        config_path,
        disable_existing_loggers=False,
        defaults={'logfilename': f'{log_dir}/{timestamp}.log'}
    )