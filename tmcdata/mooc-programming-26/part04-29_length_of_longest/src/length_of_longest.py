# Write your solution here
def length_of_longest(some_list):
    long = 0

    for word in some_list:
        if len(word) > long:
            long = len(word)
    return long
if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = length_of_longest(my_list)
    print(result)