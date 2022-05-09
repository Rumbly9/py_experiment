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
cont = 0
for i in numbers :
    if cont < i :
        cont = i
print("The largest number is", cont)

len(numbers)