from datetime import datetime as dt
class BankAccount:
    # constructor
    def __init__(self, acc_number=0, acc_holder="", balance=0):
        self.__account_number=acc_number
        self.__account_holder_name=acc_holder
        self.__balance=balance
        self.message(f'{self.__account_holder_name}, your account opened successfully!','ACK')
        
    # getters & setters
    def get_accNumber(self):
        return self.__account_number
    def get_accHolder(self):
        return self.__account_holder_name
    def set_accHolder(self,newName):
        self.__account_holder_name=newName
    def get_accBalance(self):
        return self.__balance
    def set_accBalance(self,amount):
        self.__balance=amount
        
    # methods
    def display_details(self):
        print('\n____Account Details____')
        print('Account No.:',self.get_accNumber())
        print('Account Holder:',self.get_accHolder())
        print('Balance:',self.get_accBalance())
        print()
    
    def deposit(self,amount):       # deposit amount
        if amount<=0:
            self.message('Entered invalid amount!!','INVALID')
        else:
            self.set_accBalance(self.get_accBalance()+amount)
            self.message('Amount deposited!','ACK')
            self.check_balance()
    
    def withdraw(self,amount):      # withdraw amount
        if amount>self.__balance:
            self.message('Insufficient balance!!')
        else:
            self.set_accBalance(self.get_accBalance()-amount)
            self.message('Amount withdrawn!','ACK')
            self.check_balance()
    
    def check_balance(self):        # check-balance
        print(f'Greetings! {self.__account_holder_name}.')
        print(f'Your current balance is {self.get_accBalance():.2f}')
        print()
    
    def message(self,msg,label='INFO'):     # show message   
        timestamp=dt.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f'\n{label}:{timestamp} {msg}\n')

accounts={}
    
# instatiation
accounts[123456789101]=BankAccount(123456789101,'Rtitk Ranjan',1000)
accounts[741852963741]=BankAccount(741852963741,'Harshit Pandey',35000)
accounts[789456123789]=BankAccount(789456123789,'Karunesh Tiwari',1150)

# menu driven banking system
proceed='y'
while proceed.lower()=='y':
    print("\n===== BANKING SYSTEM MENU =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Display Account Details")
    print("6. Exit")

    choice = input("Enter your choice: ")

# create account
    if choice == '1':
        # account number
        acc_no = input("Enter account number: ")
        while not acc_no.isdigit() or len(acc_no) not in range(11,17):
            print('INVALID:Enter a valid 15 digit account number!')
            acc_no = input("Enter your account number: ")
        acc_no=int(acc_no)
        # account holder name
        name = input("Enter account holder name: ")
        # balance
        bal = input("Enter initial balance: ")
        while not bal.isdigit() or float(bal)<0:
            print('INVALID:Enter a valid initial balance!')
            bal = input("Enter initial balance: ")
        bal=float(bal)
        # storing details
        accounts[acc_no] = BankAccount(acc_no, name, bal)
# Deposit Amount
    elif choice == '2':
        # input account number
        acc_no = input("Enter account number: ")
        while not acc_no.isdigit() or len(acc_no) not in range(11,17):
            print('INVALID:Enter a valid 15 digit account number!\n')
            acc_no = input("Enter account number: ")
        acc_no=int(acc_no)
        if acc_no in accounts:
            # input deposit amount
            amt = input("Enter deposit amount: ")
            while not amt.isdigit() or float(amt)<0:
                print('Enter a valid deposit amount!\n')
                amt = input("Enter deposit amount: ")
            amt=float(amt)
            accounts[acc_no].deposit(amt)
        else:
            print("NOT_FOUND:Account not found!\n")
# Withdraw Amount
    elif choice == '3':
        # input account number
        acc_no = input("Enter account number: ")
        while not acc_no.isdigit() or len(acc_no) not in range(11,17):
            print('INVALID:Enter a valid 15 digit account number!\n')
            acc_no = input("Enter account number: ")
        acc_no=int(acc_no)
        if acc_no in accounts:
            # input withdrawl amount
            amt = input("Enter withdrawal amount: ")
            while not amt.isdigit() or float(amt)<0:
                print('Invalid withdrawl amount!\n')
                amt = input("Again! Enter withdrawal amount: ")
            amt=float(amt)
            accounts[acc_no].withdraw(amt)
        else:
            print("NOT_FOUND:Account not found!\n")
# Check Balance
    elif choice == '4':
        # input account number
        acc_no = input("Enter account number: ")
        while not acc_no.isdigit() and len(acc_no) not in range(11,17):
            print('INVALID:Enter a valid 15 digit account number!\n')
            acc_no = input("Enter account number: ")
        acc_no=int(acc_no)
        if acc_no in accounts:
            accounts[acc_no].check_balance()
        else:
            print("NOT_FOUND:Account not found!\n")
# Display Details
    elif choice == '5':
        # input account number
        acc_no = input("Enter account number: ")
        while not acc_no.isdigit() and len(acc_no)!=15:
            print('INVALID:Enter a valid 15 digit account number!\n')
            acc_no = input("Enter account number: ")
        acc_no=int(acc_no)
        if acc_no in accounts:
            accounts[acc_no].display_details()
        else:
            print("NOT_FOUND:Account not found!\n")
# Good-bye
    elif choice == '6':
        print("\n***Thank you for using our banking system!***")
        break
    else:
        print("\nInvalid choice! Please try again.")

    proceed=input('Want to see operations?(y/n):')