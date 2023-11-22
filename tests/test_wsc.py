from writing_style_converter import WSC, WSCEnum
import pytest


DICT_TEST = {
    "number_of_donuts": 123,
    "number-of-donuts": 123,
    "numberOfDonuts": 123,
    "NumberOfDonuts": 123
}


async def test_case():
    wsc_dict = WSC(DICT_TEST)
    assert WSC.wsc_dict(DICT_TEST) == {"number_of_donuts": 123}
    assert wsc_dict.snake == {"number_of_donuts": 123}

    assert WSC.wsc_dict(DICT_TEST, WSCEnum.kebab_case) == {"number-of-donuts": 123}
    assert wsc_dict.kebab == {"number-of-donuts": 123}

    assert WSC.wsc_dict(DICT_TEST, WSCEnum.camel_case) == {"numberOfDonuts": 123}
    assert wsc_dict.camel == {"numberOfDonuts": 123}

    assert WSC.wsc_dict(DICT_TEST, WSCEnum.pascal_case) == {"NumberOfDonuts": 123}
    assert wsc_dict.pascal == {"NumberOfDonuts": 123}


async def test_error():
    with pytest.raises(ValueError) as _e:
        WSC.wsc_dict("test")
        
    with pytest.raises(ValueError) as _e:
        WSC.wsc_str(DICT_TEST)

    with pytest.raises(ValueError) as _e:
        WSC("test")