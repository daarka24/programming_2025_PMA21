from student import Student
import csv
from typing import List


def read_students(filename: str) -> List[Student]:
    students = []
    try:
        with open(filename, encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    grades = [int(g.strip()) for g in row["Grades"].split(",")]
                    students.append(Student(
                        first_name=row["First name"],
                        last_name=row["Last name"],
                        date=row["Date"],
                        grades=grades
                    ))
                except ValueError as e:
                    print(f"Помилка: {row['Last name']} {row['First name']}: {e}")
                except KeyError as e:
                    print(f"Відсутнє поле в CSV: {e}")
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено")
    except Exception as e:
        print(f"Помилка читання файлу: {e}")
    return students


def save_failed(students: List[Student], filename: str) -> None:
    try:
        with open(filename, "w", encoding="utf-8", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['First name', 'Last name', 'Date', 'Grades'])
            writer.writeheader()

            for s in students:
                if not s.passed_session():
                    writer.writerow({
                        'First name': s.first_name,
                        'Last name': s.last_name,
                        'Date': s.date,
                        'Grades': ', '.join(map(str, s.grades))
                    })
    except PermissionError:
        print(f"Немає доступу до файлу '{filename}'")
    except Exception as e:
        print(f"Помилка запису файлу: {e}")


if __name__ == "__main__":
    students = read_students("input.csv")
    if students:
        save_failed(students, "failed_students.csv")
        print("Готово!")
    else:
        print("Немає студентів для обробки")
