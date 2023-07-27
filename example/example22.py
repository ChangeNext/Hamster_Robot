# Mutiple Hand Follower
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# Ctrl + C to terminate

from roboid import *

hamsters = (Hamster(0), Hamster(1), Hamster(2), Hamster(3))

# wait until four robots are ready
wait_until_ready()

while True:
    for hamster in hamsters:
        # left wheel
        proximity = hamster.left_proximity()
        if proximity > 15:
            left_speed = (40 - proximity) * 4
        else:
            left_speed = 0

        # right wheel
        proximity = hamster.right_proximity()
        if proximity > 15:
            right_speed = (40 - proximity) * 4
        else:
            right_speed = 0

        hamster.wheels(left_speed, right_speed)
        wait(20) # 20 msec

dispose()
