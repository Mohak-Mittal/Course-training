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

"""
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

"""
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

"""
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