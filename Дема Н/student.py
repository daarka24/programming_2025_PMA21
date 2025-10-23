from typing import List
class Student:
    def __init__(self, name, surname, birthdate, grades):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.grades = grades

def read_stud(filename: str) -> List[Student]:
    students = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            name = parts[0]
            surname = parts[1]
            birthdate = parts[2]
            grades = list(map(float, parts[3].split()))
            students.append(Student(name, surname, birthdate, grades))
    return students
def failed_stud(students: List[Student]):
    failed = []
    for student in students:
        if any(grade < 51 for grade in student.grades):
            failed.append(student)
    return failed
students = read_stud("out.txt")
failed = failed_stud(students)
try:
    print("All students\n")
    for s in students:
        print(f"{s.name} {s.surname}, {s.birthdate}, оцінки: {s.grades}")
except FileNotFoundError:
    raise("No file")
try:
    print("\nСтуденти, які не склали сесію\n")
    for s in failed:
        print(f"{s.name} {s.surname}, {s.birthdate}, оцінки: {s.grades}")
except FileNotFoundError:
    raise("No file")

with open("in.txt", "w") as f:
    f.write("All students\n")
    for s in students:
        f.write(f"{s.name} {s.surname}, {s.birthdate}, {s.grades} \n")
    f.write("Failed\n")
    for failed in failed:
        f.write(f"{failed.name} {failed.surname}, {failed.birthdate}, {failed.grades} ")