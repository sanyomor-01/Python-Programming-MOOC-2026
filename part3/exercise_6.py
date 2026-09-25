# The sum of consecutive numbers, version 1

# Please write a program which asks the user to type in a limit. 
# The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) 
# until the sum is at least equal to the limit set by the user. 

# Solution
limit = int(input('Upper limit: '))
total = 0
number = 1
while total < limit:
     total += number
     number+= 1

print(total)

