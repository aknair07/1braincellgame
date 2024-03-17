import random

print('''
************************************************************
************************************************************       
       ________   ________    _________  ____________;_
      - ______ \ - ______ \ / _____   //.  .  ._______/
     / /     / // /     / //_/     / // ___   /
    / /     / // /     / /       .-'//_/|_/,-'
   / /     / // /     / /     .-'.-'
  / /     / // /     / /     / /
 / /     / // /     / /     / /
/ /_____/ // /_____/ /     / /
\________- \________-     /_/
************************************************************
************************************************************''')

print("Hello Agent, Welcome to your next mission")
difficulty = input("Please enter what difficulty would you like your mission to be.... Low (L) / Medium (M) / High (H) ").lower()
print("Need to put some story here")

if difficulty == "l":
    noOfRooms = random.randint(5,10)
elif difficulty == "m":
    noOfRooms = random.randint(11, 15)
else:
    noOfRooms = random.randint(20, 25)

caughtMessages = ["Oh No, you opened the door and there were 10 guards there waiting for you!!", 
                  "You open the door to find yourself welcome by hungry wolves!!",
                  "Oh No, turns out its not a room next, but open sky as it was a window trap door!!",
                  "Oh no! you set of the trap door and now you have the room filling up with lava!!"]

while(noOfRooms > 0):
    caught = random.choice(["left", "right", "forward"])
    agentChoice = input("Where do you want to go? (left/right/forward)").lower()
    if agentChoice == caught:
        print(random.choice(caughtMessages))
        print('''
************************************************************
************************************************************ 
  .-"""-.
 ( _   _ )
 ](_' `_)[
 `-. N ,-' 
   |||||
   `---'
************************************************************
************************************************************ 
          ''')
        print("Good bye Bond!! GAME OVER")
        break
    else:
        print("You have successfully gone to the next room")
        noOfRooms -= 1
if noOfRooms == 0:
    print('''
************************************************************
************************************************************ 
              .-=========-.
              \'-=======-'/
              _|   .=.   |_
             ((|   ( )   |))
              \|   /|\   |/
               \__ '`' __/
                 _`) (`_
               _/_______\_
              (___________)
************************************************************
************************************************************ 
          ''')
    print("Congratulations!!! YOU WIN!!")