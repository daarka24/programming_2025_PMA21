import ast

class Student:
    def __init__(self, name, surname, birthdate, grades_dict):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.grades_dict = grades_dict

    def is_session_passed(self):
        for key, value in self.grades_dict.items():
            if value < 51:
                return f"Student: {self.name} {self.surname}, subject: {key}, grade: {value} | RESULT: FAILED."
        return None

    def print_student(self):
        return f"{self.name}, {self.surname}, {self.birthdate}, {self.grades_dict}"

class Students:
    def __init__(self):
        self.students_list = []

    def add_student(self, student: Student):
        self.students_list.append(student)

    def print_students(self):
        for student in self.students_list:
            print(student.print_student())

    def print_failed_students(self):
        f = 0
        for student in self.students_list:
            result = student.is_session_passed()
            if result is not None:
                print(result)
                f += 1
        if f == 0:
            print("All students passed their subjects.")

def is_correct_line(line, n):
    data = [d.strip() for d in line.split(",", 3)]
    expected_size = 4
    if len(data) != expected_size:
        raise ValueError(f"error: unexpected size: {len(data)} arguments, size of line idx-{n} must be: {expected_size} arguments.")

    name, surname, birthdate, subject_dict = data
    try:
        subjects = ast.literal_eval(subject_dict)
    except ValueError as e:
        raise ValueError(f"error {e}")

    new_student = Student(name, surname, birthdate, subjects)

    return new_student

def read_file(file):
    students = []
    with open(file, "r") as r:
        for n, line in enumerate(r):
            line = line.strip()
            try:
                new_student = is_correct_line(line, n)
                #new_student.print_student()
                students.append(new_student)
                n+=1
            except ValueError as e:
                raise ValueError(f"{e}")
    return students


if __name__=="__main__":
    try:
        students = read_file("students.txt")
    except ValueError as e:
        print(f"{e}")
        exit(1)

    student_list = Students()
    n = len(students)
    for i in range(n):
        student_list.add_student(students[i])

    student_list.print_students()

    student_list.print_failed_students()