

class Account:
     def __init__(self, account_code, account_user_name, interest_rate, present_balance = 0):
        self._account_code=account_code
        self._account_user_name=account_user_name
        self._present_balance=present_balance
        self._interest_rate=interest_rate

     def have_account_code(self):
        return self._account_code
     
     def have_account_user_name(self):
         return self._account_user_name
     
     def have_interest_rate(self):
         return self._interest_rate
     
     def have_present_balance(self):
         return self._present_balance

     def set_account_user_name(self, recent_name):
         self._account_user_name=recent_name

     def set_interest_rate(self, recent_rate):
         self._interest_rate=recent_rate
      
     def deposit(self, value):
         if value > 0:
             self._present_balance+=value
             print(f"*Deposited {value} CAD | New balance: {self._present_balance}*")
         else:
             print("*Incorrect deposit amount please enter a positive amount*")

     def wihtdraw(self, value):
         if value <=self._present_balance:
             self._present_balance-=value
         else:
             print("*Insufficient funds withdrawal denied*")

class savingsAccount(Account):
    def __init__(self, account_code, account_user_name, interest_rate, present_balance, minimum_bal):
        super().__init__(account_code, account_user_name, interest_rate, present_balance)
        self._minimum_bal=minimum_bal

    def withdraw(self, value):
        if self._present_balance-value>=self._minimum_bal:
            super().withdraw(value)
        else:
            print("*Withdrawal rejected, insufficient funds to maintain the minimum balance*")

class chequingAccount(Account):
    def __init__(self, account_code, account_user_name, interest_rate, present_balance, over_lim):
        super().__init__(account_code, account_user_name, interest_rate, present_balance)
        self.over_lim=over_lim

    def withdraw(self, value):
        if self.have_present_balance()+self._over_lim>=value:
            super().withdraw(value)
        else:
            print("*Withdrawal rejected, insufficient funds*")

class Application:
    def __init__(self):
        self.variousaccounts = {}
        self.presentAccount = None

    def Show_Main_Menu(self):
        while True:
            print("\n*Banking Main Menu*")
            print("1. Select Account: ")
            print("2. Open Account: ")
            print("3. Exit")

            options = input("Please enter your choice: ")

            if options=='1':
                account_code = input("Please enter the account code: ")
                if account_code in self.account_code:
                    self.presentAccount=self.variousaccounts[account_code]
                    self.Show_Account_Menu()
                else: 
                    print("*Account can not be verified please enter the correct code*")
            elif options=='2':
                pass
            elif options=='3':
                print("*You have now exited the banking system. Have a great day!*")
                break
            else:
                print("*Invalid option please enter the correct option*")
            

    def Show_Account_Menu(self):
        while True:
            print("\n*My Account:*")
            print("1. Account Balance")
            print("2. Deposit Funds")
            print("3. Withdraw Funds")
            print("4. Logout of Account")

            options=input("Please enter your choice (1,2,3 or 4): ")

            if options=='1':
                print(f"Current Account Balance: ${self.presentAccount.check_balance()}")
            elif options=='2':
                value = float(input("Please enter the amount you would like to deposit: $"))
                print (self.presentaccount.deposit(value))
            elif options=='3':
                value = float(input("Please enter the amount you would like to withdraw: $"))
            elif options=='4':
                print("*You have now exited the account menu*")
                break
            else:
                ("*Invalid option please enter the correct option*")

    def have_real_value(self, message):
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

class bank:
    def __init__(self):
        self.variousaccounts=[]

        self.variousaccounts.appaend(chequingAccount("111222", "ABC", 2, 1000, 5000))
        self.variousaccounts.appaend(chequingAccount("222333", "DEF", 2, 200, 5000))
        self.variousaccounts.appaend(chequingAccount("333444", "GHI", 3, 1000, 5000))
        self.variousaccounts.appaend(chequingAccount("444555", "JKL", 2, 200, 5000))
        self.variousaccounts.appaend(savingsAccount("555666", "MNO", 1.5, 3000, 1000))
        self.variousaccounts.appaend(savingsAccount("666777", "PQR", 1.5, 2000, 800))
        self.variousaccounts.appaend(savingsAccount("777888", "STU", 2, 4000, 1500))
        self.variousaccounts.appaend(savingsAccount("888999", "VWX", 3, 5000, 2500))

    def find_account(self, account_code):
        for variousaccounts in self.variousaccounts:
            if variousaccounts.get_variousaccounts()==variousaccounts:
                return variousaccounts
            return None
        

app=Application()
app.run()







