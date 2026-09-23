# Please change the program from the previous exercise so that the user gets to input 
# also the base which ismultiplied (in the previous program the base was always 2).
# Please don't use the value True as the condition of your while loop in this exercise!

# solution
limit = int(input('Upper limit: '))
base = int(input('Base: '))
number = 1

while number <= limit:
    print(number)
    number *= base