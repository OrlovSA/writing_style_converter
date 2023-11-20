from typing import List


class FactoryStyle:

    def _factory_snake_case(value: List[str]) -> str:
        return "_".join(value) 

    def _factory_kebab_case(value: List[str]) -> str:
        return "-".join(value)

    def _factory_pascal_case(value: List[str]) -> str:
        return "".join([s.title() for s in value])

    def _factory_camel_case(value: List[str]) -> str:
        ferst = value.pop(0).lower()
        return ferst + "".join([s.title() for s in value])
    

    _factory_case_keys = {
        "snake_case": _factory_snake_case,
        "kebab_case": _factory_kebab_case,
        "pascal_case": _factory_pascal_case,
        "camel_case": _factory_camel_case,
    }
