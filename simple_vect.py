import math


class Vect:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vect(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vect(self.x - other.x, self.y - other.y)

    def __getitem__(self, item: int):
        if not 0 <= item <= 1:
            raise ValueError
        return self.to_tuple()[item]

    def multiply(self, factor):
        return Vect(self.x * factor, self.y * factor)

    def to_tuple(self):
        return self.x, self.y


def mag(v: Vect):
    return math.sqrt(v.x ** 2 + v.y ** 2)
