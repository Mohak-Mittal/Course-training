# Q1. Create variables to store a product's name, price, quantity,
# and GST rate (in %).Calculate and print the final payable amount
# (price × quantity + GST) with proper labels in the output.

List_1_product = ["apple","banana","orange","grapes"]
List_2_price = [100, 50, 80, 120]
List_3_quantity = [20, 30, 100, 40]
GST_rate = 5  # GST rate in percentage
b = int(input("enter 1 for apple\nenter 2 for banana\nenter 3 for orange\nenter 4 for grapes\n"))
if b == 1:
    print ("avaliable items = ",List_3_quantity[0])
    print ("product price =",List_2_price[0])
    print ("GST AMount = ",GST_rate)
    c = int(input("choose quantity\n"))
    if c > List_3_quantity[0]:
        print ("not avaliable")
    else:
        List_3_quantity[0] = List_3_quantity[0] - c
        print (f"remaining product {List_3_quantity[0]}")
        GST_Amount = List_2_price[0] * c * GST_rate/100
        Total_Amount = List_2_price[0] * c + GST_Amount
        print ("GST AMount = ",GST_Amount)
        print ("Total Amount = ",Total_Amount)
if b == 2:
    print ("avaliable items",List_3_quantity[1])
    print ("product price ",List_2_price[1])
    print ("GST AMount = ",GST_rate)
    c = int(input("choose quantity\n"))
    if c > List_3_quantity[1]:
        print ("not avaliable")
    else:
        List_3_quantity[1] = List_3_quantity[1] - c
        print (f"remaining product {List_3_quantity[1]}")
        GST_Amount = List_2_price[1] * c * GST_rate/100
        Total_Amount = List_2_price[1] * c + GST_Amount
        print ("GST AMount = ",GST_Amount)
        print ("Total Amount = ",Total_Amount)
if b == 3:
    print ("avaliable items",List_3_quantity[2])
    print ("product price ",List_2_price[2])
    print ("GST AMount = ",GST_rate)
    c = int(input("choose quantity\n"))
    if c > List_3_quantity[2]:
        print ("not avaliable")
    else:
        List_3_quantity[2] = List_3_quantity[2] - c
        print (f"remaining product {List_3_quantity[2]}")
        GST_Amount = List_2_price[2] * c * GST_rate/100
        Total_Amount = List_2_price[2] * c + GST_Amount
        print ("GST AMount = ",GST_Amount)
        print ("Total Amount = ",Total_Amount)
if b == 4:
    print ("avaliable items",List_3_quantity[3])
    print ("product price ",List_2_price[3])
    print ("GST AMount = ",GST_rate)
    c = int(input("choose quantity\n"))
    if c > List_3_quantity[3]:
        print ("not avaliable")
    else:
        List_3_quantity[3] = List_3_quantity[3] - c
        print (f"remaining product {List_3_quantity[3]}")
        GST_Amount = List_2_price[3] * c * GST_rate/100
        Total_Amount = List_2_price[3] * c + GST_Amount
        print ("GST AMount = ",GST_Amount)
        print ("Total Amount = ",Total_Amount)


""" output
enter 1 for apple
enter 2 for banana
enter 3 for orange
enter 4 for grapes
1
avaliable items =  20
product price = 100
GST AMount =  5
choose quantity
12
remaining product 8
GST AMount =  60.0
Total Amount =  1260.0
Press any key to continue . . ."""




        # Q2. NovaMart is running a "Buy More, Save More" offer. Given the cart total,
# apply a discount using arithmetic and comparison operators: 5%
# if total > 1000, 10% if total > 5000 (do this using operators only
# no if-else yet — just show the arithmetic expression using boolean-to-number
# tricks or explain why operators alone are insufficient).

bill = int(input("enter bill anount\n"))
dis = 0.05*(bill>1000) + 0.05*(bill>5000)
Final_Bill = bill - (bill*dis)
print (Final_Bill)

"""output
enter bill anount
10000
9000.0
Press any key to continue . . ."""



# Q3. A delivery partner's salary depends on base pay +
# (distance_km * rate_per_km) deductions. Using assignment operators
#  (+=, -=, *=), simulate three days of pay updates for a single
#  variable representing weekly earnings.

Base_Pay = 500
Rate_Per_KM = 6
deduct = 200
Weekly_Pay = 0
Distance_Pay = 0
for i in range (1,4):
    Distance = int(input(f"enter day {i} Distance \n"))
    Distance *= Rate_Per_KM
    Today_Pay = Base_Pay + Distance
    print (f"day {i} pay = {Today_Pay}")
    Weekly_Pay +=  Today_Pay
Weekly_Pay -= deduct
print(Weekly_Pay)

"""output
enter day 1 Distance
10
day 1 pay = 560
enter day 2 Distance
10
day 2 pay = 560
enter day 3 Distance
10
day 3 pay = 560
1480
Press any key to continue . . ."""



# Q4. Write a program to swap the "cash balance" and "card balance" of
#  a customer'swallet without using a third/temporary variable,
#  using arithmetic operators.

a = 1000
b = 5000
print(f" cash {a} card {b}")
a = a+b
b = a-b
a = a-b
print(f" cash {a} card {b}")

"""output
cash 1000 card 5000
 cash 5000 card 1000
Press any key to continue . . ."""


# Q5. A customer enters their full name with extra spaces and inconsistent casing, e.g.
# "  raJEsh KUMAr  ". Clean this string to produce a properly formatted name: "Rajesh Kumar".

name = "  raJEsh KUMar  "
print (name)
b = name.lstrip().title().rstrip()
print(b)

"""  raJEsh KUMar
Rajesh Kumar
Press any key to continue . . ."""



# Q6. Validate a customer's email input by checking (using string methods only, no regex)
# whether it contains exactly one '@' symbol and ends with '.com'. Print whether the
# email is valid.

Email = input("Enter Your Email\n")
a = (Email.find("@"))
b = (Email.find(".com"))
if a > 0 and b > 0:
    print("Varified Email")
else:
    print("Wrong Email")


    """Enter Your Email
mohakmttal92@gmail.com
Varified Email
Press any key to continue . . ."""


# Q7. Given a customer's phone number as a string, mask all digits except the last 4,
# e.g. "9876543210" -> "******3210". This is used for order confirmation SMS previews.

num = "9876543210"
mask_num = ""
for i in range (0,len(num)):
    if i >= len(num) - 4:
        mask_num = mask_num + num[i]
    else:
        mask_num = mask_num + "*"
print(mask_num)

"""******3210
Press any key to continue . . ."""



# Q8. Marketing wants a personalized coupon code generated as: first 3 letters
# of the customer's name (uppercase) + last 2 digits of their phone number +
# "NM26". Build this using string slicing and concatenation.

name = input("enter your name\n")
no = int(input("enter your number\n"))
code = "NM26"
b = str(no)
ncode = ""
numcode = ""
Cupon = ""
for i in range (0,3):
    ncode = ncode + name[i]
for i in range (-2,0):
    numcode =numcode + b[i]
Cupon = ncode + numcode + code
print(Cupon.upper())

"""enter your name
mohak
enter your number
9876543210
MOH10NM26
Press any key to continue . . ."""


# Q9. A student is eligible for a scholarship if attendance >= 75% AND
# (marks >= 85 OR is_sports_captain is True). Write a program that takes
# these three inputs and prints whether the student is eligible.

a = int(input("Enter Your Attendence\n"))
b = int(input("Enter Your Marks\n"))
c = str(input("Are You In Any Games? Yes or No?\n"))
if a >= 75 and b >= 85:
    print("Eligible For Scholarship")
elif c == 'yes':
    print("Eligible For Scholarship")
else:
    print("Not Eligible")

"""Enter Your Attendence
67
Enter Your Marks
97
Are You In Any Games? Yes or No?
no
Not Eligible
Press any key to continue . . """



# Q10. Build a grading system:
# marks >= 90 -> 'A+',
# >= 75 -> 'A',
# >= 60 -> 'B',
# >= 40 -> 'C',
# else -> 'Fail'.
# Additionally, if the student scored 100, print a special "Topper of the Year" message.

print("Grading System\nmarks == 100 -> 'topper' \nmarks >= 90 -> 'A+',\nmarks >= 75 -> 'A',\nmarks >= 60 -> 'B',\nmarks >= 40 -> 'C',\nelse -> 'Fail'.")
a = int(input("Enter Your Marks\n"))
if a == 100:
    print("Topper Of The Year")
elif a >= 90:
    print("A+")
elif a >= 75:
    print("A")
elif a >= 60:
    print("B")
elif a >= 40:
    print("C")
else:
    print("Fail")

"""Grading System
marks == 100 -> 'topper'
marks >= 90 -> 'A+',
marks >= 75 -> 'A',
marks >= 60 -> 'B',
marks >= 40 -> 'C',
else -> 'Fail'.
Enter Your Marks
98
A+
Press any key to continue . . ."""



# Q11. A ride-booking feature at BrightPath's transport wing charges fare based
# on time of day: Peak hours (8-10 AM, 6-8 PM) add a 20% surcharge; late night
# (11 PM-5 AM) adds a 15% night charge; otherwise, normal fare applies. Write
# nested if-else logic to compute the final fare for a given hour (24-hr format)
# and base fare.

a = int(input("Enter Your Time In 24-hr Formet\n"))
b = 100
f = 0
s = 0
if a >= 6 and a <= 22:
    if a >= 8 and a <= 10:
        s = b * 20/100
        f = b + s
        print(f)
    elif a >= 18 and a <= 20:
        s = b * 20/100
        f = b + s
        print(f)
    else:
        print(b)
else:
     s = b * 15/100
     f = b + s
     print(f)


"""Enter Your Time In 24-hr Formet
23
115.0"""