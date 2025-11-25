from datetime import datetime as dt
class BankAccount:
    # constructor
    def __init__(self, acc_number=0, acc_holder="", balance=0):
        self.__account_number=acc_number
        self.__account_holder_name=acc_holder
        self.__balance=balance
        self.message(f'{dt.now().strftime("%Y-%m-%d %H:%M:%S")} Account opened!')
        self.display_details()
        
    # getters & setters
    # account number
    def get_accNumber(self):
        return self.__account_number
    # account holder
    def get_accHolder(self):
        return self.__account_holder_name
    def set_accHolder(self,newName):
        self.__account_holder_name=newName
    # account balance
    def get_accBalance(self):
        return self.__balance
    def set_accBalance(self,amount):
        self.__balance=amount
        
    # methods
    def display_details(self):
        print('____Account Details____')
        print('Account No.:',self.get_accNumber())
        print('Account Holder:',self.get_accHolder())
        print('Balance:',self.get_accBalance())
        print()
    
    def deposit(self,amount):       # deposit
        if amount<=0:
            self.message('Entered invalid amount!!','INVALID')
        else:
            self.set_accBalance(self.get_accBalance()+amount)
            self.message(f'{dt.now().strftime("%Y-%m-%d %H:%M:%S")} Amount deposited!')
            self.check_balance()
    
    def withdraw(self,amount):      # withdraw
        if amount>self.__balance:
            self.message('Insufficient balance!!')
        else:
            self.set_accBalance(self.get_accBalance()-amount)
            self.message(f'{dt.now().strftime("%Y-%m-%d %H:%M:%S")} Amount withdrawn!')
            self.check_balance()
    
    def check_balance(self):        # check-balance
        print(f'Greetings! {self.__account_holder_name}.')
        print(f'Your current balance is {self.get_accBalance():.2f}')
        print()
    
    def message(self,msg,label='INFO'):     # show message   
        print(f'{label}:{msg}')
        print()
    
# instatiation
ritik=BankAccount(123456789101,'Rtitk Ranjan',1000)
harshit=BankAccount(741852963741,'Harshit Pandey',35000)
karunesh=BankAccount(789456123789,'Karunesh Tiwari',1150)
# deposit
ritik.deposit(-50000)
ritik.deposit(50000)
# withdrawl
harshit.withdraw(2666)
# display
karunesh.display_details()
