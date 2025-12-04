from datetime import date
import logging
import re

# display utility functions
def display_data(data, header):
    print("\n"+"="*35, f"{header}", "="*35)
    print(f"{'ITEM_ID':<10} {'ITEM_NAME':<25} {'CATEGORY':<15} {'QUANTITY':<10} {'PRICE':<10} {'LAST_RESTOCK':<12}")
    print("-"*88)
    for pid, details in data.items():
        print(f"{pid:<10} {details['name']:<25} {details['category']:<15} {details['quantity']:<10} {details['price']:<10} {details['last_restock']:<12}")
    print("="*88)
    
# VALIDATORS
# search input validator
def validate_search_input():
    while True:
        search_term = input("Enter product name or category to search: ").strip()
        if search_term != '' and not search_term.isdigit():
            return search_term
        else:
            logging.warning("Search term cannot be empty or numeric. Please enter a valid name or category.")

# product ID validator
def validate_product_id():
    while True:
        product_id = input("Enter product ID (eg. 1): ").strip()
        try:
            product_id = int(product_id)
            if product_id in inventory_data:
                return product_id
            else:
                logging.warning(f"Product ID {product_id} not found in inventory. Please enter a valid product ID.") 
        except ValueError:
            logging.warning("Invalid product ID format. Please enter a numeric value.")

# quantity change validator
def validate_qty_change():
    while True:
        qty_change = input("Enter quantity change (positive to add, negative to remove): ").strip()
        try:
            qty_change = int(qty_change)
            if qty_change == 0:
                raise ValueError("Quantity change cannot be zero.")
            return qty_change
        except ValueError:
            logging.warning("Invalid quantity format. Please enter an integer value.")

# name validator
def validate_name_input():
    while True:
        name=input("Enter product name: ").strip()
        pattern = r'^[A-Za-z0-9\s\(\)]+$'  # allows letters, numbers, spaces, and some special characters
        if re.match(pattern, name) and not name.isdigit() and name!='':
            return name
        else:
            logging.warning("Product name is invalid. Please enter a valid name string.")

# category validator
def validate_category_input():
    while True:
        category=input("Enter product category: ").strip()
        pattern = r'^[A-Za-z0-9\s\(\)]+$'  # allows letters, numbers, spaces, and some special characters
        if re.match(pattern, category) and not category.isdigit() and category !='':
            return category
        else:
            logging.warning("Product category is invalid. Please enter a valid category string.")

# quantity validator
def validate_quantity_input():
    while True:
        qty_input=input("Enter product quantity: ").strip()
        try:
            qty_input=int(qty_input)
            if int(qty_input)>=0:
                return int(qty_input)
            else:
                logging.warning("Quantity cannot be negative. Please enter a non-negative integer.")
        except ValueError:
            logging.warning("Invalid quantity. Please enter an integer value.")

# price validator
def validate_price_input():
    while True:
        price_input=input("Enter product price: ").strip()
        try:
            price=float(price_input)
            if price> 0:
                return price
            else:
                logging.warning("Price cannot be negative or zero. Please enter a valid price.")
        except ValueError:
            logging.warning("Invalid price format. Please enter a numeric value.") 

# date validator
def validate_date_input():
    while True:
        last_restock=input("Enter last restock date or leave blank for today (YYYY-MM-DD): ").strip()
        pattern="%Y-%m-%d"
        if last_restock=='':
            return date.today().isoformat()
        elif re.match(r'^\d{4}-\d{2}-\d{2}$', last_restock):
            return last_restock
        else:
            logging.warning("Invalid date format. Please enter date in YYYY-MM-DD format or leave blank for today.")
 
# product data validator
def validate_product_data(inventory_data):
    data = {}
    try:
        name = validate_name_input()
        for values in inventory_data.values():
            # check for duplicate product names
            if name.lower() == values['name'].lower():
                logging.warning("Product with this name already exists in inventory. Use update stock option instead.")
        category = validate_category_input()
        quantity= validate_quantity_input()
        price= validate_price_input()
        last_restock = validate_date_input()
        data['name'] = name
        data['category'] = category
        data['quantity'] = quantity
        data['price'] = price
        data['last_restock'] = last_restock
        return data
    except Exception as e:
        logging.error(e)
        return data
    

