from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet!', prompt='Choose a color: ')


red = Turtle(shape='turtle')
red.color('red')
red.penup()
red.goto(x=-230, y=60)
red.forward(randint(1, 10))

purple = Turtle(shape='turtle')
purple.color('purple')
purple.penup()
purple.goto(x=-230, y=30)
purple.forward(randint(1, 10))

green = Turtle(shape='turtle')
green.color('green')
green.penup()
green.goto(x=-230, y=0)
green.forward(randint(1, 10))

blue = Turtle(shape='turtle')
blue.color('blue')
blue.penup()
blue.goto(x=-230, y=-30)
blue.forward(randint(1, 10))

brown = Turtle(shape='turtle')
brown.color('brown')
brown.penup()
brown.goto(x=-230, y=-60)
brown.forward(randint(1, 10))

list_of_turtles = [red, purple, green, blue, brown]

# for racer in list_of_turtles:
#     if racer.position(x=230):
#         print(racer.color)

screen.exitonclick()