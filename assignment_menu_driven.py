def find_total(marks):
    total = 0
    for mark in marks:
        if mark != -1:
            total += mark
    return total


def find_average(marks,absent):
    t = find_total(marks)

    # considering absent
    if absent:
        return t / n
    # not considering absent
    else:
        return t / (n - find_absent_student(marks))


def find_min(marks):
    minimum = None
    for mark in marks:
        if mark != -1:
            if minimum == None:
                minimum = mark
            elif mark < minimum:
                minimum = mark

    return minimum

def find_max(marks):
    maximum = marks[0]
    for mark in marks:
        if mark > maximum:
            maximum = mark

    return maximum

def print_marks(marks):
    print("Marks: ")
    for mark in marks:
        print(mark)

def find_highest_frequency(marks):
    number = []
    frequency = []

    ## Setting frequency of each number
    for mark in marks:
        if mark != -1:
            if mark not in number:
                number.append(mark)
                frequency.append(1)
            else:
                index = number.index(mark)
                frequency[index] += 1

    ## Finding marks with highest frequency                
    maximum_index = None
    for i in range(len(frequency)):
        if maximum_index == None:
            maximum_index = i
        elif frequency[i] > frequency[maximum_index]:
            maximum_index = i

    return number[maximum_index]


def find_absent_student(marks):
    no_absent = 0
    for mark in marks:
        if mark == -1:
            no_absent += 1

    return no_absent

## MAIN CODE    

n = int(input("Number of students: "))
# displaying menu

marks = []
for _ in range(n):
    marks.append(int(input("Input marks: ")))

print("Menu")
print("1) Average considering absent students")
print("2) Average not considering absent students")
print("3) Maximum marks")
print("4) Minimum marks")
print("5) Absent Students")
print("6) Marks with highest frequency")
print("7) Print all marks")

while True:
    option = int(input("Enter menu option you want: "))

    if option == 1:
        print("Average considering absent student",find_average(marks,True))
    elif option == 2:
        print("Average not considering absent student" , find_average(marks, False))
    elif option == 3:
        print("Maximum marks",find_max(marks))
    elif option == 4:
        print("Minimum marks" , find_min(marks))
    elif option == 5:
        print("Absent students are", find_absent_student(marks))
    elif option == 6:
        print("Marks with highest frequency" , find_highest_frequency(marks))
    elif option == 7:
        print_marks(marks)
    elif option == -1:
        break
    else:
        print("Invalid option")

