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
#import timer
nums = []

while True:
    num = input("Enter Number:- ")
    if num.isnumeric():
        nums.append(int(num))
    elif num == 'done':
        break
    elif num.startswith('random'):
        for t in range(int(num[6:])):
            nums.append(random.randint(0,10000000000000000))
        break
    else:
        print("Type a number or 'done' to view results.")
originalnums = nums

# BUBBLE SORT

def swap(i1 ,i2):
    nums.insert(i1 , nums[i2])
    nums.pop(i2+1)
#print(nums)
check = 0
loopcounterout =0
loopcounterin = 0
while loopcounterout<len(nums)-1:
    loopcounterout += 1
    for t in range(len(nums)-1):
        loopcounterin += 1
        if nums[t+1] < nums[t]:
            swap(t , t+1)
            check += 1
    if check  ==0  :
        break
    check =0
#print(nums)
print(loopcounterout+loopcounterin, 'loops were required for sorting using bubble sort.')

nums = originalnums

# selection SORT

loopcounter =0
min = None # storing index not actual value

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

print(loopcounter  , 'loops were required by selection sort')
