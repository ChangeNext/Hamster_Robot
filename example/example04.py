# Led
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

hamster = Hamster()

hamster.leds("red", "green") # turn on both LEDs
wait(500) # 0.5 seconds

hamster.left_led("off") # turn off left LED
wait(500) # 0.5 seconds

hamster.left_led("blue") # turn on left LED
wait(500) # 0.5 seconds

hamster.right_led("off") # turn off right LED
wait(500) # 0.5 seconds

hamster.right_led("yellow") # turn on right LED
wait(500) # 0.5 seconds

hamster.leds("off") # turn off both LEDs

dispose()
