import os
def say(msg = "Game Over", voice = "Daniel"):
    os.system(f'say -v {voice} {msg}')

say()