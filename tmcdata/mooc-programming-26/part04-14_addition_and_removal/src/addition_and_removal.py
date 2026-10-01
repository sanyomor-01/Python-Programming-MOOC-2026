# Write your solution here
d_list = []
counter = 0
print(f'The list is now {d_list}')

while True:
    choice = input('a(d)d, (r)emove or e(x)it: ')

    if choice == 'd':
        d_list.append(counter + 1)
        print(f'The list is now {d_list}')
        counter += 1

    elif choice == 'r':
        d_list.remove(counter)
        print(f'The list is now {d_list}')

        counter -= 1
    elif choice == 'x':
        print(f'Bye!')
        break

