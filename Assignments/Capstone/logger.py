from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
import os

# load variables from .env
load_dotenv()

# directory and file paths
directory = Path.cwd() / os.getenv('PROJECT_DIR')
transactions = directory / os.getenv('LOG_FILE')

# File handler (rotating)
file_handler = RotatingFileHandler(
    transactions,
    maxBytes=1_000_000,
    backupCount=5
)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))

# Create main logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(console_handler)