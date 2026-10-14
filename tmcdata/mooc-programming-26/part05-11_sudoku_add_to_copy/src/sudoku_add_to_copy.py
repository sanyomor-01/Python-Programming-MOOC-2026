def print_sudoku(sudoku: list):
    for row in range(9):
        if row > 0 and row % 3 == 0:
            print()
        for col in range(9):
            if col > 0 and col % 3 == 0:
                print(' ', end = '')

            value = sudoku[row][col]
            if value == 0:
                print('_', end = ' ')
            else:
                print(value, end = ' ')
        print()

def  copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_sudoku = [[0] * 9 for i in range(9)]

    for row in range(9):
        for col in range(9):
            new_sudoku[row][col] = sudoku[row][col]
    
    new_sudoku[row_no][column_no] = number
    return new_sudoku

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

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)