# Factorial
while True:
    number = int(input('Please type in a number: '))

    if number <= 0:
        print('Thanks and bye!')
        break

    results = 1
    num = 1
    while num <= number:
        results *= num
        num += 1

    print(f'The factorial of the number {number} is {results}')
