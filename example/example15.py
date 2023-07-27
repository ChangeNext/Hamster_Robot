# Extension - Button
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# This example requires a Hamster's extension kit
# Ctrl + C to terminate

from roboid import *

hamster = Hamster()

# set a port B to the digital input mode
hamster.io_mode_b("digital input")

while True:
    if hamster.input_b() == 0:
        hamster.buzzer(1000)
    else:
        hamster.buzzer(0)
    wait(20) # 20 msec

dispose()
