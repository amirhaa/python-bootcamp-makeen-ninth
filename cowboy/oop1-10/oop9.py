class BankAccount:
    def __init__(self,accountNumber,name,balance) :
        self.accountNumber = int(accountNumber)
        self.name = str(name)
        self.balance = float(balance)


    def Deposit(self,deposit):
        self.balance = self.balance + deposit
        return self.balance
    def Withraw(self,withdraw):
        self.balance = self.balance - withdraw
        return self.balance
    def bankFees(self):
        self.balance = self.balance - (self.balance) * 0.05
        return self.balance
    def display(self):
        self.Deposit(float(input("Enter deposit :")))
        self.Withraw(float(input("Enter withraw :")))
        self.bankFees()
        return {"AccountNumber" : self.accountNumber , "Name" : self.name , "balance" : self.balance}

bankA_1 = BankAccount(1234863,"catfishbilly",1000)
print(bankA_1.display())


    




