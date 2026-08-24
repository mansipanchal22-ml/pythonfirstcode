#q-7 Create a program to show method overloading using the same method name area() but performing different operations for a circle and rectangle by using @staticmethod or @classmethod.

class Shape:

    @staticmethod
    def area(a, b=None):

        if b is None:
            return 3.14 * a * a
        else:
            return a * b


print("Circle Area:", Shape.area(5))
print("Rectangle Area:", Shape.area(10, 5))