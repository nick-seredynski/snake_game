


from turtle import Turtle, Screen


screen = Screen()
tim = Turtle()

def move_left():
    tim.setheading(180)
    tim.forward(10)

def move_right():
    tim.setheading(0)
    tim.forward(10)


screen.onkey(move_left, key="Left")
screen.onkey(move_right, key="Right")

screen.listen()

screen.exitonclick()
