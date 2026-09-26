# Find the second occurrence of substrings.

word = input('Please type in a word: ')
sub_str = input('Please type in a character: ')

index = 0
count = 0

while (index + len(sub_str)) <= len(word):
    if word[index: index + len(sub_str)] == sub_str:
        count += 1
        if count == 2:
            s_index = index
        index += len(sub_str)
    else:
        index += 1
if count >= 2:
    print(f'The second occurrence of the substring is at index {s_index}.')
else:
    print('The substring does not occure twice in the string.')