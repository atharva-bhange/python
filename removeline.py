file = open(input("name")+".txt", 'r')
newfile = open("result.txt", 'w')
for line in file:
	newfile.write(line[:len(line)-1])
