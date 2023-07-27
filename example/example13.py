# Hand Detector
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

hamster = Hamster()

# wait while the value of the left proximity is less than 30
while hamster.left_proximity() < 30:
    wait(10) # 10 msec

# move backward for 1 second after beep sound
hamster.beep()
hamster.move_backward()

dispose()
