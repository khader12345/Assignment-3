

class Account:
     def __init__(self, accountNumber, accountHolderName, rateOfinterest, currentBalance = 0):
        self._accountNumber=accountNumber
        self._accountHolderName=accountHolderName
        self._currentBalance=currentBalance
        self.rateOfinterest=rateOfinterest

     def getAccountNumber(self):
        return self._accountNumber
    
     def getAccountHolderName(self):
         return self._accountHolderName
     
     def getRateOfinterest(self):
         return self._rateOfinterest
     
     def getCurrentBalance(self):
         return self._currentBalance

     def setAccountHolderName(self, recent_name):
         self._account_user_name=recent_name

     def setRateOfinterest(self, recent_rate):
         self._rateOfinterest=recent_rate
      
     def deposit(self, value):
         self._currentBalance += value
         return f"*Deposit was sucessfull | New balance: {self._currentBalance:.2f}*"
     
     def withdraw(self, value):
         self._currentBalance -= value
         return f"*Withdraw was sucessfull | New balance: {self._currentBalance:.2f}"
        
class savingsAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfinterest, currentBalance, minimum_bal):
        super().__init__(accountNumber, accountHolderName, rateOfinterest, currentBalance)
        self._minimum_bal=minimum_bal

    def withdraw(self, value):
        if self._currentBalance - value >= self._minimum_bal:
            super().withdraw(value)
            return f"Withdrew {value} CAD | New balance: {self.getCurrentBalance()}"
        else:
            return"*Withdrawal rejected, insufficient funds to maintain the minimum balance*"

class chequingAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfinterest, currentBalance, over_lim):
        super().__init__(accountNumber, accountHolderName, rateOfinterest, currentBalance)
        self._over_lim=over_lim

    def withdraw(self, value):
        if value > self.getCurrentBalance() + self._over_lim:
            return"*Withdrawal rejected, insufficient funds*"
        else:
            super().withdraw(value)
            return f"Withdrew {value} CAD | New balance: {self.getCurrentBalance()}"

class Application:
    def __init__(self):
        self.variousaccounts=[]
        self.presentAccount=None

    def Show_Main_Menu(self):
        while True:
            print("\n*Banking Main Menu*")
            print("1. Select Account (user must open an account first to be registered in the bank): ")
            print("2. Open Account: ")
            print("3. Exit")

            options = input("Please enter your choice: ")

            if options=='1':
                self.choosing_account()
            elif options=='2':
                self.open_new_account()
                pass
            elif options=='3':
                print("*You have now exited the banking system. Have a great day!*")
                break
            else:
                print("*Invalid option please enter the correct option*")

    def choosing_account(self):
        accountNumber=input("Please enter the account number: ")
        account=bank.find_account(accountNumber)
        if account:
            self.presentAccount=account
            self.Show_Account_Menu()
        else:
            print("*Account not found please enter the correct account number*")

    def open_new_account(self):
        account_type=input("Please enter account type (Savings or Chequing): ")
        accountNumber=input("Please enter the account number: ")
        accountHolderName=input("Please enter the accounts owners name: ")
        rateOfinterest=float(input("Please enter the rate of interest: "))
        currentBalance=float(input("Please enter the current balance: "))

        if account_type=="Savings":
            more_param=float(input("Please enter the minimum amount for Savings account: "))
        elif account_type=="Chequing":
            more_param=float(input("Please enter the overdraft limit amount for Chequings account: "))
        else:
            print("*Incorrect account type*")
            return
        
        bank.open_new_account(account_type, accountNumber, accountHolderName, rateOfinterest, currentBalance, more_param)
        print(f"*New {account_type} account has opened successfully*")

    def Show_Account_Menu(self):
        while True:
            print("\n*My Account*")
            print("1. Account Balance")
            print("2. Deposit Funds")
            print("3. Withdraw Funds")
            print("4. Logout of Account")

            options=input("Please enter your choice (1,2,3 or 4): ")

            if options=='1':
                print(f"Current Account Balance: ${self.presentAccount.getCurrentBalance()}")
            elif options=='2':
                value = self.get_real_value("Please enter the amount you would like to deposit: $")
                print(self.presentAccount.deposit(value))
            elif options=='3':
                value = self.get_real_value("Please enter the amount you would like to withdraw: $")
                print(self.presentAccount.withdraw(value))
            elif options=='4':
                print("*You have now exited the account menu*")
                break
            else:
                ("*Invalid option please enter the correct option*")

    def get_real_value(self, message):
        while True:
            try:
                value=float(input(message))
                if value<0:
                    print("*Invalid value please enter a positive value*")
                else:
                    return value
            except ValueError:
                print("*Incorrect input please input the correct number*")

    def run(self):
        self.Show_Main_Menu()

class Bank:
    def __init__(self):
        self.variousaccounts=[]

        self.variousaccounts.append(chequingAccount("111222", "ABC", 2, 1000, 5000))
        self.variousaccounts.append(chequingAccount("222333", "DEF", 2, 200, 5000))
        self.variousaccounts.append(chequingAccount("333444", "GHI", 3, 1000, 5000))
        self.variousaccounts.append(chequingAccount("444555", "JKL", 2, 200, 5000))
        self.variousaccounts.append(savingsAccount("555666", "MNO", 1.5, 3000, 1000))
        self.variousaccounts.append(savingsAccount("666777", "PQR", 1.5, 2000, 800))
        self.variousaccounts.append(savingsAccount("777888", "STU", 2, 4000, 1500))
        self.variousaccounts.append(savingsAccount("888999", "VWX", 3, 5000, 2500))

    def find_account(self, accountNumber):
        for account in self.variousaccounts:
            if account.getAccountNumber()==accountNumber:
                return account
        return None
        

    def open_new_account(self, account_type, accountNumber, accountHolderName, rateOfinterest, CurrentBalance, more_param):
        if account_type=="Savings":
            new_opened_account=savingsAccount(accountNumber, accountHolderName, rateOfinterest, CurrentBalance, more_param)
        elif account_type=="Chequing":
            new_opened_account=chequingAccount(accountNumber, accountHolderName, rateOfinterest, CurrentBalance, more_param)
        else:
            print("*Not a valid account type*")
            return
        self.variousaccounts.append(new_opened_account)
        print(F"*Your new {account_type} account has now been opened successfully*")


if __name__ == "__main__":
    bank=Bank()

    bank_app=Application()
    bank_app.variousaccounts = bank.variousaccounts
        
    bank_app.run()

