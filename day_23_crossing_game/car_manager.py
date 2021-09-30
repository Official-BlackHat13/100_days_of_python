from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_POSITIONS = []


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []

    def create_car(self):
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(COLORS))
        self.setheading(180)
        self.penup()
        self.goto(randint(200, 250), randint(-255, 255))


