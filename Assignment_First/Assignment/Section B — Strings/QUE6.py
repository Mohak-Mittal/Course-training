# Validate a customer's email input by checking (using string methods only, no regex)
# whether it contains exactly one '@' symbol and ends with '.com'. Print whether the
# email is valid.

Email = input("Enter Your Email\n")
a = (Email.find("@"))
b = (Email.find(".com"))
if a > 0 and b > 0:
    print("Varified Email")
else:
    print("Wrong Email")