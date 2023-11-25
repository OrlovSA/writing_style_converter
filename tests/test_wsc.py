import pytest

from writing_style_converter import WSC


DICT_TEST = {
    "snake_case": {"value_one": 123, "value_two": [{"value_three": 123}]},
    "kebab-case": {"value-one": 123, "value-two": [{"value-three": 123}]},
    "camelCase": {"valueOne": 123, "valueTwo": [{"valueThree": 123}]},
    "PascalCase": {"ValueOne": 123, "ValueTwo": [{"ValueThree": 123}]},
}

SNAKE_CASE_RESULT = {
    "snake_case": {"value_one": 123, "value_two": [{"value_three": 123}]},
    "kebab_case": {"value_one": 123, "value_two": [{"value_three": 123}]},
    "camel_case": {"value_one": 123, "value_two": [{"value_three": 123}]},
    "pascal_case": {"value_one": 123, "value_two": [{"value_three": 123}]},
}

KEBAB_CASE_RESULT = {
    "snake-case": {"value-one": 123, "value-two": [{"value-three": 123}]},
    "kebab-case": {"value-one": 123, "value-two": [{"value-three": 123}]},
    "camel-case": {"value-one": 123, "value-two": [{"value-three": 123}]},
    "pascal-case": {"value-one": 123, "value-two": [{"value-three": 123}]},
}
CAMEL_CASE_RESULT = {
    "snakeCase": {"valueOne": 123, "valueTwo": [{"valueThree": 123}]},
    "kebabCase": {"valueOne": 123, "valueTwo": [{"valueThree": 123}]},
    "camelCase": {"valueOne": 123, "valueTwo": [{"valueThree": 123}]},
    "pascalCase": {"valueOne": 123, "valueTwo": [{"valueThree": 123}]},
}
PASCAL_CASE_RESULT = {
    "SnakeCase": {"ValueOne": 123, "ValueTwo": [{"ValueThree": 123}]},
    "KebabCase": {"ValueOne": 123, "ValueTwo": [{"ValueThree": 123}]},
    "CamelCase": {"ValueOne": 123, "ValueTwo": [{"ValueThree": 123}]},
    "PascalCase": {"ValueOne": 123, "ValueTwo": [{"ValueThree": 123}]},
}
HUMIDITIES_FALSE_RESULT = {
    "snake_case": {"value_one": 123, "value_two": [{"value_three": 123}]},
    "kebab_case": {"value-one": 123, "value-two": [{"value-three": 123}]},
    "camel_case": {"valueOne": 123, "valueTwo": [{"valueThree": 123}]},
    "pascal_case": {"ValueOne": 123, "ValueTwo": [{"ValueThree": 123}]},
}


async def test_case():
    wsc_dict = WSC(DICT_TEST)
    assert wsc_dict.value == DICT_TEST
    assert wsc_dict.snake == SNAKE_CASE_RESULT
    assert wsc_dict.kebab == KEBAB_CASE_RESULT
    assert wsc_dict.camel == CAMEL_CASE_RESULT
    assert wsc_dict.pascal == PASCAL_CASE_RESULT


async def test_error():
    with pytest.raises(TypeError) as _e:
        WSC("test")


async def test_humidities_false():
    wsc_dict = WSC(DICT_TEST, humidities=False)
    assert wsc_dict.snake == HUMIDITIES_FALSE_RESULT
