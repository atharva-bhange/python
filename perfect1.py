'''
Perfect Numbers
The Perfect numbers are the numbers which can be expressed as the sum of
all its factors including 1 and excluding the number itself.

1.Write a python code to print all the perfect numbers between 1 to 9999.
2.Write a python code to check whether input is perfect number or not.
You may increase the range as needed...
'''
pnumbers = list()
num = int(input("Enter the number:- "))
cal = 1
for t in range(2,num):
    for n in range(2,t):
        if (t%n == 0):
            cal = cal + n
            if (cal > t):
                cal = 0
                break
    if (cal == t ):
        pnumbers.append(t)
print(pnumbers)
