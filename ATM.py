# Q15. Build a simple "ATM Transaction Simulator" for a bank client: (1) Store an account holder's name and
# balance as variables. (2) Display a menu (Deposit / Withdraw / Check Balance / Exit) inside a loop using
# while True. (3) Use if-elif-else to handle each menu choice. (4) For withdrawals, use comparison operators
# to prevent overdraft and string formatting to display a clean, formatted receipt message. (5) The loop
# should continue until the user selects Exit.

a = [1 , 2]
a[0] = ["varun", 2002, 10000]
a[1] = ["anish", 2004, 20000]
for i in a:
    b = str(input("Enter Your Name\n"))
    c = int(input("Enter Your Password\n"))
    if i[0] == b and i[1] == c:
        print ("Balance : ",i[2])
        d = ""
        while d != "e":
            e = str(input("What To Do?\nPress d For Deposit\nw For Withdraw\nc ForvCheck Balance\ne For Exit\n"))
            d = e
            if e == "d":
                f = int(input("Enter Amount\n"))
                i[2] = i[2] + f
                print(f"New Amount is : {i[2]}")
            elif e == "w":
                f = int(input("Enter Amount\n"))
                if i[2] < f:
                    print("Not Enough Balance")
                else:
                    i[2] = i[2] - f
                    print(f"Remainiing Amount is : {i[2]}")
            else:
                print("Balance : ",i[2])
    elif a[1][0] == b and a[1][1] == c:
        print ("Balance : ", a[1][2])
        d = ""
        while d != "e":
            e = str(input("What To Do?\nPress d For Deposit\nw For Withdraw\nc ForvCheck Balance\ne For Exit\n"))
            d = e
            if e == "d":
                f = int(input("Enter Amount\n"))
                a[1][2] = a[1][2] + f
                print(f"New Amount is : {a[1][2]}")
            elif e == "w":
                f = int(input("Enter Amount\n"))
                if a[1][2] < f:
                    print("Not Enough Balance")
                else:
                    a[1][2] = a[1][2] - f
                    print(f"Remaining Amount is : {a[1][2]}")
            else:
                 print("balance : ",a[1][2])
    else:
        print("Wrong User Name Or Password")
    break
