#R246282H
#Assignment 2
#Question 3

class Shape:
    def __init__(self):
        print("Shape constructor called.")

    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()  # This is to initialize the Shape class
        self.length = length
        self.width = width
        print("Rectangle constructor called.")

    def calculate_area(self):
        return self.length * self.width

# Demonstrating the use of super()
rect = Rectangle(10, 5)
print(f"Rectangle area: {rect.calculate_area()}")