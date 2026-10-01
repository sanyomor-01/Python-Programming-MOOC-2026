# Write your solution here
d_list = []

while True:
    item = int(input('New item: '))
    if item == 0:
        print('Bye!')
        break

    d_list.append(item)
    print(f'The list now: {d_list}')
    print(f'The list in order: {sorted(d_list)}')