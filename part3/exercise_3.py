# Please write a program which asks the user for a number. The program then prints out all integer numbers greater than zero but smaller than the input.

limit = int(input('Upper limit: '))
integer = 1

while integer < limit:
    print(integer)
    integer += 1
