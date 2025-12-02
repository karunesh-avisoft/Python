from inventory_management_system import *
from utilities import *

def main():
    # start the weekly backup scheduler
    start_scheduler()

    consent = 'y'
    while consent == 'y':
        print("\n" + "="*31)
        print(" INVENTORY MANAGEMENT SYSTEM ")
        print("="*31)
        print("1. View Current Inventory")
        print("2. Add New Product")
        print("3. Update Product Stock")
        print("4. Search Product")
        print("5. Delete Product") 
        print("6. Generate Inventory Report")
        print("7. View Transaction Logs")
        # print("8. Backup Data") auto incremental backup after every save
        print("8. Restore Data")
        print("9. Exit")
        print("="*30) 
        try:
            # get user choice
            choice = input("\nEnter your choice (1-9): ").strip()
            while not choice.isdigit() or int(choice) not in range(1, 10):
                choice = input("Invalid choice. Please enter a number between 1 and 9: ").strip()

            # process user choice
            if choice == '1':
                display_inventory()

            elif choice == '2':
                while True:
                    add_new_product()
                    another = input("\nDo you want to add another product? (y/n): ").strip().lower()
                    while another not in ['y', 'n']:    
                        another = input("Invalid input. Please enter 'y' for yes or 'n' for no: ").strip().lower()
                    if another == 'n':
                        break

            elif choice == '3':
                product_id = input("Enter product ID to update stock: ").strip()
                qty_change = int(input("Enter quantity change (positive to add, negative to remove): ").strip())
                update_stock(product_id, qty_change)

            elif choice == '4':
                search_term = input("Enter product name or category to search: ").strip()
                found_data = search_product(search_term)
                if found_data:
                    display_data(found_data, 'SEARCH RESULTS')

            elif choice == '5':
                product_id = input("Enter product ID to delete: ").strip()
                delete_product(product_id)

            elif choice == '6':
                generate_inventory_report()

            elif choice == '7':
                view_transactions()

            elif choice == '8':
                restore_data()

            elif choice == '9':
                print("*** Exiting the system. Goodbye! ***")
                break

            # get user consent for another operation
            consent = input("\nDo you want to perform another operation? (y/n): ").strip().lower()
            while consent not in ['y', 'n']:
                consent = input("Invalid input. Please enter 'y' for yes or 'n' for no: ").strip().lower()

        # except keyboard and EOF errors to exit gracefully
        except (KeyboardInterrupt, EOFError):
            print("\n*** Exiting the system. Goodbye! ***")
            break
    
    # stop the scheduler thread before exiting
    stop_scheduler_thread()



# run the main function
if __name__ == '__main__':
    main()