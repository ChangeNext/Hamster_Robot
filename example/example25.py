# Advanced Simple Hand Follower
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# Ctrl + C to terminate

from roboid import *

hamster = Hamster()

def execute():
    proximity = hamster.left_proximity()
    if proximity > 15:
        hamster.left_wheel((40 - proximity) * 4)
    else:
        hamster.left_wheel(0)

    # right wheel
    proximity = hamster.right_proximity()
    if proximity > 15:
        hamster.right_wheel((40 - proximity) * 4)
    else:
        hamster.right_wheel(0)

# set a periodic (20 msec) callback
set_executable(execute)

wait(-1) # wait forever

dispose()
