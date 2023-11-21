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
                print("*You are now exiting the banking system. Have a great day!*")
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







