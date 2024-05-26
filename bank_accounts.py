class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self, initial_amount, AccountName):
        self.balance = initial_amount
        self.name = AccountName
        print(f"\nAccount '{self.name}' created. \nBalance = ${self.balance:.2f}")
    
    def getBalance(self):
        print(f"\nBalance for account '{self.name}': ${self.balance:.2f}")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposit complete.\nBalance for account '{self.name}': ${self.balance:.2f}")

    def viabletransaction(self, amount):
        if(amount>self.balance):
            raise BalanceException("Sorry, Insufficient Funds")
        else:
            return
    
    def withdraw(self, amount):
        try:
            self.viabletransaction(amount)
            self.balance -= amount
            print("\nWithdraw Completed")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
    
    def transfer(self,amount,name):
        try:
            print("\n**********\n\nBeginning Transfer..🚀")
            self.viabletransaction(amount)
            self.withdraw(amount)
            name.deposit(amount)
            print("\nTransfer complete ✅\n\n**********")
        except BalanceException as error:
            print(f"\n Transfer interrupted❌: {error}")

class   InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += 1.05*amount  #additional 5 percent to these type of accounts
        print(f"\nDeposit complete.\nBalance for account '{self.name}': ${self.balance:.2f}")



