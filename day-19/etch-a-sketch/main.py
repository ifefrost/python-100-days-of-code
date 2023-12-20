from turtle import Turtle, Screen

tim = Turtle(shape="turtle")
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a colour: ")

tim.teleport(-230, -100)

screen.exitonclick()
