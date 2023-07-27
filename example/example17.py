# Extension - Potentiometer
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# This example requires a Hamster's extension kit
# Ctrl + C to terminate

from roboid import *

hamster = Hamster()

# set a port A to the analog input mode
hamster.io_mode_a("analog input")

while True:
    potentiometer = hamster.input_a()
    hamster.buzzer(potentiometer)
    wait(20) # 20 msec

dispose()
