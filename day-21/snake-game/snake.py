from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake_body = []
        self.x = 0
        self.make_snake()
        self.head = self.snake_body[0]

    def make_snake(self):
        for _ in range(3):
            snake_part = Turtle("square")
            snake_part.color("white")
            snake_part.penup()
            snake_part.setx(self.x)
            self.snake_body.append(snake_part)
            self.x -= 20

    def reset(self):
        for part in self.snake_body:
            part.goto(1000, 1000)
        self.snake_body.clear()
        self.make_snake()
        self.head = self.snake_body[0]

    def grow(self):
        snake_part = Turtle("square")
        snake_part.color("white")
        snake_part.penup()
        pos = self.snake_body[-1].pos()
        snake_part.setpos(pos)
        self.snake_body.append(snake_part)

    def move(self):
        for part in range(len(self.snake_body) - 1, 0, -1):
            pos = self.snake_body[part - 1].pos()
            self.snake_body[part].goto(pos)
        self.snake_body[0].forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)
