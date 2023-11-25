from typing import List

from .enums import WSCEnum
from .preparation_style import PreparationStyle


class FactoryStyle:
    def __factory_snake_case(value: List[str]) -> str:
        return "_".join(value)

    def __factory_kebab_case(value: List[str]) -> str:
        return "-".join(value)

    def __factory_pascal_case(value: List[str]) -> str:
        return "".join([s.title() for s in value])

    def __factory_camel_case(value: List[str]) -> str:
        ferst = value.pop(0).lower()
        return ferst + "".join([s.title() for s in value])

    _factory_case_keys = {
        "snake_case": __factory_snake_case,
        "kebab_case": __factory_kebab_case,
        "pascal_case": __factory_pascal_case,
        "camel_case": __factory_camel_case,
    }

    @classmethod
    def _conver_dict(
        cls, value_dict: dict, humidities: bool, case: WSCEnum = WSCEnum.snake_case
    ) -> dict:
        def _process_dict(input_dict: dict) -> dict:
            result_dict = dict()

            for key, value in input_dict.items():
                processed_key = cls._factory_case_keys[case](
                    PreparationStyle._preparation(key)
                )

                if isinstance(value, dict) and humidities:
                    result_dict[processed_key] = _process_dict(value)
                elif isinstance(value, list) and humidities:
                    result_dict[processed_key] = [_process_dict(item) for item in value]
                else:
                    result_dict[processed_key] = value

            return result_dict

        return _process_dict(value_dict)
