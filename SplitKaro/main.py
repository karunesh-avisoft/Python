from utilities import *

def main():
    while True:
        print("\n=========== SPLIT YOU BILLS HERE ===========")
        print("""----- ACTION MENU -----
1. Add User
2. View Users
3. Create Group
4. View Groups
5. Add Bill
6. View Balances
7. Settle Balance
8. Exit        """)
        print("="*46)
        choice = input("Enter choice: ").strip()
        
        if choice == "1":
            add_user()
        elif choice == "2":
            view_users()
        elif choice == "3":
            create_group()
        elif choice == "4":
            view_groups()
        elif choice == "5":
            add_bill_to_group()
        elif choice == "6":
            group_id = input("Enter group ID: ").strip()
            calculate_balances(group_id)
        elif choice == "7":
            group_id = input("Enter group ID: ").strip()
            settle_balance(group_id)
        elif choice == "8":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
