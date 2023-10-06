# Welcome to the code for the game! I like to comment a lot so feel free to look around and see the beautiful monstrosity I've come up with...

# Self notes: we don't use semicolons here ;-; 

# Some preprocessor directives
import time # Allows the program to wait (for dramatic effect)

# Variables
currency = 50
bag = ["Empty!"]
health = 100
statnames = ["Strength", "Luck", "Stamina"]
statvalues = ["10", "0", "20"]
name = "Unknown"
choice = 0

'''
# Intro
print("--------")
print("...")
time.sleep(2)
print("A story told in Python...")
time.sleep(2)
print("Narrator et Toi...")
time.sleep(2)
print("Also known as *Terminal Narrator!*")
print("--------")

# Prologue (yes, they're different here)
time.sleep(2)
print("...")
time.sleep(2)
print("It's really dark... How did you end up here?\n")
'''

choice = 0
while (int(choice) < 1 or int(choice) > 3):
    choice = input("|1. I don't know... | 2. I... uh... | 3. I opened a file on my computer...| 4. How do I...?| : ")
    print("--------")
    if int(choice) == 1:
        print("Oh... I'll be honest, I don't know either.")
        print("\nDo you at least know your name?")
    elif int(choice) == 2:
        print("You seem just as confused as I am...")
        print("\nMaybe we should start with a more basic question. What's your name?")
    elif int(choice) == 3:
        print("A file on a computer? Huh...")
        print("\nAnyways, I probably shouldn't ask further into that question. But, I would like to know, what is your name?")
    elif int(choice) == 4:
        print("-> Type the number of your choice.")
    else:
        print("\nSorry, I don't think I got that. Come again?")

name = input("Enter your name: ")
print("\nYour name is...")
time.sleep(2)
print(name + "?")

choice = 0
while (int(choice) < 1 or int(choice) > 3):
    choice = input("\n|1. Yes.| 2. No. | 3. What? | : ")
    print("--------")
    if int(choice) == 1:
        print("Cool! Nice to meet you, " + name + "!")
    elif int(choice) == 2:
        print("\nOh, my bad. What was it again?")
        name = input("Enter your name: ")
        print("Oh, so it's " + name + ". Got it!")
    elif int(choice) == 3:
        print("-> Type the number of your choice.")
    else:
        print("Come again?")