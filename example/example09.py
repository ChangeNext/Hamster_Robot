# Theremin Sound
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# Ctrl + C to terminate

from roboid import *

hamster = Hamster()

hz = 0
while True:
    proximity = hamster.left_proximity()
    if proximity < 10:
        proximity = 0
    hz = (hz * 5 + proximity * 50) / 10.0
    hamster.buzzer(hz)

    wait(20) # 20 msec

dispose()
