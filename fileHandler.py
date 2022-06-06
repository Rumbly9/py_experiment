fHandPrompt = input("What is the name of the file that you want to open?\n>>>")
lookForPrompt = input("What are you looking for?\n>>>")

try :
    fHandler = open(fHandPrompt)
except :
    print("Sorry, we can't find the file that you are looking for. Please try again.")
    quit()
    
counter = 0
for line in fHandler :
    line = line.rstrip()
    if lookForPrompt in line.lower() :
        counter = counter + 1
        print(line)
print("There are", counter, "lines of", lookForPrompt, "in", fHandPrompt)