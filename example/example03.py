# Acceleration
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

hamster = Hamster()

# acceleration
for i in range(50):
    hamster.wheels(i, i)
    wait(20) # 20 msec

# 0.5 seconds
wait(500)

# deceleration
for i in range(50, 0, -1):
    hamster.wheels(i, i)
    wait(20) # 20 msec

hamster.stop()

dispose()
