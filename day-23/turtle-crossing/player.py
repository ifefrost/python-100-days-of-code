from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.seth(90)
        self.reset_player()

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.sety(new_y)

    def reset_player(self):
        self.goto(STARTING_POSITION)

    def at_goal(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
