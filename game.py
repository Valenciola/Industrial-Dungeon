# Welcome to the code for the game! I like to comment a lot so feel free to look around and see the beautiful monstrosity I've come up with...

# Self notes: we don't use semicolons here ;-; 

# Some preprocessor directives
import time # Allows the program to wait (for dramatic effect)

# Variables
currency = 50
bag = []
health = 100
statnames = ["Strength", "Luck", "Stamina"]
statvalues = ["10", "0", "20"]
name = "Unknown"
choice = 0
waittime = 0
storyline = 0
room = 0

'''
# Intro
print("--------")
print("...")
time.sleep(2)
print("A story told in Python...")
time.sleep(2)
print("Narrator et Toi...")
time.sleep(2)
print("Also known as *Terminal Narrator*")
print("--------")
'''

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

name = input("\nEnter your name: ")
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
time.sleep(3)
print("I don't think it would be fair to force you into anything, " + name + ", so I think I'll give you some say in what happens.")
time.sleep(3)
print("Now, I think we should really get a move-on. I have a place in mind where we can go to, but you might want to prepare yourself first.")
time.sleep(3)
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
        print("\nAlright! It's been " + waittime + " seconds! Let's go!!!") 
    elif int(choice) == 3:
        print("-> Type the number of your choice.")
    else:
        print("I don't understand... Maybe I should ask again?")


# Scene 1 To the Dungeon Office!
storyline = 1

time.sleep(2)
print("\n-----------------------------")
print("~~~Into the Story~~~")
print("-----------------------------")
time.sleep(3)
print("\nIt's 7 in the morning. The sky is still finding its way back to the usual bright blue from the indigo darkness.")
time.sleep(5)
print("It's nice to think that a blue sky is something that everyone thinks is normal. After all, " + name + " could use a break from all the surrounding abnormal normalities...")
time.sleep(5)
print("Oh. Who's " + name + "? Just an office worker...")
time.sleep(3)
print("...In the Industrial Dungeon. Home to many of the most mind-blowing fantastical creatures!")
time.sleep(5)
print("Yes, here, dragons and trolls and goblins and all sorts of different creatures exist! And many of them are truly a sight to behold...")
time.sleep(6)
print("However, " + name + " does not behold them on a daily basis. Why? Because " + name + " works in the public relations department.")
time.sleep(3)
print("In other words, " + name + " keeps people from getting mad or overly sensitive about things relating to the fantastical creatures.")
time.sleep(4)
print("It's a boring job, but " + name + " thinks that it pays well, so what else can be done?")
time.sleep(5)
print("Anyhow, " + name + " arrives to work and heads to the familiar desk. It's time to get to work!")
time.sleep(3)
print(" -> You'll need your task folder. It's in your locker...")
time.sleep(5)

choice = 0
while (int(choice) != 3:
    time.sleep(2)
    print("\nWhat would you like to do?")
    choice = input("| 1. Check your desk | 2. Check your bag | 3. Go to your locker | 4. HELP | : ")
    print("--------")
    if int(choice) == 1:
        print(name + " checks the desk. It's adorned with some pictures of the things that " + name + " really likes.")
    elif int(choice) == 2:
        if len(bag) == 0:
            print("Your bag is empty!")
        else:
            print("Contents of the bag: ")
            for x in range (len(bag)):
                print(x + ".: " + bag[x])
    elif int(choice) == 3:
        storyline = 2
    elif int(choice) == 4:
        print(" -> Enter the number of your choice")
    else:
        print("This isn't one of the options...")