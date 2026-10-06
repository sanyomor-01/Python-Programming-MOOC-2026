# Write your solution here
def all_the_longest(words):
    l_words = []

    for word in words:
        if l_words== [] or len(word)> len(l_words[0]):
            l_words = [word]
        elif len(word) == len(l_words[0]):
            l_words.append(word)
    return l_words


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) 