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

            # Process user choice
            # view inventory
            if choice == '1':
                # how do you want to display? all or filtered
                print("\nView Inventory Options:")
                print("1. View All Items")  
                print("2. Filter by Category")
                print("3. Filter by Stock Status")
                view_choice = input("Enter your view choice (1-3): ").strip()    
                while view_choice not in ['1', '2', '3']:
                    view_choice = input("Invalid choice. Please enter 1, 2, or 3: ").strip()     
                # call display inventory with appropriate filters  
                if view_choice == '1':
                    display_inventory()
                elif view_choice == '2':
                    category = validate_category_input()
                    display_inventory(category=category)
                elif view_choice == '3':
                    stock_status = input("Enter stock status to filter (in/out): ").strip().lower()
                    while stock_status not in ['in', 'out']:
                        stock_status = input("Invalid input. Please enter 'in-stock' or 'out-of-stock': ").strip().lower()
                    display_inventory(stock_status=stock_status)

            # add new product
            elif choice == '2':
                add_new_product() 

            # update product stock
            elif choice == '3':
                update_stock()  

            # search product
            elif choice == '4':
                search_product()

            # delete product
            elif choice == '5':
                delete_product()

            # generate inventory report
            elif choice == '6':
                generate_inventory_report()

            # view transaction logs
            elif choice == '7':
                view_transactions()

            # restore data from backup
            elif choice == '8':
                restore_data()

            # exit the system   
            elif choice == '9':
                print("*** Exiting the system. Goodbye! ***")
                break

            # get user consent for another operation
            consent = input("\nDo you want to perform another operation? (y/n): ").strip().lower()
            while consent not in ['y', 'n']:
                consent = input("Invalid input. Please enter 'y' for yes or 'n' for no: ").strip().lower()
                if consent == 'n':
                    logging.info("Exit after operations completed successfully.")
                    break

        # except keyboard and EOF errors to exit gracefully
        except (KeyboardInterrupt, EOFError):
            print()
            logging.info("User initiated exit.")
            print("\n*** Exiting the system. Goodbye! ***")
            break
            
    # stop the scheduler thread before exiting
    stop_scheduler_thread()



# run the main function
if __name__ == '__main__':
    main()