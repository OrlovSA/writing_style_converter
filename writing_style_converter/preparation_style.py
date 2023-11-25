from typing import List
import re


class PreparationStyle:
    def __preparation_snake_case(value: str) -> List[str]:
        return [v.lower() for v in value.split("_")]

    def __preparation_kebab_case(value: str) -> List[str]:
        return [v.lower() for v in value.split("-")]

    def __preparation_pascal_case(value: str) -> List[str]:
        pattern = re.compile(r"([a-z]+|[A-Z][a-z]*)")
        return [v.lower() for v in pattern.findall(value)]

    def __preparation_camel_case(value: str) -> List[str]:
        pattern = re.compile(r"([a-z]+|[A-Z][a-z]*)")
        return [v.lower() for v in pattern.findall(value)]

    @classmethod
    def _preparation(cls, value: str) -> List[str]:
        if "_" in value:
            return cls.__preparation_snake_case(value)
        elif "-" in value:
            return cls.__preparation_kebab_case(value)
        elif value.istitle():
            return cls.__preparation_pascal_case(value)
        return cls.__preparation_camel_case(value)
