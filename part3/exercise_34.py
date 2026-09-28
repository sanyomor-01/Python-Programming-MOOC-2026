def squared(text, size):
    i = 0
    index = 0

    while i < size:
        j = 0
        row = ''
        while j < size:
            row     += text[index % len(text)]
            index   += 1
            j       += 1
        print(row)
        i += 1

if __name__ == '__main__':
    squared('Preconception', 6)