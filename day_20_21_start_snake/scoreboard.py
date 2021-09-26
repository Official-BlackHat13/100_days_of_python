from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def wall_hit(self):
        self.goto(0, 0)
        self.write(f"Game Over\nYou hit a wall\nFinal score: {self.score}", align=ALIGNMENT, font=FONT)

    def tail_hit(self):
        self.goto(0, 0)
        self.write(f"Game Over\nYou hit your tail\nFinal score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
