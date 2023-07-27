# Keyboard Controller
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# Ctrl + C to terminate

from roboid import *

hamster = Hamster()

while True:
    key = Keyboard.read()
    if key:
        if key == Keyboard.UP:
            hamster.wheels(30, 30) # move forward
        elif key == Keyboard.DOWN:
            hamster.wheels(-30, -30) # move backward
        elif key == Keyboard.LEFT:
            hamster.wheels(-30, 30) # turn left
        elif key == Keyboard.RIGHT:
            hamster.wheels(30, -30) # turn right
        elif key == " ":
            hamster.stop() # stop
    wait(10) # 10 msec

dispose()
