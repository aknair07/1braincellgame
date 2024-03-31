import random
import Testing_Sound as ts
import graphics
import messages
import game_mechanics_options

def roomCount(difficulty):
    if difficulty == "l":
        noOfRooms = random.randint(5,10)
    elif difficulty == "m":
        noOfRooms = random.randint(11, 15)
    else:
        noOfRooms = random.randint(20, 25)
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
    exits = availableExits()
    printOptions(exits)
    ts.say(messages.makeChoiceMessage)
    if len(exits) > 1:
        return multiExitRoom(exits, noOfRooms)
    else:
        return singeExitRoom(exits, noOfRooms)

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
    ts.say("Good bye Agent Bond!! GAME OVER")

def availableExits():
    noOfExits = random.randint(1, len(game_mechanics_options.move))
    exits = random.choice(game_mechanics_options.move, k = noOfExits)
    return exits

def printOptions(options):
    print(f"You have the following Options{options}")
    return

