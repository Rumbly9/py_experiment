fileHandler = open("romeo.txt")

# unique words finder

cont = list()
for line in fileHandler :
    line = line.rstrip()
    splitter = line.split()
    for word in splitter :
        if not word in cont :
            cont.append(word)
cont.sort()
print(cont)