def parse_student(line: str):
    parts = line.strip().split(',')

    if len(parts) < 4:
        print(f"Некоректний формат рядка, пропускаю: '{line}'")
        return None

    try:
        name = parts[0].strip()
        surname = parts[1].strip()
        birth = parts[2].strip()

        grades = [int(g.strip()) for g in parts[3:]]

        student = {
            "name": name,
            "surname": surname,
            "birth": birth,
            "grades": grades
        }
        return student

    except ValueError:
        print(f"Не вдалось розпізнати оцінки в рядку, пропускаю: '{line}'")
        return None
    except Exception as e:
        print(f"Невідома помилка при парсингу рядка '{line}': {e}")
        return None


def load_students_from_file(filename: str):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
        return []

    students = []
    for line in lines:
        line = line.strip()
        if line:
            student = parse_student(line)
            if student:
                students.append(student)

    print(f"Завантажено {len(students)} студент(ів).")
    return students


def generate_student_report(students_list: list, output_filename: str, pass_threshold: int = 60):
    print(f"Починаю генерування...")

    passed_list = []
    failed_list = []

    for student in students_list:
        has_failed_grade = False
        for grade in student['grades']:
            if grade < pass_threshold:
                has_failed_grade = True
                break

        if has_failed_grade:
            failed_list.append(student)
        else:
            passed_list.append(student)

    try:
        with open(output_filename, "w", encoding="utf-8") as f:

            f.write(f"--- Загальний звіт по сесії (Поріг: {pass_threshold}) ---\n")

            f.write("\n--- НЕ СКЛАЛИ ---\n\n")
            if not failed_list:
                f.write("Немає студентів, які не склали сесію.\n")
            else:
                for student in failed_list:
                    f.write(f"Студент: {student['name']} {student['surname']} (Дата нар.: {student['birth']})\n")
                    f.write(f"   Оцінки: {student['grades']}\n\n")

            f.write("\n--- СКЛАЛИ ---\n\n")
            if not passed_list:
                f.write("Немає студентів, які успішно склали сесію.\n")
            else:
                for student in passed_list:
                    f.write(f"Студент: {student['name']} {student['surname']} (Дата нар.: {student['birth']})\n")
                    f.write(f"   Оцінки: {student['grades']}\n\n")

        print(f"Звіт збережено у файл '{output_filename}'.")

    except IOError as e:
        print(f"Помилка запису у файл '{output_filename}': {e}")


students_file = "students.txt"
results_file = "students_result.txt"

all_students = load_students_from_file(students_file)

if all_students:
    generate_student_report(all_students, results_file, 60)
else:
    print(f"Список студентів порожній або файл '{students_file}' не знайдено.")
    print("Завершення роботи.")