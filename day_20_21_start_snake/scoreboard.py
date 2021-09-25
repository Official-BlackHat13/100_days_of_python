from turtle import Turtle
from main import got_food


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))

