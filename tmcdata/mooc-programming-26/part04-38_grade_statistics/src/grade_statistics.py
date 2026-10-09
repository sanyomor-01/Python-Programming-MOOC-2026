# Write your solution here
# user inputs

stats = []
while True:
    user_input = input('Exams points and exercises completed: ')

    if user_input == "":
        break

    exam_pts, exercises = user_input.split()
    stats.append([int(exam_pts), int(exercises)])
