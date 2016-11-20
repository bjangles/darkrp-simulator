#!/bin/python3

import random

newGameMessages = [
"At last, you have finally finished downloading sixty gigabytes of content only paid users can access. Your eyes are filled with colors and your ears are overwhelmed with the sound of screaming prepubescent children. The world is your oyster.",
"You have finally arrived in the promised land. It's a shame, though. You were just starting to like that Scary Monsters & Nice Sprites remix played at full volume.",
"34 minutes and 12 seconds later. If only you had more time, you could've memorised the rules!",
]

def parse(command):
    print(command)
    print("")

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
    
    print(newGameMessages[random.randint(1, len(newGameMessages))-1])

    listen()

def listen():
    while Health > 0:
        parse(input(">"))


newgame()
