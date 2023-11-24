from enum import Enum
import json

from .factory_style import FactoryStyle
from .preparation_style import PreparationStyle


__all__ = ("WSCEnum", "WSC")


class WSCEnum(str, Enum):
    snake_case = "snake_case"  # number_of_donuts
    kebab_case = "kebab_case"  # number-of-donuts
    camel_case = "camel_case"  # numberOfDonuts
    pascal_case = "pascal_case"  # NumberOfDonuts


class WSC:
    def __init__(self, value: dict) -> None:
        if not isinstance(value, dict):
            raise TypeError(f"{value=} is not dict")

        self.value = value

    def __str__(self) -> dict:
        return json.dumps(self.value)

    @classmethod
    def wsc_dict(cls, data: dict, case: WSCEnum = WSCEnum.snake_case) -> dict:
        if not isinstance(data, dict):
            raise TypeError(f"{data=} is not dict")

        def _process_dict(input_dict: dict, case: WSCEnum) -> dict:
            result_dict = dict()

            for key, value in input_dict.items():
                processed_key = FactoryStyle._factory_case_keys[case](
                    PreparationStyle._preparation(key)
                )

                if isinstance(value, dict):
                    result_dict[processed_key] = _process_dict(value, case)
                elif isinstance(value, list):
                    result_dict[processed_key] = [
                        _process_dict(item, case) for item in value
                    ]
                else:
                    result_dict[processed_key] = value

            return result_dict

        return _process_dict(data, case)

    @classmethod
    def wsc_str(cls, data: str, case: WSCEnum = WSCEnum.snake_case) -> str:
        if not isinstance(data, str):
            raise TypeError(f"{data=} is not string")

        return FactoryStyle._factory_case_keys[case](
            PreparationStyle._preparation(data)
        )

    @property
    def snake(cls) -> dict:
        return cls.wsc_dict(cls.value)

    @property
    def kebab(cls) -> dict:
        return cls.wsc_dict(cls.value, WSCEnum.kebab_case)

    @property
    def camel(cls) -> dict:
        return cls.wsc_dict(cls.value, WSCEnum.camel_case)

    @property
    def pascal(cls) -> dict:
        return cls.wsc_dict(cls.value, WSCEnum.pascal_case)
