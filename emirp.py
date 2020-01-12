def swap(number):
    num_string = str(number)
    x = len(num_string)-1
    new_string = ""
    while x >=0 :
        new_string = new_string+num_string[x]
        x= x -1
    new_string = int(new_string)
    return new_string

def checkprime(number):
    if (number % 2 == 0 ):
        return False
    else :
        for t in list(range(number)):
            if (t > 2):
                if (number % t == 0):
                    return False
                elif (number % t != 0):
                    continue
    return True

try :
    num = int(input("Type the number:- "))
    truth = True
except :
    truth = False

if truth == False :
    print("Please input a number only!")
else:
    if (checkprime(num) == True):
        if (checkprime(swap(num)) == True):
            print("This is a Emirp Number!")
        else:
            print("Not Emirp Number!")
    elif (checkprime(num) == False):
        print("Number Entered is Not Prime!")
