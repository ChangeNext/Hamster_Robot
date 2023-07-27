import json

json_data = {}



dict_data = {
    "data": {
        {
        "instruction": " ",
        "input": '앞으로 움직였다가 뒤로 움직이고 1초 동안 왼쪽, 오른쪽으로 속도 30으로 움직이기',
        "output" :  "hamster.move_backward() #\
                       hamster.turn_left()   #\
                       hamster.turn_right()"
        },
        {
        "instruction": " ",
       "input"  : '앞으로 움직였다가 뒤로 움직이고 2초 동안 왼쪽, 오른쪽으로 속도 30 으로 움직이기',
       "output" : "hamster.move_forward(2) #\
                   hamster.move_backward(2)#\
                   hamster.turn_left(2)    #\
                   hamster.turn_right(2)"
        },
        {
        "instruction": " ",
        "input" : '앞으로 움직였다가 뒤로 움직이고 1.5초 동안 왼쪽, 오른쪽으로 속도 60 으로 움직이기',
        "output" : "hamster.move_forward(1.5, 60)  #\
                    hamster.move_backward(1.5, 60) #\
                    hamster.turn_left(1.5, 60)     #\
                    hamster.turn_right(1.5, 60) "
        },
        {
        "instruction": " ",
        "input" : '앞으로 움직였다가 뒤로 움직이고 1.5초 동안 왼쪽, 오른쪽으로 속도 60 으로 움직이기',
        "output" : "hamster.move_forward(1.5, 60)  #\
                    hamster.move_backward(1.5, 60) #\
                    hamster.turn_left(1.5, 60)     #\
                    hamster.turn_right(1.5, 60) "
        }
    }
}


                       
print(dict_data)