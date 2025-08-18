# Lists to store student names and grades
students = []
grades = []

# Add a new student and grade
def add_student(name, grade):
    students.append(name)
    grades.append(grade)
    print(f"{name} added with grade {grade}.")

# Update a student's grade
def update_grade(name, new_grade):
    if name in students:
        index = students.index(name)
        grades[index] = new_grade
        print(f"{name}'s grade updated to {new_grade}.")
    else:
        print(f"{name} not found.")

# Remove a student
def remove_student(name):
    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print(f"{name} removed from the list.")
    else:
        print(f"{name} not found.")

# Display average grade
def display_average():
    if grades:
        avg = sum(grades) / len(grades)
        print(f"Average grade: {avg:.2f}")
    else:
        print("No grades to calculate average.")

# Display highest and lowest grade
def display_highest_lowest():
    if grades:
        max_grade = max(grades)
        min_grade = min(grades)
        print(f"Highest grade: {max_grade}")
        print(f"Lowest grade: {min_grade}")
    else:
        print("No grades to analyze.")

# Menu to test functionality
while True:
    print("\n1. Add Student\n2. Update Grade\n3. Remove Student\n4. Display Average\n5. Display Highest & Lowest\n6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        name = input("Enter student name: ")
        grade = float(input("Enter grade: "))
        add_student(name, grade)

    elif choice == '2':
        name = input("Enter student name to update: ")
        grade = float(input("Enter new grade: "))
        update_grade(name, grade)

    elif choice == '3':
        name = input("Enter student name to remove: ")
        remove_student(name)

    elif choice == '4':
        display_average()

    elif choice == '5':
        display_highest_lowest()

    elif choice == '6':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
