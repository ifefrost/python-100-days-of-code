from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.current_speed = STARTING_MOVE_DISTANCE

    def make_car(self):
        one_chance = random.randint(1, 6)
        if one_chance == 1:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.car_list.append(car)

    def move_cars(self):
        for car in self.car_list:
            car.backward(self.current_speed)

    def increase_speed(self):
        self.current_speed += MOVE_INCREMENT
