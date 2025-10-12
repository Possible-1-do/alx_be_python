import math

# Base class
class Shape:
    def area(self):
        # This forces derived classes to implement their own area method
        raise NotImplementedError("Subclasses must override this method")

#  Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
