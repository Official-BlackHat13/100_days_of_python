from turtle import Turtle, Screen

screen = Screen()
UP = 90
DOWN = 270
DISTANCE = 20


class Player1:

    def __init__(self):
        self.paddle = None
        self.create_paddle()

    def create_paddle(self):
        new_paddle = Turtle(shape='square')
        new_paddle.shapesize(1, 5)
        new_paddle.penup()
        new_paddle.color('white')
        new_paddle.goto((370, 0))
        self.paddle = new_paddle
        self.paddle.setheading(UP)

    def move_up(self):
        if self.paddle.position() != (370.00, 360.00):
            self.paddle.setheading(UP)
            screen.update()
            self.paddle.forward(DISTANCE)
            print(self.paddle.position())

    def move_down(self):
        if self.paddle.position() != (370.00, -360.00):
            self.paddle.setheading(DOWN)
            screen.update()
            self.paddle.forward(DISTANCE)
            print(self.paddle.position())


class Player2(Player1):

    def __init__(self):
        self.create_paddle()
        self.paddle.goto((-370, 0))

    def up(self):
        if self.paddle.position() != (-370.00, 360.00):
            self.move_up()

    def down(self):
        if self.paddle.position() != (-370.00, -360.00):
            self.move_down()
