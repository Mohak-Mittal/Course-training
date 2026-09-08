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
