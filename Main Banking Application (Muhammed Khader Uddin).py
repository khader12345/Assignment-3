

class Account:
     def __init__(self, account_number, account_holder, rate_of_interest, present_balance = 0):
        self._account_number=account_number
        self._account_holder=account_holder
        self._present_balance=present_balance
        self.rate_of_interest=rate_of_interest

     def get_account_number(self):
        return self._account_number
    
     def get_account_holder(self):
         return self._account_holder
     
     def get_rate_of_interest(self):
         return self._rate_of_interest
     
     def get_present_balance(self):
         return self._present_balance

     def set_account_holder(self, recent_name):
         self._account_user_name=recent_name

     def set_rate_of_interest(self, recent_rate):
         self._rate_of_interest=recent_rate
      
     def deposit(self, value):
             self._present_balance+=value
             return f"*Deposited {value} CAD | New balance: {self._present_balance:.2f}*"
     
     def wihtdraw(self, value):
             self._present_balance-=value
             return f"*Withdraw {value} CAD | New balance: {self._present_balance:.2f}"
        
class savingsAccount(Account):
    def __init__(self, account_number, account_holder, rate_of_interest, present_balance, minimum_bal):
        super().__init__(account_number, account_holder, rate_of_interest, present_balance)
        self._minimum_bal=minimum_bal

    def withdraw(self, value):
        if self._present_balance-value>=self._minimum_bal:
            super().withdraw(value)
            return f"*Withdraw {value} CAD | New balance: {self.get_present_balance()}"
        else:
            return"*Withdrawal rejected, insufficient funds to maintain the minimum balance*"

class chequingAccount(Account):
    def __init__(self, account_number, account_holder, rate_of_interest, present_balance, over_lim):
        super().__init__(account_number, account_holder, rate_of_interest, present_balance)
        self._over_lim=over_lim

    def withdraw(self, value):
        if value > self.get_present_balance()+self._over_lim:
            return"*Withdrawal rejected, insufficient funds*"
        else:
            super().wihtdraw(value)
            return f"*Withdrew {value} CAD. New balance: {self.get_present_balance()}"
class Application:
    def __init__(self):
        self.variousaccounts = []
        self.presentAccount = None

    def Show_Main_Menu(self):
        while True:
            print("\n*Banking Main Menu*")
            print("1. Select Account: ")
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
        account_number=input("Please enter the account number: ")
        account=bank.find_account(account_number)
        if account:
            self.presentAccount=account
            self.Show_Account_Menu()
        else:
            print(*"Account not found please enter the correct account number*")

    def open_new_account(self):
        account_type=input("Please enter account type (Savings or Chequing): ")
        account_number=input("Please enter the account number: ")
        account_holder=input("Please enter the accounts owners name: ")
        rate_of_interest=input("Please the rate of interest: ")
        present_balance=input("Please enter the current balance: ")

        if account_type=="Savings":
            more_param=float(input("Please enter the minimum amount for Savings account: "))
        elif account_type=="Chequing":
            more_param=float(input("Please enter the overdraft limit amount for Chequings account: "))
        else:
            print("*Incorrect account type*")
            return
        
        bank.open_new_account(account_type, account_number, account_holder, rate_of_interest, present_balance, more_param)
        print(f"*New {account_type} account has opened successfully*")

    def Show_Account_Menu(self):
        while True:
            print("\n*My Account:*")
            print("1. Account Balance")
            print("2. Deposit Funds")
            print("3. Withdraw Funds")
            print("4. Logout of Account")

            options=input("Please enter your choice (1,2,3 or 4): ")

            if options=='1':
                print(f"Current Account Balance: ${self.presentAccount.get_present_balance()}")
            elif options=='2':
                value = self.get_real_value("Please enter the amount you would like to deposit: $")
                print(self.presentAccount.deposit(value))
            elif options=='3':
                value = self.get_real_value(input("Please enter the amount you would like to withdraw: $"))
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

    def find_account(self, account_number):
        for account in self.variousaccounts:
            if account.get_account_number()==account_number:
                return account
            return None
        

    def open_account(self, account_preference, account_code, account_holder, interest_rate, present_balance, more_param):
        if account_preference=="Savings":
            new_opened_account=savingsAccount(account_code, account_holder, interest_rate, present_balance, more_param)
        elif account_preference=="Chequing":
            new_opened_account=chequingAccount(account_code, account_holder, interest_rate, present_balance, more_param)
        else:
            print("*Not a valid account type*")
            return
        self.variousaccounts.append(new_opened_account)
        print(F"*your new {account_preference} account has now been opened successfully*")
        

app=Application()
app.run()







