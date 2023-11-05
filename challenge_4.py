class Account():

    def __init__(self,title=None,Balance=0):
        self.title=title
        self.Balance=Balance

class SavingsAccount(Account):
    def __init__(self,title=None,Balance=0,interestRate=0):
        super().__init__(title,Balance)
        self.interestRate=interestRate


user1=SavingsAccount("Ashish",5000, 5)
print(user1.title)
print(user1.Balance)
print(user1.interestRate)