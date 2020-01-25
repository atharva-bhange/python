'''
Write a Python program that returns the next largest number that can be created from the
same digits as the input.


Examples
next_number(19) ➞ 91
next_number(3542) ➞ 4235
next_number(5432) ➞ 5432
next_number(58943) ➞ 59348

Notes
If no larger number can be formed, return the number itself.
'''
import itertools

num = list(input("Enter the number:- "))
tupnum = ()
for t in num:
    num[num.index(t)] = int(t)
tupnum = tuple(num)
smallest = None
for t in itertools.permutations(num, len(num)):
    if t > tupnum :
        if smallest == None:
            smallest = t
        elif t < smallest:
            smallest = t
if smallest == None:
    smallest = tupnum
for t in smallest:
    print(t , end='')
