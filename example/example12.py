# Builtin Line Tracer Intersection
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

hamster = Hamster()

# # move to a front intersection
hamster.cross_forward()

# move to a left intersection
hamster.cross_left()

# move to a right intersection
hamster.cross_right()

# u-turn and move to an intersection
hamster.cross_uturn()

dispose()

