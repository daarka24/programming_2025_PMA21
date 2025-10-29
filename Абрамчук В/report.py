def show_student(students, student_id):
    if student_id in students:
        student = students[student_id]
        result = f"\nСтудент ID: {student_id}\n"
        for key, value in student.items():
            result += f"  { key}: {value}\n"
        return result
    return f"Студента з ID {student_id} не знайдено"

def show_all_students(students):
    if not students:
        return "Список студентів порожній"

    result = "\nВсі студенти:\n" + "=" * 50 + "\n"
    for student_id, data in students.items():
        result += f"\nID: {student_id}\n"
        for key, value in data.items():
            result += f"  {key}: {value}\n"
    return result

def show_failed_students(students, min_passing_score):

    failed_students_info = []
    for student_id, data in students.items():
        if data['середній_бал'] < min_passing_score:
            failed_students_info.append((student_id, data))

    if not failed_students_info:
        return f"Студентів з середнім балом < {min_passing_score} не знайдено."

    result = f"\nСтуденти, що не склали сесію (бал < {min_passing_score}):\n" + "=" * 50 + "\n"
    for student_id, data in failed_students_info:
        result += f"ID: {student_id}, Ім'я: {data['ім\'я']}, Бал: {data['середній_бал']}\n"

    return result
