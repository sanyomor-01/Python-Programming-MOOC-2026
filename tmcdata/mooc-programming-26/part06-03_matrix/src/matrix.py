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

