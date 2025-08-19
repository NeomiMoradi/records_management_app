from enum import Enum, auto


class MenuOption(Enum):
    SAVE_NEW_ENTRY = auto()
    SEARCH_BY_ID = auto()
    PRINT_AVERAGE_AGE = auto()
    PRINT_NAMES = auto()
    PRINT_IDS = auto()
    PRINT_ALL = auto()
    PRINT_BY_INDEX = auto()
    SAVE_TO_CSV = auto()
    EXIT = auto()
