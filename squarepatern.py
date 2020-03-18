'''
Prob. No. 12
1.Write a program to display this type.

01  02  03  04  05
16  17  18   19  06
15  24  25  20  07
14  23  22  21  08
13  12  11  10   09
*We are type the number (ie. We type number 5)
'''
i =0
j =0

def refresh():
    global number
    global prefix
    if number > 9 :
        prefix = ""

matrix = []
colm = []

num = int(input("Patern of size"))
size = int(num ** 0.5)
check = (num ** 0.5) - size

if check != 0 :
    print("Input number should be square number.")
    quit()

for k in range(size):
    matrix.append([])
for t in range(len(matrix)):
    for l in range(size):
        matrix[t].append("")

number = 1
prefix = "0"
while i == 0 and j < size:
    matrix[i].remove("")
    matrix[i].insert(j,prefix+str(number))
    j+=1
    number += 1
j -= 1
i += 1
refresh()
while j == size -1 and i < size:
    refresh()
    matrix[i].pop(j)
    matrix[i].insert(j,prefix+str(number))
    i+=1
    number += 1
i -= 1
j -=1
refresh()
while i == size -1 and j>=0:
    refresh()
    matrix[i].pop(j)
    matrix[i].insert(j,prefix+str(number))
    j-=1
    number += 1
j += 1

refresh()
while j == 0 and i>0:
    refresh()
    matrix[i].pop(j)
    matrix[i].insert(j,prefix+str(number))
    i-=1
    number += 1


print(matrix)


#print(matrix)
print(number)
print("i is " ,i)
print("j is " , j)
