# Write your solution here
def sum_of_positives(numbers):
    acc = 0
    for i in numbers:
        if i > 0:
            acc += i
    return acc

if __name__ == '__main__':
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)