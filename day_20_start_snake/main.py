# snake game
import turtle as t
from turtle import Screen
from snake import Snake
from food import Food
import time

t.colormode(255)
# creating screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor((186, 199, 1))
screen.title('Snake')
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head_of_snake.distance(food) < 15:
        food.refresh()


screen.exitonclick()
