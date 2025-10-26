import json

def display_all_students(database):
    print("\n=== All Students ===")
    for student_id, student_info in database.items():
        print(f"ID: {student_id}")
        for key, value in student_info.items():
            print(f"  {key}: {value}")
        print()

def display_single_student(database, student_id):
    try:
        print(f"\n=== Student {student_id} ===")
        for key, value in database[student_id].items():
            print(f"{key}: {value}")
    except:
        print(f"Student {student_id} not found")

def add_new_student(database, student_id, first_name, last_name, age, grade_point_average, major):
    database[student_id] = {"first_name": first_name, "last_name": last_name, "age": age, "grade_point_average": grade_point_average, "major": major}
    print(f"Student {student_id} added successfully")

def delete_student(database, student_id):
    try:
        del database[student_id]
        print(f"Student {student_id} deleted successfully")
    except:
        print(f"Student {student_id} not found")

def update_student_information(database, student_id, field_name, new_value):
    try:
        database[student_id][field_name] = new_value
        print(f"Student {student_id} updated successfully")
    except:
        print(f"Update failed")

def save_to_file(database, filename):
    try:
        with open(filename, 'w') as file_handle:
            json.dump(database, file_handle, indent=4)
        print(f"Data saved to {filename}")
    except:
        print("Save failed")

def load_from_file(filename):
    try:
        with open(filename, 'r') as file_handle:
            return json.load(file_handle)
    except:
        print("Load failed")
        return {}

def main_menu():
    student_database = {}
    filename = input("Enter database filename to load: ")
    student_database = load_from_file(filename)
    while True:
        print("\n=== Student Database Menu ===")
        print("1. Display all students")
        print("2. Display single student")
        print("3. Add new student")
        print("4. Delete student")
        print("5. Update student information")
        print("6. Save to file")
        print("7. Load from file")
        print("8. Exit")
        user_choice = input("Enter your choice: ")
        if user_choice == "1":
            display_all_students(student_database)
        elif user_choice == "2":
            student_id = input("Enter student ID: ")
            display_single_student(student_database, student_id)
        elif user_choice == "3":
            student_id = input("Enter student ID: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            age = int(input("Enter age: "))
            grade_point_average = float(input("Enter GPA: "))
            major = input("Enter major: ")
            add_new_student(student_database, student_id, first_name, last_name, age, grade_point_average, major)
        elif user_choice == "4":
            student_id = input("Enter student ID to delete: ")
            delete_student(student_database, student_id)
        elif user_choice == "5":
            student_id = input("Enter student ID: ")
            field_name = input("Enter field name to update: ")
            new_value = input("Enter new value: ")
            update_student_information(student_database, student_id, field_name, new_value)
        elif user_choice == "6":
            filename = input("Enter filename: ")
            save_to_file(student_database, filename)
        elif user_choice == "7":
            filename = input("Enter filename: ")
            student_database = load_from_file(filename)
        elif user_choice == "8":
            print("Exiting program")
            break
        else:
            print("Invalid choice")

main_menu()