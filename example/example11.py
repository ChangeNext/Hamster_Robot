# Builtin Line Tracer
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

hamster = Hamster()

hamster.line_left() # follow black line with left floor sensor
wait(5000) # 5 seconds

hamster.line_speed(8) # speed up
wait(5000) # 5 seconds

hamster.line_right() # follow black line with right floor sensor
wait(5000) # 5 seconds

hamster.line_speed(5) # speed down
wait(5000) # 5 seconds

hamster.line_both() # follow black line with both floor sensors
wait(5000) # 5 seconds

hamster.stop() # stop

dispose()
