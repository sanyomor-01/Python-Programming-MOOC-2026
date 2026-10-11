# Write your solution here
def longest(words: list):
    length = 0
    l_word = ''
    for word in words:
        if len(word) > length:
            length = len(word)
            l_word = word
    return(l_word)

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))