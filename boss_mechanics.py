import random
import game_mechanics_options as gmo

def callBoss():
    level = bossLevel()
    win = 0
    for i in range(5):
        if rockPaperScissors():
            win += 1
        if win >= level:
            return True
        if i - win + 1 >= level:
            return False
    return True

def bossLevel():
    level = random.randint(1,3)
    return level

def rockPaperScissors(): 
    while True:
        bossSelect = random.choice(gmo.select)
        playerSelect = input("Enter answer").lower()
        print((playerSelect, bossSelect))
        if bossSelect == playerSelect:
            print ('It was a tie, please re-do the turn')
            continue
        else:
            if (gmo.select.index(playerSelect), gmo.select.index(bossSelect)) in [(0,2), (1,0), (2,1)]:
                print('you win')
                return True
            else:
                print('you lose')
                return False


