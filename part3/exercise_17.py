# Please write a program which asks the user to type in a string. 
# The program then prints out all the substrings which begin with the first character, 
# from the shortest to the longest. 

# solution
word =  'Mimi'#input('Word: ')
count = 1

while count <= len(word):
    print(word[:count])
    count += 1
