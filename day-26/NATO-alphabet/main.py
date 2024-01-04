import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def prompt():
    word = input("Enter a word: ")

    try:
        nato_word_list = [nato_dict[letter] for letter in word.upper()]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        prompt()
    else:
        print(nato_word_list)


prompt()
