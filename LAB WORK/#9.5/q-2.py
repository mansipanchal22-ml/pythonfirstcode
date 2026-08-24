#q-2 -Add another abstract method perimeter() in the Shape class.
# -Implement it in Rectangle and Circle subclasses.
# -Verify both area() and perimeter() work correctly.
# -Try to instantiate a new subclass without implementing one method — observe the error.

from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):

    def area(self):
        len = 10
        wid  = 5
        return len * wid

    def perimeter(self):
        len = 10
        wid = 5
        return 2* (len * wid)
    
class Circle(Shape):

    def area(self):
        radius = 5
        return math.pi * radius * radius
    
    def perimeter(self):
        radius = 5
        return 2 * math.pi * radius
    
rectangle = Rectangle()
circle =  Circle()

print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())

print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

class Triangle(Shape):

    def area(self):
        return 20
    
triangle = Triangle
