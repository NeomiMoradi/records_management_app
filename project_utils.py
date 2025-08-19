import re
from project_state_keys_cls import StateKeys


def is_valid_ID(ID: str) -> bool:
    return ID.isdigit() and len(ID) in (9, 10)


def is_new_ID(ID: str, state: dict) -> bool:
    return ID not in state[StateKeys.ID_LIST]


def is_valid_name(name: str) -> bool:
    return re.match(r"^[\u0590-\u05FFa-zA-Z\s-]+$", name) is not None


def is_valid_age(age: str) -> bool:
    return age.isdigit() and 0 <= int(age) <= 120


def input_until_valid(prompt: str, validate_func, error_message: str) -> str:
    while True:
        value = input(prompt).strip()
        if validate_func(value):
            return value
        print(error_message)



    
    print(errors.get(field, "Invalid input."))



