from enum import Enum


class WSCEnum(str, Enum):
    snake_case = "snake_case"  # number_of_donuts
    kebab_case = "kebab_case"  # number-of-donuts
    camel_case = "camel_case"  # numberOfDonuts
    pascal_case = "pascal_case"  # NumberOfDonuts
