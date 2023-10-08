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
rooms = [0, 0, 0, 0, 0]
quickpro = []

# Delete these resetting tools
name = "Valerie"

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
time.sleep(3)

choice = 0
while int(choice) != 3:
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

print(name + " heads over to the office lockers to get the task folder. But...")
time.sleep(3)
print("Wait a minute! Where's " + name + "'s key?")
time.sleep(3)
print(" -> Hmm... Perhaps the key is in your desk?")

choice = 0
while int(choice) != 1:
    time.sleep(2)
    print("\nWhat would you like to do?")
    choice = input("| 1. Head back your desk | 2. Check your bag | 3. Try to open the locker | 4. HELP | : ")
    print("--------")
    if int(choice) == 1:
        storyline = 3
    elif int(choice) == 2:
        if len(bag) == 0:
            print("Your bag is empty!")
        else:
            print("Contents of the bag: ")
            for x in range (len(bag)):
                print(x + ".: " + bag[x])
    elif int(choice) == 3:
        if ("key" in bag):
            # change storyline here to finish
            break
        else:
            print(name + " tries to open the locker, but it can't be opened without the key, which " + name + " doesn't have.")
    elif int(choice) == 4:
        print(" -> Enter the number of your choice")
    else:
        print("This isn't one of the options...")

print(name + " heads back to the desk in search of the key.")

choice = 0
quickpro = [0]
while int(choice) != 3:
    time.sleep(2)
    print("\nWhat would you like to do?")
    choice = input("| 1. Open some desk drawers | 2. Check your bag | 3. Ask your co-workers | 4. HELP | : ")
    print("--------")
    if int(choice) == 1:
        if quickpro[0] == 1:
            print(name + " opens the desk drawers again, but all of the same stuff is still there. The key is probably not at the desk.")
        else:
            print(name + " opens some desk drawers, but all there is are a few random papers, eraser shavings, and bent staples.")
            quickpro[0] = 1
    elif int(choice) == 2:
        if len(bag) == 0:
            print("Your bag is empty!")
        else:
            print("Contents of the bag: ")
            for x in range (len(bag)):
                print(x + ".: " + bag[x])
    elif int(choice) == 3:
        storyline = 4
    elif int(choice) == 4:
        print(" -> Enter the number of your choice")
    else:
        print("This isn't one of the options...")

print(name + " decides that it might be a good idea to speak to nearby colleagues.")
time.sleep(2)
print(name + " looks around and identifies Sandra, Pieter, and Taro occupying the three nearest desks. Perhaps they know something?")

choice = 0
quickpro = [0, 0, 0]
while int(choice) != 3:
    time.sleep(2)
    print("\nWhat who do you want to talk to?")
    choice = input("| 1. Sandra | 2. Pieter | 3. Taro | 4. No one | 5. HELP | : ")
    print("--------")
    if int(choice) == 1:
        if quickpro[0] == 0:
            print(name + " approaches Sandra, who is applying some lipstick at her desk.")
            time.sleep(2)
            print(name + " hesitates, feeling awkward about interrupting her, but decides to ask anyway.")
            time.sleep(2)
            print(name + " calls Sandra's name, but she doesn't respond, so " +
                name + " just launches right into it and asks about the key.")
            time.sleep(2)
            print("Sandra rolls her eyes and says, \"Oh, " + name +
                "! Has the perfect employee lost something? That's quite a shame, isn't it? Sorry, but I can't help you there.\"")
            time.sleep(2)
            print(name + " bristles at Sandra's disdain, but decides that getting into an argument won't help find the key. So " + name + " walks away.")
            quickpro[0] = 1
        else:
            print(name + " thinks of approaching Sandra again, but realizes that she'll probably be just as helpful as she was last time. Which was not at all.")
    elif int(choice) == 2:
        if quickpro[1] == 0:
            print(name + " heads over to Pieter's desk.")
            time.sleep(2)
            print("When Pieter notices " + name + " heading to him, he looks up and smiles politely.")
            time.sleep(2)
            print("\"Good morning, " + name + "! Do you need something?\" he asks cheerfully.")
            time.sleep(2)
            print(name + " explains the key situation and asks if Pieter knows anything. Unfortunately, he shakes his head and says that he doesn't.")
            time.sleep(2)
            print(name + " thanks Pieter anyway and heads back to the desk.")
            quickpro[1] = 1
        elif quickpro[1] == 1 and quickpro[0] == 1:
            print(name + " considers asking Pieter about the key again, but since he was so much nicer than Sandra, " + name + " decides not to.")
        else:
            print(name + " considers asking Pieter about the key again, but figures that it won't do any good.")
    elif int(choice) == 3:
        storyline = 5
        print(name + " walks up to Taro, thinking he might have an idea about the key.")
    elif int(choice) == 4:
        print(name + " considers just staying at the desk and hoping the key will turn up, but realizes that it likely won't just appear out of thin air. It's probably better to ask for more information...")
    elif int(choice) == 5:
        print(" -> Enter the number of your choice.")
    else:
        print("This isn't one of the options...")

time.sleep(2)
print("\"The key, huh?\" he asks curiously, propping his head on his fists.")
time.sleep(2)
print("\"Nope, haven't seen your key anywhere, " + name + ",\" he says after a moment, much to " + name +"'s disappointment.")
time.sleep(2)
print("\"BUT!\" Taro says suddenly, startling " + name + ". \"I bet it ended up somewhere in the fantastical creature rooms.\"")
time.sleep(2)
print("\"I know that the green elves especially love shiny things around here. Keys are a shiny thing. How about taking a trip into the hall?\"")

choice = 0
while (int(choice) < 1 or int(choice) > 2):
    time.sleep(2)
    print("\nHow will you respond?")
    choice = input("\n|1. \"I guess it's worth a look...\" | 2. \"I don't know...\" | 3. HELP | : ")
    print("--------")
    if int(choice) == 1:
        print("Taro smiles. \"Excellent!\" he exclaims. \"Oh, and why don't you tell me what you find out while you're there? Working in PR can be so boring.\"")
        time.sleep(4)
        print(name + " can't help but smile at Taro's authenticity. " + name + " thanks Taro for his help and heads back to the desk.")
    elif int(choice) == 2:
        print("Taro shrugs and smiles. \"Well, I guess the halls aren't for everyone. But still, I'm betting that you'll find your key in there, " + name + ".\"")
        time.sleep(3)
        print(name + " thanks Taro for the information and heads back to the desk.")
    elif int(choice) == 3:
        print(" -> Enter the number of your choice.")
    else:
        print("This isn't one of the options...")

storyline = 6
time.sleep(2)
print(name + " has now returned to the desk. It seems that Taro's theory is worth investigating. Plus, it could be a lot more fun than dealing with people...")
time.sleep(2)

choice = 0
while (int(choice) != 1):
    time.sleep(2)
    print("\nWhat would you like to do?")
    choice = input("\n|1. Investigate the halls | 2. Do nothing | 3. HELP | : ")
    print("--------")
    if int(choice) == 1:
        print(name + " decides to enter the halls, in search of the prized key.")
        storyline = 7
    elif int(choice) == 2:
        print(name + " decides to just chill at the desk.")
        time.sleep(10)
        print("After about 10 seconds, " + name + " gets bored.")
    elif int(choice) == 3:
        print(" -> Type the number of your chosen action")
    else:
        print("This isn't one of the options...")

time.sleep(2)
print(name + " stands up from the desk and heads to a dark hallway opening. Taro smirks as " + name + " goes.")
time.sleep(2)
print("And so, with a stride of bravery and determination, " + name + " heads into the darkness.")
'''
# Chapter 2
time.sleep(2)
print("\n-----------------------------")
print("~~~Into the Halls~~~")
print("-----------------------------")
time.sleep(3)