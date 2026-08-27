class Bank:
    def __init__(self,owner, balance):
        self.owner = owner
        self.balance = balance
    def greetings(self):
        print(f"NOMOSHKAR THIS BANK ACCOUNT BELONGS TO {self.owner} HAVING BALANCE OF {self.balance}")
    def deposit(self, amount):
        self.balance+= amount
        print(f"{self.balance} is the updated balance")

    def withdraw(self,withdrawl):
        if withdrawl<= self.balance:
            self.balance-=withdrawl
            print(f"{self.balance} is the updated balance")
        else:
            print("INSUFFICIENT BALANCE")


mayukh = Bank("MAYUKH DEY DHARA", 5000)

choice = int (input("What would you like to do?\n1. Deposit \n2. Withdraw\n"))

if choice == 1:
    amount = int (input("Enter the amount you want to deposit\n"))
    mayukh.deposit(amount)

elif choice == 2:
    withdrawl = int (input("Enter the amount you want to withdraw\n"))
    mayukh.withdraw(withdrawl)

