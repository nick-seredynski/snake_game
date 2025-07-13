
import time
from turtle import Screen
from snake_dependency import Snake
from food import Food

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.onkey(snake.turn_left, key="Left")
screen.onkey(snake.turn_right, key="Right")
screen.onkey(snake.turn_up, key="Up")
screen.onkey(snake.turn_down, key="Down")

screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move_segments()

    if snake.segments[0].distance(food) < 15:
        food.new_food()

