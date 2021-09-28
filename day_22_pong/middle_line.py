from turtle import Turtle, Screen


class Line(Turtle):
    screen = Screen()

    def __init__(self):
        super().__init__()
        self.color('White')
        self.hideturtle()
        self.penup()
        self.goto(0, 390)
        self.setheading(270)
        for _ in range(20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
