# mutiplication

number = int(input('Please type in a number: '))
i = 1

while i <= number:
    start = 1
    while start <= number:
        print(f'{i} x {start} = {i * start}')
        start += 1

    i += 1