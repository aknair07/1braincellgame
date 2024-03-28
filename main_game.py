import messages
import game_mechanics as gm

difficulty = gm.getDifficulty()

noOfRooms = gm.roomCount(difficulty)

caughtMessages = messages.caughtMessages

while(noOfRooms > 0):
    noOfRooms = gm.roomChoice(noOfRooms)

if noOfRooms == 0:
    gm.gameVictroy()