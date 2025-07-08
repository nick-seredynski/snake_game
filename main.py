import turtle
import time
from turtle import Turtle, Screen
start_pos = [(0,0), (-20,0), (-40,0)]
turtle_list = []

tim = Turtle()
screen = Screen()
x_pos = 0

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

for new_pos in start_pos:
    new_seg = Turtle("square")
    new_seg.shape("square")
    new_seg.penup()
    new_seg.color("white")
    new_seg.goto(new_pos)
    turtle_list.append(new_seg)

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
