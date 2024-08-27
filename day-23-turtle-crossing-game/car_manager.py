from turtle import Turtle
import random

COLORS = ["dark turquoise", "sandy brown", "hot pink", "orange red", "coral", "gold", "indian red", "medium spring green", "dark cyan", "dodger blue", "cornflower blue", "orchid", "medium slate blue"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X_AXIS = 260

class CarManager():

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.pu()
            y_axis = random.randint(-250, 250)
            new_car.goto(X_AXIS, y_axis)
            self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

