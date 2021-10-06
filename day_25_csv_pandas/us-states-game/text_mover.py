from turtle import Turtle


class TextMover(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_state(self, name, x, y):
        self.goto(x, y)
        self.write(name, align='center', font=('Arial', 8, 'normal'))
