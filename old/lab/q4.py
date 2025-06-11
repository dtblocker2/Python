class bank():
    def __init__(self,name_of_bank):
        self.accounts = {}
        self.bank_name = name_of_bank
        self.loan_accounts = {}
        self.loan_interests = {"1":[0.44,"personal"],"2":[0.128,"home"],"3":[0.16,"education"],"4":[0.1695,"gold"]}
    
    def create_account(self,user_name,initial_money):
        acc_num = self.bank_name + str(len(self.accounts))
        self.accounts[acc_num] = [user_name, initial_money]
        print(f"Account successfully created with \nName: {user_name} \nAccount number: {acc_num} \nBalance: {initial_money}")

    def deposit(self,acc_num,money):
        self.accounts[acc_num] += money
        self.check_balance(acc_num)
    
    def withdraw(self,acc_num,money):
        if (self.accounts[acc_num][1] - money)>=0:
            self.accounts[acc_num][1] -= money
            self.check_balance(acc_num)
        else:
            loan = input("You dont have sufficient funds.\n\nDo you want loan?(Y/N)")

            if loan=="Y":
                self.loan(acc_num)
            else:
                print("OK")

    def check_balance(self,acc_num):
        print(f"Your bank balance is: {self.accounts[acc_num][1]}")

    def loan(self,acc_num):
        if acc_num in self.loan_accounts:
            print("You already have loan on your name please pay previous loans")
        else:
            loan_type = input("Which type of loan you want to consider?\n1. Personal \n2. Home \n3. Education \n4. Gold")
            interest = self.loan_interests[loan_type][0]


sbi = bank("SBI")

while True:
    query = int(input("What do you want to do? \n1. Deposit money\n2. Create New Account\n3. Withdraw Money\n4. Check Balance"))
    if query in [1,3,4]:
        a= input("Enter account number")
        if a not in sbi.accounts:
            print("enter valid account number")
            continue

    if query == 1:
        b = int(input("Enter amount to be deposited: "))
        sbi.deposit(a,b)

    elif query == 2:
        a = input("Enter your name: ")
        b = int(input("Enter amount to be deposited: "))
        sbi.create_account(a,b)
    
    elif query == 3:
        b = int(input("Enter amount to be withdrawn"))
        sbi.withdraw(a,b)
    
    elif query == 4:
        sbi.check_balance(a)

    print("--------------------------------------")