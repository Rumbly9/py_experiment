import code
from operator import concat


a = 5
b = 10
def math() :
    print(a*b)
math()

def tell_name():
    ask_name = input("What is your name?")
    print("Hello " + ask_name)
tell_name()

# Temperature Conversion
def temp_convert():
    temp_type = input("Convert from what?").lower()
    conv_to = input("To what?").lower()

    if temp_type == "c" :
        if conv_to == "f" :
            ask_temp = input("What's the temperature in Celsius?")
            formula = (int(ask_temp) * 9/5) + 32
            print("The temperature in Fahrenheit is " + str(formula) + " F")
        if conv_to == "k" :
            ask_temp = input("What's the temperature in Celsius?")
            formula = int(ask_temp) + 273.15
            print("The temperature in Kelvin is " + str(formula) + " K")

    if temp_type == "f" :
        if conv_to == "c" :
            ask_temp = input("What's the temperature in Fahrenheit?")
            formula = (int(ask_temp) - 32) * 5/9
            print("The temperature in Celsius is " + str(formula) + " C")
        if conv_to == "k" :
            ask_temp = input("What's the temperature in Fahrenheit?")
            formula = (int(ask_temp) - 32) * 5/9 + 273.15
            print("The temperature in Kelvin is " + str(formula) + " K")

    if temp_type == "k" :
        if conv_to == "c" :
            ask_temp = input("What's the temperature in Kelvin?")
            formula = int(ask_temp) - 273.15
            print("The temperature in Celsius is " + str(formula) + " C")
        if conv_to == "f" :
            ask_temp = input("What's the temperature in Kelvin?")
            formula = (int(ask_temp) - 273.15) * 9/5 + 32
            print("The temperature in Fahrenheit is " + str(formula) + " F")

temp_convert()

# While iters
n = 0
while n < 5 :
    n = n + 1
    print(n)
print ("It's lights out")
print ("AND AWAY WE GO!!!")

while True:
    line = input("> ")
    if line == "done":
        break
    print(line)
print("Done!")

# for iters
for letter in "Bananas":
    print(letter)

fruits = ["Banana", "Grape", "Orange"]
for item in fruits :
    print(item)
    for letter in item :
        print(letter)

for fruit in fruits :
    print("I love", fruit)

# Finding largest number from list
numbers = [12, 3, 55, 23, 19, 79]
cont = None
for i in numbers :
    if cont == None :
        cont = numbers[0]
    else :
        if cont < i :
            cont = i
print("The largest number is", cont)

len(numbers)

# Finding smallest number from list
nums = [32, 55, 34, 66, 15, 23]
cont2 = None
for i in nums :
    if cont2 == None :
        cont2 = nums[0]
    else :
        if cont2 > i :
            cont2 = i
print("The smallest number is", cont2)

# Counting list
numero = [12, 34, 123, 44, 12, 66, 7878, 1]

counter = 0
total = 0
print("Before", counter)

for i in numero :
    counter = counter + 1
    total = total + i
    print(counter, i, total)

print("After", counter, total, total/counter)

# Boolean number finder
numo = [1, 3, 54, 7, 67, 5, 32]
numo2 = [3, 5, 100, 25]
concatList = numo + numo2 #<<<<<<<< This is concatenation of lists
print(concatList)

index = -1
finder = False
for i in numo :
    index = index + 1
    if i == 5 :
        finder = True
        break
print("Found number 5 in numo list at index number", index)

#######################

device = "phone"
print("n" in device)
if "o" in device:
    print("Found it!")

# Finder

item = "laptop"
def item_finder(x) :
    if item.find(x) != -1 :
        print("The letter that you search is at index number", item.find(x))
    elif item.find(x) == -1 :
        print("Sorry, the letter that you search is not in the item")

# Replace

def item_replacer(old, new, count = 99999) :
    return item.replace(old, new, count)

######################

str = "X-DSPAM-Confidence: 0.8475"

dashPos = str.find("-")
endDashPos = str.find("-", dashPos+1)
codeFind = str[dashPos+1 : endDashPos]
print(dashPos, endDashPos, codeFind)

colpos = str.find(":")
tgt = str[colpos+2:]
val = float(tgt)
count = val * 1.23
print(colpos, tgt, count)

str2 = "From: stephen.marquard@uct.ac.za Sat Jan 5"

atPos = str2.find("@")
spacePos = str2.find(" ", atPos)
domainFind = str2[atPos+1 : spacePos]
print(atPos, spacePos, domainFind)

#############################

friends = ["John", "Barbara", "Frank"]

for i in range(len(friends)) :
    friend = friends[i]
    print(f"Hello {friend}!") #<<<<<<<< This is f-strings template literals

#-----making list from scratch-----#

listMaker = list()
listMaker.append("Hello")
listMaker.append(25)
listMaker.append(True)
print(listMaker)
listMaker.insert(1, "Jumbo")
listMaker.reverse()
print(listMaker)

#-----Counting average using list-----#

listCont = list()
while True :
    inpt = input("Enter a number: ")
    if inpt.lower() == "done" :
        break
    val = float(inpt)
    listCont.append(val)
average = sum(listCont) / len(listCont)
print(average)

#-----splitting strings-----#

words = "Hello there, Kenobi"
splitter = words.split() #<<<<< split without splitter annotation will use whitespace as default
print(splitter)