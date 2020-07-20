# student_grades = {
#     'Joe': [90, 80, 70, 100],
#     'Mark': [80, 99, 71, 99],
#     'Ivanka': [90, 69, 100, 88]
# }

# """ student_grades_avg = {}

# for student, scores in student_grades.items():
#     avg = sum(scores) / len(scores)
#     student_grades_avg[student] = avg

# print(student_grades_avg) """

# student_grades_avg = {}


# def calc_avg(scores):
#     avg = sum(scores) / len(scores)
#     return avg

# # for student, scores in student_grades.items():
# #     student_grades_avg[student] = calc_avg(scores)
# # # print(student_grades_avg)





# print(calc_avg([90,80,70]))

def total_pay_net(hours, hourly_pay):
    '''calculates the weeks pay
    Assumes that 10% of the gross pay will be deducted

    Parameters
    --------
    hours : float
        the number of hours worked for the week
    hourly_pay : float
        the hourly payment

    Returns
    -------
    float
        the gross pay expected
        the net pay expected'''
    gross_pay = hours * hourly_pay
    net_pay = gross_pay * 0.90
    monthly_payment = net_pay * 4
    print(f'Your gross pay is: ${gross_pay:.2f}')
    print(f'Your net pay is: ${net_pay:.2f}')
    print(f'You montlhy pay is: ${monthly_payment:.2f}')
    

    return net_pay, gross_pay, monthly_payment
print('Introduce horas trabajadas')
horas = input()
print('Introduce pago por horas')
Payment = input()
total_pay_net(float(horas), float(Payment))