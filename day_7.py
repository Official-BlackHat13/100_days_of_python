import random
# hangman
random_words = ['desktop', 'telephone', 'monday']
guess = input('guess a letter: ').lower()

print(guess)

chosen_word = random.choice(random_words)

for letter in chosen_word:
    if letter == guess:
        print('innit')
    else:
        print('try again')        
