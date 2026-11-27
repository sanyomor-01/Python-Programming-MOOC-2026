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



