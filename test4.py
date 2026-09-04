a = int(input("Enter a number: "))
b =[]
c = 0
d = 1
for k in range (1, a+1):
    if k == a:
        print (k, end=" ")
    else:
        print (k,"X", end=" ")
    d = d * k
print("=",d)
for i in range(1, a+1):
    b.append(pow(i, 2))
print (b)
for j in b:
    c = c + j
print(c)
