from project_person_cls import Person
from project_utils import *

class Employee(Person):

    def __init__(self, ID: str, name: str, age: str):
        super().__init__(ID, name, age)

        self.job_title = input("Enter job title: ").strip()

        self.salary = float(
            input_until_valid("Enter salary: ", self.is_valid_salary, "Salary must be a positive number.")
        )

    def is_valid_salary(self, salary: str) -> bool:
        return salary.isdigit() and int(salary) > 0

    def __str__(self) -> str:
        return (
            f"{super().__str__()}, Type=Employee, "
            f"Job Title={self.job_title}, Salary={self.salary}"
        )

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update(
            {
                "Job Title": self.job_title,
                "Salary": self.salary,
            }
        )
        return base

    def my_func(self):
        print(f"I'm an employee and my name is {self.name}.")
