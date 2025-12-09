from datetime import datetime
from typing import List

class Student:
    def __init__(self, first_name: str, last_name: str, dob: str, grades: List[int]):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = datetime.strptime(dob, "%Y-%m-%d").date()
        self.grades = grades
    def has_failed_session(self, passing_grade: int = 60) -> bool:
        return any(grade < passing_grade for grade in self.grades)
    def __str__(self):
        return (f"ПІБ: {self.last_name} {self.first_name}\n"
                f"Дата народження: {self.date_of_birth.strftime('%d.%m.%Y')}\n"
                f"Оцінки: {', '.join(map(str, self.grades))}")
def read(filename: str) -> List[Student]:
    students = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            # Обробляємо файл по 4 рядки на кожного студента
            for i in range(0, len(lines), 4):
                if len(lines) >= i + 4:
                    first_name = lines[i].strip()
                    last_name = lines[i + 1].strip()
                    dob = lines[i + 2].strip()
                    grades_str = lines[i + 3].strip().split(',')
                    grades = [int(g.strip()) for g in grades_str if g.strip().isdigit()]
                    student = Student(first_name, last_name, dob, grades)
                    students.append(student)
    except FileNotFoundError:
        print(f"Помилка: Файл '{filename}' не знайдено.")
    except Exception as e:
        print(f"Помилка під час читання файлу: {e}")
    return students
def find(students: List[Student], passing_grade: int = 60):
    failed_students = []
    for student in students:
        if student.has_failed_session(passing_grade):
            failed_students.append(student)
    if failed_students:
        print("Студенти, які не склали сесію (оцінка < 60)")
        for student in failed_students:
            print(student)
    else:
        print("Усі студенти успішно склали сесію!")
if __name__ == "__main__":
    file_name = "students.txt"
    passing = 60
    all_students = read(file_name)
    if all_students:
        print(f"Зчитано {len(all_students)} студентів.")
        find(all_students, passing)