import pandas

{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ")

nato_word_list = [nato_dict[letter] for letter in word.upper()]

print(nato_word_list)
