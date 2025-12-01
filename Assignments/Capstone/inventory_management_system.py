from pathlib import Path
from dotenv import load_dotenv
import os
import json
import logging

# load variables from .env
load_dotenv()

# directory and file paths
directory = Path.cwd() / os.getenv('PROJECT_DIR')
inventory = os.getenv('INVENTORY_FILE')
transactions = os.getenv('LOG_FILE')
backup = os.getenv('BACKUP_FILE')

# Ensure the directory exists
directory.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename = directory / transactions,
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

# FILE HANDLING
def load_data():
    try:
        with open(inventory, 'r') as f:
            json_data = json.load(f)
        logging.info("Inventory data loaded successfully.")
    except FileNotFoundError:
        logging.error(f"The file '{inventory}' was not found.")
        return {}
    except json.JSONDecodeError as e:
        logging.error(e)
    except Exception as e:
        logging.error(e)