from project_person_cls import Person
from project_utils import *


class Student(Person):
    def __init__(self, ID: str, name: str, age: str):
        super().__init__(ID, name, age)

        grades_str = input_until_valid(
            "Enter grades separated by commas: ", self.is_valid_grades, "Grades must be numbers separated by commas."
        )
        self.grades = self.parse_grades(grades_str)

        self.field_of_study = input("Enter field of study: ").strip()

        self.year_of_study = input_until_valid(
            "Enter year of study: ", self.is_valid_year_of_study, "Year must be a positive number."
        )

        self.average_score = self.get_average_score()

    def is_valid_grades(self, grades_str: str) -> bool:
        return all(g.strip().isdigit() for g in grades_str.split(",") if g.strip())

    def add_grades(self, new_grades) -> None:
        self.grades.extend(new_grades)

    def parse_grades(self, grades_str: str) -> list[int]:
        return [int(g.strip()) for g in grades_str.split(",") if g.strip().isdigit()]

    def get_average_score(self) -> float:
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

    def is_valid_year_of_study(self, year: str) -> bool:
        return year.isdigit() and 1 <= int(year) <= 6

    def __str__(self) -> str:
        return (
            f"{super().__str__()}, Type=Student, "
            f"Field={self.field_of_study}, Year={self.year_of_study}, "
            f"Grades={self.grades}, Average Score={self.get_average_score():.2f}"
        )

    def to_dict(self):
        base = super().to_dict()
        base.update(
            {
                "Field": self.field_of_study,
                "Year": self.year_of_study,
                "Grades": ", ".join(map(str, self.grades)),
                "Average": self.get_average_score(),
            }
        )
        return base

    def my_func(self):
        print(f"I'm a student and my name is {self.name}.")
