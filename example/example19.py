# Extension - Servo
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# This example requires a Hamster's extension kit
# Ctrl + C to terminate

from roboid import *

hamster = Hamster()

# set a port A to the servo output mode
hamster.io_mode_a("servo output")

while True:
    hamster.output_a(180) # move to 180 degrees
    wait(1000) # 1 second

    hamster.output_a(10) # move to home
    wait(1000) # 1 second

dispose()
