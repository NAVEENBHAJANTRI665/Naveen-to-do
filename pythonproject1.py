import json
import os

FILE_NAME = "students.json"

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def add_student():
    students = load_data()
    roll = input("Enter Roll Number: ")

    for s in students:
        if s["roll"] == roll:
            print("Student already exists!")
            return

    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    students.append({
        "roll": roll,
        "name": name,
        "marks": marks
    })

    save_data(students)
    print("Student added successfully!")

def view_students():
    students = load_data()
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for s in students:
        print(f"Roll: {s['roll']}")
        print(f"Name: {s['name']}")
        print(f"Marks: {s['marks']}")
        print("----------------------")

def search_student():
    students = load_data()
    roll = input("Enter Roll Number to search: ")

    for s in students:
        if s["roll"] == roll:
            print("\nStudent Found")
            print(f"Roll: {s['roll']}")
            print(f"Name: {s['name']}")
            print(f"Marks: {s['marks']}")
            return

    print("Student not found.")

def update_student():
    students = load_data()
    roll = input("Enter Roll Number to update: ")

    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter New Name: ")
            s["marks"] = input("Enter New Marks: ")
            save_data(students)
            print("Student updated successfully!")
            return

    print("Student not found.")

def delete_student():
    students = load_data()
    roll = input("Enter Roll Number to delete: ")

    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            save_data(students)
            print("Student deleted successfully!")
            return

    print("Student not found.")

def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
