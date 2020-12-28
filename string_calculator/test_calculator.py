from calculator import Calculator
from contextlib import contextmanager
import pytest 

@contextmanager
def not_raises(ExpectedException):
    try:
        yield

    except ExpectedException as error:
        raise AssertionError(f"Raised exception {error} when it should not!")

    except Exception as error:
        raise AssertionError(f"An unexpected exception {error} raised.")

class TestCalculator:
    def test_method_existis(self):
        calc = Calculator()
        with not_raises(AttributeError):
            function = getattr(calc, "add")

    @pytest.mark.parametrize("input, expected", (
        ("", 0),
        ("1,2", 3),
        ("1\n2", 3),
        ("//;\n1;2", 3),
        ("//;\n1;2000", 1),
        ("//;;;\n1;;;2", 3),
        ("//[*][%]\n1*2%3", 6)
    ))
    def test_correct_cases(self, input, expected):
        calc = Calculator()
        result = calc.add(input)
        assert result == expected

    @pytest.mark.parametrize("input, expected", (
        ("//;\n1;2", ";"),
        ("1\n2", None),
        ("//;;;\n1;2", ";;;"),
         ("//[*][%]\n1*2%3", "\*|%") # regex escaped
    ))
    def test_get_delimiter(self, input, expected):
        calc = Calculator()
        result = calc.get_delimiter(input)
        if not expected:
            expected = calc.split_regex
        assert result == expected


    @pytest.mark.parametrize("input, exception", [
        ("1,\n2", ValueError),
        ("1,-2", AttributeError),
        ("1,\n-2", ValueError)

    ])
    def test_raises_exception(self, input, exception):
        calc = Calculator()
        with pytest.raises(exception):
            result = calc.add(input)

    def test_filter_negatives(self):
        calc = Calculator()
        assert calc.check_negatives([1, 2, 3]) is None
        with pytest.raises(AttributeError):
            assert calc.check_negatives([-1, 2, 3]) is None

    @pytest.mark.parametrize("input, expected", [
        ([1, 2, 3], [1, 2, 3]),
        ([1, 2, 3000], [1, 2]),
    ])
    def test_filter_1000(self, input, expected):
        calc = Calculator()
        res = calc.filter_1000(input)
        assert res == expected

