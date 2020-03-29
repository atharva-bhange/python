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

num = int(input("Patern of size:- "))
size = num ** 0.5

if size - int(size) != 0  :
    print("Input number should be square number.")
    quit()
size = int(size)
prefix = '0'
## Creating Empty matrix
matrix = []
for i in range(size):
    matrix.append([])
    for j in range(size):
        matrix[i].append("")
counter = 1
#

def check(cnt):
    global prefix
    global num
    if cnt >= num:
        return
    if cnt >= 10:
        prefix = ""

def cycle(i_given , j_given , level):
    global size
    global matrix
    global counter
    i = i_given
    j = j_given
    while  j <= size-1-level:
        matrix[i][j] = prefix+str(counter)
        counter+=1
        check(counter)
        j+=1
    j-= 1
    i +=1
    while i <= size-1-level:
        matrix[i][j] = prefix+str(counter)
        counter +=1
        check(counter)
        i+=1
    i-= 1
    j-=1
    while j>=0+level:
        matrix[i][j] = prefix+str(counter)
        counter +=1
        check(counter)
        j -= 1
    j+= 1
    i-= 1
    while i >=0+level+1:
        matrix[i][j] = prefix+str(counter)
        counter += 1
        check(counter)
        i -= 1
    i += 1

i = 0
j = 0
l = 0
while counter <=num:
    cycle(i,j,l)
    i+=1
    j+=1
    l+=1

## printing matrix
for i in range(size):
    for j in range(size):
        print(matrix[i][j],"" , end = "")
    print("")
