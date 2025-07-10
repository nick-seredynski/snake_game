
from turtle import Turtle, Screen
import time

screen = Screen()
tim = Turtle()

def move_left():
    tim.setheading(0)
    tim.forward(10)

def move_right():
    tim.setheading(180)
    tim.forward(10)

start = True
while start:

    screen.onkey(move_left, key="Left")
    screen.onkey(move_right, key="Right")

    screen.listen()
