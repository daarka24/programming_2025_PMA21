class Student:
    def __init__(self, name, surname, birth_date, grades):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.grades = grades

def read_students(filename):
    students = []
    with open(filename, 'r', encoding='utf-8') as f:
        n = int(f.readline().strip())
        for _ in range(n):
            parts = f.readline().strip().split()
            name, surname, birth_date = parts[:3]
            m = int(parts[3])
            grades = list(map(int, parts[4:4 + m]))
            students.append(Student(name, surname, birth_date, grades))
    return students

def failed_students(students):
    return [s for s in students if any(g < 51 for g in s.grades)]

def print_student(s):
    print(f"{s.name} {s.surname} ({s.birth_date}) — оцінки: {', '.join(map(str, s.grades))}")

def main():
    students = read_students("students.txt")

    failed = failed_students(students)

    with open("results.txt", "w", encoding="utf-8") as f:
        f.write("Студенти, які не склали сесію:\n\n")
        if not failed:
            f.write("Усі студенти склали сесію\n")
        else:
            for s in failed:
                f.write(f"{s.name} {s.surname} ({s.birth_date}) — оцінки: {', '.join(map(str, s.grades))}\n")

if __name__ == "__main__":
    main()
