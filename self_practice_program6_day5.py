import random

SCHOOL_NAME = "New School Of Learning"
CLASS_NAME = "Class XI"
TOTAL_SUBJECT_MARKS = 50
TOTAL_MARKS = TOTAL_SUBJECT_MARKS * 3
NUMBER_STUDENTS = 10

student_names = []
physics_marks = []
chemistry_marks = []
mathematics_marks = []

def input_student_data():
    for i in range(NUMBER_STUDENTS):
        name = input("Enter name of student: ")
        student_names.append(name)

        physics_marks.append(random.randint(0, TOTAL_SUBJECT_MARKS))
        chemistry_marks.append(random.randint(0, TOTAL_SUBJECT_MARKS))
        mathematics_marks.append(random.randint(0, TOTAL_SUBJECT_MARKS))


def print_report():
    for i in range(NUMBER_STUDENTS):

        total_student_marks = (
            physics_marks[i]
            + chemistry_marks[i]
            + mathematics_marks[i]
        )

        phys_perc = round((physics_marks[i] / TOTAL_SUBJECT_MARKS) * 100, 2)
        chem_perc = round((chemistry_marks[i] / TOTAL_SUBJECT_MARKS) * 100, 2)
        math_perc = round((mathematics_marks[i] / TOTAL_SUBJECT_MARKS) * 100, 2)
        overall_perc = round((total_student_marks / TOTAL_MARKS) * 100, 2)

        print(f"\n{SCHOOL_NAME} - {CLASS_NAME} - {student_names[i]}")
        print("-" * 71)
        print(f"| {'Subject':^15} | {'Total Marks':^15} | {'Marks Obtained':^15} | {'Percentage':^13} |")
        print("-" * 71)
        print(f"| {'Physics':^15} | {TOTAL_SUBJECT_MARKS:^15} | {physics_marks[i]:^15} | {phys_perc:^13} |")
        print(f"| {'Chemistry':^15} | {TOTAL_SUBJECT_MARKS:^15} | {chemistry_marks[i]:^15} | {chem_perc:^13} |")
        print(f"| {'Mathematics':^15} | {TOTAL_SUBJECT_MARKS:^15} | {mathematics_marks[i]:^15} | {math_perc:^13} |")
        print("-" * 71)
        print(f"| {'Total':^15} | {TOTAL_MARKS:^15} | {total_student_marks:^15} | {overall_perc:^13} |")
        print("-" * 71)


input_student_data()
print_report()