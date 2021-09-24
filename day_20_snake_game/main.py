# snake game
import turtle as t
from turtle import Screen, Turtle
import time
t.colormode(255)
# creating screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor((186, 199, 1))
screen.title('Snake')
screen.tracer(0)

# creating tha snake body
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle(shape='square')
    new_segment.penup()
    new_segment.color((109, 95, 0))
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)
screen.exitonclick()
