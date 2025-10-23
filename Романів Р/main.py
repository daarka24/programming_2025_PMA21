from student import Student
import csv


def input_students_from_file(filename):
    data = []
    with open(filename, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                grades = [int(n) for n in row["Grades"].split(",")]

                if len(grades) != 4:
                    raise ValueError("Оцінок має бути 4")

                data.append(Student(
                    row["First name"],
                    row["Last name"],
                    row["Date"],
                    grades
                ))
            except ValueError as e:
                print(f"{row['Last name']} {row['First name']}: {e}")
    return data


def did_not_passed(students, filename):
    new_students = [student for student in students if not all(map(lambda n: int(n) >= 51, student.grades))]
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Студенти, які не здали:\n")
        for index, student in enumerate(new_students):
            file.write(f"{index+1}. {student.last_name} {student.first_name}\n")

if __name__ == "__main__":
    students = input_students_from_file("input.csv")

    did_not_passed(students, "output.txt")


    print("All students:")
    for index, student in enumerate(students):
        print(f"{index+1}. {student}")