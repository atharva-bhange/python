x = input("Input String:- ")
len = len(x)
small_len = len -1
new_string = ""
new_string = new_string+x[len-1]
for t in list(range(small_len)):
    new_string = new_string+x[t]
print(new_string)
