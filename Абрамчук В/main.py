inputfile = "student.txt"
outfile = "result.txt"


def load_students():
    students = {}
    try:
        with open(inputfile, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue

                parts = line.split('|')
                command = parts[0]

                if command not in ['ADD', 'DELETE', 'UPDATE', 'SHOW', 'SHOW_ALL']:
                    try:
                        student_id = parts[0]
                        students[student_id] = {
                            "name": parts[1],
                            "course": int(parts[2]),
                            "specialty": parts[3],
                            "average_grade": float(parts[4])
                        }
                    except (IndexError, ValueError):
                        print(f"Warning: Skipped corrupted data line: {line}")

    except FileNotFoundError:
        pass
    return students


def save_students(students):
    lines_to_keep = []

    try:
        with open(inputfile, 'r') as f:
            all_lines = f.readlines()

        for line in all_lines:
            stripped = line.strip()
            if not stripped or stripped.startswith('#'):
                lines_to_keep.append(line)
                continue

            parts = stripped.split('|')
            command = parts[0]

            if command in ['ADD', 'DELETE', 'UPDATE', 'SHOW', 'SHOW_ALL']:
                lines_to_keep.append(line)

    except FileNotFoundError:
        pass

    with open(inputfile, 'w') as f:
        for student_id, data in students.items():
            line = f"{student_id}|{data['name']}|{data['course']}|{data['specialty']}|{data['average_grade']}\n"
            f.write(line)

        f.writelines(lines_to_keep)


def add_student(students, student_id, name, course, specialty, grade):
    students[student_id] = {
        "name": name,
        "course": course,
        "specialty": specialty,
        "average_grade": grade
    }
    return f"Added student {name} (ID: {student_id})"


def delete_student(students, student_id):
    if student_id in students:
        name = students[student_id]["name"]
        del students[student_id]
        return f"Deleted student {name} (ID: {student_id})"
    return f"Student with ID {student_id} not found"


def update_student(students, student_id, field, value):
    if student_id in students:
        if field in students[student_id]:
            old_value = students[student_id][field]

            try:
                if field == "course":
                    value = int(value)
                elif field == "average_grade":
                    value = float(value)
            except ValueError:
                return f"Error: Invalid value '{value}' for field '{field}'"

            students[student_id][field] = value
            return f"Updated {field}: {old_value} -> {value} for student ID {student_id}"
        return f"Field '{field}' does not exist"
    return f"Student with ID {student_id} not found"


def show_student(students, student_id):
    if student_id in students:
        student = students[student_id]
        result = f"\nStudent ID: {student_id}\n"
        for key, value in student.items():
            result += f"  {key}: {value}\n"
        return result
    return f"Student with ID {student_id} not found"


def show_all_students(students):
    if not students:
        return "Dictionary is empty"

    result = "\nAll students:\n" + "=" * 50 + "\n"
    for student_id, data in students.items():
        result += f"\nID: {student_id}\n"
        for key, value in data.items():
            result += f"  {key}: {value}\n"
    return result


def process_commands():
    students = load_students()
    output_lines = []

    output_lines.append("=" * 60)
    output_lines.append("AVAILABLE COMMANDS:")
    output_lines.append("=" * 60)
    output_lines.append("ADD|student_id|name|course|specialty|grade  - add student")
    output_lines.append("DELETE|student_id                           - delete student")
    output_lines.append("UPDATE|student_id|field|new_value           - update data")
    output_lines.append("SHOW|student_id                             - show student")
    output_lines.append("SHOW_ALL                                    - show all")
    output_lines.append("=" * 60)
    output_lines.append("")

    try:
        with open(inputfile, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        output_lines.append(f"File {inputfile} not found!")
        with open(outfile, 'w') as f_out:
            f_out.write('\n'.join(output_lines))
        print(f"File {inputfile} not found! Report created in {outfile}.")
        return

    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue

        parts = line.split('|')
        command = parts[0].strip()

        if command not in ['ADD', 'DELETE', 'UPDATE', 'SHOW', 'SHOW_ALL']:
            continue

        output_lines.append(f"\nCommand: {line}")
        output_lines.append("-" * 50)

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

        except (IndexError, ValueError) as e:
            output_lines.append(f"Error in command (incorrect number of arguments or data type): {str(e)}")
        except Exception as e:
            output_lines.append(f"Unknown error: {str(e)}")

    save_students(students)

    with open(outfile, 'w') as f:
        f.write('\n'.join(output_lines))

    print(f"Processing complete! Results written to {outfile}")
    print(f"Updated data and commands saved to {inputfile}")


if __name__ == "__main__":
    process_commands()