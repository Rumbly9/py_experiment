fHandPrompt = input("What is the name of the file that you want to open?\n>>>")
# lookForPrompt = input("What are you looking for?\n>>>")

try :
    fHandler = open(fHandPrompt)
except :
    print("Sorry, we can't find the file that you are looking for. Please try again.")
    quit()
    
counter = 0
for line in fHandler :
    line = line.rstrip()
    #---email finder---#
    if line.startswith("From:") :
        splitter = line.split()
        senderEmail = splitter[1]
        senderSplitter = senderEmail.split("@")
        senderDomain = senderSplitter[1]
        print(f"The sender is: {senderEmail}\nfrom domain: {senderDomain}\n")
    # if lookForPrompt in line.lower() :
    #     counter = counter + 1
    #     print(line)
# print(f"There are {counter} lines of {lookForPrompt} in {fHandPrompt}")