#!/bin/python3

import random

#Global Variables
Cash = 0
Health = 0
Intelligence = 0
Perception = 0
Charisma = 0
Luck = 0
PlayerCount = 0
AdminCount = 0
Attitude = calm
Position = { x = 0, y = 0 }
hasAK47 = False
hasShotgun = False
hasM4A1 = False
hasDEagle = False


def parse(command):
    print(command)
    print("")

def newgame():
    Cash = 1000
    Health = 100
    Intelligence = random.randint(1, 10)
    Perception = random.randint(1, 10)
    Charisma = random.randint(1, 10)
    Luck = random.randint(1, 10)
    PlayerCount = random.randint(4, 64)
    AdminCount = random.randint(0, int(PlayerCount - PlayerCount * 0.6))
    Attitude = 0
