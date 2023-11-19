def get_count(word):
    """ Returns number of vowels and consonants in a word """

    # Adjust the word
    word = word.lower()
    vowels = "aeiouy"
    num_vowels = 0

    # Literally count
    for vowel in vowels:
        num_vowels += word.count(vowel)

    # Return numbers
    return num_vowels, len(word) - num_vowels

# Get input
words = input("Enter a sentence: ").split()

total_vowels = 0
total_consonants = 0

for word in words:
    vowel_count, consonant_count = get_count(word)
    total_vowels += vowel_count
    total_consonants += consonant_count

print(f"There are {total_vowels} vowel(s) and {total_consonants} consonant(s)")
