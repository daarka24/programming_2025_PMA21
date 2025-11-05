from students import Student, passing_count, passing_score
from typing import List

INPUT_FILE = "students.txt"
OUTPUT_FILE = "output.txt"


def read_from_file(filename: str) -> List[Student]:
    students = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(',')

                if len(parts) < 3:
                    print(f"неправильний формат рядка, пропускаємо: {line}")
                    continue

                try:
                    name_from_file = parts[0]
                    surname_from_file = parts[1]
                    birth_from_file = parts[2]

                    grades = []
                    if len(parts) > 3:
                        grades = [int(grade) for grade in parts[3:]]

                    student = Student(
                        Surname=surname_from_file,
                        Name=name_from_file,
                        birth=birth_from_file,
                        grades=grades
                    )
                    students.append(student)

                except ValueError:
                    print(f"Некоректні оцінки, пропускаємо рядок: {line}")
                except Exception as e:
                    print(f"Помилка обробки рядка {line}: {e}")

    except FileNotFoundError:
        print(f"Помилка файл не знайдено.")


    return students


def write_failing_students(student_list: List[Student], output_filename: str):
    failing_data = []

    for student in student_list:
        failed, reason = student.check_session_failure()
        if failed:
            failing_data.append((student, reason))

    try:
        with open(output_filename, 'a') as f:
            if not failing_data:
                f.write("Всі студенти успішно склали сесію.\n")
                return

            f.write(f"Студенти, які не склали сесію:\n")


            for student, reason in failing_data:
                f.write(f"Студент: {student.full_name()} (Дата народження: {student.birth})\n")


    except IOError as e:
        print(f"Помилка запису у файл '{output_filename}': {e}")


def main():
    all_students = read_from_file(INPUT_FILE)

    if all_students:
        write_failing_students(all_students, OUTPUT_FILE)
    else:
        print("Не вдалося зчитати дані студентів. Програма завершує роботу.")


if __name__ == "__main__":
    main()

