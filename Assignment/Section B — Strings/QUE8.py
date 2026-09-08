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