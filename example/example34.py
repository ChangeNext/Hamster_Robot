# Advanced Multiple Hand Detector
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

hamster1 = Hamster(0)
hamster2 = Hamster(1)

# user-defined function
def check(robot):
    return robot.left_proximity() > 30

# wait until the value of the left proximity is greater than 30
wait_until(check, hamster1)

# move backward for 1 second after beep sound
hamster1.beep()
hamster1.move_backward()

# wait until the value of the left proximity is greater than 30
wait_until(check, hamster2)

# move backward for 1 second after beep sound
hamster2.beep()
hamster2.move_backward()

dispose()
