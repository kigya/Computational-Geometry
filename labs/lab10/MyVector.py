from math import sqrt


class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def getPerpendicular(x, y):
        return Vector2d(y, -x)

    @staticmethod
    def scalar_product(v1, v2):
        return v1.x * v2.x + v1.y * v2.y

    def getLen(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def mutl(self, koef):
        self.x *= koef
        self.y *= koef
        return self

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __str__(self):
        return "[" + self.x.__str__() + "," + self.y.__str__() + "]"
