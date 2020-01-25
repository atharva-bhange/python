'''
Print this pattern

AbC0
dEf1
GhI2
jKl3
MnO4
pQr5
StU6
vWx7
YzY8
xWv9
UtS0
rQp1
OnM2
lKj3
IhG4
fEd5
CbA6
'''
string1 = list()
for x in range(97 , 123):
    if (x % 2 != 0):
        string1.append(chr(x).upper())
    else :
        string1.append(chr(x).lower())
string2 = string1[::-1]
string2.pop(0)
string = string1 + string2
counter = 0
escape = 0
for t in string:
    if escape <3:
        print(t , end = '')
        escape += 1
        if escape >3:
            escape =0
    elif escape == 3:
        print(counter)
        print(t,end ='')
        escape = 1
        counter += 1
        if counter > 9:
            counter = 0
print(counter)
