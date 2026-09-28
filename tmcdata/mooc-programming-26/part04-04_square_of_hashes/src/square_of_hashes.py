# Copy here code of line function from previous exercise
def line(length, text):
    if text:
        print(text[0] * length)
    else:
        print('*' * length)
        
def square_of_hashes(size):
        l_size = size
        while size > 0:
             line(l_size, "#")
             size -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
