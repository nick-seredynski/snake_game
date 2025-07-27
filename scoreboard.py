
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 260)
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = file.read()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.write(f"Score: {self.score} High Score: {self.high_score}", True, "center", ('arial', 24, 'normal'))


    def update_score(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score} High Score: {self.high_score}", True, "center", ('arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()




