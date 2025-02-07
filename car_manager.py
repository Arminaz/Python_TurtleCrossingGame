from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            colour = random.choice(COLORS)
            rand_y = random.randint(-250, 250)
            new_car.color(colour)
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.goto(300, rand_y)
            self.all_cars.append(new_car)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    
