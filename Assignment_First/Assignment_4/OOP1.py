class method:
    def add(self,*args):
        return sum(*args)

m = method()
a = []
b = int(input("Enter numbers to add : "))
for i in range(b):
    a.append(int(input(f"Enter number {i+1} to add : ")))
print(m.add(a))