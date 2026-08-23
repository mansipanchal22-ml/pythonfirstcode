#q-3 write a program to demostrate a parameterized constructor in the class Rectangle.
# -intilize the lenght and width using the constructor and calculate the area

class Rectangle:

    def __init__(self,length, width):
        self.lenght = length
        self.width = width

    def calculate_area(self):
        area = self.lenght  * self.width
        print("Area of Rectangle:", area)

r1 = Rectangle(10, 5)

r1.calculate_area()
