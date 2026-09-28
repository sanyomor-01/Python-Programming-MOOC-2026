def line(length, text):
    if text:
        print(text[0] * length)
    else:
        print('*' * length)


def triangle(size):
    i = 1
    while i <= size:
        line(i, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
