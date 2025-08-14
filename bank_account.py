class BankAccount:
    bankName = "Sinapi Aba"
    interestRate = 10.39
    def __init__(self,accountHolder,initialBalance=0):
        self.accountHolder = accountHolder
        self.initialBalance = initialBalance
        self.balance = self.initialBalance
        self.accountNumber = self.generateAccountNumber()

    def generateAccountNumber(self):
        import random
        return(f"OOP{random.randint(100000, 999999)}")
    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            return(f"Deposit ${amount}. New Balance: ${self.balance}")
        else:
            return("Invalid eposit amount!")
        
    def withDrawal(self,amountWithDraw=0):
        amountWithDraw = int(input("Enter amount to withdraw: "))
        if amountWithDraw <= 0:
            return(f"Invalid withdrawal amount!")

        if self.balance > amountWithDraw:
            self.balance -= amountWithDraw
            return(f"You have withdrawn {amountWithDraw} from your account")
        else:
            return("Insufficient funds! Withdrawal amount exceeds your current balance.")
        
    def getAccountInfo(self):
        return(f"Account: {self.accountNumber}.\nAvailable Balance: ${self.balance}")

# myAccount = BankAccount(accountHolder="John Doe", initialBalance=500)

# print(myAccount.getAccountInfo())

# # print(myAccount.deposit(200))

# # print(myAccount.getAccountInfo())

# print(myAccount.withDrawal())

account1 = BankAccount("Othniel Johnson", 5000)
print(account1.bankName)
print(account1.deposit(500))
print(account1.getAccountInfo())