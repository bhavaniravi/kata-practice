from calculator import Calculator
import pytest
class TestCalculator:
    @pytest.mark.parametrize(
        "input, expected",
        [
            ("", 0),
            ("1", 1),
            ("1,2", 3),
            ("1\n2", 3),
            ("1\n2\n2", 5),
            ("1,2,2", 5),
            ("1,2,1000", 3),
            ("//#\n1#2#2", 5),
            ("//[###]\n1###2###2", 5),
            ("//[#][,]\n1#,2#,2", 5)
        ]
    )
    def test_add_method(self, input, expected):
        calc = Calculator()
        assert expected == calc.add(input)
    
    def test_exception(self):
        calc = Calculator()
        with pytest.raises(Exception):
            expected == calc.add("-1,2")