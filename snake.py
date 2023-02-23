from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()


    def create_snake(self):
        for loop in range(3):
            new_square = Turtle()
            new_square.shape("square")
            new_square.color("white")
            new_square.shapesize(1, 1, 1)
            new_square.penup()
            new_square.setx(-20 + loop * 20)
            self.segments.append(new_square)

    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def increase_length(self):
        new_square = Turtle()
        new_square.speed(0)
        new_square.shape("square")
        new_square.color("white")
        new_square.shapesize(1, 1, 1)
        new_square.penup()
        self.segments.append(new_square)
        self.segments[-1].position()


    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)