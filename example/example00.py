from roboid import *

hamster = Hamster()

# move forward/backward, turn left/right for 1 second with default velocity(30%)
hamster.move_forward(2, 100) 
# hamster.move_backward()
# hamster.turn_left(2, 100)
# hamster.turn_right()

# # move forward/backward, turn left/right for 2 seconds with default velocity(30%)
# hamster.move_forward(2)
# hamster.move_backward(2)
# hamster.turn_left(2)
# hamster.turn_right(2)

# # move forward/backward, turn left/right for 1.5 seconds with 60% velocity
# hamster.move_forward(1.5, 60)
# hamster.move_backward(1.5, 60)
# hamster.turn_left(1.5, 60)
# hamster.turn_right(1.5, 60)

# # move forward/backward, turn left/right for 1.5 seconds with 60% velocity
hamster.wheels(100, -100)
wait(2000)
# hamster.wheels(-60, -60)
# wait(1500)
# hamster.wheels(-60, 60)
# wait(1500)
# hamster.wheels(60, -60)
# wait(1500)

# stop
hamster.stop()

dispose()
