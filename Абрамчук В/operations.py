def add_student(students, student_id, name, course, specialty, grade):
    if student_id in students:
        return f"Помилка: Студент з ID {student_id} вже існує."
    students[student_id] = {
        "ім'я": name,
        "курс": course,
        "спеціальність": specialty,
        "середній_бал": grade
    }
    return f"Додано студента {name} (ID: {student_id})"

def delete_student(students, student_id):
    if student_id in students:
        name = students[student_id]["ім'я"]
        del students[student_id]
        return f"Видалено студента {name} (ID: {student_id})"
    return f"Студента з ID {student_id} не знайдено"

def update_student(students, student_id, field, value):
    if student_id in students:
        if field in students[student_id]:
            old_value = students[student_id][field]

            try:
                if field == "курс":
                    value = int(value)
                elif field == "середній_бал":
                    value = float(value)
            except ValueError:
                return f"Помилка: Неправильний тип даних для поля '{field}'."

            students[student_id][field] = value
            return f"Оновлено {field}: {old_value} → {value} для студента ID {student_id}"
        return f"Поле '{field}' не існує"
    return f"Студента з ID {student_id} не знайдено"
