#A class is made by the name of "Acount" with its varibales being defined and all those attributes are initialized.

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
     
#Setting the new account holders name along with the interest rate.

     def setAccountHolderName(self, recent_name):
         self._account_user_name=recent_name

     def setRateOfinterest(self, recent_rate):
         self._rateOfinterest=recent_rate

#The method "deposit" is defined that deposits funds into the account along with "withdraw" that will take money out of the account.
      
     def deposit(self, value):
         self._currentBalance += value
         return f"*Deposit was sucessfull | New balance: {self._currentBalance:.2f}*"
     
     def withdraw(self, value):
         self._currentBalance -= value
         return f"*Withdraw was sucessfull | New balance: {self._currentBalance:.2f}"
     
#Savings account class is defined that takes in from the base "Account" class.
#Along with that it starts the the savings account attributes.
        
class savingsAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfinterest, currentBalance, minimum_bal):
        super().__init__(accountNumber, accountHolderName, rateOfinterest, currentBalance)
        self._minimum_bal=minimum_bal

#Checks if withdraw amount is within the minimum limit as outlined in the code.
#Furthermore it calls upon the withdraw method from the class and gives a message.

    def withdraw(self, value):
        if self._currentBalance - value >= self._minimum_bal:
            super().withdraw(value)
            return f"Withdrew {value} CAD | New balance: {self.getCurrentBalance()}"
        else:
            return"*Withdrawal rejected, insufficient funds to maintain the minimum balance*"

#Chequing account class is defined that takes in fromt he base "Account" class.
#It also starts with its attributes.

class chequingAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfinterest, currentBalance, over_lim):
        super().__init__(accountNumber, accountHolderName, rateOfinterest, currentBalance)
        self._over_lim=over_lim

#Checks if withdraw amount is within the given balance and maximum limit.
#Furthermore it calls upon the withdraw method form the class and gives a message.

    def withdraw(self, value):
        if value > self.getCurrentBalance() + self._over_lim:
            return"*Withdrawal rejected, insufficient funds*"
        else:
            super().withdraw(value)
            return f"Withdrew {value} CAD | New balance: {self.getCurrentBalance()}"
        
#A new class is created by the name of "Application" to get the user to give inputs.
#A list is also created to store different accounts along witht the present account.

class Application:
    def __init__(self):
        self.variousaccounts=[]
        self.presentAccount=None

#The banking main menu with the different prompts to choose from along with conditions that print various statments depending on the input.

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

#New method is made which is choosing an existing account.

    def choosing_account(self):
        accountNumber=input("Please enter the account number: ")
        account=bank.find_account(accountNumber)
        if account:
            self.presentAccount=account
            self.Show_Account_Menu()
        else:
            print("*Account not found please enter the correct account number*")

#New method is made which is to open a new account along with the varibales that are defined to give the user a prompt.

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
        
#The bank's opening of a new account method to make a new account for the user.
        
        bank.open_new_account(account_type, accountNumber, accountHolderName, rateOfinterest, currentBalance, more_param)
        print(f"*New {account_type} account has opened successfully*")

#Account menu is created with the prompts as shown to interact with the user.

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

#Method was made to get a valid numerical value for the applicaiton to work otherwise it wont.

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

#This method was created for the bank applicaiton to function.

    def run(self):
        self.Show_Main_Menu()

#Bank class was developed to manage accounts along wiht a list to store those various accounts.

class Bank:
    def __init__(self):
        self.variousaccounts=[]

#Some accounts were initially created for our special VIP members that are part of our banking assoication.

        self.variousaccounts.append(chequingAccount("111222", "ABC", 2, 1000, 5000))
        self.variousaccounts.append(chequingAccount("222333", "DEF", 2, 200, 5000))
        self.variousaccounts.append(chequingAccount("333444", "GHI", 3, 1000, 5000))
        self.variousaccounts.append(chequingAccount("444555", "JKL", 2, 200, 5000))
        self.variousaccounts.append(savingsAccount("555666", "MNO", 1.5, 3000, 1000))
        self.variousaccounts.append(savingsAccount("666777", "PQR", 1.5, 2000, 800))
        self.variousaccounts.append(savingsAccount("777888", "STU", 2, 4000, 1500))
        self.variousaccounts.append(savingsAccount("888999", "VWX", 3, 5000, 2500))

#Method was made to find those accounts by its account number.

    def find_account(self, accountNumber):
        for account in self.variousaccounts:
            if account.getAccountNumber()==accountNumber:
                return account
        return None
    
#Another method was created open a new account that would get added to the list of various accounts.

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

#This final piece makes an instance of the bank and applicatiton class along with the final code at the end to run the banking application.

if __name__ == "__main__":
    bank=Bank()

    bank_app=Application()
    bank_app.variousaccounts = bank.variousaccounts
        
    bank_app.run()

