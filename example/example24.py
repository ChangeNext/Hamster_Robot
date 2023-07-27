# Advanced Theremin Sound
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# Ctrl + C to terminate

from roboid import *

hamster = Hamster()
hz = 0

def execute():
    global hz
    
    proximity = hamster.left_proximity()
    if proximity < 10:
        proximity = 0
    hz = (hz * 5 + proximity * 50) / 10.0
    hamster.buzzer(hz)

# set a periodic (20 msec) callback
set_executable(execute)

wait(-1) # wait forever

dispose()
