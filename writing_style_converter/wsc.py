import json

from .enums import WSCEnum
from .factory_style import FactoryStyle


__all__ = "WSC"


class WSC:
    def __init__(self, value_dict: dict, humidities: bool = True) -> None:
        if not isinstance(value_dict, dict):
            raise TypeError(f"{value_dict=} is not dict")

        self.value_dict = value_dict
        self.humidities = humidities

    def __str__(self):
        return json.dumps(self.value, indent=2)

    @property
    def value(cls) -> dict:
        return cls.value_dict

    @property
    def snake(cls) -> dict:
        return FactoryStyle._conver_dict(cls.value_dict, cls.humidities)

    @property
    def kebab(cls) -> dict:
        return FactoryStyle._conver_dict(
            cls.value_dict, cls.humidities, WSCEnum.kebab_case
        )

    @property
    def camel(cls) -> dict:
        return FactoryStyle._conver_dict(
            cls.value_dict, cls.humidities, WSCEnum.camel_case
        )

    @property
    def pascal(cls) -> dict:
        return FactoryStyle._conver_dict(
            cls.value_dict, cls.humidities, WSCEnum.pascal_case
        )
