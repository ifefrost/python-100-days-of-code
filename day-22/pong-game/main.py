from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")


game_running = True
while game_running:
    time.sleep(ball.game_speed)
    screen.update()
    ball.move()

    # Detect collision with walls
    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(right_paddle) < 50 or ball.distance(left_paddle) < 50) and abs(ball.xcor()) > 320:
        ball.bounce_x()

    # if ball goes past paddles
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
