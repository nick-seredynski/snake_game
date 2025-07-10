
import time
from turtle import Turtle, Screen
from snake_dependency import Snake

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)


snake = Snake()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)

    snake.move_segments()
