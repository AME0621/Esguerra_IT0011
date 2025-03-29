import os

# Clear Screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Grade Calculation
def calculate_grade(class_standing, exam_grade):
    return 0.6 * class_standing + 0.4 * exam_grade

# Shows all student records
def show_all_students():
    if not students:
        print("No records found.")
    else:
        for student in students:
            student_id, full_name, class_standing, exam_grade = student
            grade = calculate_grade(class_standing, exam_grade)
            print(f"ID: {student_id}")
            print(f"Name: {full_name[0]} {full_name[1]}")
            print(f"Class Standing: {class_standing}")
            print(f"Major Exam Grade: {exam_grade}")
            print(f"Final Grade: {grade:.2f}")
            print("-" * 30) 

# Order by last name
def order_by_last_name():
    sorted_students = sorted(students, key=lambda x: x[1][1])
    for student in sorted_students:
        student_id, full_name, class_standing, exam_grade = student
        grade = calculate_grade(class_standing, exam_grade)
        print(f"ID: {student_id}")
        print(f"Name: {full_name[0]} {full_name[1]}")
        print(f"Class Standing: {class_standing}")
        print(f"Major Exam Grade: {exam_grade}")
        print(f"Final Grade: {grade:.2f}")
        print("-" * 30) 

# Order by grade
def order_by_grade():
    sorted_students = sorted(students, key=lambda x: calculate_grade(x[2], x[3]), reverse=True)
    for student in sorted_students:
        student_id, full_name, class_standing, exam_grade = student
        grade = calculate_grade(class_standing, exam_grade)
        print(f"ID: {student_id}")
        print(f"Name: {full_name[0]} {full_name[1]}")
        print(f"Class Standing: {class_standing}")
        print(f"Major Exam Grade: {exam_grade}")
        print(f"Final Grade: {grade:.2f}")
        print("-" * 30) 

# Finding specific student by ID
def show_student_record(student_id):
    for student in students:
        if student[0] == student_id:
            full_name, class_standing, exam_grade = student[1], student[2], student[3]
            grade = calculate_grade(class_standing, exam_grade)
            print(f"ID: {student_id}")
            print(f"Name: {full_name[0]} {full_name[1]}")
            print(f"Class Standing: {class_standing}")
            print(f"Major Exam Grade: {exam_grade}")
            print(f"Final Grade: {grade:.2f}")
            return
    print("Student record not found.")

# Adding student's record
def add_record():
    student_id = int(input("\nEnter Student ID (6-digit number): "))
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    full_name = (first_name, last_name)
    class_standing = float(input("Enter Class Standing Grade: "))
    exam_grade = float(input("Enter Major Exam Grade: "))
    students.append((student_id, full_name, class_standing, exam_grade))
    print("\nRecord added successfully.")

# Edit student's record
def edit_record(student_id):
    for idx, student in enumerate(students):
        if student[0] == student_id:
            print(f"Editing record for {student[1][0]} {student[1][1]}")
            new_first_name = input(f"Enter new first name (current: {student[1][0]}): ")
            new_last_name = input(f"Enter new last name (current: {student[1][1]}): ")
            new_class_standing = float(input(f"Enter new class standing grade (current: {student[2]}): "))
            new_exam_grade = float(input(f"Enter new major exam grade (current: {student[3]}): "))
            students[idx] = (student_id, (new_first_name, new_last_name), new_class_standing, new_exam_grade)
            print("\nRecord updated successfully.")
            return
    print("Student record not found.")

# Delete student's record
def delete_record(student_id):
    for idx, student in enumerate(students):
        if student[0] == student_id:
            students.pop(idx)
            print("\nRecord deleted successfully.")
            return
    print("Student record not found.")

# Record management main menu
def menu():
    while True:
        clear_screen()
        print("\n==============================")
        print("    * RECORD  MANAGEMENT *    ")
        print("==============================")
        print("1. Show All Students Record")
        print("2. Order by Last Name")
        print("3. Order by Grade")
        print("4. Show Student Record")
        print("5. Add Record")
        print("6. Edit Record")
        print("7. Delete Record")
        print("8. Exit")
        print("------------------------------")
        choice = input("Enter choice: ")

        if choice == '1':
            print("\nLIST OF ALL STUDENTS")
            print("------------------------------")
            show_all_students()
        elif choice == '2':
            print("\nORDER BY STUDENT'S LAST NAME")
            print("------------------------------")
            order_by_last_name()
        elif choice == '3':
            print("\nORDER BY STUDENT'S GRADE")
            print("------------------------------")
            order_by_grade()
        elif choice == '4':
            student_id = int(input("\nEnter student ID: "))
            show_student_record(student_id)
        elif choice == '5':
            add_record()
        elif choice == '6':
            student_id = int(input("\nEnter student ID to edit: "))
            edit_record(student_id)
        elif choice == '7':
            student_id = int(input("\nEnter student ID to delete: "))
            delete_record(student_id)
        elif choice == '8':
            print("\nExiting program...")
            break
        else:
            print("\nInvalid choice, please try again.")

        input("\nPress Enter to return to the menu...") 

# Run the menu
if __name__ == "__main__":
    students = [] 
    menu()
