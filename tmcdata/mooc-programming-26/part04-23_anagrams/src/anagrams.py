# Write your solution here
def anagrams(f_word : str, s_word: str):
    return sorted(f_word) == sorted(s_word)

if __name__ == '__main__':
    print(anagrams("Mich", 'Mcih'))