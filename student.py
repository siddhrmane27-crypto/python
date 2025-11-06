student_names = []
student_grades = []

def add_student(name, grade):
    student_names.append(name)
    student_grades.append(grade)
    print(f"Added: {name} with grade {grade}")

def update_grade(name, new_grade):
    if name in student_names:
        index = student_names.index(name)
        student_grades[index] = new_grade
        print(f"Updated: {name}'s grade to {new_grade}")
    else:
        print(f"{name} not found.")

def remove_student(name):
    if name in student_names:
        index = student_names.index(name)
        student_names.pop(index)
        student_grades.pop(index)
        print(f"Removed: {name}")
    else:
        print(f"{name} not found.")

def display_average_grade():
    if student_grades:
        avg = sum(student_grades) / len(student_grades)
        print(f"Average grade: {avg:.2f}")
    else:
        print("No grades to calculate average.")

def display_highest_and_lowest():
    if student_grades:
        print(f"Highest grade: {max(student_grades)}")
        print(f"Lowest grade: {min(student_grades)}")
    else:
        print("No grades available.")

add_student("Abhishek", 80)
add_student("vijay", 100)
add_student("Ranjit", 66)

update_grade("Abhishek", 88)

remove_student("Ranjit")

display_average_grade()

display_highest_and_lowest()
