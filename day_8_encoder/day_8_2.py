import day_8
# check if the number prime or not
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input('type \'ecnode\' to encrypt or \'decode\' to decrypt: ')
text = input('type your message: ').lower().replace('', ' ').split()
shift = int(input('type your shift number: '))
encrypted_word = ''


def encrypt(text_func, shift_func, encrypted_word_func):
    for l in range(len(text_func)):
        position = letters.index(text[l])
        encrypted_word_func += letters[position + shift_func]
    print(encrypted_word_func)

if direction == 'encode':
    encrypt(text_func=text, shift_func=shift, encrypted_word_func=encrypted_word)


# kakaK






