# students.py
from dataclasses import dataclass, field
from typing import List, Tuple

passing_count = 4
passing_score = 51


@dataclass
class Student:
    Surname: str
    Name: str
    birth: str
    grades: List[int] = field(default_factory=list)

    def full_name(self) -> str:
        return f"{self.Name} {self.Surname}"

    def check_session_failure(self) -> Tuple[bool, str]:

        if len(self.grades) < passing_count:
            return (True, f"Замало оцінок")

        if len(self.grades) > passing_count:
            return (True, f"помилка, вказано забагато оцінок ({len(self.grades)})")

        failing_grades = []
        for grade in self.grades:
            if grade < passing_score:
                failing_grades.append(grade)

        if failing_grades:
            return (True, f"Не склав")

        return (False, "")