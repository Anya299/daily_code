# Student Management System (Python 3)

students = []

def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "id": sid,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("✅ Student added successfully\n")


def view_students():
    if not students:
        print("❌ No students found\n")
        return

    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Course: {s['course']}")
    print()


def search_student():
    sid = input("Enter Student ID to search: ")
    for s in students:
        if s["id"] == sid:
            print("🎯 Student Found:", s, "\n")
            return
    print("❌ Student not found\n")


def delete_student():
    sid = input("Enter Student ID to delete: ")
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("🗑 Student deleted successfully\n")
            return
    print("❌ Student not found\n")


def menu():
    while True:
        print("---- Student Management System ----")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("👋 Exiting program")
            break
        else:
            print("❌ Invalid choice\n")


menu()
