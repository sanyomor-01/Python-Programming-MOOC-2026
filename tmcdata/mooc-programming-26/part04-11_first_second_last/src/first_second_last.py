# Write your solution here
def first_word(sentence):
    i = 0
    length = len(sentence)

    while i < length and sentence[i] == ' ': i += 1
    start = i

    while i< length:
        if sentence[i] == ' ':
            break
        i += 1
    end = i
    return sentence[start:end]

# second word
def second_word(sentence):
    i = 0
    length = len(sentence)

    # space at the begining checkin
    while i < length and sentence[i] == ' ': i += 1
    # skipping first word
    while i < length and sentence[i] != ' ': i += 1
    while i < length and sentence[i] == ' ': i += 1
    start = i

    while i < length and sentence[i] != ' ': i += 1
    end = i
    return sentence[start:end]

# last word
def last_word(sentence):
    i = len(sentence) - 1
    while i >= 0 and sentence[i] == ' ':
        i -= 1
    end = i + 1

    while i >= 0 and sentence[i] != ' ':
        i -= 1
    start = i + 1

    return sentence[start: end]



# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))