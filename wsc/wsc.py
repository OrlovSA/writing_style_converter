from enum import Enum
from preparation_style import PreparationStyle
from factory_style import FactoryStyle


class WSCEnum(str, Enum):
    snake_case = "snake_case"  #  number_of_donuts
    kebab_case = "kebab_case"  #  number-of-donuts
    camel_case = "camel_case"  #  numberOfDonuts
    pascal_case = "pascal_case"  #  NumberOfDonuts


class WSC:
    @classmethod
    def wsc_dict(cls, data: dict, case: WSCEnum) -> dict:
        if not isinstance(data, dict):
            raise Exception(f"{data=} is not dict")
        
        result_dict = dict()
        for key, value in data.items():
            result_dict[
                FactoryStyle._factory_case_keys[case]
                (PreparationStyle._preparation(key))
            ] = value
        return result_dict
    

    @classmethod
    def wsc_str(cls, data: str, case: WSCEnum) -> str:
        if not isinstance(data, str):
            raise Exception(f"{data=} is not string")
        
        return FactoryStyle._factory_case_keys[case](
            PreparationStyle._preparation(data)
        )
