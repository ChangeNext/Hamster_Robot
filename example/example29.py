# Advanced Dual Theremin Sound
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# Ctrl + C to terminate

from roboid import *

hamster1 = Hamster(0)
hamster2 = Hamster(1)
hz1 = 0
hz2 = 0

# wait until two robots are ready
wait_until_ready()

def execute():
    global hz1
    global hz2

    proximity = hamster1.left_proximity()
    if proximity < 10:
        proximity = 0
    hz1 = (hz1 * 5 + proximity * 50) / 10.0
    hamster1.buzzer(hz1)

    proximity = hamster2.left_proximity()
    if proximity < 10:
        proximity = 0
    hz2 = (hz2 * 5 + proximity * 50) / 10.0
    hamster2.buzzer(hz2)

# set a periodic (20 msec) callback
set_executable(execute)

wait(-1) # wait forever

dispose()
