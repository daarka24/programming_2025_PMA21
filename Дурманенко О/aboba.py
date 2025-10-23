from dataclasses import dataclass
passing_grade = 51
@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    grades: list
    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    def passed_session(self):
        return self.get_average_grade() >= passing_grade
def _parse_student_line(line, line_number):
    parts = [p.strip() for p in line.strip().split('|')]
    if len(parts) != 4:
        return None, f"Line {line_number}: Expected 4 fields separated by '|', but got {len(parts)}"
    first_name, last_name, birth_date, grades_str = parts
    if not first_name:
        return None, f"Line {line_number}: First name is empty"
    if not last_name:
        return None, f"Line {line_number}: Last name is empty"
    if not birth_date:
        return None, f"Line {line_number}: Birth date is empty"
    try:
        grades = [int(g.strip()) for g in grades_str.split(',') if g.strip()]
        if not grades:
            return None, f"Line {line_number}: No valid grades found"
    except:
        return None, f"Line {line_number}: Invalid grade format. Grades must be integers separated by commas."
    student = Student(first_name, last_name, birth_date, grades)
    return student, None
def read_students_from_file(filename):
    students = []
    errors = []
    try:
        with open(filename, 'r') as file:
            for i, line in enumerate(file, 1):
                if not line.strip():
                    continue
                student, error = _parse_student_line(line, i)
                if error:
                    errors.append(error)
                else:
                    students.append(student)
    except:
        errors.append(f"Error: Cannot open file '{filename}' or an unexpected error occurred.")
    return students, errors
def write_failed_students(students, errors, output_filename):
    failed_students = [s for s in students if not s.passed_session()]
    try:
        with open(output_filename, 'w') as file:
            if errors:
                file.write("ERRORS FOUND DURING FILE READING:\n\n")
                for error in errors:
                    file.write(f"- {error}\n")
                file.write("\n")
            file.write(f"Successfully processed: {len(students)} students\n\n")
            if not failed_students:
                file.write("All students passed the session!\n")
            else:
                file.write(f"Students who failed the session ({len(failed_students)}):\n\n")
                for student in failed_students:
                    avg = student.get_average_grade()
                    file.write(f"Name: {student.first_name} {student.last_name}\n")
                    file.write(f"Birth date: {student.birth_date}\n")
                    file.write(f"Grades: {', '.join(map(str, student.grades))}\n")
                    file.write(f"Average grade: {avg:.2f}\n\n")
        print(f"Report successfully generated in '{output_filename}'")
    except:
        print(f"Error: Could not write to file '{output_filename}'.")
input_filename = "students.txt"
output_filename = "failed_students.txt"
students, errors = read_students_from_file(input_filename)
write_failed_students(students, errors, output_filename)