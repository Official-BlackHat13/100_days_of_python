from random import randint

# black jack
list_of_cards = [
    # ACES:
    # [1, 11], [1, 11], [1, 11], [1, 11],
    # COMMONS
    2, 2, 2, 2,
    3, 3, 3, 3,
    4, 4, 4, 4,
    5, 5, 5, 5,
    6, 6, 6, 6,
    7, 7, 7, 7,
    8, 8, 8, 8,
    9, 9, 9, 9,
    10, 10, 10, 10,
    # JACKS:
    10, 10, 10, 10,
    # QUEENS:
    10, 10, 10, 10,
    # KINGS:
    10, 10, 10, 10
]

comp_cards = []
user_cards = []
comp_total = sum(comp_cards)
user_total = sum(user_cards)
len_of_list = len(list_of_cards)
def game():
    should_continue = input('type \'y\' to get another card or \'n\' to pass: ')

    def choosen_card():
        global list_of_cards
        random_card = randint(0, len_of_list - 1)
        print(random_card)
        card = list_of_cards[random_card]
        print(card)
        list_of_cards.remove(list_of_cards[random_card])
        if card == [1, 11]:
            print('hello')
        return card

    if should_continue == 'y':
        comp_cards.append(choosen_card())
        user_cards.append(choosen_card())

        print(f'computer\'s first card: {comp_cards}\nyour card(s): {user_cards}, current score: {sum(user_cards)}')
        game()

game()