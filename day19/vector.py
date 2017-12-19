class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.current_index = 0

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        return Vector(k * self.x, k * self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index < 2:
            ret = (self.x, self.y)[self.current_index]
            self.current_index += 1
            return ret
        raise StopIteration()
