class Student:
    def __init__(self, name=None, surname=None, birth_date=None, grades=None):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.grades = grades

    def has_failed(self):
        for grade in self.grades:
            if grade < 60:
                return True
        return False

    def print_info(self):
        grades_str = ", ".join(map(str, self.grades))
        print(f"{self.name} {self.surname}, {self.birth_date}, оцінки: {grades_str}")
