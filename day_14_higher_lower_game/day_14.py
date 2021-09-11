# higher lower game
from game_data import *
from random import randint

def game():
    def chose_account():
        global accounts
        random_number = randint(0, len(accounts) - 1)
        random_account = accounts[random_number]
        accounts.remove(accounts[random_number])
        return random_account

    name1 = chose_account()
    print(name1)
    print('\nVS\n')
    name2 = chose_account()
    print(name2)
    user_guess = input('which one got more followers?: ')


game()