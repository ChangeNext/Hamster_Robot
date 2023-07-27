# Multiple When-Do Hand Detector
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# Ctrl + C to terminate

from roboid import *

hamsters = (Hamster(0), Hamster(1), Hamster(2), Hamster(3))

# wait until four robots are ready
wait_until_ready()

# when hand found
def condition(robot):
    return robot.left_proximity() > 30 or robot.right_proximity() > 30

# move backward for 1 second after beep sound
def move(robot):
    robot.beep()
    robot.move_backward()

for hamster in hamsters:
    when_do(condition, move, hamster)

wait(-1) # wait forever

dispose()
