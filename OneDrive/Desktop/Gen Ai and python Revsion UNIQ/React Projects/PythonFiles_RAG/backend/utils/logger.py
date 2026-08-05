"""
utils/logger.py

Application Logger
------------------
Centralized logging configuration for the
Resume AI Screening Assistant.
"""

import os
import logging
from logging.handlers import RotatingFileHandler


# ==========================================================
# Create Logs Directory
# ==========================================================

LOG_DIRECTORY = "logs"

os.makedirs(LOG_DIRECTORY, exist_ok=True)


# ==========================================================
# Log File
# ==========================================================

LOG_FILE = os.path.join(LOG_DIRECTORY, "resume_ai.log")


# ==========================================================
# Logger Configuration
# ==========================================================

logger = logging.getLogger("ResumeAIScreening")

logger.setLevel(logging.INFO)


# ==========================================================
# Formatter
# ==========================================================

formatter = logging.Formatter(

    "%(asctime)s | %(levelname)s | %(filename)s | %(message)s"

)


# ==========================================================
# File Handler
# ==========================================================

file_handler = RotatingFileHandler(

    LOG_FILE,

    maxBytes=5 * 1024 * 1024,

    backupCount=5

)

file_handler.setFormatter(formatter)


# ==========================================================
# Console Handler
# ==========================================================

console_handler = logging.StreamHandler()

console_handler.setFormatter(formatter)


# ==========================================================
# Prevent Duplicate Logs
# ==========================================================

if not logger.handlers:

    logger.addHandler(file_handler)

    logger.addHandler(console_handler)


# ==========================================================
# Helper Functions
# ==========================================================

def log_info(message):

    logger.info(message)


def log_warning(message):

    logger.warning(message)


def log_error(message):

    logger.error(message)


def log_debug(message):

    logger.debug(message)