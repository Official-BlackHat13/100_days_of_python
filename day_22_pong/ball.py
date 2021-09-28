from turtle import Turtle

DIRECTIONS = [55, 45, 35]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.penup()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        print(self.position())

    def bounce(self):
        self.y_move *= -1
