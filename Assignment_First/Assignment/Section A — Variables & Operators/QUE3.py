# Q3. A delivery partner's salary depends on base pay +
# (distance_km * rate_per_km) deductions. Using assignment operators
#  (+=, -=, *=), simulate three days of pay updates for a single
#  variable representing weekly earnings.

Base_Pay = 500
Rate_Per_KM = 6
deduct = 200
Weekly_Pay = 0
Distance_Pay = 0
for i in range (1,4):
    Distance = int(input(f"enter day {i} Distance \n"))
    Distance *= Rate_Per_KM
    Today_Pay = Base_Pay + Distance
    print (f"day {i} pay = {Today_Pay}")
    Weekly_Pay +=  Today_Pay
Weekly_Pay -= deduct
print(Weekly_Pay)