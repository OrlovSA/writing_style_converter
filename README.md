# Writing Style Converter

## Overview

The **writing_style_converter** is a Python utility that addresses the common pain points associated with managing different naming conventions (styles) in Python code, particularly when dealing with models and data structures received from external APIs. The primary motivation behind this tool is to streamline the process of converting between various naming styles, such as "snake_case," "kebab_case," "camel_case," and "pascal_case."

## Key Challenges

1. **Model Aliasing for External APIs:**
   Writing aliases for models to match the Pythonic style of response from an external API can be cumbersome. This tool simplifies the process of converting between different styles seamlessly.

2. **Swagger Documentation Inconsistency:**
   When a model, with aliases, is used as an output from an external API and consumed in a FastAPI application, Swagger documentation may become inconsistent. This utility helps maintain consistency by converting models to a specified style.

## Features

### Available Styles

- **"snake_case"**: e.g., `number_of_donuts`
- **"kebab_case"**: e.g., `number-of-donuts`
- **"camel_case"**: e.g., `numberOfDonuts`
- **"pascal_case"**: e.g., `NumberOfDonuts`

## Usage Examples

### Converting Dictionary Keys

```python
camel_case_in = {
    "isAccepted": True,
    "patientId": "test",
    "clientId": 123,
}

from writing_style_converter import WSC, WSCEnum

# Convert dictionary keys from camel_case to snake_case
snake_case_result: dict = WSC.wsc_dict(camel_case_in, WSCEnum.snake_case) 
# Output: {'is_accepted': True, 'patient_id': 'test', 'client_id': 123}

# Convert back from snake_case to camel_case
WSC.wsc_dict(snake_case_result, WSCEnum.camel_case)
# Output: {'isAccepted': True, 'patientId': 'test', 'clientId': 123}
```

### Converting Strings

```python
# Convert string from camel_case to snake_case
WSC.wsc_str("isAccepted", WSCEnum.snake_case)
# Output: 'is_accepted'

# Convert string from camel_case to kebab_case
WSC.wsc_str("isAccepted", WSCEnum.kebab_case)
# Output: 'is-accepted'
```

### Converting Pydantic Models

```python
from pydantic import BaseModel, root_validator
from writing_style_converter import WSC, WSCEnum


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
        return WSC.wsc_dict(value, WSCEnum.snake_case)

    @property
    def camel_case(cls):
        return WSC.wsc_dict(cls.dict(), WSCEnum.camel_case)
        

data_snake_case = DataSnake(**camel_case_in) 
# DataSnake(is_accepted=True, patient_id='test', client_id=123)

# Convert Pydantic model to pascal_case dictionary
WSC.wsc_dict(data_snake_case.dict(), WSCEnum.pascal_case)
# Output: {'IsAccepted': True, 'PatientId': 'test', 'ClientId': 123}
```

## Installation

```bash
pip install writing_style_converter
```

## Acknowledgments

This project is inspired by the need for consistent naming conventions in Python projects, especially when dealing with external APIs and FastAPI applications. The utility provided by **writing_style_converter** aims to simplify the development process and enhance code readability. Contributions and feedback are welcome!