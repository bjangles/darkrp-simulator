#!/bin/python3

import os
import random
import string

newGameMessages = [
"At last, you have finally finished downloading sixty gigabytes of content only paid users can access. Your eyes are filled with colors and your ears are overwhelmed with the sound of screaming prepubescent children. The world is your oyster.",
"You have finally arrived in the promised land. It's a shame, though. You were just starting to like that Scary Monsters & Nice Sprites remix played at full volume.",
"34 minutes and 12 seconds later. If only you had more time, you could've memorised the rules!",
"Woah! You totally forgot you were joining a server. Now it's time to stop forgetting and start regretting.",
]

misunderstoodMessages = [
"I'm sorry, I didn't quite catch that.",
"I'm not sure I understand what you mean.",
"This is an English-only server.",
"Huh?",
"Pardon?",
"Could you rephrase that?",
"What a concept!",
]

rules = [
"=====Lasciate ogne speranza, voi ch'intrate=====",
"Rule 1: No cheating/exploiting/hacking/misbehaving/tomfoolery/mischief/deviation",
"Rule 2: No random death matching, henceforth known as 'artyem'",
"Rule 3: Any actions, covert or otherwise, displayed in a roleplaying context must be advertised publicly to everybody on the server. Absolutely no exceptions.",
"Rule 4: Absolutely no disrespect to members of our staff will be tolerated. Unprovoked abuse towards unprivileged players is otherwise acceptable.",
"Rule 5: Artyem is absolutely prohibited, unless you provide a warning milliseconds beforehand.",
"Rule 6: All roleplaying chat must be broadcast in out-of-character chat, in order to ensure maximum 'arpee' experience.",
" *** Your eyes glaze over as the rule count extends into the hundreds. *** ",
]

#Verbs
def read(args):
    if len(args) < 2:
        print("What do you want to read?")
        print()
        return
    if args[1] == "rules":
        for i in rules:
            print(i)
        print() 

def respawn():
    if Health < 1:
    	print("You have respawned.")
        Health = 100
        #Set player position to spawnpoint
        hasAK47 = False
        hasShotgun = False
        hasM4A1 = False
        hasDEagle = False
    else:
        print("... You aren't dead, dummy.")
    print()

def check(args):
    if len(args) < 2:
        print("... Check what?")
        print()
        return
    if args[1] == "players" or args[1] == "playercount":
        print("Players Online: " + str(PlayerCount))
        print()
    if args[1] == "admins" or args[1] == "admincount":
        print("Admins Online: " + str(AdminCount))
        print()

def parse(command):
    words = command.split(" ")
    verb = words[0]
    
    if verb == "read":
        read(words)
    elif verb == "respawn":
        respawn()
    elif verb == "check":
        check(words)
    elif True:
        print(misunderstoodMessages[random.randint(1, len(misunderstoodMessages)-1)])
        print()

def newgame():
    #Global Variables
    global Cash
    global Health
    global Intelligence
    global Perception
    global Charisma
    global Luck
    global PlayerCount
    global AdminCount
    global Attitude
    global Position
    global hasAK47
    global hasShotgun
    global hasM4A1
    global hasDEagle
    Cash = 1000
    Health = 100
    Intelligence = random.randint(1, 10)
    Perception = random.randint(1, 10)
    Charisma = random.randint(1, 10)
    Luck = random.randint(1, 10)
    PlayerCount = random.randint(4, 64)
    AdminCount = random.randint(0, int(PlayerCount - PlayerCount * 0.6))
    Attitude = 0
    Position = {0, 0}
    hasAK47 = False
    hasShotgun = False
    hasM4A1 = False
    hasDEagle = False

    for i in range(1, 60):
        print()
    
    print(newGameMessages[random.randint(1, len(newGameMessages))-1])
    print()

    print("Players Online: " + str(PlayerCount))
    print("Admins Online: " + str(AdminCount))
    if Attitude <= 25:
        print("Server Attitude: Calm")
    elif Attitude > 25 and Attitude < 75:
        print("Server Attitude: Unrest")
    elif Attitude >= 75:
        print("Server Attitude: Anarchy")
    print()

    listen()

def listen():
    while Health > 0:
        parse(input(">"))


newgame()
