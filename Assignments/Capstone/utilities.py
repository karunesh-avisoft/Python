from datetime import date
import logging
import re

# display utility functions
def display_data(data, header):
    print("\n"+"="*33, f"{header}", "="*33)
    print(f"{'ID':<6} {'Name':<25} {'Category':<15} {'Quantity':<10} {'Price':<10} {'Last Restock':<12}")
    print("-"*84)
    for pid, details in data.items():
        print(f"{pid:<6} {details['name']:<25} {details['category']:<15} {details['quantity']:<10} {details['price']:<10} {details['last_restock']:<12}")
    print("="*84)

# VALIDATORS

# name validator
def validate_name_input():
    while True:
        name=input("Enter product name: ").strip()
        pattern = r'^[A-Za-z0-9\(\)]+$'  # allows letters, numbers, spaces, and some special characters
        if re.match(pattern, name) and not name.isdigit() and name!='':
            return name
        else:
            logging.warning("Product name is invalid. Please enter a valid name string.")

# category validator
def validate_category_input():
    while True:
        category=input("Enter product category: ").strip()
        if not category.isdigit() and category!='':
            return category
        else:
            logging.warning("Product category cannot be empty or numeric. Please enter a valid category.")

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
            if price>0:
                return price
            else:
                logging.warning("Price cannot be negative. Please enter a valid price.")
        except ValueError:
            logging.warning("Invalid price format. Please enter a numeric value.") 

# date validator
def validate_date_input():
    while True:
        last_restock=input("Enter last restock date (YYYY-MM-DD): ").strip()
        pattern="%Y-%m-%d"
        if last_restock=='':
            return date.today().isoformat()
        elif re.match(r'^\d{4}-\d{2}-\d{2}$', last_restock):
            return last_restock
        else:
            logging.warning("Invalid date format. Please enter date in YYYY-MM-DD format or leave blank for today.")
 
# product data validator
def validate_product_data():
    data = {}
    try:
        name = validate_name_input()
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
    

