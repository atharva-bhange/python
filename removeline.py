name = input("name")+".txt"
file = open(name, 'r')
ls = list(file.read().split("\n"))
file.close()
file = open(name, 'w')

for t in ls:
	file.write(t)

'''
newfile = open("result.txt", 'w')

for line in file:
	newfile.write(line[:len(line)-1])
'''
