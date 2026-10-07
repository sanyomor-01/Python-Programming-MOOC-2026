# Write your solution here
def most_common_character(my_string: str):
    best_char = my_string[0]
    best_count = 0

    for char in my_string:
        current_count = 0

        for next_char in my_string:
            if char == next_char:
                current_count = current_count + 1

        if current_count > best_count:
            best_count = current_count
            best_char = char
    return best_char


if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))