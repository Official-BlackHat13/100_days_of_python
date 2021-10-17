import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def generate_password():
    password = ''

    for letter in range(4):
        random_letters = random.randint(0, 52)
        password += letters[random_letters - 1]

    for symbol in range(4):
        random_symbols = random.randint(0, 9)
        password += symbols[random_symbols - 1]

    for number in range(4):
        random_numbers = random.randint(0, 10)
        password += numbers[random_numbers - 1]

    list_password = list(password)
    random.shuffle(list_password)
    password = ''.join(list_password)
    return password

