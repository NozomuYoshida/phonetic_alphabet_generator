# Phonetic code words generator
import pandas

data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_dictionary = {row.letter: row.code for (index, row) in data_frame.iterrows()}

is_correct_input = False
while not is_correct_input:
    letter_list = list(input('What\'s you name?: ').upper())
    try:
        phonetic_code_words_list = [phonetic_dictionary[letter] for letter in letter_list]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
    else:
        is_correct_input = True
        print(phonetic_code_words_list)
        break


