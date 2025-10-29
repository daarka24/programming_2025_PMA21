from config import INPUT_FILE, OUTPUT_FILE, KNOWN_COMMANDS
from file import load_students, save_students
from operations import add_student, delete_student, update_student
from report import show_student, show_all_students, show_failed_students

def get_help_text():
    lines = [
        "=" * 60,
        "ДОСТУПНІ КОМАНДИ:",
        "=" * 60,
        "ADD|student_id|name|course|specialty|grade  - додати студента",
        "DELETE|student_id                           - видалити студента",
        "UPDATE|student_id|field|new_value           - оновити дані",
        "SHOW|student_id                             - показати студента",
        "SHOW_ALL                                    - показати всіх",
        "SHOW_FAILED|min_score                       - показати 'двієчників'",
        "=" * 60,
        ""
    ]
    return '\n'.join(lines)

def process_commands():
    students = load_students()
    output_lines = [get_help_text()]

    command_lines_to_process = []
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue

                parts = line.split('|')
                command = parts[0].strip()

                if command in KNOWN_COMMANDS:
                    command_lines_to_process.append(line)

    except FileNotFoundError:
        output_lines.append(f"Файл {INPUT_FILE} не знайдено! Створено новий.")
        pass

    if not command_lines_to_process:
        output_lines.append("Команд для обробки у файлі не знайдено.")

    for line in command_lines_to_process:
        output_lines.append(f"\nКоманда: {line}")
        output_lines.append("-" * 50)

        parts = line.split('|')
        command = parts[0].strip()

        try:
            if command == "ADD":
                result = add_student(students, parts[1], parts[2],
                                     int(parts[3]), parts[4], float(parts[5]))
                output_lines.append(result)

            elif command == "DELETE":
                result = delete_student(students, parts[1])
                output_lines.append(result)

            elif command == "UPDATE":
                result = update_student(students, parts[1], parts[2], parts[3])
                output_lines.append(result)

            elif command == "SHOW":
                result = show_student(students, parts[1])
                output_lines.append(result)

            elif command == "SHOW_ALL":
                result = show_all_students(students)
                output_lines.append(result)

            elif command == "SHOW_FAILED":
                min_score = float(parts[1])
                result = show_failed_students(students, min_score)
                output_lines.append(result)

        except (IndexError, ValueError) as e:
            output_lines.append(f"Помилка в команді: {str(e)}. Перевірте кількість аргументів.")

    save_students(students)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))

    print(f"Обробка завершена! Результати записано в {OUTPUT_FILE}")
    print(f"Оновлену базу студентів збережено в {INPUT_FILE}")
