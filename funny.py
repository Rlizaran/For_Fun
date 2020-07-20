student_grades = {
    'Joe': [90, 80, 70, 100],
    'Mark': [80, 99, 71, 99],
    'Ivanka': [90, 69, 100, 88]
}

""" student_grades_avg = {}

for student, scores in student_grades.items():
    avg = sum(scores) / len(scores)
    student_grades_avg[student] = avg

print(student_grades_avg) """

student_grades_avg = {}


def calc_avg(scores):
    avg = sum(scores) / len(scores)
    return avg

# for student, scores in student_grades.items():
#     student_grades_avg[student] = calc_avg(scores)
# # print(student_grades_avg)






print(calc_avg([90,80,70]))