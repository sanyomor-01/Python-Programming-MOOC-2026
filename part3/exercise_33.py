# chessboard
def chessboard(size):
    i = 0
    while i < size:
        j = 0
        row = ''
        while j < size:
            if (i +j) % 2 == 0:
                row += '1'
            else:
                row += '0'
            j += 1
        print(row)
        i += 1

if __name__ == '__main__':
    chessboard(4)