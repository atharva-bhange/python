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
def swap(i1 ,i2):
    nums.insert(i1 , nums[i2])
    nums.pop(i2+1)

nums = []

while True:
    num = input("Enter Number:- ")
    if num.isnumeric():
        nums.append(int(num))
    elif num == 'done':
        break
    elif num.startswith('random'):

        for t in range(int(num[6:])):
            nums.append(random.randint(0,10000))
        break
    else:
        print("Type a number or 'done' to view results.")
print(nums)
check = 0
loopcounter =0
while True:
    loopcounter += 1
    for t in range(len(nums)):
        if t+1 <=len(nums)-1:
            if nums[t+1] < nums[t]:
                swap(t , t+1)
                check += 1
    if check  ==0  :
        break
    check =0
print(nums)
print(loopcounter, 'loops were required for sorting.')
