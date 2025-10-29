from datetime import date, datetime


class Student:
    def __init__(self, name, surname, birthday, marks):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.marks = marks
    def __str__(self):
        return f'{self.name} {self.surname} {str(self.birthday)} {self.marks}'
    def talon(self):
        for mark in self.marks:
            if int(mark) < 51:
                print(self)
                return True
        return False
group = []
with open("students.txt", "r") as f:
    for line in f:
        line = line.strip().split()
        name = line[0]
        surname = line[1]
        birthday = datetime.strptime(line[2], "%Y-%m-%d").date() #перетворюємо рядок в об'єкт типу дейттайм
        marks = line[3:]
        student = Student(name, surname, birthday, marks)
        group.append(student)
for student in group:
    print(student)
print("\nStudents failed session:")
with open("talonniky.txt", "w") as f:
    for student in group:
        if student.talon():
            f.write(student.__str__())






