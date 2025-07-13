
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 260)
        self.score = 0
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.write(f"Score: {self.score}", True, "center", ('arial', 24, 'normal'))


    def update_score(self):
        self.clear()
        self.goto(0, 260)
        self.score += 1
        self.write(f"Score: {self.score}", True, "center", ('arial', 24, 'normal'))


    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER. FINAL SCORE: {self.score}", True, "center", ('arial', 24, 'normal'))


