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
            nums.append(random.randint(0,20))
        break
    else:
        print("Type a number or 'done' to view results.")
print(nums)
print("")
loopcounterout = 0
loopcounterin = 0


# main algorithm
for index in range(len(nums)):
    loopcounterout +=1
    sample = index
    t= sample - 1
    while t>0:
        loopcounterin += 1
        if nums[t] > nums[sample]:
            temp = nums[t]
            nums[t] = nums[sample]
            nums[sample] = temp
            sample -= 1
        t -= 1
print(nums)
print(loopcounterin+loopcounterout , 'loops were required for insertion sort.')
