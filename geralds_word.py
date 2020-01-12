word = input("Input the word:- ")

letter_list = list()
for t in list(range(len(word))):
    letter_list.append(word[t])

for t in list(range(len(letter_list)-1)):
    if (letter_list[t] == letter_list[len(word)-1]):
        new_checkindex = t-1
        index_counter = 0
        degree = 1
        while new_checkindex >=0:
            if (letter_list[new_checkindex] != letter_list[len(word)-1-1-index_counter] ):
                bool = False
                break
            else:
                degree = degree +1
            index_counter = index_counter + 1
            new_checkindex = new_checkindex -1
        if (degree == t+1):
            bool = True

if (bool == True):
    print("It is a Garals's Word with degree "+str(degree))
else :
    print("It is not a Gerald's Word")
