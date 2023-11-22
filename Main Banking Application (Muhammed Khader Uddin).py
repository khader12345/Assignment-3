

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
         self._present_balance+=value

     def wihtdraw(self, value):
         if value <=self._present_balance:
             self._present_balance-=value
         else:
             print("*Insufficient funds, withdrawal of funds not permitted*")

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
    
    def run(self):
        self.Show_Main_Menu()

app=Application()
app.run()







