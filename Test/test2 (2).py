a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = str(input("Enter operation to perform: "))
if c == "+":
    print (a + b)
elif c == "-":
    print (a - b)
elif c == "*":
    print (a * b)
elif c == '/':
    print (a / b)
else:
    print("wrong input")