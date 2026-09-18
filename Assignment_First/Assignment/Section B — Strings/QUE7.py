# Q7. Given a customer's phone number as a string, mask all digits except the last 4,
# e.g. "9876543210" -> "******3210". This is used for order confirmation SMS previews.

num = "9876543210"
mask_num = ""
for i in range (0,len(num)):
    if i >= len(num) - 4:
        mask_num = mask_num + num[i]
    else:
        mask_num = mask_num + "*"
print(mask_num)

