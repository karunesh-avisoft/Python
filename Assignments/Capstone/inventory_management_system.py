from pathlib import Path
from dotenv import load_dotenv
import os
import json
from logger import logging

# load variables from .env
load_dotenv()

# directory and file paths
directory = Path.cwd() / os.getenv('PROJECT_DIR')
inventory = directory / os.getenv('INVENTORY_FILE')
transactions = directory / os.getenv('LOG_FILE')
backup = directory / os.getenv('BACKUP_FILE')

# Ensure the directory exists
directory.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename = transactions,
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

# FILE HANDLING
def load_data():
    try:
        with open(inventory, 'r') as f:
            json_data = json.load(f)
        logging.info("Inventory data loaded successfully.")
        return json_data
    except FileNotFoundError:
        logging.error(f"The file '{inventory}' was not found.")
        return {}
    except json.JSONDecodeError as e:
        logging.error(e)
    except Exception as e:
        logging.error(e)

def save_data(inventory_data={}):
    try:
        with open(inventory, 'w') as f:
            json.dump(inventory_data, f, indent=4)
        logging.info("Inventory data saved successfully.")
    except Exception as e:
        logging.error(e)

# BACKUP HANDLING
# def backup_data():
#     try:
#         with open(inventory, 'r') as f:
#             data = json.load(f)
#         with open(backup, 'w') as f:
#             json.dump(data, f, indent=4)
#         logging.info("Backup created successfully.")
#     except Exception as e:
#         logging.error(e)

# RESTORE HANDLING
# def restore_data(): 
#     try:
#         with open(backup, 'r') as f:
#             data = json.load(f)
#         with open(inventory, 'w') as f:
#             json.dump(data, f, indent=4)
#         logging.info("Data restored from backup successfully.")
#     except Exception as e:
#         logging.error(e)

# TRANSACTION LOG MANAGEMENT
def log_transaction(t_type, product_id, qty_change, previous_qty):
    try:
        log_entry = f"{t_type} | Product ID: {product_id} | Change: {qty_change} | Previous Qty: {previous_qty}\n"
        logging.log(f"{log_entry.strip()}")
    except Exception as e:
        logging.error(e)

def view_transactions():
    try:
        with open(transactions, 'r') as f:
            logs = f.readlines()
        for log in logs:
            print(log.strip())
        logging.info("Transaction log viewed successfully.")   
    except Exception as e:
        logging.error(e)