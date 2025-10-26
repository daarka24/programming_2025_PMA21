from datetime import datetime
from typing import List


class Student:
    def __init__(self, first_name: str, last_name: str, date: str, grades: List[int]):
        self.first_name = first_name
        self.last_name = last_name
        self.date = self._validate_date(date)
        self.grades = grades

    def _validate_date(self, d: str) -> str:
        try:
            return datetime.strptime(d, "%d.%m.%Y").strftime("%d.%m.%Y")
        except ValueError:
            raise ValueError(f"Невірний формат дати: '{d}'. Очікується формат дд.мм.рррр")

    def passed_session(self) -> bool:
        return all(g >= 51 for g in self.grades)
