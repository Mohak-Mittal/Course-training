# Q2. NovaMart is running a "Buy More, Save More" offer. Given the cart total,
# apply a discount using arithmetic and comparison operators: 5%
# if total > 1000, 10% if total > 5000 (do this using operators only
# no if-else yet — just show the arithmetic expression using boolean-to-number
# tricks or explain why operators alone are insufficient).

bill = int(input("enter bill anount\n"))
dis = 0.05*(bill>1000) + 0.05*(bill>5000)
Final_Bill = bill - (bill*dis)
print (Final_Bill)