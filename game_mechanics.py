import random
import Testing_Sound as ts
import graphics
import messages

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
    caught = random.choice(["left", "right", "forward"])
    ts.say(messages.makeChoiceMessage)
    agentChoice = input().lower()
    if agentChoice == caught:
        gameLoss()
        return -1
    else:
        if noOfRooms != 1:
            ts.say(messages.correctDoorMessage)
        return noOfRooms - 1

def gameVictroy():
    graphics.printVictory()
    ts.say()

def gameLoss():
    ts.say(random.choice(messages.caughtMessages))
    graphics.printDeath()
    ts.say("Good bye Agent Bond!! GAME OVER")