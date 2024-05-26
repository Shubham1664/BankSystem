from bank_accounts import *

John = BankAccount(1000, "John")
Doe = BankAccount(2000, "Doe") 

John.getBalance()
Doe.getBalance()

John.deposit(2000)
Doe.deposit(1000)

#John.withdraw(4000)
#Doe.withdraw(2000)

John.transfer(1000, Doe)

John.getBalance()
Doe.getBalance()

Jane = InterestRewardsAccount(1000, "Jane")
Jane.getBalance()
Jane.deposit(100)
