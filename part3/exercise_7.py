# The sum of consecutive numbers, version 2
# Please write a new version of the program in the previous exercise. 
# In addition to the result it should also print out the calculation performed:

# Sample output
# Limit: 2
# The consecutive sum: 1 + 2 = 3

limit = int(input('Limit: '))
total = 1
word = '1'
number = 1
while total < limit:
    number+= 1
    total += number

    word += f" + {number}"

print(f'The consecutive sum: {word} = {total}')