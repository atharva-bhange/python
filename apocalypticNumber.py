num = int(input("Enter number to be tested:- "))
cal = str(2**num)
count = cal.count("666")
if count ==0:
	print("Safe")
elif count == 1:
	print("Single")
elif count == 2:
	print("Double")
elif count ==3:
	print("Triple")
else:
	print("More than three.")