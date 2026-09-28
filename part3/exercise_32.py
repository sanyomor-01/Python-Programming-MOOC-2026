# square of hashes
def hash_square(number):
    hashes = '#' * number

    while number > 0:
        print(hashes)
        number -= 1


# Testing the function
if __name__ == '__main__':
    hash_square(3)