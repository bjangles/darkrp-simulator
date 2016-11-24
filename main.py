#!/usr/bin/env python3

import os
import random
import string

misunderstoodMessages = [
    "I'm sorry, I didn't quite catch that.",
    "I'm not sure I understand what you mean.",
    "This is an English-only server.",
    "Huh?",
    "Pardon?",
    "Could you rephrase that?",
]

class VerbSystem:
    def __init__(self):
        self.Verbs = {}

    def AddVerb(self, **kwargs):
        VerbEntry = {}

        for k in kwargs:
            VerbEntry[k] = kwargs[k]

        self.Verbs[kwargs["verb"]] = VerbEntry

    def Execute(self, args):
        Verb = args.split()[0]
        Entry = self.Verbs.get(Verb, None)

        if Entry != None:
            Entry["function"](args.split())
            if Entry["endturn"]:
                HandleTurn()
        else:
            print(random.choice(misunderstoodMessages))
            print()

class Inventory:
    def __init__(self):
        self.Inventory = {}

    #Takes a dict with attributes of an item
    #Returns True if successful, False otherwise
    def AddItem(self, item):
        ItemEntry = self.Inventory.get(item["name"], None)
        IsItemUnique = item.get("unique", False)

        if item["unique"]:
            if ItemEntry != None:
                self.Inventory[item["name"]] = item
                return True
            else:
                #User already has unique item, so return False to notify this
                return False
        else:
            #The item we're adding is not unique, so append some random numbers to the key in order to prevent KeyValue errors
            #Probably not the best way to tackle the problem, but cheap
            self.Inventory[item["name"] + string(random.randomint(1000, 9999))] = item
            return True

    #Returns True if successful, False otherwise
    def RemoveItem(self, key):
        if self.Inventory.pop(key, None) != None:
            return True
        else:
            return False

class Player:
    def __init__(self):
        self.Health = 100
        self.Cash = 1000
        self.Banned = False

        self.Skills = {}
        self.Skills["Intelligence"] = 4
        self.Skills["Charisma"] = 4
        self.Skills["Perception"] = 4
        self.Skills["Agility"] = 4
        self.Skills["Luck"] = 4

        self.Position = (0, 0)

    def Spawn(self):
        #Find a spawn tile, and move us there
        #Also set our health back to full
        SpawnTile = None
        for y in Map:
            for x in Map:
                if Map[x][y].get("type", "") == "spawn":
                    SpawnTile = (x, y)
                    break
        self.Position = SpawnTile
        self.Health = 100

    def Roll(self, attribute, luck=True, silent=False):
        #Roll a number, from 1 to 20, then add the attribute's value
        Roll = random.randint(1, 20)
        if not silent:
            print("You cast the die: " + str(Roll))

        Roll += int(self.Skills[attribute] / 2)
        if not silent:
            print("Your " + attribute.lower() + " aids your chances: " + str(Roll))

        #Add luck attribute, if desired
        if luck:
            if (self.Skills["Luck"]/2)/10 > random.random():
                Roll += 4
                if not silent:
                    print("A group of leprechauns smile upon you: " + str(Roll))

        if not silent:
            print()
        return Roll

def HandleTurn():
    Player.Roll("Intelligence", True, True)
    print()

def FluctuatePlayers():
    global PlayerCount
    global AdminCount

    #Define behavior for player count to fluctuate
    chance = random.randint(1, 6) #1/6 chance :^)
    if chance == 1 and PlayerCount > 1:
        PlayerCount -= 1
        if random.random() <= AdminCount/PlayerCount and AdminCount > 0:
            AdminCount -= 1
    elif chance == 6:
        PlayerCount += 1
        if random.random() <= AdminCount/PlayerCount:
            AdminCount += 1


def BuildMap(size):
    global Map

    #rp_seriousarpee_v1
    Map = [
                    [{"type": ""}, {"type": ""}, {"type": ""}, {"type": "wall"}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": "wall"}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""},],
                    [{"type": ""}, {"type": ""}, {"type": ""}, {"type": "wall"}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": "wall"}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""},],
                    [{"type": ""}, {"type": ""}, {"type": ""}, {"type": "wall"}, {"type": "wall"}, {"type": "wall"}, {"type": "wall"}, {"type": "wall"}, {"type": ""}, {"type": ""}, {"type": "wall"}, {"type": "wall"}, {"type": "wall"}, {"type": ""}, {"type": ""},],
                    [{"type": "wall"}, {"type": "wall"}, {"type": "door"}, {"type": "wall"}, {"type": "spawn"}, {"type": ""}, {"type": ""}, {"type": "door"}, {"type": ""}, {"type": ""}, {"type": "wall"}, {"type": "wall"}, {"type": "wall"}, {"type": ""}, {"type": ""},],
                    [{"type": ""}, {"type": "door"}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": "wall"}, {"type": "wall"}, {"type": "wall"}, {"type": "wall"}, {"type": "wall"}, {"type": "wall"}, {"type": ""}, {"type": ""},],
                    [{"type": ""}, {"type": "wall"}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": "wall"}, {"type": "door"}, {"type": "wall"},],
                    [{"type": ""}, {"type": "wall"}, {"type": ""}, {"type": "wall"}, {"type": "door"}, {"type": "wall"}, {"type": "wall"}, {"type": ""}, {"type": "wall"}, {"type": "wall"}, {"type": "wall"}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""},],
                    [{"type": "wall"}, {"type": "wall"}, {"type": ""}, {"type": "wall"}, {"type": ""}, {"type": ""}, {"type": "wall"}, {"type": ""}, {"type": "door"}, {"type": ""}, {"type": "wall"}, {"type": "wall"}, {"type": "wall"}, {"type": "wall"}, {"type": "wall"},],
                    [{"type": ""}, {"type": ""}, {"type": ""}, {"type": "wall"}, {"type": ""}, {"type": ""}, {"type": "wall"}, {"type": ""}, {"type": "wall"}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""},],
                    [{"type": "wall"}, {"type": "wall"}, {"type": ""}, {"type": "wall"}, {"type": "wall"}, {"type": "door"}, {"type": "wall"}, {"type": ""}, {"type": "wall"}, {"type": "wall"}, {"type": "wall"}, {"type": "wall"}, {"type": "wall"}, {"type": ""}, {"type": ""},],
                    [{"type": ""}, {"type": "wall"}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": "wall"}, {"type": "wall"}, {"type": "wall"},],
                    [{"type": ""}, {"type": "wall"}, {"type": "door"}, {"type": "wall"}, {"type": "wall"}, {"type": ""}, {"type": ""}, {"type": "wall"}, {"type": "wall"}, {"type": "door"}, {"type": "wall"}, {"type": ""}, {"type": "door"}, {"type": ""}, {"type": ""},],
                    [{"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": "wall"}, {"type": ""}, {"type": ""}, {"type": "wall"}, {"type": ""}, {"type": ""}, {"type": "wall"}, {"type": "wall"}, {"type": "wall"}, {"type": ""}, {"type": ""},],
                    [{"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": "wall"}, {"type": "wall"}, {"type": "wall"}, {"type": "wall"}, {"type": ""}, {"type": ""}, {"type": "wall"}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""},],
                    [{"type": ""}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": "wall"}, {"type": "wall"}, {"type": "wall"}, {"type": "wall"}, {"type": ""}, {"type": ""}, {"type": "wall"}, {"type": ""}, {"type": ""}, {"type": ""}, {"type": ""},],
                ]

def CreateVariables():
    #Global Variables
        global Cash
        Cash = 1000
        global Health
        Health = 100
        global Banned
        Banned = False
        global PlayerCount
        PlayerCount = random.randint(4, 64)
        global AdminCount
        AdminCount = random.randint(0, int(PlayerCount - PlayerCount * 0.75))
        global Attitude
        Attitude = 0
        global AttitudeMod
        AttitudeMod = 0

def main():
    global VerbSystem
    VerbSystem = VerbSystem()

    global Player
    Player = Player()

    def run(args):
        print()
    VerbSystem.AddVerb(
        verb = "run",
        function = run,
        endturn = True,
        )

    while True:
        VerbSystem.Execute(input(">").lower())

main()