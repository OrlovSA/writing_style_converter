import pytest

from writing_style_converter import WSC
from writing_style_converter import WSCEnum


DICT_TEST = {
    "snake_case": {"value_one": 123, "value_two": [{"value_three": 123}]},
    "kebab-case": {"value_one": 123, "value_two": [{"value_three": 123}]},
    "camelCase": {"value_one": 123, "value_two": [{"value_three": 123}]},
    "PascalCase": {"value_one": 123, "value_two": [{"value_three": 123}]},
}

snake_case_result = {
    "snake_case": {"value_one": 123, "value_two": [{"value_three": 123}]},
    "kebab_case": {"value_one": 123, "value_two": [{"value_three": 123}]},
    "camel_case": {"value_one": 123, "value_two": [{"value_three": 123}]},
    "pascal_case": {"value_one": 123, "value_two": [{"value_three": 123}]},
}

kebab_case_result = {
    "snake-case": {"value-one": 123, "value-two": [{"value-three": 123}]},
    "kebab-case": {"value-one": 123, "value-two": [{"value-three": 123}]},
    "camel-case": {"value-one": 123, "value-two": [{"value-three": 123}]},
    "pascal-case": {"value-one": 123, "value-two": [{"value-three": 123}]},
}
camel_case_result = {
    "snakeCase": {"valueOne": 123, "valueTwo": [{"valueThree": 123}]},
    "kebabCase": {"valueOne": 123, "valueTwo": [{"valueThree": 123}]},
    "camelCase": {"valueOne": 123, "valueTwo": [{"valueThree": 123}]},
    "pascalCase": {"valueOne": 123, "valueTwo": [{"valueThree": 123}]},
}
pascal_case_result = {
    "SnakeCase": {"ValueOne": 123, "ValueTwo": [{"ValueThree": 123}]},
    "KebabCase": {"ValueOne": 123, "ValueTwo": [{"ValueThree": 123}]},
    "CamelCase": {"ValueOne": 123, "ValueTwo": [{"ValueThree": 123}]},
    "PascalCase": {"ValueOne": 123, "ValueTwo": [{"ValueThree": 123}]},
}


async def test_case():
    wsc_dict = WSC(DICT_TEST)
    assert WSC.wsc_dict(DICT_TEST) == snake_case_result
    assert wsc_dict.snake == snake_case_result

    assert WSC.wsc_dict(DICT_TEST, WSCEnum.kebab_case) == kebab_case_result
    assert wsc_dict.kebab == kebab_case_result

    assert WSC.wsc_dict(DICT_TEST, WSCEnum.camel_case) == camel_case_result
    assert wsc_dict.camel == camel_case_result

    assert WSC.wsc_dict(DICT_TEST, WSCEnum.pascal_case) == pascal_case_result
    assert wsc_dict.pascal == pascal_case_result


async def test_error():
    with pytest.raises(TypeError) as _e:
        WSC.wsc_dict("test")

    with pytest.raises(TypeError) as _e:
        WSC.wsc_str(DICT_TEST)

    with pytest.raises(TypeError) as _e:
        WSC("test")
