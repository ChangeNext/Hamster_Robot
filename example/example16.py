# Extension - Led Blink
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# This example requires a Hamster's extension kit
# Ctrl + C to terminate

from roboid import *

hamster = Hamster()

# set a port A to the digital output mode
hamster.io_mode_a("digital output")

while True:
    hamster.output_a(1) # turn on
    wait(1000) # 1 second

    hamster.output_a(0) # turn off
    wait(1000) # 1 second

dispose()
