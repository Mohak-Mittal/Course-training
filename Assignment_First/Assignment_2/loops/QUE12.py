# Q12. The warehouse receives daily stock counts for 7 days in a week. Using a loop,
# calculate the total, average, and the day (1-7) with the highest stock received.
b = 0
c = 0
avg = 0
for i in range (1,8):
	a = int(input(f"Enter day {i} stock\n"))
	c = c + a
	if b < a:
		b = a
		d = i
avg = c/7
print (f"day {d} has most stock")
print (f"Total Stock is : {c}")
print (f"average of storck is : {avg}")