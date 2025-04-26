import json
import os

DATA_FILE = "grades_data.txt"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_student(data):
    name = input("Enter student's name: ").strip()
    if name in data:
        print("Student already exists. Adding new grades to existing student.")
    else:
        data[name] = {}
    while True:
        subject = input("Enter subject name (or type 'done' to finish): ").strip()
        if subject.lower() == 'done':
            break
        try:
            grade = float(input(f"Enter grade for {subject}: "))
            if 0 <= grade <= 100:
                data[name][subject] = grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid grade input. Please enter a number.")
    save_data(data)
    print(f"Grades saved for {name}.")

def calculate_average(student_grades):
    if not student_grades:
        return 0
    return sum(student_grades.values()) / len(student_grades)

def view_student(data):
    name = input("Enter student's name to view: ").strip()
    if name not in data:
        print("Student not found.")
        return
    grades = data[name]
    print(f"\n--- {name.upper()}'s REPORT ---")
    for subject, grade in grades.items():
        print(f"{subject}: {grade}")
    average = calculate_average(grades)
    print(f"\nAverage Grade: {average:.2f}")

def view_all_students(data):
    if not data:
        print("No student data available.")
        return
    for name, grades in data.items():
        print(f"\n--- {name.upper()}'s REPORT ---")
        for subject, grade in grades.items():
            print(f"{subject}: {grade}")
        average = calculate_average(grades)
        print(f"Average Grade: {average:.2f}")

def menu():
    data = load_data()
    while True:
        print("\n=== STUDENT GRADE TRACKER ===")
        print("1. Add Student and Grades")
        print("2. View a Student's Report")
        print("3. View All Students' Reports")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_student(data)
        elif choice == '2':
            view_student(data)
        elif choice == '3':
            view_all_students(data)
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
