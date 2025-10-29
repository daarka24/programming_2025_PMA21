from dataclasses import dataclass
from datetime import datetime

# structure for student
@dataclass
class Student:
    name: str
    surname: str
    birthdate: datetime
    grades: list

def read_students():
    students = []
    try:
        with open("starters.txt", "r") as file:
            for line in file:
                parts = line.strip().split(";")
                if len(parts) != 4:
                    continue
                name = parts[0]
                surname = parts[1]
                try:
                    birthdate = datetime.strptime(parts[2], "%Y-%m-%d").date()
                except ValueError:
                    print(f"Bad date format for {name} {surname}")
                    continue

                try:
                    grades = [int(x) for x in parts[3].split(",")]
                except ValueError:
                    print(f"Bad grades for {name} {surname}")
                    continue

                students.append(Student(name, surname, birthdate, grades))

    except FileNotFoundError:
        print("File not found.")
    except Exception as error:
        print("Something went wrong:", error)

    return students

def print_failed_students(students):
    failed_students = []
    try:
        with open("result.txt", "w") as out_file:
            out_file.write("Students who failed session:\n")
            for s in students:
                if any(g < 60 for g in s.grades):
                    text = f"{s.name} {s.surname}, born {s.birthdate}, grades: {s.grades}\n"
                    print(text.strip())
                    out_file.write(text)
                    failed_students.append(s)
        print("\nAll failed students saved to 'failed_students.txt'")
    except Exception as e:
        print("Error while writing file:", e)

    return failed_students

students = read_students()
print_failed_students(students)
