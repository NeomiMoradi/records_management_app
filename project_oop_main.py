import pandas as pd
from typing import Type
from project_menu_cls import MenuOption
from project_state_keys_cls import StateKeys
from project_utils import *
from project_person_cls import Person
from project_student_cls import Student
from project_employee_cls import Employee


def display_menu() -> str:
    print("============ Menu ============")
    for option in MenuOption:
        print(f"{option.value}. {option.name.replace('_', ' ').title()}")
    print("==============================")
    return input(
        f"Select option {next(iter(MenuOption)).value}-{list(MenuOption)[-1].value} or Enter to refresh: "
    )


def select_person_type(person_types: list[Type[Person]]) -> Type[Person] | None:
    print("Select person type:")
    for i, person in enumerate(person_types):
        print(f"{i}. {person.__name__}")

    choice = input("Enter number (or Enter to cancel): ").strip()
    if not choice:
        return None
    if not choice.isdigit() or not (0 <= int(choice) < len(person_types)):
        print("Invalid choice.")
        return None
    return person_types[int(choice)]


def print_error(field: str) -> None:
    errors = {
        "ID": "ID must be a number with 9 or 10 digits.",
        "age": "Age must be a number between 0 and 120.",
        "name": "Name must contain only letters, spaces, or hyphens.",
        "exists": "ID already exists.",
        "data": "No data available.",
        "field": "Field must be a non-empty name.",
    }


def input_new_entry(person_cls: Type[Person]) -> Person | None:
    ID = input("Enter ID: ")
    if not is_valid_ID(ID):
        print_error("ID")
        return None

    name = input("Enter name: ")
    if not is_valid_name(name):
        print_error("name")
        return None

    age = input("Enter age: ")
    if not is_valid_age(age):
        print_error("age")
        return None

    return person_cls(ID, name, age)


def save_new_object(person: Person, state: dict) -> None:
    ID = person.get_id()
    if not is_new_ID(ID, state):
        print_error("exists")
        return

    state[StateKeys.DATA_DICT][ID] = person
    state[StateKeys.ID_LIST].append(ID)
    state[StateKeys.TOTAL_AGE] += person.get_age()
    state[StateKeys.ENTRY_COUNT] += 1

    print("Entry saved successfully.")


def print_entry(ID: str, state: dict) -> None:
    if ID in state[StateKeys.ID_LIST]:
        print(state[StateKeys.DATA_DICT][ID])
    else:
        print(f"ID {ID} does not exist.")


def is_data_available(state: dict) -> bool:
    if not state[StateKeys.DATA_DICT]:
        print_error("data")
        return False
    return True


def search_ID(ID: str, state: dict) -> None:
    if not is_data_available(state):
        return
    print_entry(ID, state)


def print_ages_average(state: dict) -> None:
    if state[StateKeys.ENTRY_COUNT] == 0:
        print_error("data")
    else:
        print(
            f"Average age: {state[StateKeys.TOTAL_AGE] / state[StateKeys.ENTRY_COUNT]:.2f}"
        )


def print_data(state: dict, type: str = "all") -> None:
    if not is_data_available(state):
        return
    match type:
        case "names":
            for person in state[StateKeys.DATA_DICT].values():
                print(f"ID={person.ID}, Name={person.name}")
        case "ids":
            for ID in state[StateKeys.DATA_DICT]:
                print(f"ID={ID}")
        case "all":
            for ID in state[StateKeys.DATA_DICT]:
                print_entry(ID, state)


def print_by_index(state: dict) -> None:
    if not state[StateKeys.ID_LIST]:
        print("No data.")
        return
    idx = input("Enter index: ")
    if not idx.isdigit() or not (0 <= int(idx) < len(state[StateKeys.ID_LIST])):
        print("Invalid index.")
        return
    print_entry(state[StateKeys.ID_LIST][int(idx)], state)


def save_df_to_csv(state: dict) -> None:
    if not is_data_available(state):
        return
    data_rows = [
        obj.to_dict() for obj in state[StateKeys.DATA_DICT].values()
    ]  # list of dict of each obj
    df = pd.DataFrame(data_rows)

    filename = input("Enter base filename (without extension): ").strip()
    if not filename:
        filename = "data"
    full_filename = f"{filename}.csv"
    df.to_csv(full_filename, index=False)
    print(f"Data saved to {full_filename}")


def main() -> None:
    state = {
        StateKeys.DATA_DICT: {},
        StateKeys.ID_LIST: [],
        StateKeys.TOTAL_AGE: 0,
        StateKeys.ENTRY_COUNT: 0,
    }
    person_types = [Student, Employee, Person]

    try:
        while True:
            choice = display_menu()
            if choice == "":
                continue
            try:
                selected_option = MenuOption(int(choice))
            except (ValueError, KeyError):
                print(f"Invalid choice: {choice}")
                continue
            while True:
                try:
                    if selected_option == MenuOption.SAVE_NEW_ENTRY:
                        person_cls = select_person_type(person_types)
                        if not person_cls:
                            break
                        obj = input_new_entry(person_cls)
                        if obj:
                            save_new_object(obj, state)

                    elif selected_option == MenuOption.SEARCH_BY_ID:
                        ID = input("Enter ID: ")
                        if not is_valid_ID(ID):
                            print_error("ID")
                            break
                        search_ID(ID, state)

                    elif selected_option == MenuOption.PRINT_AVERAGE_AGE:
                        print_ages_average(state)

                    elif selected_option == MenuOption.PRINT_NAMES:
                        print_data(state, "names")

                    elif selected_option == MenuOption.PRINT_IDS:
                        print_data(state, "ids")

                    elif selected_option == MenuOption.PRINT_ALL:
                        print_data(state, "all")

                    elif selected_option == MenuOption.PRINT_BY_INDEX:
                        print_by_index(state)

                    elif selected_option == MenuOption.SAVE_TO_CSV:
                        save_df_to_csv(state)

                    elif selected_option == MenuOption.EXIT:
                        if (
                            input("Are you sure you want to exit? (y/n): ").lower()
                            == "y"
                        ):
                            print("Goodbye!")
                            return
                        else:
                            break

                    repeat_mode = choice in {"1", "2", "7"}
                    if repeat_mode:
                        again = input("Repeat? (y/n) or Enter to menu: ").lower()
                        if again != "y":
                            break
                    else:
                        input("Press Enter to menu: ")
                        break

                except Exception as e:
                    print(f"An error occurred: {e}")

    except KeyboardInterrupt:
        print("\nExiting program. Goodbye!")


if __name__ == "__main__":
    main()
