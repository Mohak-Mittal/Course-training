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
    print("pow of ",i,"is ",b[-1])
print (b)
for j in b:
    if j == b[-1]:
        print(j, end=" ")
    else:
        print(j,"+", end=" ")
    c = c + j
print("=",c)
