class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        if amount>self.balance:
            print("Insufficient balance ")
            return

        self.balance=self.balance-amount 

    def deposit(self, amount):
        self.balance=self.balance+amount
           
    def getBalance(self):
         print("Balance Available :",self.balance)

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        interest_amount=self.interestRate * self.balance//100
        print("Interest Amount :",interest_amount)


demo1 = SavingsAccount("Ashish", 2000, 5)   # initializing a SavingsAccount object

demo1.deposit(300)
demo1.getBalance()
demo1.withdrawal(200)
demo1.getBalance()
demo1.interestRate = 5
demo1.interestAmount()