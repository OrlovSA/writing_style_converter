from enum import Enum
from preparation_style import PreparationStyle
from factory_style import FactoryStyle


__all__ = ("WSCEnum", "WSC")


class WSCEnum(str, Enum):
    snake_case = "snake_case"  #  number_of_donuts
    kebab_case = "kebab_case"  #  number-of-donuts
    camel_case = "camel_case"  #  numberOfDonuts
    pascal_case = "pascal_case"  #  NumberOfDonuts


class WSC:

    @classmethod
    def wsc_dict(cls, data: dict, case: WSCEnum.snake_case) -> dict:
        if not isinstance(data, dict):
            raise ValueError(f"{data=} is not dict")
        
        result_dict = dict()
        for key, value in data.items():
            result_dict[
                FactoryStyle._factory_case_keys[case]
                (PreparationStyle._preparation(key))
            ] = value
        return result_dict
    

    @classmethod
    def wsc_str(cls, data: str, case: WSCEnum = WSCEnum.snake_case) -> str:
        if not isinstance(data, str):
            raise ValueError(f"{data=} is not string")
        
        return FactoryStyle._factory_case_keys[case](
            PreparationStyle._preparation(data)
        )

from pydantic import BaseModel, root_validator

camel_case_in = {
    "isAccepted": True,
    "patientId": "test",
    "clientId": 123,
}
class DataSnake(BaseModel):
    # is_accepted: bool = Field(alias="isAccepted")
    # patient_id: str = Field(alias="patientId")
    # client_id: int = Field(alias="clientId")
    # ...
    # or
    is_accepted: bool 
    patient_id: str 
    client_id: int

    @root_validator(pre=True)
    def _pre(cls, value):
        return WSC.wsc_dict(value, "snake_case")
    
    @property
    def camel_case(cls):
        return WSC.wsc_dict(cls.dict(), WSCEnum.camel_case)
    

print(DataSnake(**camel_case_in).camel_case)