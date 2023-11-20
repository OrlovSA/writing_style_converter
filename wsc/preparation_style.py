from typing import List
import re


class PreparationStyle:
    def _preparation_snake_case(value: str) -> List[str]:
        return [v.lower() for v in  value.split("_")]

    def _preparation_kebab_case(value: str) -> List[str]:
        return [v.lower() for v in  value.split("-")]

    def _preparation_pascal_case(value) -> List[str]:
        pattern = re.compile(r'([a-z]+|[A-Z][a-z]*)')
        return  [v.lower() for v in  pattern.findall(value)]

    def _preparation_camel_case(value) -> List[str]:
        pattern = re.compile(r'([a-z]+|[A-Z][a-z]*)')
        return  [v.lower() for v in  pattern.findall(value)]

    @classmethod
    def _preparation(cls, value: str) -> List[str]:
        if "_" in value:
            return PreparationStyle._preparation_snake_case(value)
        elif "-" in value:
            return PreparationStyle._preparation_kebab_case(value)
        elif value.istitle():
            return PreparationStyle._preparation_pascal_case(value)
        return PreparationStyle._preparation_camel_case(value)
