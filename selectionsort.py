print('\n')
print("-------------------------------------------------------")
print("NOTE :-")
print("Enter a number to input a number one by one and then press enter")
print("After you are done inputing number type 'done' to start sorting.")
print("If you want random number generation type 'random19' 19 number shows")
print("how many random number you want.")
print("-------------------------------------------------------")
print("\n")

import random

nums = []

while True:
    num = input("Enter Number:- ")
    if num.isnumeric():
        nums.append(int(num))
    elif num == 'done':
        break
    elif num.startswith('random'):
        for t in range(int(num[6:])):
            nums.append(random.randint(0,10000000000))
        break
    else:
        print("Type a number or 'done' to view results.")
loopcounter =0
min = None # storing index not actual value
print(nums)
print("")
for shifter in range(0,len(nums)):
    loopcounter += 1
    for checker in range(shifter , len(nums)):
        loopcounter += 1
        if min == None:
            min = checker
        if nums[checker]<nums[min]:
            min = checker
    temp = nums[shifter]
    nums[shifter] = nums[min]
    nums[min] = temp
    min = None
print(nums)
print(loopcounter)
