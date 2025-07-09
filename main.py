
import time
from turtle import Turtle, Screen
from snake_dependency import Snake
turtle_list = []

tim = Turtle()
screen = Screen()
x_pos = 0

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

Snake()

screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)

    for seg in range(len(turtle_list) - 1, 0, -1):
        new_x = turtle_list[seg - 1].xcor()
        new_y = turtle_list[seg - 1].ycor()
        turtle_list[seg].goto(new_x, new_y)
    turtle_list[0].forward(20)

