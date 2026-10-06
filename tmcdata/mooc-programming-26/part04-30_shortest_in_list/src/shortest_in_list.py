# Write your solution here
def shortest(words):
    s_word = words[0]
    for word in words:
        if len(word) < len(s_word):
            s_word = word
    return s_word


if __name__ == '__main__':
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)