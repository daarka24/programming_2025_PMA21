from dataclasses import dataclass

PASSING_GRADE = 51

@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    grades_list: list

    def get_average(self):
        if not self.grades_list:
            return 0
        return sum(self.grades_list) / len(self.grades_list)

    def has_passed(self):
        return self.get_average() >= PASSING_GRADE


def parse_student_line(line_text, line_index):
    parts = [p.strip() for p in line_text.strip().split('|')]
    if len(parts) != 4:
        return None, f"Line {line_index}: Expected 4 fields separated by '|', but got {len(parts)}"

    first_name, last_name, birth_date, grades_text = parts

    if not first_name:
        return None, f"Line {line_index}: First name is empty"
    if not last_name:
        return None, f"Line {line_index}: Last name is empty"
    if not birth_date:
        return None, f"Line {line_index}: Birth date is empty"

    try:
        grades_list = [int(g.strip()) for g in grades_text.split(',') if g.strip()]
        if not grades_list:
            return None, f"Line {line_index}: No valid grades found"
    except:
        return None, f"Line {line_index}: Invalid grade format. Grades must be integers separated by commas."

    student_obj = Student(first_name, last_name, birth_date, grades_list)
    return student_obj, None


def load_students(input_path):
    students_data = []
    parse_errors = []
    try:
        with open(input_path, 'r') as file:
            for i, line_text in enumerate(file, 1):
                if not line_text.strip():
                    continue
                student_obj, error_msg = parse_student_line(line_text, i)
                if error_msg:
                    parse_errors.append(error_msg)
                else:
                    students_data.append(student_obj)
    except:
        parse_errors.append(f"Error: Cannot open file '{input_path}' or an unexpected error occurred.")
    return students_data, parse_errors


def save_failed_students(students_data, parse_errors, output_path):
    failed_list = [s for s in students_data if not s.has_passed()]
    try:
        with open(output_path, 'w') as file:
            if parse_errors:
                file.write("ERRORS FOUND DURING FILE READING:\n\n")
                for err in parse_errors:
                    file.write(f"- {err}\n")
                file.write("\n")

            file.write(f"Successfully processed: {len(students_data)} students\n\n")

            if not failed_list:
                file.write("All students passed the session!\n")
            else:
                file.write(f"Students who failed the session ({len(failed_list)}):\n\n")
                for student_obj in failed_list:
                    avg_score = student_obj.get_average()
                    file.write(f"Name: {student_obj.first_name} {student_obj.last_name}\n")
                    file.write(f"Birth date: {student_obj.birth_date}\n")
                    file.write(f"Grades: {', '.join(map(str, student_obj.grades_list))}\n")
                    file.write(f"Average grade: {avg_score:.2f}\n\n")

        print(f"Report successfully generated in '{output_path}'")
    except:
        print(f"Error: Could not write to file '{output_path}'.")


input_path = "data.txt"
output_path = "result.txt"

students_data, parse_errors = load_students(input_path)
save_failed_students(students_data, parse_errors, output_path)
