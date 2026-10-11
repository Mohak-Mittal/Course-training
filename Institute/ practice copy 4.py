class atm:
    def __init__ (self,balance):
        self.__balance = balance
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdraw")
            return self.__balance
        else:
            print("Insufficient Balance")
    def diposite(self,amount):
        self.__balance += amount
        print("Diposite")
        return self.__balance
    def checkbalance(self):
        print("Check Balance")
        return self.balance
A = atm(100000)
amount = int(input("enter the amount : "))
print("what do you want to do\n 1 for withdraw\n 2 for diposite\n 3 for checkbalance")
op = int(input("enter your option : "))
if op == 1:
    print(A.withdraw(amount))
elif op == 2:
    print(A.diposite(amount))
elif op == 3:
    print(A.checkbalance())
else:
    print("Invalid option")