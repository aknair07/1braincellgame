import random
import Testing_Sound as ts
import graphics
import messages
import game_mechanics_options
import room_mechanics as rm
import boss_mechanics as bm

def roomCount(difficulty):
    if difficulty == "l":
        noOfRooms = random.randint(3,6)
    elif difficulty == "m":
        noOfRooms = random.randint(7, 9)
    else:
        noOfRooms = random.randint(10, 11)
    return noOfRooms

def printIntro():
    graphics.printIntro()
    ts.say(messages.introMessage)
    ts.say(messages.inputDifficultyMessage)

def getDifficulty():
    printIntro()
    difficulty = input(" ").lower()
    graphics.printSlow(messages.introStory)
    return difficulty

def roomChoice(noOfRooms):
    if random.randin(0,1) > 0:
        value = bm.callBoss()
    if value:
        exits = availableExits()
        printOptions(exits)
        ts.say(messages.makeChoiceMessage)
        if len(exits) > 1:
            return rm.multiExitRoom(exits, noOfRooms, gameLoss)
        else:
            return rm.singeExitRoom(exits, noOfRooms)
    else:
        print(f'Sorry you lost to the boss')

def multiExitRoom(exits, noOfRooms):
    caught = random.choice(exits)
    agentChoice = input().lower()
    if agentChoice == caught:
        gameLoss()
        return -1
    else:
        if noOfRooms != 1:
            ts.say(messages.correctDoorMessage)
        return noOfRooms - 1

def singeExitRoom(exits, noOfRooms):
    for i in range(3):
        agentChoice = input().lower()
        if agentChoice == exits[0]:
            ts.say(messages.correctDoorMessage)
            return noOfRooms - 1
        else:
            ts.say(messages.remakeChoice)
    ts.say(messages.caughtSingleChoice)
    return -1

def gameVictroy():
    graphics.printVictory()
    ts.say()

def gameLoss():
    ts.say(random.choice(messages.caughtMessages))
    graphics.printDeath()
    ts.say("Good bye Agent Bond !! GAME OVER")

def availableExits(): # This works
    noOfExits = random.randint(1, len(game_mechanics_options.move))
    exits = random.choices(game_mechanics_options.move,  k=noOfExits)
    return exits

def printOptions(options):
    print(f"You have the following Options{options}")
    return

