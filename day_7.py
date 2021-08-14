import random
# hangman
random_words = ['desktop', 'telephone', 'monday']
guess = input('guess a letter: ').lower()

chosen_word = list(random.choice(random_words))

blank = ['_']

while not len(blank) == len(chosen_word):
    blank += '_'

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        blank[position] = letter
print(blank)
