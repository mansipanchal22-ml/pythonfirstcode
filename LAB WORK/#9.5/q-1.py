#q-1 -Create an abstract class Shape with an abstract method area().
# -Inherit two child classes Rectangle and Circle, each implementing the area() method.
# -Demonstrate that creating an object of Shape directly raises an error.
# -Compute and display the area for both Rectangle and Circle.

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def area(self):
        length = 10
        width = 5
        return length * width

class Circle(Shape):

    def area(self):
        radius = 5
        return 3.14 * radius * radius

rectangle = Rectangle()
circle = Circle()

print("Rectangle Area:", rectangle.area())
print("Circle Area:", circle.area())

shape = Shape()
