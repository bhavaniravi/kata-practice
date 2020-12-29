from bowling_calculator import BowlingCalculator, Frame
import pytest

class TestBowlingCalculator:
    def test_roll(self):
        calc = BowlingCalculator(frame_length=2)
        assert calc.frame_length == 2
        assert calc.frames != None

        frame = 1
        for i, val in enumerate(range(10)):
            # 0 - 1
            # 1 - 1
            # 2 - 2
            # 3 - 2
            # 4 - 3
            # 5 - 3
            if i!=0 and i % 2 == 0:
                frame = frame + 1 
            calc.roll(val)
            assert len(calc.frames) == frame
        
    def test_roll_with_strike_spare(self):
        calc = BowlingCalculator(frame_length=2)
        calc.roll(10) # 12
        calc.roll(1) # 1
        calc.roll(1) # 1
        calc.roll(5) 
        calc.roll(5) # 10
        assert len(calc.frames) == 3

        score = calc.score()
        assert score == 24 # (10 + 1 + 1) + (1 + 1) + (5 + 5)

        calc = BowlingCalculator(frame_length=3)
        calc.roll(10)
        calc.roll(1)
        assert len(calc.frames) == 2
        
        score = calc.score()
        assert score == 12 # (10 + 1) + 1



    @pytest.mark.parametrize("frames", (
        [1, 2],
        (1, 2)
    ))
    def test_frame(self, frames):
        frame = Frame(frames)
        assert frame.deliveries == frames

    @pytest.mark.parametrize("frames", (
        [1, 2, 3],
        1,
        "abc"
    ))
    def test_bad_frame(self, frames):
        with pytest.raises(TypeError):
            frame = Frame(frames)