from bowling_calculator import BowlingCalculator, Frame
import pytest

class TestFrame:
    def test_frame(self):
        frame = Frame()
        frame.add(2)
        assert frame.is_empty() == True

        frame.add(None)
        assert frame.is_empty() == False




class TestBowlingCalculator:
    @pytest.mark.parametrize("rolls, frame_length, score",
        (
            ((1, 2), 1, 3),
            ([1]*20, 10, 20),
            ((10, ), 1, 10),
            ((5, 5), 1, 10),
            ((5,), 1, 5),

            ((5, 5, 3), 2, 16),
            ((10, 1, 2), 2, 16),
        )
    )
    def test_rolls(self, rolls, frame_length, score):
        calc = BowlingCalculator()
        for roll in rolls:
            calc.roll(roll)

        assert len(calc.frames) == frame_length
        assert calc.score() == score

    @pytest.mark.parametrize("rolls",
        (
            # roll negative
            ((-1, -2),)
        )
    )
    def test_calc_error(self, rolls):
        calc = BowlingCalculator()

        with pytest.raises(TypeError):
            for roll in rolls:
                calc.roll(roll)
