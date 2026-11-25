def add_student(students: dict, name: str):
    students[name] = []

def print_student(students: dict, name: str):
    if name in students:
        print(f"{name}: ")
        if len(students[name]) == 0 :
            print(' no completed courses')
#        else:
#            print(f'{len(students[name])} completed courses')
    else:
        print(f'{name}: no such person in the database')

#def add_courses(students: dict, name: str, courses: tuple):
#    students[name].append(courses)


if __name__ == '__main__':
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")