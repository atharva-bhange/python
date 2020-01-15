'''
Perfect Numbers
The Perfect numbers are the numbers which can be expressed as the sum of
all its factors including 1 and excluding the number itself.

1.Write a python code to print all the perfect numbers between 1 to 9999.
2.Write a python code to check whether input is perfect number or not.
You may increase the range as needed...
'''
cal = 0
number = int(input("Enter the number to be checked."))
for t in range(1,number):
    if (number%t == 0):
        cal = cal + t
        if (cal > number):
            cal = 0
            break
if (cal == number):
    print("It is a Perfect Number")
else :
    print("It is not a Perfect NUmber")
