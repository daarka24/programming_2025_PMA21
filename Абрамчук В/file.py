import os
from config import INPUT_FILE, KNOWN_COMMANDS

def load_students():
    students = {}
    if not os.path.exists(INPUT_FILE):
        return students

    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue

                parts = line.split('|')
                if parts[0] not in KNOWN_COMMANDS:
                    student_id = parts[0]
                    try:
                        students[student_id] = {
                            "ім'я": parts[1],
                            "курс": int(parts[2]),
                            "спеціальність": parts[3],
                            "середній_бал": float(parts[4])
                        }
                    except (IndexError, ValueError) as e:
                        print(f"Помилка завантаження рядка (пропущено): {line} | {e}")
    except FileNotFoundError:
        pass
    return students

def save_students(students):
    lines_to_write = []
    command_lines = []

    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            all_lines = f.readlines()
    except FileNotFoundError:
        all_lines = []

    for line in all_lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            lines_to_write.append(line)
        elif stripped.split('|')[0] in KNOWN_COMMANDS:
            command_lines.append(line)
        else:
            pass

    for student_id, data in students.items():
        line = f"{student_id}|{data['ім\'я']}|{data['курс']}|{data['спеціальність']}|{data['середній_бал']}\n"
        lines_to_write.append(line)

    if command_lines:
        lines_to_write.append("\n# Команди для обробки\n")
        lines_to_write.extend(command_lines)

    with open(INPUT_FILE, 'w', encoding='utf-8') as f:
        f.writelines(lines_to_write)
