
from turtle import Turtle
start_pos = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.create_segments()


    def create_segments(self):
        for positions in start_pos:
            self.segments = Turtle("square")
            self.segments.shape("square")
            self.segments.penup()
            self.segments.color("white")
            self.segments.goto(positions)

