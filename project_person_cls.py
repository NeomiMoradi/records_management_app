class Person:
    def __init__(self, ID: str, name: str, age: int):
        self.ID = ID
        self.name = name
        self.age = int(age)

    def get_id(self) -> str:
        return self.ID

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return self.age

    def __str__(self) -> str:
        return f"ID={self.ID}, Name={self.name}, Age={self.age}"

    def to_dict(self):
        return {"ID": self.ID, "Name": self.name, "Age": self.age}

    def my_func(self):
        print(f"I'm a person and my name is {self.name}.")
