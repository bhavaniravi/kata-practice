
class BowlingCalculator:
    def __init__(self, frame_length):
        self.frame_length = frame_length
        self.frames = []
        self.num_rolls = 0

    def roll(self, pins_knocked):
        self.num_rolls += 1
        try:
            latest_frame = self.frames[-1]
            if len(latest_frame) < self.frame_length:
                if sum(latest_frame) == 10:
                    raise IndexError
                latest_frame.append(pins_knocked)
            else:
                raise IndexError
        except IndexError:
            latest_frame = [pins_knocked]
            self.frames.append(latest_frame)
    
    def score(self):
        score = 0
        for i, frame in enumerate(self.frames):
            frame_sum = sum(frame)
            if frame_sum == 10:
                try:
                    if len(frame) == 1: # strike
                        frame_sum += sum(self.frames[i+1][:2])
                    elif len(frame) == 2: # spare
                        frame_sum += self.frames[i+1][0]
                except IndexError:
                    pass

            score = score + frame_sum
        return score


    def calculate():
        pass


class Frame:
    def __init__(self, deliveries, frame_length=2):
        if not (
            (isinstance(deliveries, list)
            or isinstance(deliveries, tuple))
            and len(deliveries) <= frame_length
        ):
            raise TypeError("Invalid type")
        self.deliveries = deliveries