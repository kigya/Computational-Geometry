import math


class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.pos = 0

    def __init__(self, x, y, pos):
        self.x = x
        self.y = y
        self.pos = pos

    def input(self):
        self.x = float(input())
        self.y = float(input())

    def equals(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "[" + self.x.__str__() + "," + self.y.__str__() + "], pos: " + self.pos.__str__() + "."

    def __gt__(self, other):
        return self.x > other.x and self.y > self.y

    def __lt__(self, other):
        return self.x < other.x and self.y < self.y

    def output(self):
        print("x =", self.x)
        print("y =", self.y)
