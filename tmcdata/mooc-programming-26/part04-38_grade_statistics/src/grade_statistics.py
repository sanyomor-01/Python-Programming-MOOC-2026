# Write your solution here
# user inputs
total_pts = 0
stats = []
while True:
    user_input = input('Exams points and exercises completed: ')

    if user_input == "":
        break

    exam_pts, exercises = user_input.split()
    stats.append([int(exam_pts), int(exercises)])

# exercise points
def exercise_points(exercises: int):
    exercises // 10


# calculating the grade
def calculate_grad(exam_pts, exercise_pts):
    if exam_pts < 10:
        return 0

    total_points = exam_pts + exercise_pts

    if total_points <= 14:
        return 0
    elif total_points <= 17:
        return 1
    elif total_points <= 20:
        return 2
    elif total_points <= 23:
        return 3
    elif total_points <= 27:
        return 4
    else:
        return 5
    