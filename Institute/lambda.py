a = lambda x:x*2
print (a(2))

b = [1,2,3,4,5]
c = list(map(lambda x:x*2,b))
print(c)
d = list(filter(lambda x:x%2==0,b))
print(d)