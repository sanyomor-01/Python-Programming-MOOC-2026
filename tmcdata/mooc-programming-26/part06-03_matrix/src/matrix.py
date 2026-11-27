def read_file():
    with open('matrix.txt') as data:
        database = []
    
        for line in data:
            line = line.strip()
            if line != "": # skips empty line from spliting
                number_str = line.split(",")

                # store list of numbers
                row = []
                for number in number_str:
                    row.append(int(number))
                
                database.append(row)

        return database

# Summing rows
def row_sums():
    results_of_each_row = []
    
    data = read_file()
    for row in data:
        accummulator = 0
        for number in row:
            accummulator += number
    
        results_of_each_row.append(accummulator)
    return results_of_each_row

# matrix sum
def matrix_sum():
    results = 0

    data = row_sums()
    for row_sum in data:
        results += row_sum

    return results


# max element in matrix

def matrix_max():
    data = read_file()

    largest = data[0][0]

    for row in data:
        for number in row:
            if number > largest:
                largest = number
    return largest


if __name__ == "__main__":
    print(f'Data: {read_file()}')
    print()
    print(f"Sum of matrix: {matrix_sum()}")
    print()
    print(f'Sum of each row: {row_sums()}')
    print()
    print(f'Maximum number: {matrix_max()}')
    