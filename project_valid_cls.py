import re


class Validator:
    @staticmethod
    def is_valid_ID(ID: str) -> bool:
        return ID.isdigit() and len(ID) in (9, 10)

    @staticmethod
    def is_new_ID(ID: str, state: dict) -> bool:
        return ID not in state["data_set"]

    @staticmethod
    def is_valid_name(name: str) -> bool:
        return re.match(r"^[\u0590-\u05FFa-zA-Z\s-]+$", name) is not None

    @staticmethod
    def is_valid_age(age: str) -> bool:
        return age.isdigit() and 0 <= int(age) <= 120

    @staticmethod
    def is_valid_grades(grades_str: str) -> bool:
        return all(g.strip().isdigit() for g in grades_str.split(",") if g.strip())

    @staticmethod
    def parse_grades(grades_str: str) -> list[int]:
        return [int(g.strip()) for g in grades_str.split(",") if g.strip().isdigit()]

    @staticmethod
    def is_valid_salary(salary: str) -> bool:
        return salary.isdigit() and int(salary) > 0

    @staticmethod
    def is_valid_year_of_study(year: str) -> bool:
        return year.isdigit() and 1 <= int(year) <= 6  # בהנחה שיש עד 6 שנות לימוד

    @staticmethod
    def input_until_valid(prompt: str, validate_func, field_name: str) -> str:
        while True:
            value = input(prompt).strip()
            if validate_func(value):
                return value
            Validator.print_error(field_name)

    @staticmethod
    def print_error(field: str) -> None:
        errors = {
            "ID": "ID must be a number with 9 or 10 digits.",
            "age": "Age must be a number between 0 and 120.",
            "name": "Name must contain only letters, spaces, or hyphens.",
            "exists": "ID already exists.",
            "grades": "Grades must be numbers separated by commas.",
            "field": "Field must be a non-empty name.",
            "year": "Year must be a positive number.",
            "job": "Job title must not be empty.",
            "salary": "Salary must be a positive number.",
            "data": "No data available.",
        }
        print(errors.get(field, "Invalid input."))
