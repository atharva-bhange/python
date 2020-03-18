'''
Write a program to display this type.

01  02  03  04  05
16  17  18  19  06
15  24  25  20  07
14  23  22  21  08
13  12  11  10  09

01 02 03
08 09 04
07 06 05

01 02 03 04
12 13 14 05
11 16 15 06
10 09 08 07

01 02
04 03

*We type the number (ie. We type number 5)
'''


try:
    num = int(input("Enter the number:- "))
except:
    num = -1

box = list()
if num > 0:                                                                                                                                                                                                                                                                                                                                                   
    for t in range(num):
        box[t] = list();
        for m in box[t]:
            box[t][m] = ""
print(box`)

else:
    print("Please type an integer greater than 0")
