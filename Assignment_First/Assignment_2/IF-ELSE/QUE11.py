# Q11. A ride-booking feature at BrightPath's transport wing charges fare based
# on time of day: Peak hours (8-10 AM, 6-8 PM) add a 20% surcharge; late night
# (11 PM-5 AM) adds a 15% night charge; otherwise, normal fare applies. Write
# nested if-else logic to compute the final fare for a given hour (24-hr format)
# and base fare.

a = int(input("Enter Your Time In 24-hr Formet\n"))
b = 100
f = 0
s = 0
if a >= 6 and a <= 22:
    if a >= 8 and a <= 10:
        s = b * 20/100
        f = b + s
        print(f)
    elif a >= 18 and a <= 20:
        s = b * 20/100
        f = b + s
        print(f)
    else:
        print(b)
else:
     s = b * 15/100
     f = b + s
     print(f)
