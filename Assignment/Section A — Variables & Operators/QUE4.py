# Q4. Write a program to swap the "cash balance" and "card balance" of
#  a customer'swallet without using a third/temporary variable,
#  using arithmetic operators.

a = 1000
b = 5000
print(f" cash {a} card {b}")
a = a+b
b = a-b
a = a-b
print(f" cash {a} card {b}")