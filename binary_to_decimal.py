'''
# Binary to Decimal Converter

Take any Binary number as input and
convert it to Decimal number.
Remember that validating the input
is also a main segment of code...validate
the input for only binary numbers in this case.
'''

bin = list(input("Input Binary num:- "))
bin = bin[::-1]
multiplier = [1]
for t in range(1, len(bin)+1):
    multiplier.append(2**t)
cal = 0
for t in range(0,len(bin)):
    cal = cal + (int(bin[t])*int(multiplier[t]))
print(cal)
