import pandas

# 1. CSV ko DataFrame me padho
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# 2. Dictionary banao: {A: Alfa, B: Bravo...}
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# 3. User se word lo
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()