# Q13. Write a program using a while loop that keeps asking a warehouse staff member to enter
# product codes until they type 'DONE'. Count how many valid product codes (assume any
# 6-character alphanumeric string is valid) were entered.

b = 0
print ("Enter done To Exit")
a = str(input("Enter Product Key\n"))
while a != 'done':
    a = str(input("Enter Product Key\n"))
    if len(a)==6 and a.isalnum():
        b = b + 1
print ("Valid Product Codes Are : ",b)
