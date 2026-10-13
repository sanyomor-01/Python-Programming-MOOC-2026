def print_sudoku(sudoku: list):
    for row in range(9):
        if row > 0 and row % 3 == 0:
            print()
        for col in range(9):
            if col > 0 and col % 3 == 0:
                print(' ', end = ' ')

            value = sudoku[row][col]
            if value == 0:
                print('_', end = ' ')
            else:
                print(value, end = ' ')
        print()

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print_sudoku(sudoku)
    # add_number(sudoku, 0, 0, 2)
    # add_number(sudoku, 1, 2, 7)
    # add_number(sudoku, 5, 7, 3)
    # print()
    # print("Three numbers added:")
    # print()
    # print_sudoku(sudoku)