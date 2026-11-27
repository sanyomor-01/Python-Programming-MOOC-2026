student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

students = {}

with open(student_info) as std_file:
    for line in std_file:
        line = line.strip()

        if line == '':
            continue
        parts = line.split(";")

        if parts[0] == 'id':
            continue
        students[parts[0]] = f'{parts[1]} {parts[2]}'


exercise_info = {}

with open(exercise_data) as exe_file:
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


# Student and total number of exercise data
for id, name in students.items():
    if id in exercise_info:
        total_exe = 0
        for number in exercise_info[id]:
            total_exe += number

        print(f'{name} {total_exe}')
    