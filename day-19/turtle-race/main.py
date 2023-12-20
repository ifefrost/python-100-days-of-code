import random
from turtle import Turtle, Screen

racing = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet",
                            "Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtle_list = []
y = -100
for i in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.teleport(-230, y)
    y += 35
    turtle_list.append(new_turtle)

if user_bet in colors:
    racing = True

while racing:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            racing = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! the {winner} turtle is the winner")
            else:
                print(f"You've lost! the {winner} turtle is the winner")



        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()