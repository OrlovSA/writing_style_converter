# Writing Style Converter

## Overview
The WSC (**writing_style_converter**) library provides a utility for converting dictionaries between different naming conventions.

```python
from writing_style_converter import WSC


all_case_dict = {
    "snake_case": {"value_one": 123, "value_two": [{"value_three": 123}]},
    "kebab-case": {"value-one": 123, "value-two": [{"value-three": 123}]},
    "camelCase": {"valueOne": 123, "valueTwo": [{"valueThree": 123}]},
    "PascalCase": {"ValueOne": 123, "ValueTwo": [{"ValueThree": 123}]},
}

# Example with humidities set to True (default)
wsc_dict = WSC(all_case_dict)

# Access different naming conventions
print(wsc_instance.value)          # Original dictionary
print(wsc_instance.snake)          # Converted to snake_case
print(wsc_instance.kebab)          # Converted to kebab-case
print(wsc_instance.camel)          # Converted to camelCase
print(wsc_instance.pascal)         # Converted to PascalCase

# Example with humidities set to False
wsc_dict_humidities = WSC(all_case_dict, humidities=False)

print(wsc_instance_without_humidities.snake)  # Converted to snake_case without humidities
```

The **humidities** parameter controls whether the conversion process includes nested dictionaries and lists. When set to **True (default)**, the conversion includes nested structures. When set to False, only the top-level dictionary is converted.

## Installation

```bash
pip install writing_style_converter
```
