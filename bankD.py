#2. Write a  program to create a class representing a bank. Include methods for managing customer accounts
#  and transactions. For example - Deposit Money , Withdraw Money, Bank Statement etc.
class bank:
    def __init__(self,pname,anumber,balance,amount):
        self.pname=pname
        self.anumber=anumber
        self.balance=balance
        self.amount = amount
    def customer_accounts(self):
        if len(str(self.anumber))>=12:
            print("Account already exists.")
        else:
            print("Create account")
    def Deposit_Money(self):
        if len(str(self.anumber))>=12 :
            self.balance+=self.amount
            print(self.pname,"your updated balance is ",self.balance)
        else:
            print("Account not found.")
    def Withdraw_Money(self):
        if len(str(self.anumber))>=12 :
            if self.balance>=self.amount:
                self.balance-=self.amount
            print(self.pname,"your updated balance is ",self.balance,"Money is Withdrew from account")
        else:
            print("Account not found.")
account1=bank("tanuja",123456789012,1000000,500)
account2=bank("divya",987654321098,2000000,1000)
account1.customer_accounts()
account1.Deposit_Money()
account1.Withdraw_Money()