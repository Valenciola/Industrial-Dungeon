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
waittime = 0


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
print("It's really dark here...")
time.sleep(2)
print("Oh, hold on... There's someone else! Hey! How did you get here?\n")


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
'''
name = input("Enter your name: ")
print("\nYour name is...")
time.sleep(2)
print(name + "?")

choice = 0
while (int(choice) < 1 or int(choice) > 2):
    choice = input("\n|1. Yes.| 2. No. | 3. What? | : ")
    print("--------")
    if int(choice) == 1:
        print("Cool! Nice to meet you, " + name + "!")
    elif int(choice) == 2:
        print("\nOh, my bad. What was it again?")
        name = input("Enter your name: ")
        print("\nOh, so it's " + name + ". Got it!")
    elif int(choice) == 3:
        print("-> Type the number of your choice.")
    else:
        print("Come again?")

print("\nI'm the narrator. In other words, I control the story here. However...")
time.sleep(2)
print("I don't think it would be fair to force you into anything, " + name + ", so I think I'll give you some say in what happens.")
time.sleep(2)
print("Now, I think we should really get a move-on. I have three places in mind where we can go to, but you might want to prepare yourself first.")
time.sleep(2)
print("Are you ready now?")

choice = 0
waittime = 0
while (int(choice) < 1 or int(choice) > 2):
    choice = input("\n|1. Yes! | 2. No... | 3. How should I answer this? | : ")
    print("--------")
    if int(choice) == 1:
        print("Awesome! Let's go!!!")
    elif int(choice) == 2:
        print("Okay, then, how long should I give you?")
        waittime = input("Enter the time in seconds: ")
        print("Okay, " + waittime + " seconds until our departure, " + name + "!")
        time.sleep(int(waittime))
        print("\nAlright! It's been " + waittime + " seconds!") 
    elif int(choice) == 3:
        print("-> Type the number of your choice.")
    else:
        print("I don't understand... Maybe I should ask again?")