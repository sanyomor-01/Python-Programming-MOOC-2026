# Write your solution here
def spruce(height):
    star = '*'
    space = height-1
    i = 1
    print('a spruce!')
    while i <= height:
        print(f"{' '*space}{star}{' '*space}")
        star    += "**"
        space   -= 1
        i       += 1
    print(f"{' '*(height-1)}*{' '*height}")



# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)