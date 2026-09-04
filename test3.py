a = int(input("Enter a number: "))
b = 1
c = 0
for i in range(1, a):
    for j in range(0, b):
        print(i ,"+", c)
        c = c + i
        print(c)