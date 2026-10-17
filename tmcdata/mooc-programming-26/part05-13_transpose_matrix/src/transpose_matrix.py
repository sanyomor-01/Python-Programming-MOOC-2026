def transpose(matrix: list):
    size = len(matrix)

    for row in range(size):
        for col in range(row + 1, size):
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp


if __name__ == "__main__":
    matrics = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
    print(f"Original: {matrics}")
    transpose(matrics)
    print(f"Transposed: {matrics}")



