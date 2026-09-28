# Copy here code of line function from previous exercise and use it in your solution
def line(length, text):
    if text:
        print(text[0] * length)
    else:
        print('*' * length)

def triangle(size, str):
    i = 1
    while i <= size:
        line(i, str)
        i += 1

def shape(t_width, t_text, height, h_text):
    triangle(t_width, t_text)
    j = 1
    while j <= height:
        line(t_width, h_text)
        j += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")