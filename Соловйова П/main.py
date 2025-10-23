from datetime import datetime
from typing import List
class Student:
    def __init__(self, name: str, surname: str, birth_date: str, grades: List[int]):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.grades = grades

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def has_failed_session(self, passing_grade: int = 3):
        return self.get_average_grade() < passing_grade

    def get_age(self):
        try:
            birth = datetime.strptime(self.birth_date, "%d.%m.%Y")
            today = datetime.now()
            age = today.year - birth.year
            if today.month < birth.month or (today.month == birth.month and today.day < birth.day):
                age -= 1
            return age
        except ValueError:
            return "Невірний формат дати"

    def __str__(self):
        return f"{self.get_full_name()} (Дата народження: {self.birth_date}, Оцінки: {self.grades}, Середній бал: {self.get_average_grade():.2f})"


def read_students_from_file(filename: str) -> List[Student]:
    students = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) >= 4:
                        name = parts[0].strip()
                        surname = parts[1].strip()
                        birth_date = parts[2].strip()
                        grades_str = parts[3].strip()

                        grades = []
                        if grades_str:
                            try:
                                grades = [int(grade.strip()) for grade in grades_str.split()]
                            except ValueError:
                                print(f"Помилка парсингу оцінок для {name} {surname}")
                                grades = []

                        student = Student(name, surname, birth_date, grades)
                        students.append(student)
                    else:
                        print(f"Невірний формат рядка: {line}")

        print(f"Успішно завантажено {len(students)} студентів з файлу '{filename}'")
        return students

    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено")
        return []
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return []


def find_failed_students(students: List[Student], passing_grade: int = 3) -> List[Student]:
    failed_students = []

    for student in students:
        if student.has_failed_session(passing_grade):
            failed_students.append(student)

    return failed_students


def display_failed_students(students: List[Student], passing_grade: int = 3):
    failed_students = find_failed_students(students, passing_grade)

    if not failed_students:
        print(f"Всі студенти склали сесію! (мінімальний бал: {passing_grade})")
        return

    print(f"\n СТУДЕНТИ, ЯКІ НЕ СКЛАЛИ СЕСІЮ ")
    print(f"Мінімальний бал для складання: {passing_grade}")
    print(f"Кількість студентів, які не склали: {len(failed_students)}\n")

    for i, student in enumerate(failed_students, 1):
        print(f"{i}. {student}")
        print(f"   Вік: {student.get_age()}")
        print(f"   Оцінки: {student.grades}")
        print(f"   Середній бал: {student.get_average_grade():.2f}")
        print()


def display_all_students(students: List[Student]):
    if not students:
        print("Список студентів порожній")
        return

    print(f"\n ВСІ СТУДЕНТИ ({len(students)} осіб) ")
    for i, student in enumerate(students, 1):
        status = " НЕ СКЛАВ" if student.has_failed_session() else " СКЛАВ"
        print(f"{i}. {student} - {status}")

if __name__ == "__main__":
    print("СИСТЕМА УПРАВЛІННЯ СТУДЕНТАМИ ")

    students = read_students_from_file("students.txt")

    if students:
        display_all_students(students)

        display_failed_students(students)

        print("\nСТАТИСТИКА ")
        total_students = len(students)
        failed_count = len(find_failed_students(students))
        passed_count = total_students - failed_count

        print(f"Загальна кількість студентів: {total_students}")
        print(f"Склали сесію: {passed_count} ({passed_count / total_students * 100:.1f}%)")
        print(f"Не склали сесію: {failed_count} ({failed_count / total_students * 100:.1f}%)")

        if students:
            group_average = sum(student.get_average_grade() for student in students) / len(students)
            print(f"Середній бал по групі: {group_average:.2f}")
    else:
        print("Не вдалося завантажити дані студентів")
        print("Переконайтеся, що файл 'students.txt' існує та має правильний формат")
