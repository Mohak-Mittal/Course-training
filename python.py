#1 create a tuple containing three fruits
a = ("apple", "banana", "cherry")

#2 print the first element of the tuple
a = (10,20,30,40, 50)
print(a[0])

#3 print the last element of the tuple
colour =("red", "green", "blue")
print(colour[-1])
#or
print(colour[2])

#4 find the length of the tuple
animals = ("cat", "dog", "rabbit")
print(len(animals))

#5 create a tuple containing your name , age , city
person: tuple[str, int] = ("Mohak", 22, "Punjab")
print(person)

#6 print the second element
student = ("Rahul", "Aman" , "Ravi")
print(student[1])

#7 check if "apple" is present in the tuple
fruits = ("apple", "banana", "cherry")
if "apple" in fruits:
    print("Yes, 'apple' is in the tuple")
#or
print("apple" in fruits)

#8 count how many times 10 appears in the tuple
number: tuple[int] = (10, 20, 30, 10, 40, 10)
print(number.count(10))

#9 find the index/position of 'mango' in the tuple
fruits = ("apple", "banana", "cherry", "mango")
print(fruits.index("mango"))

#10 creat a tuple containing number fro 1 to 5
numbers: tuple[int] = (1, 2, 3, 4, 5)
print (numbers)

#11 print all elemnts using for loops
num: tuple[int] = (1, 2, 3, 4, 5)
for i in num:
    print(i)

#12 add all the numbers in the tuple
n: tuple[int] = (1, 2, 3, 4, 5)
print(sum(n))

#13 find the maximum number in the tuple
nu :tuple[int] = (17, 52, 30, 94, 55)
print(max(nu))

#14 find the minimum number in the tuple
Nu : tuple[int] = (17, 52, 30, 94, 55)
print(min(Nu))

#15 convert this list into a tuple
fru :list[str] = ["apple" , "banana" , "mango"]
b = tuple(fru)

#16 convert this tuple into list
Fru :tuple[str] = ("apple" , "banana" , "mango")
B = list(Fru)

#17 join this 2 tuples
a = (1 , 2 , 3)
b = (4 , 5 , 6)
c= a+b
print(c)

#18 print the first 3 elements
nUm = (10 , 20 , 30 , 40 , 50)
for i in range (0,3):
    print(nUm[i])

#19 print the last 2 elements
NUM = (10 , 20 , 30 , 40 , 50)
for i in range (3,5):
    print(NUM[i])

#20 create a tuple containing 5 student names and print them using a for loop
names = ("Alice", "Bob", "Charlie", "David", "Eva")
for name in names:
    print(name)