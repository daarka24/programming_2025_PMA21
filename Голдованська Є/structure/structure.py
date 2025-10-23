class Student:
    def __init__(self, name: str, surname: str, birthday: str, marks: list):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.marks = marks

    def __str__(self):
        return f"{self.name} {self.surname}, дата народження: {self.birthday}, список оцінок:{self.marks}"

def talon(student):
    for mark in student.marks:
        if mark < 51:
            return True
    return False

with open("in.txt", encoding="UTF-8") as file:
    data = file.read().split("\n")

students = []
for student in data:
    student = student.split()
    students.append(Student(student[0],student[1],student[2],[int(mark)for mark in student[3:]]))

talon_students = [student for student in students if talon(student)]

with open("out.txt", "w", encoding="UTF-8") as file:
    file.write("Список усіх студентів:\n\n")
    for student in students:
        file.write(f"{student}\n")
    file.write("\nСписок студентів які не склали сесію:\n\n")
    for student in talon_students:
        file.write(f"{student}\n")