# Write your solution here
def mean(numbers):
    size = len(numbers)
    acc = 0
    i = 0
    while i < size:
        acc += numbers[i]
        i += 1
    return acc/ size
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)