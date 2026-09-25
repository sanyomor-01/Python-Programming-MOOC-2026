# Please write a program which asks the user to input a string. The program then prints out different messages if the string contains any of the vowels a, e or o.
# You may assume the input will be in lowercase entirely. Have a look at the examples below.
 

# Write your solution here
word = input('Please type in a string: ')
vowel = 'aeo'
count = 0
while count <= len(vowel)-1:
    if vowel[count] in word:
        print(f'{vowel[count]} found')
    else:
        print(f'{vowel[count]} not found')
    count += 1
    