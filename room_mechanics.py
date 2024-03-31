import random
import messages
import Testing_Sound as ts


def multiExitRoom(exits, noOfRooms, gameLoss): # Confirm how functions are called in variables
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