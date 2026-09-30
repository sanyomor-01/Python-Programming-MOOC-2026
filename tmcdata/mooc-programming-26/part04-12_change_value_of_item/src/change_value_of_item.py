# Write your solution here
new_list = [1,2,3,4,5]

while True:
    index = int(input('Index: '))
    if index < 0 or index > len(new_list) -1:
        break

    value = int(input('New Value: '))
    new_list[index] = value
    print(new_list)
