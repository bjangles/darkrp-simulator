#!/usr/bin/env python3

import os
import random
import string

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

        misunderstoodMessages = [
            "I'm sorry, I didn't quite catch that.",
            "I'm not sure I understand what you mean.",
            "This is an English-only server.",
            "Huh?",
            "Pardon?",
            "Could you rephrase that?",
        ]

        if Entry != None:
            Entry["function"](args.split())
            if Entry["endturn"]:
                HandleTurn()
        else:
            print(random.choice(misunderstoodMessages))
            print()

class Map:
    def __init__(self):
        self.Map = {}

    def BuildMap(self):
        #rp_seriousarpee_v1
        self.Map = [
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

class Inventory:
    def __init__(self):
        self.Inventory = {}

    #Takes a dict with attributes of an item
    #Returns True if successful, False otherwise
    def AddItem(self, item):
        ItemEntry = self.Inventory.get(item["name"], None)
        IsItemUnique = item.get("unique", False)

        if item["unique"]:
            if ItemEntry == None:
                self.Inventory[item["name"]] = item
                print("Added item to inventory: " + item["name"])
                print()
                return True
            else:
                #User already has unique item, so return False to notify this
                return False
        else:
            #The item we're adding is not unique, so append some random numbers to the key in order to prevent KeyErrors
            #Probably not the best way to tackle the problem, but cheap
            self.Inventory[item["name"] + string(random.randomint(1000, 9999))] = item
            print("Added item to inventory: " + item["name"])
            print()
            return True

    #Returns True if successful, False otherwise
    def RemoveItem(self, key):
        if self.Inventory.pop(key, None) != None:
            return True
        else:
            return False

class Player:
    def __init__(self):
        self.Health = 0
        self.Cash = 1000
        self.Banned = False

        self.Skills = {}
        self.Skills["Intelligence"] = 4
        self.Skills["Charisma"] = 4
        self.Skills["Perception"] = 4
        self.Skills["Agility"] = 4
        self.Skills["Luck"] = 4

        self.Position = (0, 0)

        self.InventorySystem = Inventory()
        self.Spawn()

    def Spawn(self):
        #Find a spawn tile, and move us there
        #Also set our health back to full
        SpawnTile = None
        for y in Map.Map:
            for x in Map.Map:
                if Map[x][y].get("type", "") == "spawn":
                    SpawnTile = (x, y)
                    break
        self.Position = SpawnTile
        self.Health = 100

        #Clear our inventory
        for i in self.InventorySystem.Inventory:
            self.InventorySystem.RemoveItem(i)

        self.InventorySystem.AddItem(ITEM_Map)

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
    Player.Roll("Intelligence")
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

    RegisterVerbs()
    RegisterItems()

    global Map
    Map = Map()

    global Player
    Player = Player()

    while True:
        VerbSystem.Execute(input(">").lower())

#Verb Definitions#
def RegisterVerbs():
    global VerbSystem

    def Check(args):
        if len(args) < 1:
            print("Perhaps you should have checked yourself before you wrecked yourself.")

        #Check globals
        if args[1] == "health":
            print("Health: " + str(Player.Health))
            return
        if args[1] == "players" or args[1] == "playercount":
            print("Players: " + str(PlayerCount))
            return
        if args[1] == "admins" or args[1] == "admincount":
            print("Admins: " + str(AdminCount))
            return
        if args[1] == "inventory":
            for i in Player.InventorySystem.Inventory:
                print(Player.InventorySystem.Inventory[i]["name"])
            print()
            return

        #Check through the player's inventory
        FoundItems = []
        for i in Player.InventorySystem.Inventory:
            if i["name"] == args[1]:
                FoundItems.append(Player.InventorySystem.Inventory[i])

        print(args[1])
        if len(FoundItems) == 1:
            Player.InventorySystem.Inventory[i]["checkbehavior"]()
            return
        elif len(FoundItems) > 1:
            for k, v in ipairs(FoundItems):
                print(str(k) + ": " + v["name"])

            Choice = input("Which item would you like to check: ")
            if FoundItems[choice] != None:
                FoundItems[choice]["checkbehavior"]()

        #Check things in proximity
        #Store prices, etc

    VerbSystem.AddVerb(
        verb = "check",
        function = Check,
        endturn = False,
    )

#Item Definitions#
def RegisterItems():
    global ITEM_Base
    ITEM_Base = {}
    ITEM_Base["name"] = "base"
    ITEM_Base["unique"] = False
    def DropBehavior():
        return True
    ITEM_Base["dropbehavior"] = DropBehavior
    def CheckBehavior():
        return
    ITEM_Base["checkbehavior"] = CheckBehavior

    global ITEM_Map
    ITEM_Map = ITEM_Base
    ITEM_Map["name"] = "map"
    ITEM_Map["unique"] = True
    def DropBehavior():
        print("Somehow I don't believe that would be a good idea.")
        return False
    ITEM_Map["dropbehavior"] = DropBehavior
    def CheckBehavior():
        print()
        #Map Header
        row = "\t" + "╔"
        for i in range(45):
            row = row + "═"
        row = row + "╗"

        #Legend Header
        row = row + "\t" + "╔" + "═" + "╦"
        for _ in range(21):
            row = row + "═"
        row = row + "╗"

        print(row)

        for i in range(len(Map)):
            row = ""

            #Compass Rose
            if i == 0:
                row = row + "   " + "N"
            elif i == 1:
                row = row + " " + "W" + " + " + "E"
            elif i == 2     :
                row = row + "   " + "S"

            #Map Tile Wall
            row = row + "\t"
            row = row + "║"

            #Map Tiles
            for k in range(len(Map)):
                tileType = Map[i][k].get("type", "")
                tilePlayer = Map[i][k].get("player", False)
                marker = "[ ]"
                if tileType == "wall":
                    marker = "[■]"
                elif tileType == "door":
                    marker = "[D]"
                elif tilePlayer == True:
                    marker = "[X]"
                elif tileType == "gunstore":
                    marker = "[G]"
                elif tileType == "police":
                    marker = "[P]"
                elif tileType == "propblock":
                    marker = "[Q]"
                elif tileType == "spawn":
                    marker = "[S]"
                row = row + marker

            #Map Tile Wall
            row = row + "║"

            legendData = [
                ("X", "You!"),
                ("P", "Police Station"),
                ("G", "Gun Store"),
                ("Q", "Prop Block"),
                ("S", "Spawn Point"),
                ("D", "Door"),
                ("■", "Wall"),
            ]

            #Legend Rows
            if i < len(legendData):
                row = row + " " + "║" + legendData[i][0] + "║" + " " + legendData[i][1]
                if len(legendData[i][1]) < 13:
                    row = row + "\t" + "\t" + "║"
                else:
                    row = row + "\t" + "║"

            elif i == len(legendData):
                row = row + " " + "╚" + "═" + "╩"
                for i in range(21):
                    row = row + "═"
                row = row + "╝"


            print(row)

        row = "\t" + "╚"
        for i in range(45):
            row = row + "═"
        row = row + "╝"
        print(row)
        return
    ITEM_Map["checkbehavior"] = CheckBehavior

main()