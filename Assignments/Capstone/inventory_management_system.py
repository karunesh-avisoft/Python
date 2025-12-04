from datetime import date
from pathlib import Path
import threading
from dotenv import load_dotenv
from logger import logging
import random
import os
import json
from utilities import *
# for scheduling weekly backups
import schedule
import time

# load variables from .env
load_dotenv()

# directory and file paths
directory = Path.cwd() / os.getenv('PROJECT_DIR')
inventory = directory / os.getenv('INVENTORY_FILE')
transactions = directory / os.getenv('LOG_FILE')
backup = directory / os.getenv('BACKUP_FILE')

# Ensure the directory exists
directory.mkdir(parents=True, exist_ok=True)


# DATA PERSISTENCE FUNCTIONS
def load_data():
    try:
        with open(inventory, 'r') as f:
            json_data = json.load(f)
        logging.debug("Inventory data loaded successfully.")
        return json_data
    except FileNotFoundError:
        logging.warning("Inventory file not found. Returning empty inventory.")
        return {}
    except json.JSONDecodeError:
        logging.error("Error decoding inventory JSON data. Returning empty inventory.")
        return {}
    except PermissionError:
        logging.error("Permission denied while accessing inventory file. Returning empty inventory.")
        return {}
    except Exception as e:
        logging.error(e)
        return {}

def save_data(inventory_data={}):
    try:
        with open(inventory, 'w') as f:
            json.dump(inventory_data, f, indent=4)
        backup_data()  # create backup after every save
        logging.debug("Inventory data saved successfully.")
    except FileNotFoundError:
        logging.warning("Inventory file not found. Unable to save data.")
    except json.JSONDecodeError:
        logging.error("Error decoding inventory JSON data. Unable to save data.")
    except PermissionError:
        logging.error("Permission denied while accessing inventory file. Unable to save data.")
    except Exception as e:
        logging.error(e)


# BACKUP & RESTORE HANDLING
def backup_data():
    try:
        with open(inventory, 'r') as f:
            data = json.load(f)
        with open(backup, 'w') as f:
            json.dump(data, f, indent=4)
        logging.debug("Backup created successfully.")
    except Exception as e:
        logging.error(e)

def restore_data(): 
    try:
        with open(backup, 'r') as f:
            data = json.load(f)
        with open(inventory, 'w') as f:
            json.dump(data, f, indent=4)
        logging.info("Data restored from backup successfully.")
    except Exception as e:
        logging.error(e)

# WEEKLY BACKUP SCHEDULER
def weekly_backup():
    print("\n"+"="*30)
    logging.info("Running scheduled weekly backup...")
    backup_data()

# scheduler thread
def run_scheduler():
    schedule.every().monday.at("02:00").do(weekly_backup)
    # schedule.every(5).seconds.do(weekly_backup)  # for testing, runs every 5 seconds       

    while not stop_scheduler.is_set():
        schedule.run_pending()
        time.sleep(1)

# scheduler control functions
stop_scheduler = threading.Event() # <-- stop signal

def start_scheduler():
    global scheduler_thread
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()
    print("Scheduler started.")

def stop_scheduler_thread():
    stop_scheduler.set()       # <-- stop signal
    scheduler_thread.join()    # waits for thread to exit
    print("Scheduler stopped.")


# TRANSACTION LOG MANAGEMENT
def log_transaction(t_type, product_id, qty_change, previous_qty):
    try:
        log_entry = f"{t_type} | Product ID: {product_id} | Change in Quantity(+/-): {qty_change} | Previous Qty: {previous_qty}\n"
        logging.info(f"{log_entry.strip()}")
    except Exception as e:
        logging.error(e)

def view_transactions():
    try:
        with open(transactions, 'r') as f:
            logs = f.readlines()
            if logs:
                print("\n"+"="*30, "TRANSACTION LOGS", "="*30)
                for log in logs: 
                        print(log.strip())
                print("="*78)
                logging.debug("Transaction log viewed successfully.")
            else:
                logging.info("No transactions found in the log.")   
    except Exception as e:
        logging.error(e)

# additional function to clear transaction log
def clear_transactions():
    try:
        open(transactions, 'w').close()
        logging.debug("Transaction log cleared successfully.")
    except Exception as e:
        logging.error(e)
    

# INVENTORY MANAGEMENT FUNCTIONS
def add_new_product():
    # abort adding new
    print("\nAdding new product. To abort, press Ctrl+C.")
    try:
        inv_data = load_data()
        # Get product details
        product_details = validate_product_data(inv_data)

        # Generate unique product ID
        product_id=max([int(pid) for pid in inv_data.keys()], default=100)+1
       
        # Add to inventory 
        inv_data[product_id] = product_details
        save_data(inv_data)
        log_transaction('NEW_ITEM', product_id, product_details['quantity'], 0)
    except KeyboardInterrupt:
        logging.debug("Add new product operation aborted by user.")
        print("\n*** Adding new product aborted by user. ***")
    except Exception as e:
        logging.error(e)
    else:
        another = input(f"\nWant to add another product? (y/n): ").strip().lower()
        while another not in ['y', 'n']:    
            another = input("Invalid input. Please enter 'y' for yes or 'n' for no: ").strip().lower()
        add_new_product() if another == 'y' else None
    
def update_stock():
    print("\nUpdating product stock. To abort, press Ctrl+C.")
    try:
        inv_data = load_data()
        product_id = validate_product_id(inv_data)
        qty_change = validate_qty_change()
        if product_id in inv_data:
            previous_qty = inv_data[product_id]['quantity']
            if inv_data[product_id]['quantity'] + qty_change < 0:
                logging.warning(f"Insufficient stock to remove the specified quantity. Available quantity: {inv_data[product_id]['quantity']}")
                return
            inv_data[product_id]['quantity'] += qty_change   
            inv_data[product_id]['last_restock'] = date.today().isoformat()
            save_data(inv_data)
            log_transaction('STOCK_UPDATE', product_id, qty_change, previous_qty)
        else:
            logging.warning(f"Product ID {product_id} not found in inventory.")
    except KeyboardInterrupt:
        logging.debug("Update product operation aborted by user.")
        print("\n*** Update product operation aborted by user. ***")
    except Exception as e:
        logging.error(e)
    else:
        another = input(f"\nWant to update another product? (y/n): ").strip().lower()
        while another not in ['y', 'n']:    
            another = input("Invalid input. Please enter 'y' for yes or 'n' for no: ").strip().lower()
        update_stock() if another == 'y' else None

def search_product():
    print("\nSearching product. To abort, press Ctrl+C.")
    search_term = validate_search_input()

    try:
        inv_data = load_data()
        results = {}
        for pid, details in inv_data.items():
            if (search_term.lower() in details['name'].lower()) or (search_term.lower() in details['category'].lower()):
                results[pid] = details
        if results:
            logging.info(f"Found {len(results)} matching products.")
            display_data(results, 'SEARCH RESULTS')
        else:
            logging.info("No matching products found.")
    except KeyboardInterrupt:
        logging.debug("Search product operation aborted by user.")
        print("\n*** Search product operation aborted by user. ***")
    except Exception as e:
        logging.error(e)
    else:
        another = input(f"\nWant to search for another product? (y/n): ").strip().lower()
        while another not in ['y', 'n']:    
            another = input("Invalid input. Please enter 'y' for yes or 'n' for no: ").strip().lower()
        search_product() if another == 'y' else None

# additional function to delete a product  
def delete_product():
    print("\nDeleting product. To abort, press Ctrl+C.")
    try:
        inv_data = load_data()
        product_id = validate_product_id()
        if product_id in inv_data:
            change_qty = -inv_data[product_id]['quantity']
            previous_qty = inv_data[product_id]['quantity']
            del inv_data[product_id]
            save_data(inv_data)
            log_transaction('DELETE_ITEM', product_id, change_qty, previous_qty)
        else:
            logging.warning(f"Product ID {product_id} not found in inventory.")
    except KeyboardInterrupt:
        logging.debug("Delete product operation aborted by user.")
        print("\n*** Delete product operation aborted by user. ***")
    except Exception as e:
        logging.error(e)
    else:
        another = input(f"\nWant to delete another product? (y/n): ").strip().lower()
        while another not in ['y', 'n']:    
            another = input("Invalid input. Please enter 'y' for yes or 'n' for no: ").strip().lower()
        delete_product() if another == 'y' else None


# REPORTING FUNCTIONS
def generate_inventory_report():
    inv_data = load_data()
    try:
        total_items = len(inv_data)
        total_value = sum(details['quantity'] * details['price'] for details in inv_data.values())
        low_stock = sum(1 for details in inv_data.values() if details['quantity'] < 10)
        out_of_stock = sum(1 for details in inv_data.values() if details['quantity'] <= 0)

        # lambda to find most stocked item
        most_stocked_item = max(inv_data.items(), key=lambda x: x[1]['quantity']) if inv_data else (None, None)
        # print("Most stocked:", most_stocked_item) --> ('106', {'name': 'Ball Pen Pack (10 pcs)', 'category': 'Stationery', 'quantity': 200, 'price': 75.0, 'last_restock': '2025-02-01'})

        # Display detailed inventory
        print("\n"+"="*30, "INVENTORY REPORT", "="*30)
        print(f"Total Unique Items: {total_items}")
        print(f"Total Inventory Value: INR{total_value:.2f}")
        print(f"Low Stock Items (qty<10): {low_stock}")
        print(f"Out of Stock Items: {out_of_stock}")
        print(f"Most Stocked Category: {most_stocked_item[1]['category'] if most_stocked_item[1] else 'N/A'} (Qty: {most_stocked_item[1]['quantity'] if most_stocked_item[1] else 'N/A'})")
        print("="*78)

        logging.info("Inventory report generated successfully.")
    except Exception as e:
        logging.error(e)

def display_inventory(category=None, stock_status=None):
    try:
        inv_data = load_data()
        # filtered data based on category and stock status
        filtered_data={}
        for pid, details in inv_data.items():
            if category and category.lower() not in inv_data[pid]['category'].lower():
                continue
            if stock_status=='in_stock' and inv_data[pid]['quantity']<=0:
                continue
            if stock_status=='out_of_stock' and inv_data[pid]['quantity']>0:
                continue
            filtered_data[pid]=details
        if filtered_data:
            display_data(filtered_data, 'INVENTORY DATA')
            logging.info("Inventory viewed successfully.")
        else:
            logging.info("No products found matching the specified criteria.")
    except Exception as e:
        logging.error(e)

