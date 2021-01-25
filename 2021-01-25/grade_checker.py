
# Ask for the student's name
# Ask for the grade of that student
# Return whether  that student passed or not

def get_passing_grade():
    return 80

def check_student_passed(student_grade):
    if student_grade >= get_passing_grade():
        passed = True
    else:
        passed = False
    return passed

def student_message(student_grade):
    if student_grade >= get_passing_grade():
        message = f'{name} has passed.'
    else:
        message = f'{name} has failed.'
    return message

def set_student_info(name, grade):
    return {
        'name': name,
        'grade': grade,
        'passed': check_student_passed(grade)
    }

name = input('What is your name: ')
grade = int(input('What is your grade: '))
student1 = set_student_info(name, grade)
message = student_message(grade)
print(message)
print(student1)

name = input('What is your name: ')
grade = int(input('What is your grade: '))
student2 = set_student_info(name, grade)
message = student_message(grade)
print(message)
print(student2)

name = input('What is your name: ')
grade = int(input('What is your grade: '))
student3 = set_student_info(name, grade)
message = student_message(grade)
print(message)
print(student3)