# Write your solution here
def greatest_number(a,b,c):
    max_number = a
    if max_number < b:
        max_number = b
    if max_number < c:
        max_number = c

    return max_number
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)