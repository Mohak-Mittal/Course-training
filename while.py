a = str(input("Enter a name: "))
b = int(input("Enter roll no: "))
if b == 1:
    a = { "Math": 50, "Science": 60, "English": 80, "History": 70, "Physics": 85 }
elif b == 2:
    a = { "Math": 90, "Science": 50, "English": 67, "History": 86, "Physics": 94 }

for subject, marks in a.items():
    if marks >= 90:
        print(f"{subject}: A")
    elif marks >= 60:
        print(f"{subject}: B")
    elif marks >= 40:
        print(f"{subject}: C")
    else:
        print(f"{subject}: F")
