def histogram(strings: str):
    chars = {}

    for char in strings:
       
        if char not in chars:
            chars[char] = 0

        chars[char] += 1
    for key, value in chars.items():
        print(f"{key} {'*' * value}")


if __name__ == "__main__":
    histogram("abba")