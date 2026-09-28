# Find the first substrings, print firt three character slice.

word = input('Please type in a word: ')
char = input('Please type in a character: ')

index = 0
while index +3 <= len(word):
    if word[index] == char:
        print(word[index: index + 3])
    index += 1