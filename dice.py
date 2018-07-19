import random

class Dice():
    num_sides = 0
    current_side_up = 1
    range_of_values = (1, 2, 3, 4, 5, 6)

    # def __init__(self, num_sides, current_side_up, range_of_values):
        # self.
    def roll(self):
        self.current_side_up = random.choice(self.range_of_values)

    def __str__(self):
        return str(self.current_side_up)
