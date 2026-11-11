
class bankaccount:
    def __init__(self,accno,accname,acctype,accbal):
        self.accountnumber=accno
        self.accountname=accname
        self.accounttype=acctype
        self.accountbalance=accbal
    
    def deposit(self):
        amount=float(input("Enter the amount to be deposited: "))
        self.accountbalance += amount
        print("Amount deposited successfully.")
        print("Current Balance:", self.accountbalance)
    
    1
    def withdraw(self):
        amount=float(input("\nEnter the amount to be withdrawn: "))
        if self.accountbalance>=amount:
            self.accountbalance-=amount
            print("Amount successfully withdrawn!")
            print("Current Balance ",self.accountbalance)
        else:
            print("Insuffcient balance!")
            
    def display(self):
        print("\n---Bank Account Details---")
        print("Account Number:",self.accountnumber)
        print("Account Holder Name:",self.accountname)
        print("Account Type:",self.accounttype)
        print("Account Balance:",self.accountbalance)
            
accno = input("Enter account number: ")
accname = input("Enter Account Holder Name: ")
acctype =input("Enter the type: ")
accbal = float(input("Opening amount:" ))

acc1 = bankaccount(accno,accname,acctype,accbal)

acc1.deposit()
acc1.withdraw()
acc1.display()
