from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 16, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 250)
        self.display()

    def increase_score(self):
        self.score += 1
        self.display()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.display()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def display(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
