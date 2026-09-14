def name(a,b):
    print("Name : " , a.capitalize())
    print("ID : " , b)

def calculate(*args):
    ds = salary / working_days
    ad = working_days - c
    deduct = ds * ad
    fs = salary - deduct
    print("Monthly Salary : " , salary)
    print("No Of Days Present : " , c)
    print ("Final Salary : " , fs)

def attendance(c,working_days):
    at = (c / working_days) * 100
    print("Attandence : " , at , "%")
    if at > 90:
        print ("Status : Employee Of Thhe Year\n")
    elif at > 75:
        print ("Status : Excellent\n")
    elif at > 50:
        print ("Status : Good\n")
    else:
        print ("status : Poor\n")

br = "Y"
while br == "Y":
    a = str(input("Enter Employee Name\n"))
    b = str(input("Enter Employee ID\n"))
    c = int(input("Enter No Of Days Present\n"))
    working_days = 26
    salary = 35000
    print("\tRepot\n")
    name(a,b)
    calculate(working_days,salary,c)
    attendance(c,working_days)
    re = str(input("Process Another Employee : Y for Yes N for No\n"))
    br = re
    if br == "N":
        print("Closing The App")
        break
    if br == "Y":
        pass
    else:
        print("Wrong Input")
        while br != "Y":
            re = str(input("Process Another Employee : Y for Yes N for No\n"))
            br = re
            if br == "Y":
                break
            elif br == "N":
                break
            else:
                continue
        continue