def add_student(students: dict, name: str):
    students[name] = []

def print_student(students: dict, name: str):
    if name in students:
        curr_grade = 0

        print(f"{name}: ")
        total_course = len(students[name])

        if total_course == 0 :
            print(' no completed courses')
        else:
            print(f' {total_course} completed course: ')
            for course, grade in students[name]:
                curr_grade += grade
                print(f'  {course} {grade}')

        if total_course == 0:
            print(f' average grade {0.0}')
        else:
            print(f' average grade {curr_grade/total_course}')
    else:
        print(f'{name}: no such person in the database')

def add_course(students: dict, name: str, courses: tuple):
    students[name].append(courses)


if __name__ == '__main__':
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    print_student(students, "Peter")