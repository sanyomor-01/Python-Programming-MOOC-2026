def remove_smallest(numbers: list):
    small = numbers[0]
    for item in numbers:
        if item < small:
            small = item
    numbers = numbers.remove(small)


if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)