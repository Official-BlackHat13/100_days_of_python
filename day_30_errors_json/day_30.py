# FileNotFound

try:
    file = open('file.txt')
    a_dictionary = {'kak': 'a'}
    print(a_dictionary['kak'])
except FileNotFoundError:
    file = open('a_file.txt', 'w')
    file.write('somehtnsdsd')
except KeyError as error_message:
    print(f'{error_message}as')
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print(f'file was closed')