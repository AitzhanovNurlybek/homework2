import string

def chech_alphabet(letter):
    letter = letter.lower()

    vowels = "eoaiu"

    if letter in vowels:
        print("letter is vowel")
    elif letter in string.ascii_lowercase:
        print("letter is consonant")

letter = input()

print(chech_alphabet(letter))