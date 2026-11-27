students = {}

with open('students1.csv') as std_file:
    for line in std_file:
        line = line.strip()

        if line == '':
            continue
        parts = line.split(";")

        if parts[0] == 'id':
            continue
        students[parts[0]] = f'{parts[1]} {parts[2]}'


exercise_info = {}

with open('exercises1.csv') as exe_file:
    # data cleaning
    for line in exe_file:
        line = line.strip()

        if line == '':
            continue
        parts = line.split(';')
        # getting data into dictionary
        id = parts[0]
        if id == 'id':
            continue

        exercise_info[id] = []
        for exercise in parts[1: ]:
            exercise_info[id].append(int(exercise))
print(exercise_info)
    