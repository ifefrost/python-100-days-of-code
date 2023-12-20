from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.setpos(pos_x, pos_y)

    def move_up(self):
        pos = self.ycor() + 20
        self.goto(self.xcor(), pos)

    def move_down(self):
        pos = self.ycor() - 20
        self.goto(self.xcor(), pos)
