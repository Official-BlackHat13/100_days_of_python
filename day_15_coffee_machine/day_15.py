from machine import *



def game():

    # check order
    def check_order():
        def coin_identifier():
            type_of_coin = input(f"we process 'pennies', 'nickels', 'dimes', 'quarters'. Please choose one")

        # check if the machine got the resources for the chosen type of coffee
        def check_modify_availability():
            if machine_resources['water'] <= coffee['water_needed']:
                print('not enough water')
            if machine_resources['milk'] <= coffee['milk_needed']:
                print('not enough milk')
            if machine_resources['coffee_powder'] <= coffee['coffee_powder_needed']:
                print('not enough coffee')
            if machine_resources['money'] <= coffee['price']:
                print(f"please insert more money (currently got: ${machine['money']})")
            else:
                machine_resources['money'] -= coffee['price']
                print(machine_resources['money'])

        which_coffee = input('what would you like? (Espresso($1.50)/Latte($2.50)/Cappuccino($3.00)/nothing?: ').lower()
        if which_coffee == 'espresso':
            coffee = coffees[0]
            check_modify_availability()
            print(coffee)
        elif which_coffee == 'latte':
            coffee = coffees[1]
            check_modify_availability()
            print(coffee)
        elif which_coffee == 'cappuccino':
            coffee = coffees[2]
            check_modify_availability()
            print(coffee)
        elif which_coffee == 'nothing':
            print('thanks for your time')
            return
        elif which_coffee == 'report':
            print(
                f"water: {machine_resources['water']} ml\nmilk: {machine_resources['milk']} ml\ncoffee powder: {machine_resources['coffee_powder']} g\ncash: ${machine_resources['money']}")
        else:
            print('learn to type fuck face')
            game()

    check_order()




game()
