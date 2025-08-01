
# controls snake blueprint
from turtle import Turtle
start_pos = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_segments()


    def create_segments(self):
        for positions in start_pos:
            self.add_segments(positions)


    def add_segments(self, positions):
        new_seg = Turtle("square")
        new_seg.shape("square")
        new_seg.penup()
        new_seg.color("white")
        new_seg.goto(positions)
        self.segments.append(new_seg)


    def extend_segments(self):
        self.add_segments(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_segments()


    def move_segments(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(move_distance)


    def turn_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)


    def turn_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)


    def turn_up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)


    def turn_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

