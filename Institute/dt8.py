#functions

def add(a,b):
    print (a+b)

a = int(input("e\n"))
b = int(input("e\n"))
add(a,b)

def sub(**kwargs):
    print("hi",kwargs)
sub(name ='mohak')

def a(*args):
    print(*args)
a(12,32,34,45,56,67)