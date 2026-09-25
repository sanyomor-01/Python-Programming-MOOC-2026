# Please write a program which asks the user for two strings and then prints out whichever is 
# the longer of the two - that is, whichever has the more characters. 
# If the strings are of equal length, the program should print out "The strings are equally long".

# Solution 
string_1 = input('Please type in string 1: ')
string_2 = input('Please type in string 2: ')

if len(string_1) > len(string_2):
    print(f'{string_1} is longer')
elif len(string_2) > len(string_1):
    print(f'{string_2} is longer')
else:
    print('The strings are equally long')