#R246282H
#Assignment 2
#Question 2


import math
# Main class
class Shape:
    def area(self):
        pass

    def name(self):
        return self.__class__.__name__


# Circle subclass
class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r * self.r


# Rectangle subclass
class Rectangle(Shape):
    def __init__(self, l, w):
        self.l, self.w = l, w

    def area(self):
        return self.l * self.w


# Demonstration
shapes = [Circle(5), Rectangle(4, 6), Circle(3)]

for i, s in enumerate(shapes, start=1):
    print(f"Shape number {i} is a {s.name()} with an area of {s.area():.2f}")
