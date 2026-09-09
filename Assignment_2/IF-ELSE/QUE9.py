# Q9. A student is eligible for a scholarship if attendance >= 75% AND
# (marks >= 85 OR is_sports_captain is True). Write a program that takes
# these three inputs and prints whether the student is eligible.

a = int(input("Enter Your Attendence\n"))
b = int(input("Enter Your Marks\n"))
c = str(input("Are You In Any Games? Yes or No?\n"))
if a >= 75 and b >= 85:
    print("Eligible For Scholarship")
elif c == 'yes':
    print("Eligible For Scholarship")
else:
    print("Not Eligible")