'''
Problem No. 36
Task:
Create a program to take input a array of numbers and required sum.
Now you have to print the lowest two numbers from the array which sums to the required sum given as input.

Sample :-

input = [10,0,-1,20,25,30]
Required Sum = 45
output = [20,25]
'''
counter = 0
ls = []
req_sum = int(input("What is required sum? "))
while True:
    num = input("Enter the number:-")
    if num == "done":
        break
    ls.append(int(num))
    counter +=1
ls.sort()
loopcounter =0
output = []
for index_num1 in range(counter):
    loopcounter += 1
    for num2 in ls[index_num1+1:]:
        loopcounter += 1
        cal = num2 + ls[index_num1]
        if cal == req_sum:
            output.append(ls[index_num1])
            output.append(num2)
            index_num1 = counter+1
            break
print(output)
print(loopcounter)
"""
Time Complexity
O(n^2)
n(n-1)/2
I think so but not sure would like to get feedback on this.
"""
