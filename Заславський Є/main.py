from student import Student

students = []

with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split()
        name = parts[0]
        surname = parts[1]
        birth_date = parts[2]
        grades = list(map(int, parts[3:]))
        students.append(Student(name, surname, birth_date, grades))
for s in students:
    if s.has_failed():
        print("Не склав сесію:")
    else:
        print("Склав сесію:")
    s.print_info()
    print()
