from turtle import Turtle, Screen
from equipment import Player1, Player2
from middle_line import Line
import time

player1 = Player1()
player2 = Player2()
line = Line()

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.tracer(0)

screen.listen()

screen.onkey(player1.move_up, 'Up')
screen.onkey(player1.move_down, 'Down')

screen.onkey(player2.up, 'w')
screen.onkey(player2.down, 's')

screen.exitonclick()
