from datetime import datetime


class Student:
    def __init__(self, first_name=None, last_name=None, date=None, grades=None):
        self.first_name = first_name
        self.last_name = last_name

        if isinstance(date, str):
            try:
                self.date = datetime.strptime(date, "%d.%m.%Y").strftime("%d.%m.%Y")
            except ValueError:
                self.date = None
                print(f"Помилка: '{date}' має неправильний формат дати. Очікується 'дд.мм.рррр'.")
        elif isinstance(date, datetime):
            self.date = date.strftime("%d.%m.%Y")
        else:
            self.date = None

        self.grades = grades


    def __repr__(self):
        return f"Студент, якого звати {self.last_name} {self.first_name}, народився {self.date} та має оцінки: {self.grades}"

    def __str__(self):
        return self.__repr__()



if __name__ == "__main__":
    pass
