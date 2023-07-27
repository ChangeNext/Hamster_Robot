# Sensor
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# Ctrl + C to terminate

from roboid import *

hamster = Hamster()

while True:
    print("Signal Strength: ", hamster.signal_strength())
    print("Proximity: ", hamster.left_proximity(), hamster.right_proximity())
    print("Floor: ", hamster.left_floor(), hamster.right_floor())
    print("Acceleration: ", hamster.acceleration_x(), hamster.acceleration_y(), hamster.acceleration_z())
    print("Light: ", hamster.light())
    print("Temperature: ", hamster.temperature())
    print("Input: ", hamster.input_a(), hamster.input_b())
    print("Tilt: ", hamster.tilt())
    print("Battery State: ", hamster.battery_state())
    print("")

    wait(20) # 20 msec

dispose()
