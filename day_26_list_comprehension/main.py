import pandas

# TODO #1 create 'nato_alphabet_dict' out of 'csv' data
# TODO #2 get and format the message
# TODO #3 create and output the final message
nato_alphabet_data_frame = pandas.read_csv('nato_alphabet.csv')
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet_data_frame.iterrows()}

message = input('Enter your message: ').upper()
list_message = list(message)


final_message = [nato_alphabet_dict[letter] for letter in list_message]
print(final_message)
