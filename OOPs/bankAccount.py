from datetime import datetime

class UserAccount:
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.__pin = pin
        self.__balance = balance
        self.__wrong_attempts = 0
        self.__locked = False
        self.history = []     # store transaction history

    def log(self, action, amount=None):
        """Record every transaction."""
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if amount is None:
            entry = f"{time} - {action}"
        else:
            entry = f"{time} - {action}: ₹{amount}"
        self.history.append(entry)

    def validate_pin(self, pin):
        if self.__locked:
            print("❌ Account is LOCKED!")
            return False

        if pin == self.__pin:
            self.__wrong_attempts = 0
            self.log("PIN verified")
            return True
        
        else:
            self.__wrong_attempts += 1
            print("❌ Incorrect PIN!")

            if self.__wrong_attempts >= 3:
                self.__locked = True
                print("🔒 Account locked due to 3 incorrect attempts!")

            return False

    def get_balance(self):
        self.log("Checked Balance")
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        self.log("Deposited", amount)

    def withdraw(self, amount):
        if amount > self.__balance:
            print("❌ Insufficient funds!")
            self.log("Failed Withdrawal", amount)
        else:
            self.__balance -= amount
            self.log("Withdrawn", amount)


class ATM:
    def __init__(self, accounts):
        # accounts is a dict → {username: UserAccount}
        self.accounts = accounts
        self.current_user = None

    def login(self):
        print("\n==== ATM LOGIN ====")
        username = input("Enter username: ")

        if username not in self.accounts:
            print("❌ User does not exist!")
            return False

        account = self.accounts[username]
        pin = input("Enter PIN: ")

        if account.validate_pin(pin):
            self.current_user = account
            print(f"✔️ Welcome, {account.name}!")
            return True

        return False

    def show_menu(self):
        while True:
            print("""
===== ATM MENU =====
1. Check Balance
2. Deposit
3. Withdraw
4. Transaction History
5. Exit
""")

            choice = input("Select option: ")

            if choice == "1":
                print("Balance: ₹", self.current_user.get_balance())

            elif choice == "2":
                amount = float(input("Enter deposit amount: "))
                self.current_user.deposit(amount)
                print("✔️ Deposit successful.")

            elif choice == "3":
                amount = float(input("Enter withdrawal amount: "))
                self.current_user.withdraw(amount)

            elif choice == "4":
                print("\n==== Transaction History ====")
                if not self.current_user.history:
                    print("No transactions yet.")
                else:
                    for entry in self.current_user.history:
                        print(entry)
                print()

            elif choice == "5":
                print("👋 Thank you for using the ATM!")
                break

            else:
                print("❌ Invalid option")


# -----------------------------
# Example: Multiple Users
# -----------------------------

accounts = {
    "alice": UserAccount("Alice", "1111", 5000),
    "bob": UserAccount("Bob", "2222", 3500),
    "charlie": UserAccount("Charlie", "3333", 1000)
}

atm = ATM(accounts)

if atm.login():
    atm.show_menu()
