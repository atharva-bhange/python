def checkprime(number):
    truth = None
    if number == 2 :
        truth = True
        return truth
    for t in range(2,number):
        if number % t == 0:
            truth = False
            break
        elif number % t != 0 :
            truth = True
            continue
    return truth
num = int(input("What is the number? "))
pf = list()
for t in range(2 , num+1):
    if checkprime(t) == True:
        while num%t == 0 and num > 1:
            num = num/t
            pf.append(t)
print(pf)
