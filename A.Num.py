num = input('Armstrong numbers before which number to calculate?')
try:
    num = int(num)
except:
    print('Input in not a number!')
    quit()
if num>9999999999:
    print('Finding Armstrong numbers in such big range can take very long!')
    quit()
numbers = list()
count = 1
while count<=num:
    index=0
    calculation = 0
    num_str = str(count)
    str_len = len(num_str)
    while index<=str_len-1:
        str_digit = num_str[index]
        int_digit = int(str_digit)
        calculation = calculation + int_digit**3
        index = index+1
    if(calculation == count):
        numbers.append(count)
    count = count+1
print('The Armstrong numbers between 1 to '+str(num)+' are:')
for values in numbers:
    print(values)
