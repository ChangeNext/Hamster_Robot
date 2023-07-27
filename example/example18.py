# Extension - Smooth Led
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# This example requires a Hamster's extension kit
# Ctrl + C to terminate

from roboid import *

hamster = Hamster()

# set a port A to the PWM output mode
hamster.io_mode_a("pwm output")

while True:
    # turn on
    for i in range(0, 255, 5):
        hamster.output_a(i)
        wait(20) # 20 msec

    # turn off
    for i in range(255, 0, -5):
        hamster.output_a(i)
        wait(20) # 20 msec

dispose()
