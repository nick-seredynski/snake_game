
from turtle import Turtle
start_pos = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_segments()


    def create_segments(self):
        for positions in start_pos:
            new_seg = Turtle("square")
            new_seg.shape("square")
            new_seg.penup()
            new_seg.color("white")
            new_seg.goto(positions)
            self.segments.append(new_seg)


    def move_segments(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(move_distance)
