'''
# Number In Words
Take any number as input and print its digits in words as output
E.g. input - 136
        Output - one three six
'''
str = ""
convert = {'1' : "one",'2' : "two", '3' : "three",'4' : "four", '5':"five" , '6' : "six" , '7' : "seven" , '8' : "eight" , '9': "nine"}
num = list(input("type the number:- "))
for t in num:
    str = str+" "+convert[t]
print(str)
# changes
