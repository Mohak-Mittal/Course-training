# Q14. Using nested loops, print a warehouse "rack map" of size R rows x C columns (take R
# and C as input), where each cell shows its rack ID in the format R1-C1, R1-C2, etc. Use
# loop control statements (break/continue) to skip and not print any rack marked as "under
# maintenance" (hardcode 2-3 such racks).

a = int(input("Enter Number Of Rows\n"))
b = int(input("Enter Number Of Columns\n"))
for i in range (1 , a+1):
    for j in range (1 , b+1):
        if i == 3 and j == 1: # 3rd row only 1st column is under maintanence
            continue
        if i == 1 and j == 3: # 1st row 3rd and rest of the column is under maintanence
            break
        if i ==2 and j == 3:  # 2nd row 3rd and rest of te clumn are under maintanence
            break
        print (f"R{i}-C{j}")

