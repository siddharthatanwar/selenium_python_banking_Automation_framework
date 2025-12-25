# import logging
# from core.config_reader import ConfigReader
# import os

# def setup_logger():
#     log_config = ConfigReader.get("logging")

#     log_file = log_config["log_file"]
#     os.makedirs(os.path.dirname(log_file), exist_ok=True)

#     logging.basicConfig(
#         level=log_config["level"],
#         format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
#         handlers=[
#             logging.FileHandler(log_file),
#             logging.StreamHandler()
#         ]
#     )

#     return logging.getLogger("AutomationLogger")

import logging
import os
from core.config_reader import ConfigReader

def setup_logger():
    logger = logging.getLogger("AutomationLogger")

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    log_config = ConfigReader.get("logging")
    log_file = log_config["log_file"]

    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logger.setLevel(log_config["level"])

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.propagate = False

    logger.info("==== Automation Logger Initialized ====")

    return logger
