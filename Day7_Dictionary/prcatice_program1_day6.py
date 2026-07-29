# PROG 1: School Result

import random


def calculate_grade(percentage):
    if percentage > 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 30:
        return "D"
    else:
        return "F"


def create_students():
    students = {}

    for i in range(1, 21):
        name = f"Student{i}"
        gender = random.choice(["M", "F"])

        physics = round(random.uniform(0, 50), 1)
        chemistry = round(random.uniform(0, 50), 1)
        maths = round(random.uniform(0, 50), 1)

        attendance = random.randint(1, 120)

        total = round(physics + chemistry + maths, 1)
        percentage = round((total / 150) * 100, 2)
        attendance_percentage = round((attendance / 120) * 100, 2)

        grade = calculate_grade(percentage)

        if grade == "F" or percentage < 30:
            remark = "Failed, work hard to do better next time"
        else:
            remark = "Congratulations!, Passed Successfully"

        students[name] = {
            "Gender": gender,
            "Physics": physics,
            "Chemistry": chemistry,
            "Maths": maths,
            "Attendance": attendance,
            "Attendance Percentage": attendance_percentage,
            "Total": total,
            "Percentage": percentage,
            "Grade": grade,
            "Remark": remark
        }

    return students


def display_by_percentage(students):

    # means students = {name , {details}}
    # students[details][percentage]
    sorted_students = sorted(students.items(), key=lambda x: x[1]["Percentage"],reverse=True )

    for name, data in sorted_students:
        print("-" * 50)
        print(f"Name: {name}")
        print(f"Gender: {data['Gender']}")
        print("Marks:")
        print(f"- Physics: {data['Physics']}")
        print(f"- Chemistry: {data['Chemistry']}")
        print(f"- Maths: {data['Maths']}")
        print(f"Attendance: {data['Attendance']}")
        print(f"Total Marks: {data['Total']:.1f}/150")
        print(f"Percentage Marks: {data['Percentage']:.2f}%")
        print(f"Attendance: {data['Attendance']}")
        print(f"Grade: {data['Grade']}")
        print(f"Remarks: {data['Remark']}")


def display_by_grade(students):
    grade_order = ["A+", "A", "B", "C", "D", "F"]

    for grade in grade_order:
        for name, data in students.items():
            if data["Grade"] == grade:
                print("-" * 50)
                print(f"Name: {name}")
                print(f"Gender: {data['Gender']}")
                print("Marks:")
                print(f"- Physics: {data['Physics']}")
                print(f"- Chemistry: {data['Chemistry']}")
                print(f"- Maths: {data['Maths']}")
                print(f"Attendance: {data['Attendance']}")
                print(f"Total Marks: {data['Total']:.1f}/150")
                print(f"Percentage Marks: {data['Percentage']:.2f}%")
                print(f"Attendance: {data['Attendance']}")
                print(f"Grade: {data['Grade']}")
                print(f"Remarks: {data['Remark']}")


def display_summary(students):
    total_students = len(students)

    passed = [s for s in students.items() if s[1]["Percentage"] >= 30]
    pass_percentage = (len(passed) / total_students) * 100

    print("-" * 50)
    print("Summary:")
    print(f"Overall Pass Percentage: {pass_percentage:.1f}%")

    print("Grade-wise Percentage Distribution:")
    grades = ["A+", "A", "B", "C", "D", "F"]

    for grade in grades:
        count = sum(1 for s in students.values() if s["Grade"] == grade)
        print(f"- Grade {grade}: {(count / total_students) * 100:.1f}%")

    topper = max(students.items(), key=lambda x: x[1]["Total"])
    print(f"Top Student: {topper[0]}")

    physics_topper = max(students.items(), key=lambda x: x[1]["Physics"])
    chemistry_topper = max(students.items(), key=lambda x: x[1]["Chemistry"])
    maths_topper = max(students.items(), key=lambda x: x[1]["Maths"])

    print("Top Students Subject-wise:")
    print(f"- Physics: {physics_topper[0]}")
    print(f"- Chemistry: {chemistry_topper[0]}")
    print(f"- Maths: {maths_topper[0]}")

    print("List of Students Who Passed (Alphabetically sorted):")
    passed_alpha = sorted(passed, key=lambda x: x[0])

    for name, data in passed_alpha:
        print(f"- {name}: {data['Percentage']:.2f}% ({data['Grade']})")

    print("List of Students Who Passed (Sorted based on Total Marks):")
    passed_marks = sorted(passed,key=lambda x: x[1]["Total"],reverse=True)

    for name, data in passed_marks:
        print(f"- {name}: {data['Total']:.1f}/150 "f"({data['Percentage']:.2f}%, {data['Grade']})")


def main():
    students = create_students()

    choice = input(
        "Enter 'grade' to display results by grade or 'percentage' to display results by percentage: "
    ).lower()

    if choice == "grade":
        display_by_grade(students)
    elif choice == "percentage":
        display_by_percentage(students)
    else:
        print("Invalid Choice")
        return

    display_summary(students)


main()