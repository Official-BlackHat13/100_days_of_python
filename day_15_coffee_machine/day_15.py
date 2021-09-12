from machine import *


def game():
    which_coffee = input('what would you like? (Espresso/Latte/Cappuccino/nothing)?: ').lower()
    if which_coffee == 'espresso':
        coffee = coffees[0]
        print(coffee)
    elif which_coffee == 'latte':
        coffee = coffees[1]
        print(coffee)
    elif which_coffee == 'cappuccino':
        coffee = coffees[2]
        print(coffee)
    elif which_coffee == 'nothing':
        print('thanks for your time')
        return
    elif which_coffee == 'report':
        print(f"water: {machine_resources['water']} ml\nmilk: {machine_resources['milk']} ml\ncoffee powder: {machine_resources['coffee_powder']} g\ncash: ${machine_resources['money']}")
    else:
        print('learn to type fuck face')
        game()

game()
