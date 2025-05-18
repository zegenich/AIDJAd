import pytest
from src.string_utils import StringUtils
from contextlib import nullcontext


class TestStringUtils:
    @pytest.mark.parametrize(
        "input_str, expected",
        [
            ("adc", "cda"),
            ("", ""),
            ("123", "321"),

        ]
    )
    def test_reverse_string(self, input_str, expected):
        utils = StringUtils()
        assert utils.reverse_string(input_str) == expected


    @pytest.mark.parametrize(
        "input_str, expected",
        [
            ("adc", "cda"),
            #("", ""),
            #("123", "321"),
            (1233, pytest.raises(TypeError)),
            ("%", pytest.raises(TypeError))
        ]
    )
    def test_revers_negative(self, input_str, expected):
        utils = StringUtils()
        if isinstance(expected, str):
            assert utils.reverse_string(input_str) == expected
        else:
            with expected:
                utils.reverse_string(input_str)



    @pytest.mark.parametrize(
        "full_name, expected",
        [
            ("igor vin", "IV"),
            ("", pytest.raises(ValueError)),
        ]
    )
    def test_get_initials(self, full_name, expected):
        utils = StringUtils()
        if isinstance(expected, str):
            assert utils.get_initials(full_name) == expected
        else:
            with expected:
                utils.get_initials(full_name)
