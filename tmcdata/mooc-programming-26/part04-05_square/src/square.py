# Copy here code of line function from previous exercise
def line(length, text):
    if text:
        print(text[0] * length)
    else:
        print('*' * length)

def square(size, character):
    l_size = size
    while size > 0:
        line(l_size, character)
        size -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")