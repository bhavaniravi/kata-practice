class Frame:
    def __init__(self, frame_size=2):
        self.frame_size = frame_size
        self.slots = []

    def add(self, value):
        self.slots.append(value)

    def is_empty(self):
        return len(self.slots) < self.frame_size and self.sum_frame() != 10

    def __len__(self):
        return len(self.slots)

    def sum_frame(self):
        return sum([i for i in self.slots if i])

    def __repr__(self):
        return f"slots :: {self.slots}"

    def __getitem__(self, i):
        return self.slots[i]

class BowlingCalculator:
    def __init__(self):
        self.frames = []
        self.current_frame = Frame()
        self.frames.append(self.current_frame)

    def roll(self, roll):
        if roll < 0:
            raise TypeError(f"{roll} negative not supported")
        # print ("\n", roll, self.frames, "curr-frame=", self.current_frame, self.current_frame.is_empty())
        if not self.current_frame.is_empty():
            self.current_frame = Frame()
            self.frames.append(self.current_frame)

        self.current_frame.add(roll)

        # print (roll, self.frames, "curr-frame=", self.current_frame, self.current_frame.is_empty())


    def score(self):
        total_sum = 0
        for i, frame in enumerate(self.frames):
            frame_sum = frame.sum_frame()
            if frame_sum == 10:
                try:
                    if len(frame) == 1:
                        frame_sum += self.frames[i+1].sum_frame()   
                    elif len(frame) == 2:
                        frame_sum += self.frames[i+1][0]
                except IndexError:
                    pass

            total_sum += frame_sum
        return total_sum
