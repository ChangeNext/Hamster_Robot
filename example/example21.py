# Mutiple Simple Movement
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# Ctrl + C to terminate

from roboid import *

hamsters = (Hamster(0), Hamster(1), Hamster(2), Hamster(3))

# wait until four robots are ready
wait_until_ready()

while True:
    # move forward
    for hamster in hamsters:
        hamster.wheels(50, 50)

    wait(500) # 0.5 seconds

    # move backward
    for hamster in hamsters:
        hamster.wheels(-50, -50)

    wait(500) # 0.5 seconds

    # turn left
    for hamster in hamsters:
        hamster.wheels(-50, 50)

    wait(500) # 0.5 seconds

dispose()
