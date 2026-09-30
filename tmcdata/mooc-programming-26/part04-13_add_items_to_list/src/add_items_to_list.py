# Write your solution here
items_count = int(input('How many items: '))

c_lists = []
i= 1

while i <= items_count:
    items = int(input(f'Item {i}: '))
    c_lists.append(items)
    i += 1
print(c_lists)
