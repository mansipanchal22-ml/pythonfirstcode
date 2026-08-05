#Q.16 Implement a program to create a function that returns a tuple containing the square and cube of a given number.

def sqaure_cube(n):
    return n**2,n**3

sqaure, cube = sqaure_cube(5)

print("Square =", sqaure)
print("Cube =", cube)