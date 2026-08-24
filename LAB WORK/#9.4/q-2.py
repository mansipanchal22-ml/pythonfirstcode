# Implement a program to demostrate polymorphism in class inheritance.
# -Create a base class Shape with a method area(),and derive classes Circle and Recantangle overidding the area() method for their specific calculations.

class Shape:

    def area(self):
        return 0


class Circle(Shape):

    def area(self):
        return 3.14 * 5 * 5


class Rectangle(Shape):

    def area(self):
        return 10 * 5


circle = Circle()
rectangle = Rectangle()

print("Circle Area:", circle.area())
print("Rectangle Area:", rectangle.area())