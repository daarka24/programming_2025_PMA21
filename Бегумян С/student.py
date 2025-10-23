class Student:
    def __init__(self, name, surname, birth_date, marks):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.marks = marks

def passed_session(student):
    for mark in student.marks:
        if mark < 51:
            return False
    return True

students = []

try:
    with open("students.txt", "r") as file:
        first = file.readline()
        if not first:
            print("File is empty")
            exit()
        try:
            n = int(first.strip())
        except:
            print("Invalid format for number of students")
            exit()

        for i in range(n):
            line = file.readline()
            if not line:
                print("Not enough lines in file")
                break
            parts = line.strip().split()
            if len(parts) < 4:
                print("Wrong line (no date or no name and else):", line)
            else:
                name = parts[0]
                surname = parts[1]
                birth_date = parts[2]
                marks = []
                bad_marks = False
                for m in parts[3:]:
                    try:
                        marks.append(int(m))
                    except:
                        print("Wrong mark:", line)
                        bad_marks = True
                        break
                if not bad_marks:
                    students.append(Student(name, surname, birth_date, marks))
except:
    print("Cannot open students.txt file")
    exit()

print("Students who failed the session:")
for s in students:
    if not passed_session(s):
        print(s.surname + " " + s.name + " (" + s.birth_date + ")")