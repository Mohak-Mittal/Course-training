# Q10. Build a grading system:
# marks >= 90 -> 'A+',
# >= 75 -> 'A',
# >= 60 -> 'B',
# >= 40 -> 'C',
# else -> 'Fail'.
# Additionally, if the student scored 100, print a special "Topper of the Year" message.

print("Grading System\nmarks == 100 -> 'topper' \nmarks >= 90 -> 'A+',\nmarks >= 75 -> 'A',\nmarks >= 60 -> 'B',\nmarks >= 40 -> 'C',\nelse -> 'Fail'.")
a = int(input("Enter Your Marks\n"))
if a == 100:
    print("Topper Of The Year")
elif a >= 90:
    print("A+")
elif a >= 75:
    print("A")
elif a >= 60:
    print("B")
elif a >= 40:
    print("C")
else:
    print("Fail")