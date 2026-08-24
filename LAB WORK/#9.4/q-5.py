# Write a program to demonstrate method overloading by creating a class Calculator with a method multiply() that works for two or three arguments.
#-Use default arguments or variable-length arguments.

class Calculator:

    def multiply(self, a, b, c=1):
        return a * b * c


obj = Calculator()

print("Multiplication of two numbers:", obj.multiply(2, 3))
print("Multiplication of three numbers:", obj.multiply(2, 3, 4))